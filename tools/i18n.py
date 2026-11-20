#!/usr/bin/env python3
"""Confere as strings de interface (i18n/*.toml) contra quem as usa.

Existe porque o Hugo não reclama de nenhum destes erros: `{{ i18n "chave" }}` com chave
inexistente renderiza VAZIO (um aria-label="" passa no build e some para o leitor de
tela), e o JS só descobre a chave ausente quando ela aparece crua na tela.

Quatro checagens, todas estáticas (nada de build):

1. PARIDADE: toda chave de um idioma existe no outro.
2. TEMPLATES: toda chave citada em `i18n "x"` (layouts/) existe nos dois idiomas.
3. JS: toda chave citada em `tr("x")` (assets/js/) está na lista $jsKeys do baseof —
   que é o que de fato chega ao navegador — e existe nos dois idiomas.
4. PLACEHOLDER: chave usada pelo JS (js_*) não pode ter `{{ }}`: o Hugo resolveria no
   build, com contexto vazio, antes de o tr() ver o texto.

Sai com código 1 se algo reprovar — é um gate, não um relatório.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("pt-br", "en")

# `i18n "chave"` e `T "chave"`; chave montada (printf "month_%d") não é literal — os
# meses são conferidos à parte, abaixo.
TEMPLATE_KEY = re.compile(r'\b(?:i18n|T)\s+"([A-Za-z0-9_]+)"')
# tr("chave") e tr(cond ? "a" : "b"): toda string literal dentro da chamada é chave.
JS_CALL = re.compile(r"\btr\(([^()]*(?:\([^()]*\)[^()]*)*)\)")
JS_STRING = re.compile(r'"([A-Za-z0-9_]+)"')
BASEOF_KEYS = re.compile(r"\$jsKeys\s*:=\s*slice((?:\s+\"[A-Za-z0-9_]+\")+)")


def main() -> int:
    errors: list[str] = []
    keys = {lang: set(tomllib.loads((ROOT / f"i18n/{lang}.toml").read_text())) for lang in LANGS}
    tables = {lang: tomllib.loads((ROOT / f"i18n/{lang}.toml").read_text()) for lang in LANGS}

    a, b = LANGS
    for k in sorted(keys[a] - keys[b]):
        errors.append(f"só em {a}.toml: {k}")
    for k in sorted(keys[b] - keys[a]):
        errors.append(f"só em {b}.toml: {k}")
    both = keys[a] & keys[b]

    used_tpl: dict[str, str] = {}
    for p in sorted((ROOT / "layouts").rglob("*")):
        if p.is_file():
            for m in TEMPLATE_KEY.finditer(p.read_text()):
                used_tpl.setdefault(m.group(1), str(p.relative_to(ROOT)))
    for n in range(1, 13):
        used_tpl.setdefault(f"month_{n}", "single.html/post-card.html (printf)")
        used_tpl.setdefault(f"month_{n}_abbr", "single.html/post-card.html (printf)")
    for k, where in sorted(used_tpl.items()):
        if k not in both:
            errors.append(f"template sem tradução: {k} ({where})")

    baseof = (ROOT / "layouts/_default/baseof.html").read_text()
    m = BASEOF_KEYS.search(baseof)
    shipped = set(JS_STRING.findall(m.group(1))) if m else set()
    if not m:
        errors.append("baseof.html: lista $jsKeys não encontrada")
    for k in sorted(shipped - both):
        errors.append(f"$jsKeys sem tradução: {k}")

    used_js: dict[str, str] = {}
    for p in sorted((ROOT / "assets/js").glob("*.js")):
        if p.name == "i18n.js":
            continue
        for call in JS_CALL.finditer(p.read_text()):
            for k in JS_STRING.findall(call.group(1)):
                used_js.setdefault(k, p.name)
    for k, where in sorted(used_js.items()):
        if k not in shipped:
            errors.append(f"tr(\"{k}\") em {where} fora do $jsKeys do baseof")
        if k not in both:
            errors.append(f"tr(\"{k}\") em {where} sem tradução")

    for lang in LANGS:
        for k, v in tables[lang].items():
            if k in shipped and isinstance(v, str) and "{{" in v:
                errors.append(f"{lang}.toml: {k} é do JS e tem {{{{ }}}} — use {{nome}}")

    if errors:
        print("\n".join(f"  [x] {e}" for e in errors))
        return 1
    print(f"  [ok] i18n: {len(both)} chaves nos {len(LANGS)} idiomas; "
          f"{len(used_tpl)} usadas em template, {len(used_js)} no JS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
