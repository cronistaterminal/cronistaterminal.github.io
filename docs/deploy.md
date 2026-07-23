# Deploy do dablog

O site vai ao ar em **GitHub Pages**, em `https://cronistaterminal.github.io/`.
O workflow é `.github/workflows/deploy.yml`; este documento é o mapa dele.

## O que faz

O GitHub Pages **não constrói Hugo** — ele só serve arquivos. Então o workflow
faz o build e publica o `public/` como artefato de Pages. Dois jobs:

1. **`build`** — instala o Hugo extended, roda o mesmo build do `just build`
   (`hugo --gc --minify` → `npx pagefind --site public`) e sobe o `public/` via
   `actions/upload-pages-artifact`.
2. **`deploy`** — `actions/deploy-pages` publica o artefato.

Dispara em `push` na `main` e por `workflow_dispatch` (à mão, na aba Actions).

## Site de USUÁRIO → servido na RAIZ

`cronistaterminal.github.io` é um site de usuário/org, então o GitHub serve na
**raiz** do domínio. Isso **não é detalhe**: o site tem paths absolutos
hardcoded (`/icons/`, `/logo/`, `/fonts/` nos favicons, no wordmark e nas masks
de CSS) que não passam por `relURL`. Num project page (`…github.io/dablog/`)
todos quebrariam de uma vez. A `baseURL` fixada no `hugo.toml` é a correta e o
workflow **não a sobrescreve** com `--baseURL`.

## Pré-requisito que NÃO dá para versionar

Em **Settings › Pages › Build and deployment**, a fonte tem que ser
**"GitHub Actions"**, não "Deploy from a branch". Sem isso o `deploy-pages`
falha com `Get Pages site failed`. É a única peça do deploy que mora fora do
repositório — confirme uma vez antes do primeiro run.

## Versões pinadas

| Var | Valor | Regra |
|---|---|---|
| `HUGO_VERSION` | `0.164.0` | = o `hugo version` local. **Tem que ser a extended** (SCSS + withdeploy). |
| `PAGEFIND_VERSION` | `1.5.2` | pinada para build determinístico (o índice não deve variar por um `@latest` que andou). |

As **actions** (`uses:`) são a exceção: ficam em **major flutuante** (`@v7`, `@v6`, `@v5`)
para receber patch de segurança sem commit. O preço é que elas são a única parte do
deploy que muda sozinha. Em 2026-07-23 subiram de `@v4`/`@v5`/`@v3` porque o runner
avisava que as anteriores miravam **Node.js 20** e estavam sendo *forçadas* a rodar em
Node.js 24 — aviso, não erro, mas com prazo. Se esse aviso voltar, a verificação é o
`runs.using` do `action.yml` **na tag**, não o número da release; e lembrar que
`upload-pages-artifact` é *composite* — quem roda Node ali é o `upload-artifact` que ela
fixa por SHA.

**Para subir uma versão**: mude a env var no `deploy.yml` **e** o `hugo version`
local — a fonte da verdade é a paridade entre os dois. O Hugo vem do `.deb`
oficial (`curl -sSLf`, que falha em 4xx/5xx) em vez de uma action de terceiro:
menos superfície de confiança e a versão casa exatamente com a local.

## O que o `act` valida — e o que não valida

`act` roda o workflow em Docker local. Ele valida o **caminho buildável**: o
`.deb` do Hugo instala, a versão pina, o Node sobe, `hugo --minify` e `pagefind`
escrevem o `public/`. O que ele **não** valida são as três etapas que dependem do
backend real de Pages — `configure-pages`, `upload-pages-artifact`,
`deploy-pages` batem na API do GitHub e falham localmente com 404. Isso é
esperado, não um bug do workflow: essas só se confirmam no ar.

```
act push -j build -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## `.nojekyll`

Publicando via artefato (`deploy-pages`), o Jekyll **não** roda, então o
`.nojekyll` é tecnicamente supérfluo. Ele mora em `static/.nojekyll` (o Hugo o
copia para a raiz do `public/`) como seguro barato: se um dia o deploy virar
por branch, o Jekyll passaria a rodar e ignoraria as `_pastas`.

## Itens que só se confirmam NO AR

- `/pagefind/` servido com o Content-Type certo (o `.wasm` em especial) — o
  GitHub Pages não deixa custom headers; se vier errado, a busca morre em
  produção e passa no `just preview`.
- O `/404.html` (o GitHub Pages serve o do Bloco 6 automaticamente).
- Domínio próprio / DNS — só se sair do `…github.io` (CNAME + config).
