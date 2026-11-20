#!/usr/bin/env python3
"""Captura uma fonte para o vault: baixa, arquiva no Wayback e converte para Markdown.

Uso: capturar.py <url> <pasta-fontes> <id> [--titulo T] [--completo] [--sem-wayback]

- PDF: salva <id>.pdf e o texto extraído (pdftotext) em <id>.md. No repo do blog, o
  .gitattributes manda todo PDF/JPG/PNG de _drafts/ para o Git LFS.
- HTML: texto principal via trafilatura em <id>.md. `--completo` (ou trafilatura vazio)
  converte a página inteira com pandoc: use em lei e norma, em que nada pode faltar.
  Sem o binário `trafilatura` no PATH, roda via `uvx trafilatura` — antes, a falta dele
  caía no pandoc em silêncio, e o .md vinha com menu e rodapé no meio do texto.
- Anti-bot: 403/429/503 no urllib refaz o download com curl_cffi (fingerprint TLS de
  browser real), via `uv run --with curl_cffi`. Foi um bloqueio desses que deixou o
  van der Ham (2021) "para leitura à mão" no primeiro post.
- Wayback: pede snapshot novo (Save Page Now); se falhar, usa o mais recente que existir.
Saída: uma linha JSON com os caminhos e links, para quem chamou registrar na nota.
O campo `conversor` diz o que de fato rodou; `aviso` acumula tudo o que degradou.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

UA: str = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
WAYBACK_RE: re.Pattern[str] = re.compile(r"https?://web\.archive\.org/web/\d{8,14}[^\s\"']*")
TIMEOUT: int = 90


@dataclass
class Resultado:
    id: str
    url: str
    wayback: str
    formato: str
    conversor: str
    titulo: str
    md: str
    original: str
    aviso: str


ANTIBOT_STATUS: frozenset[int] = frozenset({403, 429, 503})

# Roda isolado (-I) num interpretador efêmero do uv: o curl_cffi vive fora do python do
# sistema. Lê a URL do argv, grava o corpo no arquivo pedido e imprime só o Content-Type.
CFFI_SCRIPT: str = (
    "import sys\n"
    "from curl_cffi import requests\n"
    "r = requests.get(sys.argv[1], impersonate='chrome', timeout=90)\n"
    "r.raise_for_status()\n"
    "open(sys.argv[2], 'wb').write(r.content)\n"
    "print(r.headers.get('content-type', ''))\n"
)


def baixar_cffi(url: str) -> tuple[bytes, str] | None:
    if not shutil.which("uv"):
        return None
    with tempfile.TemporaryDirectory() as tmp:
        destino = Path(tmp) / "corpo"
        proc = subprocess.run(
            ["uv", "run", "--quiet", "--with", "curl_cffi", "--no-project",
             "python", "-I", "-c", CFFI_SCRIPT, url, str(destino)],
            capture_output=True, text=True, timeout=TIMEOUT * 2,
        )
        if proc.returncode != 0 or not destino.exists():
            return None
        return destino.read_bytes(), proc.stdout.strip()


def baixar_wayback_cru(url: str) -> tuple[bytes, str, str] | None:
    """Último recurso: o snapshot mais recente, CRU (`id_` = sem a barra do Wayback
    injetada no HTML). Cloudflare com desafio JS barra até o curl_cffi; o Wayback
    costuma ter a cópia — medido 2026-11-20: o PDF do van der Ham (ACM) estava lá."""
    try:
        api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
        with urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": UA}), timeout=60) as resp:
            snap = json.load(resp).get("archived_snapshots", {}).get("closest", {})
        if not snap.get("available"):
            return None
        cru = f"https://web.archive.org/web/{snap['timestamp']}id_/{url}"
        with urllib.request.urlopen(urllib.request.Request(cru, headers={"User-Agent": UA}), timeout=TIMEOUT) as resp:
            return resp.read(), resp.headers.get("Content-Type", ""), snap["timestamp"]
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError):
        return None


def baixar(url: str) -> tuple[bytes, str, str]:
    """(corpo, content-type, aviso). Recua em cadeia: urllib → curl_cffi → Wayback cru."""
    if urllib.parse.urlsplit(url).scheme not in ("http", "https"):
        raise SystemExit(f"erro: só http/https: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.read(), resp.headers.get("Content-Type", ""), ""
    except urllib.error.HTTPError as e:
        if e.code not in ANTIBOT_STATUS:
            raise
        status = e.code
    via_cffi = baixar_cffi(url)
    if via_cffi:
        return *via_cffi, f"urllib recebeu {status}; baixado com curl_cffi"
    via_wb = baixar_wayback_cru(url)
    if via_wb:
        dados, ctype, ts = via_wb
        return dados, ctype, (
            f"original barrado ({status}, curl_cffi também); conteúdo do snapshot {ts} do Wayback"
        )
    raise SystemExit(f"erro: {url} barrado ({status}) no urllib, no curl_cffi e sem snapshot: ler à mão")


def trafilatura_cmd() -> list[str]:
    if shutil.which("trafilatura"):
        return ["trafilatura"]
    if shutil.which("uvx"):
        return ["uvx", "--quiet", "trafilatura"]
    return []


def decodificar(dados: bytes, content_type: str) -> str:
    candidatos: list[str] = []
    m = re.search(r"charset=([\w-]+)", content_type, re.I)
    if m:
        candidatos.append(m.group(1))
    m = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", dados[:4096], re.I)
    if m:
        candidatos.append(m.group(1).decode("ascii", "ignore"))
    candidatos += ["utf-8", "cp1252"]
    for enc in candidatos:
        try:
            return dados.decode(enc)
        except (LookupError, UnicodeDecodeError):
            continue
    return dados.decode("utf-8", "replace")


def titulo_html(texto: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", texto, re.I | re.S)
    return " ".join(html.unescape(m.group(1)).split()) if m else ""


def rodar(cmd: list[str], entrada: str | None = None, timeout: int = TIMEOUT) -> str:
    proc = subprocess.run(cmd, input=entrada, capture_output=True, text=True, timeout=timeout)
    return proc.stdout if proc.returncode == 0 else ""


def converter_html(texto: str, completo: bool) -> tuple[str, str, str]:
    """(markdown, conversor, aviso)."""
    aviso = ""
    if not completo:
        cmd = trafilatura_cmd()
        if not cmd:
            aviso = "trafilatura indisponível (nem binário, nem uvx); página inteira via pandoc"
        else:
            # O primeiro `uvx` resolve o pacote: timeout maior que o de uma conversão.
            md = rodar([*cmd, "--markdown", "--formatting", "--links", "--recall"], texto, TIMEOUT * 3)
            if len(md.strip()) >= 400:
                return md, "trafilatura", ""
            aviso = "trafilatura devolveu menos de 400 caracteres; página inteira via pandoc"
    md = rodar(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"], texto)
    return md, "pandoc", aviso


def wayback(url: str) -> tuple[str, str]:
    """Snapshot novo; se falhar, o mais recente disponível. Retorna (link, aviso)."""
    try:
        req = urllib.request.Request("https://web.archive.org/save/" + url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=180) as resp:
            final = resp.geturl()
            corpo = resp.read(200_000).decode("utf-8", "ignore")
        for candidato in (final, *WAYBACK_RE.findall(corpo)):
            if WAYBACK_RE.fullmatch(candidato.split("#")[0]) or WAYBACK_RE.match(candidato):
                return candidato, ""
    except (urllib.error.URLError, TimeoutError, OSError):
        pass
    try:
        api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
        with urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": UA}), timeout=60) as resp:
            snap = json.load(resp).get("archived_snapshots", {}).get("closest", {})
        if snap.get("available"):
            return snap["url"].replace("http://", "https://", 1), "snapshot antigo: o Save Page Now falhou"
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        pass
    return "", "sem snapshot no Wayback"


def frontmatter(r: Resultado, hoje: str) -> str:
    def esc(v: str) -> str:  # JSON é YAML válido: aspas, barras e controle saem escapados
        return json.dumps(" ".join(v.split()), ensure_ascii=False)

    return (
        "---\n"
        f"title: {esc(r.titulo)}\n"
        "type: fonte\n"
        f"formato: {r.formato}\n"
        f"url: {esc(r.url)}\n"
        f"wayback: {esc(r.wayback)}\n"
        f"acessado: {hoje}\n"
        f"conversor: {r.conversor}\n"
        "---\n\n"
        "> [!info] Cópia para leitura\n"
        f"> Original: <{r.url}>\n"
        f"> Wayback: {('<' + r.wayback + '>') if r.wayback else '—'}\n"
        f"> Capturado em {hoje} com `{r.conversor}`. Em caso de dúvida, vale o original.\n\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("pasta", type=Path)
    ap.add_argument("id")
    ap.add_argument("--completo", action="store_true", help="página inteira via pandoc (leis, normas)")
    ap.add_argument("--sem-wayback", action="store_true")
    ap.add_argument("--titulo", default="", help="título da fonte (senão, o <title> da página)")
    a = ap.parse_args()

    a.pasta.mkdir(parents=True, exist_ok=True)
    hoje = dt.date.today().isoformat()
    dados, ctype, aviso_download = baixar(a.url)
    eh_pdf = "pdf" in ctype.lower() or dados[:5] == b"%PDF-"
    md_path = a.pasta / f"{a.id}.md"
    avisos: list[str] = [aviso_download]

    if eh_pdf:
        pdf_path = a.pasta / f"{a.id}.pdf"
        pdf_path.write_bytes(dados)
        corpo = rodar(["pdftotext", "-layout", str(pdf_path), "-"])
        if not corpo.strip():
            avisos.append("pdftotext não extraiu texto (PDF escaneado?); ler o PDF à mão")
        r = Resultado(a.id, a.url, "", "pdf", "pdftotext", a.id, str(md_path), str(pdf_path), "")
        corpo = f"Arquivo original: [[{pdf_path.name}]]\n\n```text\n{corpo.strip()}\n```\n"
    else:
        texto = decodificar(dados, ctype)
        corpo, conversor, aviso_conv = converter_html(texto, a.completo)
        avisos.append(aviso_conv)
        r = Resultado(a.id, a.url, "", "html", conversor, titulo_html(texto) or a.id, str(md_path), "", "")

    if a.titulo:
        r.titulo = a.titulo
    if not a.sem_wayback:
        r.wayback, aviso_wb = wayback(a.url)
        avisos.append(aviso_wb)
    r.aviso = "; ".join(x for x in avisos if x)
    md_path.write_text(frontmatter(r, hoje) + corpo, encoding="utf-8")
    print(json.dumps(asdict(r), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
