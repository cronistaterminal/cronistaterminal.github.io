#!/usr/bin/env python3
"""Varre o build (public/) e reporta links internos que apontam para o vazio.

Existe porque o Hugo NÃO reclama disso. Um <a href="/cronista/"> escrito à mão num
partial compila, publica e serve um 404 — o Hugo só valida o que ele mesmo resolve
(.RelPermalink, ref/relref). Caminhos digitados são texto, e texto ele não confere.

Foi exatamente assim que a sidebar ficou com um link morto para /cronista/ em TODAS as
páginas, por semanas, até alguém notar lendo. Um build verde não significava nada.

Checa no DISCO, não por HTTP: o build é a verdade, e um servidor no meio só adiciona
uma corrida (porta ocupada, servidor ainda subindo) a uma pergunta que é estática.

Sai com código 1 se houver algum link quebrado — é um gate, não um relatório.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

PUBLIC = Path("public")

# href/src de qualquer tag. O Hugo minifica e TIRA AS ASPAS dos atributos simples
# (href=/tags/ em vez de href="/tags/"), então o padrão precisa aceitar as três formas:
# aspas duplas, simples e nenhuma. Sem isso o scanner passaria limpo por um build
# minificado — encontrando zero links e dando "tudo ok" por não ter olhado nada.
ATTR = re.compile(r"""\b(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'<>`]+))""", re.I)

# Rotas servidas pelo host, não escritas pelo Hugo em public/. Não são links quebrados.
HOST_ROUTES = {"/404.html"}


def target_of(url: str) -> Path | None:
    """O arquivo em public/ que esta URL deveria servir. None = não é nosso problema."""
    parts = urlsplit(url)

    # Externo (http, mailto, tel, data:), protocol-relative (//cdn…), ou âncora pura.
    if parts.scheme or parts.netloc or not parts.path:
        return None

    path = unquote(parts.path)
    if not path.startswith("/"):
        # Relativo. Não usamos — o site inteiro fala em caminhos absolutos (relURL com
        # baseURL na raiz). Se aparecer um, é bug de outra natureza: reporte, não resolva.
        return None

    if path in HOST_ROUTES:
        return None

    # "/foo/" -> foo/index.html   |   "/foo.css" -> foo.css   |   "/foo" -> foo/index.html
    rel = path.lstrip("/")
    if path.endswith("/") or not Path(rel).suffix:
        rel = f"{rel.rstrip('/')}/index.html".lstrip("/")

    return PUBLIC / rel


def main() -> int:
    if not PUBLIC.is_dir():
        print("public/ não existe — rode `just build` antes.", file=sys.stderr)
        return 1

    pages = sorted(PUBLIC.rglob("*.html"))
    if not pages:
        print("public/ existe mas não tem HTML — build incompleto?", file=sys.stderr)
        return 1

    # url quebrada -> páginas que a citam. Agrupado por ALVO e não por página porque o
    # link morto costuma nascer num partial e se multiplicar por todo o site: um bug,
    # não trinta. Ver a contagem ("em 14 páginas") já diz que a origem é compartilhada.
    broken: dict[str, set[str]] = defaultdict(set)
    checked = 0

    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        for m in ATTR.finditer(html):
            url = next(g for g in m.groups() if g is not None)
            target = target_of(url)
            if target is None:
                continue
            checked += 1
            if not target.exists():
                broken[url].add(str(page.relative_to(PUBLIC)))

    print(f"\n  {len(pages)} páginas · {checked} links internos verificados\n")

    if not broken:
        print("  [ok] nenhum link interno quebrado.\n")
        return 0

    print(f"  [!!] {len(broken)} destino(s) quebrado(s):\n")
    for url in sorted(broken):
        origins = sorted(broken[url])
        onde = origins[0] if len(origins) == 1 else f"{len(origins)} páginas ({origins[0]}, …)"
        print(f"    {url}")
        print(f"      citado em: {onde}")
    print()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
