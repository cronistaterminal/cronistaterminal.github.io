#!/usr/bin/env python3
"""Formata o JSON do Lighthouse: notas, os audits que REPROVARAM, e as métricas.

Uso: python3 tools/lh-report.py .lighthouse/home.json

Vive aqui e não no justfile porque um script de 40 linhas dentro de uma receita é um
script sem lint, sem import e sem teste — escondido atrás de uma shebang.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Só as métricas que dizem algo sobre a EXPERIÊNCIA. O Lighthouse expõe dezenas; o resto
# é diagnóstico interno dele.
METRICAS = (
    "first-contentful-paint",
    "largest-contentful-paint",
    "total-blocking-time",
    "cumulative-layout-shift",
    "speed-index",
)


def main(path: str) -> int:
    d = json.loads(Path(path).read_text(encoding="utf-8"))

    print(f"\n  {d['finalDisplayedUrl']}\n")
    for k, v in d["categories"].items():
        score = round(v["score"] * 100)
        print(f"  [{'ok' if score == 100 else '!!'}] {k:16} {score:3}")

    # Só audits BINÁRIOS contam como reprovação. Os "numeric" (FCP, LCP, TTI…) são
    # MÉTRICAS: o score é uma curva, quase nunca crava 1.0 — listá-las como falha é falso
    # alarme e ensina a ignorar o relatório.
    bad = [
        a
        for a in d["audits"].values()
        if a.get("scoreDisplayMode") == "binary"
        and a.get("score") is not None
        and a["score"] < 1
    ]
    print(f"\n  {len(bad)} audit(s) reprovado(s)" + (":" if bad else "."))
    for a in bad:
        print(f"    - {a['id']}: {a['title']}")

    print("\n  métricas:")
    for m in METRICAS:
        a = d["audits"].get(m)
        if a and a.get("displayValue"):
            print(f"    {a['title']:28} {a['displayValue']}")
    print()

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: lh-report.py <arquivo.json>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
