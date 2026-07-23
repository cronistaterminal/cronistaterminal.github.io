#!/usr/bin/env python3
"""Promove um rascunho de `_drafts/posts/` para `content/posts/`.

O rascunho vive num vault Obsidian (gitignorado) e usa front matter YAML, porque o
Obsidian só entende YAML — é o que faz o painel de Propriedades funcionar enquanto se
escreve. O repositório usa TOML. Esta ferramenta é a ponte, e ela faz quatro coisas que
não dá para fazer à mão sem errar:

1. CUNHA O SLUG, uma vez. A URL é /aaaa/mm/dd/<slug>/ e o slug carrega 4 caracteres
   aleatórios. Eles NÃO podem ser gerados no build (o Hugo é determinístico: random no
   build cunharia URL nova a cada compilação e quebraria todo link). Mesma regra do
   tools/new-post.py.

2. ATRIBUI O `num`, incremental, com 4 dígitos e zeros à esquerda ('0000', '0001'...).
   `num` NÃO é decorativo: é a chave de ordenação de TODAS as listagens (home, /posts/,
   /tags/, sidebar, palette, RSS, recomendados — sete `sort "Params.num" "desc"`), e é
   `id` do DOM (#post-NNNN, more-NNNN, hit-NNNN). Colisão duplicaria id e quebraria o
   "ver mais", que é CSS-only (um <label for> apontando o checkbox).

   Ele é STRING, não inteiro: TOML proíbe zeros à esquerda em inteiro (`num = 0000` é
   erro de parse). Isso rende um discriminador de graça — os posts seed legados têm
   `num` INTEIRO (1220…1234), os do esquema novo têm STRING. Então o próximo número sai
   de `max(num que é string) + 1`, sem limiar mágico. Quando os seed saírem, a regra
   continua idêntica.

3. EXTRAI OS DOIS TL;DR dos callouts `> [!tldr]` / `> [!tldr-long]` e os REMOVE do corpo.
   Remover é obrigatório: o single.html já renderiza os dois no abstract, então deixá-los
   no corpo publicaria o resumo duas vezes.

4. A `date` é a data de HOJE — a data de publicação, não a de escrita.

O rascunho original NÃO é apagado nem alterado. Uso:

    just promote <arquivo>          # nome com ou sem .md
    just promote <arquivo> -n       # dry-run: mostra o resultado, não escreve
"""

import datetime
import pathlib
import random
import re
import string
import sys
import tomllib
import unicodedata

ALPHABET = string.ascii_lowercase + string.digits  # [a-z0-9]
DRAFTS_DIR = pathlib.Path("_drafts/posts")
POSTS_DIR = pathlib.Path("content/posts")
NUM_WIDTH = 4

# Ordem dos campos no TOML gerado — espelha archetypes/posts.md.
FIELD_ORDER = ["title", "slug", "date", "draft", "num", "recomendado", "epoca", "tldr", "tldr_long", "tags"]


def die(msg: str) -> None:
    print(f"erro: {msg}", file=sys.stderr)
    raise SystemExit(1)


