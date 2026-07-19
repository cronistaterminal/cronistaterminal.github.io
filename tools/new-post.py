#!/usr/bin/env python3
"""Cria um post novo com o `slug` já congelado.

Por que existe: a URL do post é /aaaa/mm/dd/<slug>/, e o <slug> carrega 4
caracteres aleatórios que NÃO podem ser gerados no build (o Hugo é determinístico;
random-no-build cunharia URL nova a cada compilação e quebraria todo link). A
entropia é gerada UMA vez, aqui, e gravada no front matter — depois é imutável.

O `hugo new` não serve: o archetype é um template estático, sem como sortear os 4
chars. Então esta ferramenta lê o MESMO archetype (fonte única do conjunto de
campos), preenche title/date e insere o slug. Uso:

    just new-post "O título do post"
"""
import datetime
import pathlib
import random
import re
import string
import sys
import unicodedata

ALPHABET = string.ascii_lowercase + string.digits  # [a-z0-9]
ARCHETYPE = pathlib.Path("archetypes/posts.md")
POSTS_DIR = pathlib.Path("content/posts")


def kebab(text: str) -> str:
    """ASCII-fold (ç->c, ã->a, í->i…) + lowercase kebab. Controlado aqui, não
    delegado ao urlize do Hugo — a string do slug tem que ser previsível."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print('uso: just new-post "O título do post"', file=sys.stderr)
        return 2

    title = " ".join(sys.argv[1:]).strip()
    base = kebab(title)
    if not base:
        print(f"título sem caracteres utilizáveis: {title!r}", file=sys.stderr)
        return 2

    slug = f"{base}-{''.join(random.choices(ALPHABET, k=4))}"
    dest = POSTS_DIR / f"{base}.md"
    if dest.exists():
        print(f"já existe: {dest}", file=sys.stderr)
        return 1

    src = ARCHETYPE.read_text(encoding="utf-8")
    # o archetype traz title (do filename) e date ({{ .Date }}) — substituo os dois
    # por valores reais e insiro o slug logo após o title.
    src = re.sub(r"^title = .+$", f"title = '{title}'", src, count=1, flags=re.M)
    src = re.sub(r"^(title = .+\n)", rf"\1slug = '{slug}'\n", src, count=1, flags=re.M)
    src = re.sub(
        r"^date = .+$",
        f"date = {datetime.date.today().isoformat()}",
        src,
        count=1,
        flags=re.M,
    )

    dest.write_text(src, encoding="utf-8")
    print(f"criado: {dest}")
    print(f"  slug = '{slug}'  ->  /aaaa/mm/dd/{slug}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
