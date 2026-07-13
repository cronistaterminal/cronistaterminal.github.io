#!/usr/bin/env python3
"""Theme swatch sheet generator for dablog.

Mirrors the token system in assets/css/tokens.css + themes.css: a theme overrides only
the MASTER triple (--background / --foreground / --accent); every derived token
recomputes via color-mix(in oklab ...) / oklch(from ...). This script reproduces those
exact formulas in pure Python (sRGB <-> OKLab <-> OKLCh, no deps), computes WCAG
contrast for the load-bearing pairs, and emits an SVG validation sheet.

The point: the SVG is a FAITHFUL preview of what the CSS renders — not a hand-painted
mock. If a token formula changes in tokens.css, change it HERE too, or the sheet lies.

    python3 tools/theme-swatches.py   ->  docs/themes/swatches.svg + contrast report

Exit code is 1 if any load-bearing pair falls below its WCAG target, so this doubles as
a gate: `just swatches` fails the same way a broken build does.
"""

from __future__ import annotations

import math
import os
import sys

# --- sRGB <-> linear ---------------------------------------------------------


def _srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c: float) -> float:
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def hex_to_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    return "#" + "".join(f"{round(max(0.0, min(1.0, c)) * 255):02x}" for c in rgb)


# --- sRGB <-> OKLab (Björn Ottosson) -----------------------------------------


def srgb_to_oklab(rgb: tuple[float, float, float]) -> tuple[float, float, float]:
    r, g, b = (_srgb_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_srgb(lab: tuple[float, float, float]) -> tuple[float, float, float]:
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v**3 for v in (l_, m_, s_))
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(_linear_to_srgb(c) for c in (r, g, bl))  # type: ignore[return-value]


# --- token formulas (must mirror tokens.css / themes.css) --------------------


def mix_oklab(a_hex: str, b_hex: str, a_pct: float) -> str:
    """color-mix(in oklab, A a_pct%, B). Linear lerp in OKLab coords."""
    la = srgb_to_oklab(hex_to_rgb(a_hex))
    lb = srgb_to_oklab(hex_to_rgb(b_hex))
    w = a_pct / 100
    return rgb_to_hex(oklab_to_srgb(tuple(la[i] * w + lb[i] * (1 - w) for i in range(3))))  # type: ignore[arg-type]


def oklch_l(hex_in: str, factor: float) -> str:
    """oklch(from X calc(l * factor) c h): scale lightness, keep chroma+hue."""
    L, a, b = srgb_to_oklab(hex_to_rgb(hex_in))
    return rgb_to_hex(oklab_to_srgb((L * factor, a, b)))


def oklch_l_abs(hex_in: str, lightness: float) -> str:
    """oklch(from X <L> c h): FIX lightness to an absolute value, keep chroma+hue.
    This is the logo-stripe ramp in themes.css — note it sets L, it doesn't scale it."""
    _, a, b = srgb_to_oklab(hex_to_rgb(hex_in))
    return rgb_to_hex(oklab_to_srgb((lightness, a, b)))


def oklch(hex_in: str) -> tuple[float, float, float]:
    """(L, C, H°) in OKLCh."""
    L, a, b = srgb_to_oklab(hex_to_rgb(hex_in))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def composite(fg_hex: str, alpha: float, bg_hex: str) -> str:
    """fg at `alpha` over opaque bg -> opaque hex (contrast math on translucent text)."""
    f, b = hex_to_rgb(fg_hex), hex_to_rgb(bg_hex)
    return rgb_to_hex(tuple(f[i] * alpha + b[i] * (1 - alpha) for i in range(3)))  # type: ignore[arg-type]


def needs_underline(accent_hex: str, fg_hex: str) -> bool:
    """WCAG 1.4.1: colour alone can't distinguish a link from body text. True only when
    luminance contrast is weak AND hue/chroma also fail to separate them — a
    neutral-on-neutral pair (white/white) or a same-hue pair (green/green). A saturated
    accent over neutral text (amber/off-white) stays distinguishable -> no underline.

    Must agree with the hand-written selector list at the bottom of themes.css."""
    if contrast(accent_hex, fg_hex) >= 1.7:
        return False
    _, c_ac, h_ac = oklch(accent_hex)
    _, c_fg, h_fg = oklch(fg_hex)
    if c_ac < 0.05 and c_fg < 0.05:
        return True  # both ~neutral: only luminance separates them, and it is weak
    if c_ac >= 0.05 and c_fg >= 0.05:
        hue_diff = abs(h_ac - h_fg)
        return min(hue_diff, 360 - hue_diff) < 45  # same hue family (green-on-green)
    return c_ac < 0.05  # one saturated, one neutral: saturation carries the distinction