def kebab(text: str) -> str:
    """ASCII-fold (ç->c, ã->a, í->i…) + lowercase kebab. Controlado aqui, não delegado ao
    urlize do Hugo — a string do slug tem que ser previsível."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def toml_str(value: str) -> str:
    """Aspas simples (literal) por padrão, como o resto do repositório. Se o texto contém
    `'`, cai para aspas duplas (basic string) com escape — é o que os posts existentes já
    fazem à mão quando o resumo tem apóstrofo."""
    if "'" not in value:
        return f"'{value}'"
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_yaml_front_matter(text: str) -> tuple[dict, str]:
    """Front matter YAML mínimo: `chave: valor` e listas inline `[a, b]`.

    Deliberadamente NÃO usa PyYAML — a ferramenta roda no pre-commit e no fluxo do Nilton,
    e depender de um pacote externo para ler 9 campos planos é superfície de falha à toa.
    O escopo é o que o template gera; qualquer coisa fora disso vira erro explícito, não
    interpretação criativa.
    """
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        die("o rascunho não começa com front matter YAML (---)")
    raw, body = m.group(1), m.group(2)

    data: dict = {}
    for line in raw.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            die(f"linha de front matter sem `:` -> {line!r}")
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()

        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
        elif value in ("true", "false"):
            data[key] = value == "true"
        else:
            data[key] = value.strip("'\"")
    return data, body


def extract_callout(body: str, kind: str) -> tuple[str, str]:
    """Extrai um callout do Obsidian e o devolve junto do corpo SEM ele.

    Formato aceito (o que o Obsidian escreve):
        > [!tldr]            opcionalmente seguido de + ou - (dobrável) e de um título
        > primeira linha
        > segunda linha

    As linhas viram um parágrafo só: o campo do front matter é uma frase corrida, não
    markdown multi-linha.
    """
    pattern = re.compile(
        rf"^> *\[!{re.escape(kind)}\][+-]? *.*?$\n((?:^>.*$\n?)*)",
        re.M,
    )
    m = pattern.search(body)
    if not m:
        return "", body

    lines = [re.sub(r"^> ?", "", ln) for ln in m.group(1).split("\n")]
    content = " ".join(ln.strip() for ln in lines if ln.strip())
    return content, body[: m.start()] + body[m.end() :]


def strip_obsidian_comments(body: str) -> str:
    """Remove blocos `%%…%%`.

    `%%` é sintaxe EXCLUSIVA do Obsidian: some na leitura do editor, mas o Hugo publica
    como texto literal. O guia do template mora num desses blocos, então sem esta remoção
    todo post promovido sairia com a documentação do template colada no corpo. Não dá para
    depender de "lembre de apagar" — some silenciosamente enquanto se escreve e reaparece
    publicado.

    A remoção é não-gulosa, então um marcador SOLTO dentro do bloco fecharia o par cedo e
    deixaria sobra. O Obsidian tem a mesma ambiguidade — não há regex que resolva. Por isso
    o que sobra é conferido depois: melhor abortar do que publicar meio comentário.
    """
    cleaned = re.sub(r"%%.*?%%", "", body, flags=re.S)
    if "%%" in cleaned:
        die(
            "sobrou um marcador de comentário `%%` no corpo — provavelmente há um par "
            "solto DENTRO de um bloco de comentário, que fechou o bloco antes da hora"
        )
    return cleaned


def next_num(posts: list[dict]) -> str:
    """Próximo `num` do esquema novo. Ver o docstring do módulo: só entram os que são
    STRING — inteiro é seed legado e não participa da sequência."""
    used = []
    for fm in posts:
        n = fm.get("num")
        if isinstance(n, str) and n.isdigit():
            used.append(int(n))
    nxt = max(used) + 1 if used else 0
    if nxt >= 10**NUM_WIDTH:
        die(f"a sequência de num estourou {NUM_WIDTH} dígitos (chegou em {nxt})")
    return str(nxt).zfill(NUM_WIDTH)


def read_existing() -> list[dict]:
    out = []
    for p in sorted(POSTS_DIR.glob("*.md")):
        m = re.match(r"^\+\+\+\n(.*?)\n\+\+\+", p.read_text(encoding="utf-8"), re.S)
        if m:
            out.append(tomllib.loads(m.group(1)))
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if a not in ("-n", "--dry-run")]
    dry_run = len(args) != len(sys.argv[1:])
    if not args:
        print("uso: just promote <arquivo> [-n]", file=sys.stderr)
        return 2

    name = args[0]
    src = DRAFTS_DIR / (name if name.endswith(".md") else f"{name}.md")
    if not src.exists():
        die(f"rascunho não encontrado: {src}")

    fm, body = parse_yaml_front_matter(src.read_text(encoding="utf-8"))

    title = str(fm.get("title") or "").strip()
    if not title:
        die("o rascunho não tem `title` no front matter")

    base = kebab(title)
    if not base:
        die(f"título sem caracteres utilizáveis para slug: {title!r}")

    dest = POSTS_DIR / f"{base}.md"
    if dest.exists():
        die(f"já existe: {dest}")

    tldr, body = extract_callout(body, "tldr")
    tldr_long, body = extract_callout(body, "tldr-long")
    body = strip_obsidian_comments(body)
    for label, value in (("tldr", tldr), ("tldr-long", tldr_long)):
        if not value:
            die(f"não achei o callout `> [!{label}]` no corpo do rascunho")

    existing = read_existing()
    num = next_num(existing)
    if any(str(p.get("num")) == num for p in existing):
        die(f"num {num} já está em uso — a sequência está inconsistente")

    slug = f"{base}-{''.join(random.choices(ALPHABET, k=4))}"
    if any(p.get("slug") == slug for p in existing):
        die(f"colisão de slug em {slug} — rode de novo (os 4 chars são sorteados)")

    values = {
        "title": toml_str(title),
        "slug": toml_str(slug),
        "date": datetime.date.today().isoformat(),  # data de PUBLICAÇÃO
        "draft": "false",
        "num": toml_str(num),
        "epoca": toml_str(str(fm.get("epoca") or "")),
        "tldr": toml_str(tldr),
        "tldr_long": toml_str(tldr_long),
        "tags": "[" + ", ".join(toml_str(t) for t in fm.get("tags") or []) + "]",
    }
    # `recomendado` é flag da curadoria do /cronista/: só sai no arquivo quando é true.
    # Ausente já é falso para o Hugo, e um `= false` em todo post seria ruído.
    if fm.get("recomendado") is True:
        values["recomendado"] = "true"

    lines = [f"{k} = {values[k]}" for k in FIELD_ORDER if k in values]
    out = "+++\n" + "\n".join(lines) + "\n+++\n\n" + body.strip() + "\n"

    if dry_run:
        print(f"--- dry-run: {src} -> {dest} ---\n")
        print(out)
        return 0

    dest.write_text(out, encoding="utf-8")
    print(f"promovido: {src} -> {dest}")
    print(f"  num  = '{num}'")
    print(f"  slug = '{slug}'  ->  /{datetime.date.today():%Y/%m/%d}/{slug}/")
    print(f"  o rascunho foi PRESERVADO em {src} (nada foi apagado)")
    print("  próximo passo: just check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
