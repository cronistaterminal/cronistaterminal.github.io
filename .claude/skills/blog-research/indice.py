#!/usr/bin/env python3
"""Gera <pesquisa>/fontes/index.md: as fontes por assunto (uma subpasta = um assunto).

Uso: indice.py <pasta-pesquisa>   (ex.: eu/blog/<slug>/pesquisa)

- Assunto: o title do resumo.md da pasta ("Resumo — X" vira "X"); sem resumo, o nome da pasta.
- Ano: prefixo do arquivo. `0430ac` = c. 430 a.C.; `0100` = c. 100 d.C.; `sd` = sem data.
- Reescreve o index.md inteiro: não editar à mão.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Raiz do vault Obsidian = _drafts/ do repo do blog (não a raiz do repo). É dela que os
# wikilinks partem: [[posts/<slug>/pesquisa/...]]. Script em <repo>/.claude/skills/blog-research/.
VAULT: Path = Path(__file__).resolve().parents[3] / "_drafts"


def campo(md: Path, chave: str) -> str:
    texto = md.read_text(encoding="utf-8", errors="replace")
    if not texto.startswith("---"):
        return ""
    fm = texto.split("---", 2)[1]
    m = re.search(rf"^{chave}:\s*(.*)$", fm, re.M)
    if not m:
        return ""
    valor = m.group(1).strip()
    if valor.startswith('"'):
        try:
            return str(json.loads(valor))
        except ValueError:
            return valor.strip('"')
    return valor.strip("'")


def ano_legivel(nome: str) -> str:
    prefixo = nome.split("-", 1)[0]
    if prefixo == "sd":
        return "s/d"
    m = re.fullmatch(r"(\d{4})(ac)?", prefixo)
    if not m:
        return "?"
    ano = int(m.group(1))
    if m.group(2):
        return f"c. {ano} a.C."
    return f"c. {ano} d.C." if ano < 1000 else str(ano)


def link(caminho: Path, alias: str) -> str:
    rel = caminho.relative_to(VAULT).with_suffix("")
    alias = alias.replace("|", "-").replace("[", "(").replace("]", ")")
    return f"[[{rel}\\|{alias}]]"


def main() -> int:
    pesquisa = Path(sys.argv[1]).resolve()
    fontes = pesquisa / "fontes"
    linhas: list[str] = [
        "---",
        'title: "Fontes por assunto"',
        "type: index",
        "---",
        "",
        "# Fontes por assunto",
        "",
        "Gerado por `.claude/skills/blog-research/indice.py`. Não editar à mão.",
        "",
    ]
    total = 0
    for pasta in sorted(p for p in fontes.iterdir() if p.is_dir()):
        resumo = pasta / "resumo.md"
        assunto = campo(resumo, "title").removeprefix("Resumo — ") if resumo.exists() else ""
        assunto = assunto or pasta.name
        itens = sorted(p for p in pasta.glob("*.md") if p.name != "resumo.md")
        linhas += [f"## {assunto}", ""]
        linhas.append(f"`{pasta.name}/` · {link(resumo, 'resumo')}" if resumo.exists() else f"`{pasta.name}/` · sem resumo")
        linhas += ["", "| Ano | Fonte | PDF | Wayback |", "| --- | ----- | --- | ------- |"]
        for md in itens:
            titulo = campo(md, "title") or md.stem
            pdf = md.with_suffix(".pdf")
            wb = campo(md, "wayback")
            linhas.append(
                f"| {ano_legivel(md.stem)} | {link(md, titulo)} | "
                f"{'[[' + str(pdf.relative_to(VAULT)) + '\\|PDF]]' if pdf.exists() else '—'} | "
                f"{'[arquivo](' + wb + ')' if wb else '—'} |"
            )
        linhas.append("")
        total += len(itens)
    (fontes / "index.md").write_text("\n".join(linhas), encoding="utf-8")
    print(f"index.md: {total} fontes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