# --- WCAG contrast -----------------------------------------------------------


def _luminance(hex_in: str) -> float:
    r, g, b = (_srgb_to_linear(c) for c in hex_to_rgb(hex_in))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a_hex: str, b_hex: str) -> float:
    la, lb = _luminance(a_hex), _luminance(b_hex)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def grade(ratio: float, target: float) -> str:
    if target == 0.0:  # informativo — medido, não gated
        return "info"
    if ratio >= 7:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    return "FAIL"


# --- themes: the MASTER triple, mirrored from themes.css ---------------------
# `fixed` overrides derivation. Only high-contrast needs it (see themes.css:23): with a
# WHITE accent over a near-black bg, color-mix would collapse into low-contrast greys.

THEMES = [
    {
        "id": "default", "name": "fosforo", "ref": "âmbar de fósforo (CRT)",
        "bg": "#1a170f", "fg": "#eceae5", "accent": "#eec35e",
    },
    {
        "id": "high-contrast", "name": "alto-contraste", "ref": "branco máximo (AAA)",
        "bg": "#0a0a0b", "fg": "#f4f4f5", "accent": "#ffffff",
        "fixed": {
            "accent-dim": "#e6e6e9", "accent-line": "#8a8a91", "accent-mute": "#26262a",
            "chip-text": "#f4f4f5", "accent-dark": "#cfcfd4", "sidebar-bg": "#050506",
        },
    },
    {
        "id": "zuko", "name": "zuko", "ref": "vermelho Nação do Fogo (Avatar)",
        "bg": "#160a08", "fg": "#f5e3da", "accent": "#ff4b3e",
    },
    {
        "id": "jabuticaba", "name": "jabuticaba", "ref": "magenta da casca da fruta",
        "bg": "#120a14", "fg": "#f0e9ee", "accent": "#d24a9e",
    },
    {
        "id": "ametista", "name": "ametista", "ref": "violeta (Steven Universe)",
        "bg": "#140e1c", "fg": "#ece6f5", "accent": "#b07bff",
    },
    {
        "id": "bsod", "name": "bsod", "ref": "blue screen (Windows 9x)",
        "bg": "#0000aa", "fg": "#ffffff", "accent": "#aecbff",
        # o único tema que descola o fundo do código do --sidebar-bg (themes.css:88)
        "code_bg": ("oklch-l", 0.6),
    },
    {
        "id": "c64", "name": "c64", "ref": "azul Commodore (clareado p/ AA)",
        "bg": "#0a0a16", "fg": "#e6e3f5", "accent": "#8f84ec",
    },
    {
        "id": "hacker", "name": "hacker", "ref": "verde Matrix (digital rain)",
        "bg": "#0d0208", "fg": "#bff5c8", "accent": "#00ff41",
    },
]

# rampa de luminosidade das 6 faixas do logo (themes.css:124-129). Absoluta, não escalar.
STRIPE_RAMP = [0.96, 0.82, 0.67, 0.52, 0.40, 0.29]

# arco-íris do tema default (tokens.css:51-62) — só o `default` mantém as faixas
# policromáticas; qualquer tema nomeado cai no degradé monocromático do accent.
DEFAULT_STRIPES = ["#E5141E", "#D60270", "#9B4F96", "#0038A8", "#3E31A2", "#008F11"]


def derive(theme: dict) -> dict:
    bg, fg, accent = theme["bg"], theme["fg"], theme["accent"]
    fixed = theme.get("fixed", {})
    d = {"background": bg, "foreground": fg, "accent": accent}
    d["accent-dim"] = fixed.get("accent-dim", mix_oklab(accent, bg, 70))
    d["accent-line"] = fixed.get("accent-line", mix_oklab(accent, bg, 45))
    d["accent-mute"] = fixed.get("accent-mute", mix_oklab(accent, bg, 35))
    d["accent-dark"] = fixed.get("accent-dark", oklch_l(accent, 0.6))
    d["sidebar-bg"] = fixed.get("sidebar-bg", oklch_l(bg, 0.88))
    # --code-bg herda --sidebar-bg salvo override de tema (hoje só o bsod)
    d["code-bg"] = oklch_l(bg, theme["code_bg"][1]) if "code_bg" in theme else d["sidebar-bg"]
    # --chip-text é fg @ 82% alpha; para medir contraste, compomos sobre o chip
    d["chip-text"] = fixed.get("chip-text", composite(fg, 0.82, d["accent-mute"]))
    # a cor de nome-de-função do código: color-mix(accent 85%, FOREGROUND) — mistura com o
    # fg (clareia), não com o bg. Ver code.css e a lição de --accent-dim no TODO/Bloco 3.
    d["code-fn"] = mix_oklab(accent, fg, 85)
    # faixas do logo
    d["stripes"] = (
        DEFAULT_STRIPES if theme["id"] == "default"
        else [oklch_l_abs(accent, l) for l in STRIPE_RAMP]
    )
    return d


