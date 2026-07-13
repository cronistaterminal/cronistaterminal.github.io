#!/usr/bin/env bash
# Lighthouse numa página do BUILD DE PRODUÇÃO.
#
#   tools/audit.sh <path> <port> <chrome-bin>
#
# Assume public/ já construído (o `just audit` depende do `build`).
#
# Sobe um servidor EFÊMERO, mede, e o mata no trap. Deliberadamente não reaproveita o
# `just up`: um audit não deve depender do estado da sessão — se ele encontrasse uma
# porta ocupada por um servidor apontando para um public/ ANTIGO, mediria um site que
# não existe mais e daria uma nota que não significa nada.
set -euo pipefail

path="${1:-}"
port="${2:?porta}"
chrome="${3:?binário do chrome}"

trap 'kill ${SRV:-0} 2>/dev/null || true' EXIT

python3 -m http.server "$port" --directory public >/dev/null 2>&1 &
SRV=$!

# Espera o servidor ACEITAR CONEXÃO. Dormir um tempo fixo é corrida: numa máquina lenta
# o Lighthouse chega antes do socket e falha com um erro que não é sobre a página.
for _ in $(seq 1 40); do
    curl -sf -o /dev/null "http://localhost:${port}/" && break || sleep 0.1
done

mkdir -p .lighthouse
name="$(echo "$path" | tr -c 'a-zA-Z0-9' '-' | sed 's/-*$//;s/^-*//')"
out=".lighthouse/${name:-home}.json"

CHROME_PATH="$chrome" npx --yes lighthouse \
    "http://localhost:${port}/${path}" \
    --only-categories=accessibility,performance,best-practices,seo \
    --chrome-flags="--headless=new --no-sandbox" \
    --quiet --output=json --output-path="$out"

python3 tools/lh-report.py "$out"
