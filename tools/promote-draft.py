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

5. COPIA AS IMAGENS de `<slug>/assets/` para `assets/posts/<slug>/`, que é onde o
   `{{< figure src="posts/<slug>/x.png" >}}` as procura. Recusa sobrescrever: imagem já
   publicada com o mesmo nome aborta tudo ANTES de escrever qualquer arquivo.

Cada rascunho é uma PASTA, espelhando o `eu/blog/` do vault de conhecimento:

    _drafts/posts/<slug>/
      post.md       ← o post (é o que se promove)
      pesquisa/     ← notas e fontes; nunca publicadas
      assets/       ← imagens; copiadas para assets/posts/<slug>/
      examples/     ← código citado no post

6. PROMOVE A TRADUÇÃO, se o vault tiver `post.en.md` ao lado do `post.md`. Vira
   content/posts/<mesmo-nome>.en.md (o Hugo pareia pelo nome), herdando do original date,
   num e o sufixo aleatório do slug — é a mesma entrada da crônica. As tags saem de
   data/tags.toml; `traducao` é 'maquina' salvo se o rascunho disser `traducao: humana`.
   Se o original JÁ está publicado (o caso comum: a tradução chega depois), o mesmo
   comando promove só a tradução.

O rascunho original NÃO é apagado nem alterado. Uso:

    just promote <slug>             # aceita também <slug>/ e <slug>/post.md
    just promote <slug> -n          # dry-run: mostra o resultado, não escreve
