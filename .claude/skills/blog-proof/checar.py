#!/usr/bin/env python3
"""Checagem mecânica de um rascunho: o que dá para medir sem ler a prosa.

Uso (da raiz do repo): python3 .claude/skills/blog-proof/checar.py <slug>

Cobre o que quebra o build, quebra o promote, ou some em silêncio no site publicado:

- notas de rodapé: `[^x]` sem definição vira TEXTO LITERAL no post (o Goldmark não
  avisa); definição sem uso some; rótulo numérico briga com a numeração do layout.
- shortcodes de mídia: `figure`/`slide` sem `alt` derrubam o build; `src` que não resolve
  também. O src é procurado em assets/<src> (já publicado) e em
  _drafts/posts/<slug>/assets/<arquivo> (o promote copia de lá).
- `%%` ímpar: o promote aborta (ver strip_obsidian_comments em tools/promote-draft.py).
- callouts `[!tldr]` / `[!tldr-long]`: ausentes, vazios, ou longos demais para o card.
- `epoca` com hífen no intervalo (o padrão é o travessão curto –).
- tags fora do formato kebab-sem-acento, e tags NOVAS (cada uma cria uma página /tags/).
- post já publicado: avisa que corrigir o rascunho NÃO atualiza content/posts/.

Saída: linhas `ERRO` (quebra algo) e `AVISO` (decisão do autor). Exit 1 se houver ERRO.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO: Path = Path(__file__).resolve().parents[3]
DRAFTS: Path = REPO / "_drafts" / "posts"
POSTS: Path = REPO / "content" / "posts"
TLDR_MAX: int = 140
TLDR_LONG_MAX: int = 260

SHORTCODE_RE = re.compile(r"\{\{<\s*(figure|slide|audio|diagrama|embed)\b(.*?)>\}\}", re.S)
PARAM_RE = re.compile(r'(\w+)="([^"]*)"')
CODE_FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.M | re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def kebab(text: str) -> str:
    """Mesma regra do tools/promote-draft.py: é ela que dá o nome do arquivo publicado."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def front_matter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fm[key.strip()] = value.strip().strip("'\"")
    return fm, m.group(2)


def callout(body: str, kind: str) -> str | None:
    m = re.search(rf"^> *\[!{re.escape(kind)}\][+-]?.*$\n((?:^>.*$\n?)*)", body, re.M)
    if not m:
        return None
    return " ".join(re.sub(r"^> ?", "", ln).strip() for ln in m.group(1).splitlines()).strip()


def tags_em_uso(excluir: Path) -> set[str]:
    usadas: set[str] = set()
    for p in POSTS.glob("*.md"):
        m = re.search(r"^tags\s*=\s*\[(.*?)\]", p.read_text(encoding="utf-8"), re.M)
        if m:
            usadas |= {t.strip().strip("'\"") for t in m.group(1).split(",") if t.strip()}
    for p in DRAFTS.glob("*/post.md"):
        if p == excluir:
            continue
        fm, _ = front_matter(p.read_text(encoding="utf-8"))
        usadas |= {t.strip().strip("'\"") for t in fm.get("tags", "").strip("[]").split(",") if t.strip()}
    return usadas


