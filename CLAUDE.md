# dablog

Blog estático em Hugo (0.164 extended). Estética de terminal, **a11y-first**, 8 temas de
cor. PT-BR em tudo que é conteúdo e comentário; identificadores e commits em inglês.

Deploy: GitHub Pages em `https://cronistaterminal.github.io/` — site de USUÁRIO, servido
na RAIZ. É isso que faz os caminhos absolutos (`/icons/`, `/logo/`, `/fonts/`) valerem.
Um project page (`/repo/`) quebraria todos eles.

## Comandos

Tudo passa pelo `just`. Se um comando foi digitado à mão duas vezes, ele vira receita; se
a receita precisa de shebang, ela vira arquivo em `tools/`.

### Build e serviço

| Comando | O que faz |
|---|---|
| `just build` | Build de produção em `public/` + índice do Pagefind. Apaga o `public/` antes. |
| `just gate` | Compila em memória (`--renderToMemory`). O mesmo check do pre-commit. Barato. |
| `just serve` | `hugo server` — live reload, inclui drafts. **Sem busca** (o Pagefind não roda). |
| `just preview` | Serve o build de produção em primeiro plano. |
| `just up` / `just down` | Idem, mas em **fundo** — é o que usar para dirigir o browser. |
| `just hit <rota>` | Status HTTP de uma rota do servidor de fundo. |
| `just clean` | Apaga `public/`, `.lighthouse/`, `__pycache__/`. |

### Validação

`just check` roda todos de uma vez. É o que precede o fechamento de um bloco.

| Comando | Pega o quê |
|---|---|
| `just links` | Links internos mortos. **O Hugo não checa isso** — um `href` digitado à mão é texto para ele. |
| `just xml` | Feeds e sitemap bem-formados. |
| `just svg` | SVGs bem-formados — inclusive o `--` proibido dentro de comentário XML. |
| `just js` | Sintaxe do JS. O bundle é concatenado: um erro derruba todos os outros. |
| `just swatches` | Contraste WCAG dos **8 temas** + regenera `docs/themes/swatches.svg`. |
| `just audit [rota]` | Lighthouse (a11y, perf, best-practices, SEO) na rota. Sem argumento, a home. |

**`just audit` só audita o tema ATIVO.** Um `a11y 100` não diz nada sobre os outros 7 —
quem cobre esse buraco é o `just swatches`.

### Conteúdo

| Comando | O que faz |
|---|---|
| `just decay-edit` | Abre os passos do apodrecimento da 404 em texto legível (`.decay.txt`, fora do git). |
| `just decay-save` | Recodifica `.decay.txt` → `data/decay.toml` (base64), com round-trip verificado. |

Zalgo cru **não entra no repositório**: combining marks sangram para as linhas vizinhas do
editor e destroem o diff. O base64 é o artefato versionado.

## Armadilhas que já custaram caro

- **O Hugo parseia TUDO sob `layouts/` como template** — inclusive `.md`. Um README com
  `{{< shortcode >}}` quebra o build. A documentação mora em `docs/`, nunca em `layouts/`.
- **Ordem do bundle CSS não se reordena.** As 19 folhas são concatenadas na ordem listada
  em `head.html`; a cascata depende disso.
- **Estado é atributo, não classe.** Overlays setam a *propriedade* `inert`, `aria-*` e
  `hidden` — não uma classe `.is-inert`.
- **Overlays são IRMÃOS de `#page`**, nunca filhos. Ver o contrato em `docs/template/`.
- **Ícone via CSS `mask` usa caminho ABSOLUTO** (`/icons/…`, de `static/`). Relativo
  quebra no bundle com fingerprint.
- **JSON dentro de `<script>` precisa de `| safeJS`**, senão chega ao cliente escapado
  como string e o `JSON.parse` devolve texto, não objeto.
- **Link em prosa nasce azul do user-agent** (1.9:1) fora de `.post-body`. Use a classe
  `.content-link`.

## Documentação

| Arquivo | O que é |
|---|---|
| `docs/template/README.md` | O mapa do template: caixas, cascata, contrato dos overlays, shortcodes. **Canônico.** |
| `docs/deploy.md` | O runbook do GitHub Pages: workflow, versões pinadas, o pré-requisito não-versionável, o que o `act` valida. |
| `docs/themes/README.md` | Os 8 temas e todas as cores derivadas. |
| `docs/template/terminal-reference.md` | Nota histórica sobre o `panr/hugo-theme-terminal`. Não é spec. |

O que ainda falta fazer não mora em arquivo — mora nas **issues do GitHub**
(`cronistaterminal/cronistaterminal.github.io`). Antes havia um `TODO.txt` gitignorado e
um `docs/ROADMAP.md`; os dois saíram em 2026-07-23. Não recriar: um roadmap versionado
diverge do que está aberto de verdade, e um TODO gitignorado só existe na máquina de quem
o escreveu. Para saber o que falta, `gh issue list` — não um `grep`.

O protótipo standalone do layout vive na branch `layout/standalone-pass` — consulte por
`git show`, não por uma pasta espelhada.
