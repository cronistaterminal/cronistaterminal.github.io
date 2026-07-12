# dablog — atalhos de build, preview e auditoria.
#
# O `just audit` é o GATE de a11y/perf: audita o BUILD DE PRODUÇÃO (public/, com
# o bundle já concat+minify+fingerprint), não o `hugo server` — o dev server
# serve os assets crus e injeta LiveReload, então mediria uma página que nunca
# vai ao ar.

# Binário Chromium usado pelo Lighthouse: o Brave Origin (do Nilton), apontado
# DIRETO no executável real — não em /usr/bin/brave-origin-nightly, que é um
# wrapper shell. O wrapper faz `exec brave-origin "$USER_FLAGS" "$BRAVE_FLAGS"
# "$FLAG" "$@"`: com essas vars vazias E entre aspas, elas viram argumentos
# VAZIOS, que o Chromium lê como URLs-alvo -> "Multiple targets are not
# supported in headless mode" e o Lighthouse não conecta.
chrome := "/opt/brave.com/brave-origin-nightly/brave-origin"
port   := "8099"

_default:
    @just --list

# Build de produção em public/ + índice de busca.
#
# O Pagefind roda DEPOIS do Hugo, sobre o HTML já renderizado — ele é um crawler
# do próprio public/, não um plugin do Hugo. Por isso a ordem é rígida: `hugo`
# escreve o HTML, `pagefind` o lê e escreve public/pagefind/. Inverter (ou rodar
# só `hugo`) deixa o site com a palette sem índice.
#
# O que ele indexa é decidido por MARCAÇÃO no single.html (data-pagefind-body /
# -ignore / -meta / -filter), não aqui.
#
# `rm -rf public` em vez de --cleanDestinationDir: o Hugo NÃO limpa o public/ por
# padrão, só sobrescreve o que ele mesmo gera, e um public/ acumulado JÁ serviu
# HTML velho aqui mais de uma vez (datas antigas num post; e depois um <img> com
# o src do fallback num build em que o asset já existia). A flag deveria resolver,
# mas ela relata "Cleaned 0" e o resíduo continua lá — em vez de confiar no que
# ela promete, apagamos o diretório. Determinístico, e custa milissegundos.
# Vem ANTES do pagefind — se apagássemos depois, levaríamos junto o public/pagefind/
# que o indexador acabou de escrever.
build:
    rm -rf public
    hugo --gc --minify
    npx --yes pagefind@latest --site public

# Servidor de desenvolvimento (live reload, inclui drafts).
# ATENÇÃO: o `hugo server` NÃO gera o índice do Pagefind (ele serve de memória,
# sem passar pelo public/). A palette cai no estado inicial (posts recentes,
# renderizados pelo Hugo) e a busca por digitação não responde. Para exercitar a
# busca de verdade, use `just preview`.
serve:
    hugo server -D --disableFastRender

# Preview do build de produção (o mesmo bytes-a-bytes que o audit mede).
preview: build
    @echo "→ http://localhost:{{ port }}"
    cd public && python3 -m http.server {{ port }}

# Gate de a11y/perf: Lighthouse numa página. Ex.: just audit posts/algum-post/
audit path="": build
    #!/usr/bin/env bash
    set -euo pipefail
    trap 'kill ${SRV:-0} 2>/dev/null || true' EXIT
    (cd public && python3 -m http.server {{ port }} >/dev/null 2>&1) &
    SRV=$!
    # Espera o servidor aceitar conexão — dormir um tempo fixo é corrida.
    for _ in $(seq 1 40); do
        curl -sf -o /dev/null "http://localhost:{{ port }}/" && break || sleep 0.1
    done
    mkdir -p .lighthouse
    name="$(echo "{{ path }}" | tr -c 'a-zA-Z0-9' '-' | sed 's/-*$//;s/^-*//')"
    out=".lighthouse/${name:-home}.json"
    CHROME_PATH="{{ chrome }}" npx --yes lighthouse \
        "http://localhost:{{ port }}/{{ path }}" \
        --only-categories=accessibility,performance,best-practices,seo \
        --chrome-flags="--headless=new --no-sandbox" \
        --quiet --output=json --output-path="$out"
    just _lh-report "$out"

# Formata o JSON do Lighthouse: notas + os audits que REPROVARAM.
_lh-report file:
    #!/usr/bin/env python3
    import json
    d = json.load(open("{{ file }}"))
    print(f"\n  {d['finalDisplayedUrl']}\n")
    for k, v in d["categories"].items():
        score = round(v["score"] * 100)
        print(f"  [{'ok' if score == 100 else '!!'}] {k:16} {score:3}")

    # Só audits BINÁRIOS contam como reprovação. Os "numeric" (FCP, LCP, TTI…)
    # são MÉTRICAS: o score é uma curva, quase nunca crava 1.0 — listá-las como
    # falha é falso alarme e ensina a ignorar o relatório.
    bad = [
        a for a in d["audits"].values()
        if a.get("scoreDisplayMode") == "binary"
        and a.get("score") is not None
        and a["score"] < 1
    ]
    print(f"\n  {len(bad)} audit(s) reprovado(s)" + (":" if bad else "."))
    for a in bad:
        print(f"    - {a['id']}: {a['title']}")

    print("\n  métricas:")
    for m in ("first-contentful-paint", "largest-contentful-paint",
              "total-blocking-time", "cumulative-layout-shift", "speed-index"):
        a = d["audits"].get(m)
        if a and a.get("displayValue"):
            print(f"    {a['title']:28} {a['displayValue']}")
    print()