"""

import datetime
import pathlib
import random
import re
import shutil
import string
import sys
import tomllib
import unicodedata

ALPHABET = string.ascii_lowercase + string.digits  # [a-z0-9]
DRAFTS_DIR = pathlib.Path("_drafts/posts")
POSTS_DIR = pathlib.Path("content/posts")
ASSETS_DIR = pathlib.Path("assets/posts")
DRAFT_FILE = "post.md"
# A tradução em inglês, ao lado do original no vault. Vira content/posts/<base>.en.md: o
# MESMO nome-base do pt-BR (é o que o Hugo usa para parear as duas versões).
EN_DRAFT_FILE = "post.en.md"
TAGS_FILE = pathlib.Path("data/tags.toml")
TRADUCAO_VALUES = ("maquina", "humana")
# Marcadores de pasta vazia (o vault versiona assets/ vazio com .gitkeep): não são imagem.
ASSET_SKIP = {".gitkeep", ".DS_Store"}
NUM_WIDTH = 4

# Ordem dos campos no TOML gerado — espelha archetypes/posts.md.
FIELD_ORDER = ["title", "slug", "date", "draft", "traducao", "num", "recomendado", "epoca", "tldr", "tldr_long", "tags"]


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


def resolve_draft(name: str) -> pathlib.Path:
    """`<slug>`, `<slug>/` ou `<slug>/post.md` (o autocomplete do shell entrega qualquer
    um dos três) → a pasta do rascunho. Também tolera o prefixo `_drafts/posts/`."""
    name = name.strip().removeprefix(f"{DRAFTS_DIR}/").rstrip("/")
    name = name.removesuffix(f"/{DRAFT_FILE}")
    if not name or "/" in name:
        die(f"esperava o slug de uma pasta em {DRAFTS_DIR}/, recebi {name!r}")
    folder = DRAFTS_DIR / name
    if not (folder / DRAFT_FILE).is_file():
        die(f"rascunho não encontrado: {folder / DRAFT_FILE}")
    return folder


def plan_assets(folder: pathlib.Path) -> list[tuple[pathlib.Path, pathlib.Path]]:
    """Pares (origem, destino) das imagens do rascunho. Aborta se algum destino já existe —
    conferido ANTES de qualquer escrita, para o promote nunca ficar pela metade."""
    src_dir = folder / "assets"
    if not src_dir.is_dir():
        return []
    dest_dir = ASSETS_DIR / folder.name
    pairs = [
        (p, dest_dir / p.relative_to(src_dir))
        for p in sorted(src_dir.rglob("*"))
        if p.is_file() and p.name not in ASSET_SKIP
    ]
    clash = [str(d) for _, d in pairs if d.exists()]
    if clash:
        die("já existe(m) no destino, não sobrescrevo: " + ", ".join(clash))
    return pairs


def render(values: dict[str, str], body: str) -> str:
    lines = [f"{k} = {values[k]}" for k in FIELD_ORDER if k in values]
    return "+++\n" + "\n".join(lines) + "\n+++\n\n" + body.strip() + "\n"


def map_tags(pt_tags: list[str]) -> list[str]:
    """Tags do post em inglês = as do pt-BR passadas por data/tags.toml. Tag sem tradução
    aborta: o mapa é a ponte que o /en/ usa para mostrar as tags dos posts não traduzidos,
    e uma tag fora dele apareceria em pt-BR para sempre sem ninguém notar."""
    table = tomllib.loads(TAGS_FILE.read_text(encoding="utf-8"))
    missing = [t for t in pt_tags if t not in table]
    if missing:
        die(f"tag(s) sem tradução em {TAGS_FILE}: {', '.join(missing)} — acrescente lá")
    return [table[t] for t in pt_tags]


def plan_translation(folder: pathlib.Path, base: str, pt: dict) -> tuple[pathlib.Path, str] | None:
    """A versão em inglês, se o vault tiver `post.en.md`. `pt` = os campos do original
    (valores Python, não TOML). Devolve (destino, conteúdo) ou None.

    Do ORIGINAL vêm, sem negociação: date, num, recomendado e o sufixo aleatório do slug —
    as duas versões são a MESMA entrada da crônica. Do rascunho em inglês vêm: title (que
    gera a parte legível do slug), os dois TL;DR, a epoca (opcional; sem ela, a do
    original) e `traducao` (maquina | humana; default maquina — a tradução por IA vem
    primeiro, e o aviso só sai quando alguém declara o contrário). As tags NÃO se
    escrevem no rascunho: saem de data/tags.toml.
    """
    src = folder / EN_DRAFT_FILE
    if not src.is_file():
        return None
    dest = POSTS_DIR / f"{base}.en.md"
    if dest.exists():
        die(f"já existe: {dest}")

    fm, body = parse_yaml_front_matter(src.read_text(encoding="utf-8"))
    title = str(fm.get("title") or "").strip()
    if not title:
        die(f"{src} não tem `title` no front matter")
    en_base = kebab(title)
    if not en_base:
        die(f"título em inglês sem caracteres utilizáveis para slug: {title!r}")
    if fm.get("tags"):
        die(f"{src}: não escreva `tags` na tradução — elas saem de {TAGS_FILE}")

    tldr, body = extract_callout(body, "tldr")
    tldr_long, body = extract_callout(body, "tldr-long")
    body = strip_obsidian_comments(body)
    for label, value in (("tldr", tldr), ("tldr-long", tldr_long)):
        if not value:
            die(f"não achei o callout `> [!{label}]` em {src}")

    traducao = str(fm.get("traducao") or "maquina")
    if traducao not in TRADUCAO_VALUES:
        die(f"{src}: traducao = {traducao!r}; use um de: {', '.join(TRADUCAO_VALUES)}")

    suffix = str(pt["slug"])[-4:]
    values = {
        "title": toml_str(title),
        "slug": toml_str(f"{en_base}-{suffix}"),
        "date": str(pt["date"]),
        "draft": "false",
        "num": toml_str(str(pt["num"])),
        "epoca": toml_str(str(fm.get("epoca") or pt.get("epoca") or "")),
        "tldr": toml_str(tldr),
        "tldr_long": toml_str(tldr_long),
        "tags": "[" + ", ".join(toml_str(t) for t in map_tags(list(pt.get("tags") or []))) + "]",
    }
    if traducao == "maquina":
        values["traducao"] = toml_str("maquina")
    if pt.get("recomendado") is True:
        values["recomendado"] = "true"
    return dest, render(values, body)


def write_translation(plan: tuple[pathlib.Path, str], dry_run: bool) -> None:
    dest, out = plan
    if dry_run:
        print(f"--- dry-run: tradução -> {dest} ---\n")
        print(out)
        return
    dest.write_text(out, encoding="utf-8")
    slug = re.search(r"^slug = ['\"](.+?)['\"]$", out, re.M).group(1)
    print(f"tradução promovida: {dest}  ->  /en/…/{slug}/")


def main() -> int:
    args = [a for a in sys.argv[1:] if a not in ("-n", "--dry-run")]
    dry_run = len(args) != len(sys.argv[1:])
    if not args:
        print("uso: just promote <slug> [-n]", file=sys.stderr)
        return 2

    folder = resolve_draft(args[0])
    src = folder / DRAFT_FILE

    fm, body = parse_yaml_front_matter(src.read_text(encoding="utf-8"))

    title = str(fm.get("title") or "").strip()
    if not title:
        die("o rascunho não tem `title` no front matter")

    base = kebab(title)
    if not base:
        die(f"título sem caracteres utilizáveis para slug: {title!r}")

    dest = POSTS_DIR / f"{base}.md"
    if dest.exists():
        # Original já publicado: o caso normal da TRADUÇÃO, que chega depois. Promove só o
        # post.en.md, herdando date/num/sufixo do slug do que está no ar.
        if not (folder / EN_DRAFT_FILE).is_file():
            die(f"já existe: {dest} (e não há {EN_DRAFT_FILE} para promover)")
        m = re.match(r"^\+\+\+\n(.*?)\n\+\+\+", dest.read_text(encoding="utf-8"), re.S)
        if not m:
            die(f"{dest} não tem front matter TOML")
        write_translation(plan_translation(folder, base, tomllib.loads(m.group(1))), dry_run)
        if not dry_run:
            print("  próximo passo: just check")
        return 0

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

    out = render(values, body)

    assets = plan_assets(folder)
    # Tradução junto com o original (as duas no vault na hora do promote). Planejada ANTES
    # de qualquer escrita, como as imagens: se ela abortar, nada foi gravado.
    pt_plain = {"slug": slug, "date": datetime.date.today(), "num": num,
                "epoca": fm.get("epoca") or "", "tags": fm.get("tags") or [],
                "recomendado": fm.get("recomendado") is True}
    translation = plan_translation(folder, base, pt_plain)

    if dry_run:
        print(f"--- dry-run: {src} -> {dest} ---\n")
        print(out)
        for a_src, a_dest in assets:
            print(f"--- dry-run: {a_src} -> {a_dest}")
        if translation:
            write_translation(translation, dry_run)
        return 0

    dest.write_text(out, encoding="utf-8")
    if translation:
        write_translation(translation, dry_run)
    for a_src, a_dest in assets:
        a_dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(a_src, a_dest)
    print(f"promovido: {src} -> {dest}")
    if assets:
        print(f"  {len(assets)} imagem(ns) -> {ASSETS_DIR / folder.name}/")
    print(f"  num  = '{num}'")
    print(f"  slug = '{slug}'  ->  /{datetime.date.today():%Y/%m/%d}/{slug}/")
    print(f"  o rascunho foi PRESERVADO em {src} (nada foi apagado)")
    print("  próximo passo: just check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