def main() -> int:
    if len(sys.argv) != 2:
        print("uso: checar.py <slug>", file=sys.stderr)
        return 2
    slug = sys.argv[1].strip().rstrip("/").removesuffix("/post.md")
    post = DRAFTS / slug / "post.md"
    if not post.is_file():
        print(f"ERRO rascunho não encontrado: {post.relative_to(REPO)}")
        return 1

    texto = post.read_text(encoding="utf-8")
    fm, body = front_matter(texto)
    erros: list[str] = []
    avisos: list[str] = []

    # Código não conta: `[^x]` ou `{{< >}}` dentro de bloco de código é exemplo, não uso.
    prosa = INLINE_CODE_RE.sub("", CODE_FENCE_RE.sub("", body))

    # --- notas de rodapé
    defs = re.findall(r"^\[\^([^\]]+)\]:", prosa, re.M)
    refs = re.findall(r"\[\^([^\]]+)\](?!:)", prosa)
    for rot in sorted(set(refs) - set(defs)):
        erros.append(f"nota [^{rot}] usada sem definição: sai como texto literal no post")
    for rot in sorted(set(defs) - set(refs)):
        avisos.append(f"nota [^{rot}] definida e nunca usada: não aparece em Referências")
    for rot in sorted({d for d in defs if defs.count(d) > 1}):
        erros.append(f"nota [^{rot}] definida mais de uma vez")
    for rot in sorted({r for r in set(refs) | set(defs) if r.isdigit()}):
        avisos.append(f"nota [^{rot}] com rótulo numérico: o padrão é rótulo kebab pelo autor/obra")

    # --- shortcodes de mídia
    for nome, args in SHORTCODE_RE.findall(prosa):
        params = dict(PARAM_RE.findall(args))
        if nome in ("figure", "slide") and not params.get("alt", "").strip():
            erros.append(f"{nome} sem `alt` (o build falha): {args.strip()[:70]}")
        if nome == "embed" and not params.get("title"):
            erros.append(f"embed sem `title` (o build falha): {args.strip()[:70]}")
        src = params.get("src", "")
        if nome != "embed" and src and not src.startswith(("http://", "https://")):
            publicado = REPO / "assets" / src
            rascunho = DRAFTS / slug / "assets" / Path(src).name
            if not publicado.is_file() and not rascunho.is_file():
                erros.append(f"{nome} src não resolve (nem assets/{src}, nem {slug}/assets/): o build falha")
            elif not src.startswith(f"posts/{slug}/"):
                avisos.append(f"{nome} src fora de posts/{slug}/: o promote só copia para essa pasta")

    # --- comentários do Obsidian
    if body.count("%%") % 2:
        erros.append("número ímpar de `%%`: o promote aborta (bloco de comentário sem par)")

    # --- callouts
    for kind, limite in (("tldr", TLDR_MAX), ("tldr-long", TLDR_LONG_MAX)):
        valor = callout(body, kind)
        if valor is None:
            erros.append(f"callout `> [!{kind}]` ausente: o promote aborta")
        elif not valor:
            avisos.append(f"`[!{kind}]` vazio")
        elif len(valor) > limite:
            avisos.append(f"`[!{kind}]` com {len(valor)} caracteres (alvo: até ~{limite})")

    # --- front matter
    if not fm.get("title"):
        erros.append("sem `title`: o promote aborta")
    epoca = fm.get("epoca", "")
    if re.search(r"\d\s*-\s*(c\.\s*)?\d", epoca):
        avisos.append(f"epoca {epoca!r} usa hífen no intervalo: o padrão é o travessão curto (–)")
    tags = [t.strip().strip("'\"") for t in fm.get("tags", "").strip("[]").split(",") if t.strip()]
    for t in tags:
        if t != kebab(t):
            erros.append(f"tag {t!r} fora do formato (kebab, sem acento): vira rota /tags/<nome>/")
    novas = sorted(set(tags) - tags_em_uso(post))
    if novas:
        avisos.append(f"tag(s) nova(s) {novas}: cada uma cria uma página /tags/ com um post só")

    # --- já publicado?
    if fm.get("title"):
        publicado = POSTS / f"{kebab(fm['title'])}.md"
        if publicado.exists():
            avisos.append(
                f"já publicado em {publicado.relative_to(REPO)}: o promote recusa sobrescrever, "
                "então correção aqui precisa ser espelhada lá à mão"
            )

    for e in erros:
        print(f"ERRO  {e}")
    for a in avisos:
        print(f"AVISO {a}")
    if not erros and not avisos:
        print("ok: nada a apontar")
    print(f"-- {len(erros)} erro(s), {len(avisos)} aviso(s) · {len(set(refs))} notas usadas")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