# Pares medidos: (rótulo, a, b, alvo). Alvo 4.5 = texto (WCAG 1.4.3) e REPROVA o script.
# Alvo 0 = informativo: bordas decorativas não estão sujeitas a mínimo de contraste, então
# medimos e mostramos, mas não transformamos em gate — um gate que mente ensina a ignorá-lo.
#
# `dim/sidebar-bg` é o par que já mordeu três vezes: --accent-dim mistura o accent com o
# BACKGROUND (escurece), então como TEXTO ele afunda. Ver a memória accent-dim-sinks-as-text.
def pairs(d: dict) -> list[tuple[str, str, str, float]]:
    return [
        ("fg/bg", d["foreground"], d["background"], 4.5),
        ("accent/bg", d["accent"], d["background"], 4.5),
        ("chip/mute", d["chip-text"], d["accent-mute"], 4.5),
        ("code-fn/code-bg", d["code-fn"], d["code-bg"], 4.5),
        ("fg/code-bg", d["foreground"], d["code-bg"], 4.5),
        ("dim/sidebar-bg", d["accent-dim"], d["sidebar-bg"], 4.5),
        ("line/bg (borda)", d["accent-line"], d["background"], 0.0),
    ]


# --- SVG ---------------------------------------------------------------------

CARD_W, CARD_H, PAD, GAP = 980, 320, 28, 22
SW = 92
SWATCHES = [
    ("background", "bg"), ("foreground", "fg"), ("accent", "accent"),
    ("accent-dim", "dim"), ("accent-line", "line"), ("accent-mute", "mute"),
    ("accent-dark", "dark"), ("sidebar-bg", "side-bg"), ("code-bg", "code-bg"),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def card(theme: dict, y: float) -> tuple[str, list[str], bool]:
    d = derive(theme)
    bg, fg, accent = d["background"], d["foreground"], d["accent"]
    mute, line = d["accent-mute"], d["accent-line"]
    p = [f'<g transform="translate(0,{y})">']

    # o cartão imita o .term-panel: fundo do tema, borda accent, label cortando a borda
    p.append(f'<rect width="{CARD_W}" height="{CARD_H}" fill="{bg}" stroke="{accent}" stroke-width="1.5"/>')
    p.append(f'<rect x="{PAD - 8}" y="-2" width="{len(theme["name"]) * 13 + 20}" height="20" fill="{bg}"/>')
    p.append(f'<text x="{PAD}" y="13" font-family="monospace" font-size="15" font-weight="700" fill="{accent}">$ {esc(theme["name"])}</text>')
    p.append(f'<text x="{PAD}" y="42" font-family="monospace" font-size="11.5" fill="{fg}" opacity="0.75">{esc(theme["ref"])}  ·  data-theme="{esc(theme["id"])}"</text>')

    # linha de swatches dos tokens
    for i, (tok, lbl) in enumerate(SWATCHES):
        x = PAD + i * (SW + 6)
        p.append(f'<rect x="{x}" y="58" width="{SW}" height="38" fill="{d[tok]}" stroke="{line}" stroke-width="0.75"/>')
        p.append(f'<text x="{x}" y="112" font-family="monospace" font-size="9.5" fill="{fg}" opacity="0.85">{lbl}</text>')
        p.append(f'<text x="{x}" y="123" font-family="monospace" font-size="8.5" fill="{fg}" opacity="0.55">{d[tok]}</text>')

    # as 6 faixas do logo (arco-íris no default, degradé do accent nos demais)
    p.append(f'<text x="{PAD}" y="145" font-family="monospace" font-size="9.5" fill="{fg}" opacity="0.6">--stripe-1..6 (TV do logo)</text>')
    for i, s in enumerate(d["stripes"]):
        p.append(f'<rect x="{PAD + 168 + i * 26}" y="135" width="24" height="12" fill="{s}"/>')

    # mockup de UI: caixa com título, corpo, link, chip, e um bloco de código
    mx, my, mw, mh = PAD, 158, 560, 104
    p.append(f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" fill="none" stroke="{accent}" stroke-width="1"/>')
    p.append(f'<text x="{mx + 14}" y="{my + 24}" font-family="monospace" font-size="14" font-weight="700" fill="{accent}">#1234 Um título de post</text>')
    p.append(f'<text x="{mx + 14}" y="{my + 44}" font-family="monospace" font-size="11.5" fill="{fg}">corpo em foreground.</text>')

    underline = needs_underline(accent, fg)
    deco = ' text-decoration="underline"' if underline else ""
    p.append(f'<text x="{mx + 14}" y="{my + 63}" font-family="monospace" font-size="11.5" fill="{accent}"{deco}>um link aceso</text>')

    p.append(f'<rect x="{mx + 150}" y="{my + 50}" width="92" height="20" fill="{mute}" stroke="{line}" stroke-width="1"/>')
    p.append(f'<text x="{mx + 196}" y="{my + 64}" font-family="monospace" font-size="10.5" fill="{d["chip-text"]}" text-anchor="middle">#tag (12)</text>')

    # bloco de código: prova visual do --code-bg (o bsod é o único que o descola)
    cx, cy = mx + 270, my + 12
    p.append(f'<rect x="{cx}" y="{cy}" width="276" height="80" fill="{d["code-bg"]}" stroke="{line}" stroke-width="1"/>')
    p.append(f'<text x="{cx + 10}" y="{cy + 22}" font-family="monospace" font-size="10.5" fill="{d["code-fn"]}">def contar_epoca(ano):</text>')
    p.append(f'<text x="{cx + 10}" y="{cy + 40}" font-family="monospace" font-size="10.5" fill="{fg}">    return ano // 10</text>')
    p.append(f'<text x="{cx + 10}" y="{cy + 66}" font-family="monospace" font-size="9.5" fill="{fg}" opacity="0.6">--code-bg = {d["code-bg"]}</text>')

    # medições de contraste
    bx = mx + mw + 24
    p.append(f'<text x="{bx}" y="{my + 4}" font-family="monospace" font-size="10" fill="{fg}" opacity="0.7">contraste WCAG</text>')
    report, failed = [], False
    for j, (lbl, a, b, target) in enumerate(pairs(d)):
        r = contrast(a, b)
        g = grade(r, target)
        failed = failed or g == "FAIL"
        gc = "#ed333b" if g == "FAIL" else ("#8a8a91" if g == "info" else "#2ec27e")
        gy = my + 22 + j * 17
        p.append(f'<text x="{bx}" y="{gy}" font-family="monospace" font-size="10" fill="{fg}">{esc(lbl)}: {r:.1f}:1</text>')
        p.append(f'<text x="{bx + 150}" y="{gy}" font-family="monospace" font-size="10" font-weight="700" fill="{gc}">{g}</text>')
        report.append(f"{lbl} {r:.2f}:1 {g}")

    note = "link com underline (1.4.1)" if underline else "link distinguível por cor"
    p.append(f'<text x="{bx}" y="{my + 22 + len(pairs(d)) * 17 + 6}" font-family="monospace" font-size="9.5" fill="{fg}" opacity="0.6">{note}</text>')
    p.append("</g>")

    line_out = f"  {theme['name']:<15} " + " | ".join(report) + ("  [underline]" if underline else "")
    return "\n".join(p), [line_out], failed


def main() -> None:
    cards, report, any_failed = [], [], False
    y = 60
    for t in THEMES:
        svg, rep, failed = card(t, y)
        cards.append(svg)
        report.extend(rep)
        any_failed = any_failed or failed
        y += CARD_H + GAP

    total_h = y + PAD
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W + PAD * 2}" height="{total_h}" viewBox="0 0 {CARD_W + PAD * 2} {total_h}">',
        '<rect width="100%" height="100%" fill="#101013"/>',
        f'<text x="{PAD}" y="30" font-family="monospace" font-size="19" font-weight="700" fill="#eceae5">dablog — os 8 temas, derivados dos tokens</text>',
        f'<text x="{PAD}" y="47" font-family="monospace" font-size="11" fill="#eceae5" opacity="0.6">gerado por tools/theme-swatches.py a partir de assets/css/tokens.css + themes.css — não editar à mão</text>',
        f'<g transform="translate({PAD},0)">',
        *cards,
        "</g>",
        "</svg>",
    ]
    os.makedirs("docs/themes", exist_ok=True)
    with open("docs/themes/swatches.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    print("docs/themes/swatches.svg escrito.\n")
    print("Contraste por tema:")
    print("\n".join(report))
    if any_failed:
        print("\nFALHA: pelo menos um par reprovou o alvo WCAG.", file=sys.stderr)
        sys.exit(1)
    print("\nTodos os pares passam o alvo WCAG.")


if __name__ == "__main__":
    main()
