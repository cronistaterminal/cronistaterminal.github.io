# O template do dablog

Mapa canônico do template. Escrito **a partir do código**, não do protótipo: onde a
codebase diverge do desenho original, quem manda é a codebase.

Se você vai mexer no layout, leia as três seções que sustentam tudo o resto:
[a cascata do CSS](#a-ordem-do-css-não-reordenar), [as caixas da
página](#as-caixas-da-página) e o [contrato de modal](#o-contrato-de-modal).

- Cores, tokens e os 8 temas: [`docs/themes/README.md`](../themes/README.md).
- De onde veio a estética: [`terminal-reference.md`](terminal-reference.md) (nota histórica).

> Este arquivo mora em `docs/template/`, e não em `layouts/`, por um motivo do Hugo: **tudo
> dentro de `layouts/` é parseado como template**, inclusive um `.md`. Um README com
> `{{< shortcode >}}` ali dentro quebra o build.

---

## Os princípios que o código já segue

Não são aspirações — são regras que o código de hoje respeita, e que quebram algo se
você as violar.

1. **Falhar o build é melhor que publicar mentira.** Todo shortcode de mídia dá `errorf`
   se um caminho local não resolve. Já houve build que publicou `<img>` quebrado em
   produção; hoje ele não passa. Vale para `alt` e `title` também: eles são
   **obrigatórios** — `alt=""` é legal (imagem decorativa), *omitir o parâmetro* não é.
2. **A cor nunca é o único canal.** Onde o accent colapsa no foreground (alto-contraste,
   hacker, bsod), links de conteúdo ganham `underline` (WCAG 1.4.1). No bloco de código
   do tema monocromático, quem distingue os tokens é a tipografia — negrito, itálico —
   porque a cor ali não existe.
3. **Zero hex fora de `tokens.css` / `themes.css`.** Uma cor escrita à mão em qualquer
   outro arquivo é surda à troca de tema.
4. **O estado canônico é o atributo ARIA, não uma classe.** `aria-selected`,
   `aria-expanded`, `[hidden]`. O CSS estiliza a partir deles. Isso mantém o que o leitor
   de tela ouve e o que o olho vê como a *mesma* fonte de verdade, não duas.
5. **Controle que não controla não é exibido.** A galeria só mostra os botões depois que
   o JS monta (`[data-gallery-ready]`); sem JS, os slides empilham visíveis.

---

## Como uma página é montada

```
baseof.html          shell de toda página
├── head.html        <head>: meta, favicon, preload de fonte, bundle CSS, theme-init inline
├── header.html      → logo.html
├── [block "main"]   ← index | list | single | term | terms
├── sidebar.html
├── footer.html
├── palette.html     overlay de busca (toda página)
└── lightbox.html    overlay de imagem — SÓ se a página usa {{< gallery >}}
```

O `lightbox` é condicional (`.HasShortcode "gallery"` no `baseof`); a `palette` não, ela
é global porque `Ctrl+K` funciona em qualquer lugar.

| Template | Rota | Fonte dos dados |
|---|---|---|
| `index.html` | `/` | `site.RegularPages` tipo `posts`, paginado |
| `_default/list.html` | `/posts/` | `.Pages` |
| `_default/single.html` | um post | a própria Page |
| `_default/term.html` | `/tags/<slug>/` | `.Pages` + `.Data.Term` |
| `_default/terms.html` | `/tags/` | `.Data.Terms.ByCount` |

**Ordenação canônica: `sort … "Params.num" "desc"`** — em index, list, term, sidebar e
palette. A crônica é numerada, não cronológica; `num` é a chave, não `date`.

---

## As caixas da página

```
<body>
├── a.skip-link                        primeiro tabbável, aponta pro #main
├── div#page.container                 ← recebe o atributo `inert` quando um modal abre
│   ├── header#header.site-header
│   │   ├── div#logo.header-logo       TV CRT (SVG inline) + wordmark (PNG via mask)
│   │   ├── div#header-right.header-right
│   │   │   ├── div#accessibility.header-access   swatches de tema + toggle Aa
│   │   │   └── div#nav.header-nav                (vazio hoje)
│   │   └── button#menu-btn            hambúrguer (mobile)
│   ├── div#layout-body.body           grid 2 colunas
│   │   ├── main#main.content.term-panel   ← alvo do skip-link
│   │   └── aside#sidebar.sidebar.term-panel
│   └── footer#footer.site-footer.term-panel
├── div#palette-backdrop               ← IRMÃO de #page
└── div#lightbox-backdrop              ← IRMÃO de #page (condicional)
```

### Convenções que o código segue

- **`id` semântico + classe de componente.** O `id` é o gancho de JS/ARIA; a classe é o
  gancho de CSS. `#header.site-header`, `#sidebar.sidebar`, `#main.content`.
- **`.term-panel` é o primitivo TUI** — borda accent nos 4 lados + `position: relative`
  para ancorar o `.term-label` que corta a borda superior. Usado por `#main`, `#sidebar`,
  `#footer` e `#palette`. A moldura do bloco de código (`.code-figure`) **não** é um
  `.term-panel`: ela reusa só o `.term-label`, e redefine borda e posicionamento no
  `code.css`.
- **Prompt vivo = `span.typed#<escopo>-typed`**: `body-typed`, `sidebar-typed`,
  `footer-typed`. Os containers são `aria-hidden` — é chrome decorativo.
- **Overlay = `#<x>-backdrop` (wrapper) > `#<x>` (diálogo)**, `hidden` no HTML,
  `role="dialog" aria-modal="true"`, irmão de `#page`.
- **ids derivados de `num`:** `#post-{num}`, `#post-{num}-title`, `#more-{num}`, `#hit-{num}`.
- **`data-*` é sobretudo contrato de JS.** A exceção deliberada é o `[data-gallery-ready]`,
  que o CSS *usa* como gancho — é assim que os controles da galeria só aparecem depois que
  existe quem os escute.
- **Ícone decorativo = `<span>` vazio + CSS `mask`**, `aria-hidden`. O path é **absoluto**
  (`/icons/…`); relativo quebra no bundle fingerprinted. Os ícones sociais do footer são a
  exceção: são `<a class="icon">` com `aria-label` — o ícone *é* o link, então ele não pode
  ser escondido do leitor de tela.
- **Rótulo em duas camadas:** `title=` (mouse) + `span.sr-only` (leitor de tela). Nunca só
  `title`.
- **Não é BEM.** É prefixo-por-componente com hífen simples (`.post-*`, `.gallery-*`), e
  modificadores são classes adjetivas soltas (`.media-figure.inline-left`, `.is-playing`).

---

## O contrato de modal

Vale para a palette e o lightbox. O `mobile.js` implementa o mesmo espírito sem `inert`.

**O overlay é irmão do `#page`, nunca filho.** Ao abrir, o JS seta a propriedade
`page.inert = true` (o atributo nativo `inert`, não uma classe) para tirar o fundo do foco e
do leitor de tela — se o overlay estivesse *dentro* de `#page`, ele se auto-desativaria.

Ao abrir: `hidden = false` → `page.inert = true` → trava o scroll → **o foco entra**.
Ao fechar: reverte tudo e **devolve o foco ao gatilho**.
Fecha por: `Esc`, clique no backdrop, botão `×`.

O lightbox tem uma sutileza: ao fechar, o foco volta ao botão de zoom do **slide visível**,
não ao que abriu — porque navegar no lightbox sincroniza a galeria de fundo. O foco segue
o que o usuário vê.

---

## JavaScript

Dois canais de carregamento:

1. **`theme-init.js` — inline e blocking no `<head>`.** Aplica `data-theme`/`data-font` no
   `<html>` **antes do primeiro paint**. É o que evita o flash de tema errado, e é por isso
   que ele existe separado do `theme.js`: qualquer coisa `defer` chegaria tarde demais.
   A fonte é `?theme=` na URL **e depois** o `localStorage` — nessa precedência (o query
   param serve para deep-link e para auditar um tema específico no Lighthouse). O valor passa
   por uma whitelist, então `?theme=` não injeta atributo arbitrário.
2. **Bundle único `defer` no fim do `<body>`**, concatenado nesta ordem:
   `prompt → palette → gallery → audio → share → theme → mobile`.

Nenhum módulo exporta símbolo para outro — a ordem é convenção de leitura, não dependência.
Todo o acoplamento real é **template ↔ JS**, via `id` e `data-*`.

| Arquivo | Papel | Hooks | localStorage |
|---|---|---|---|
| `theme-init.js` | aplica tema/fonte antes do paint | `<html>`, `?theme=` | lê `theme`, `font` |
| `theme.js` | sincroniza os controles, anima o logo | `.theme-input`, `.aa-input`, `.logo-tv` | escreve `theme`, `font` |
| `prompt.js` | typewriter dos prompts | `#*-typed`, `#palette-input` | — |
| `palette.js` | busca (Ctrl+K) sobre o Pagefind | `#palette-*`, `[data-command]` | — |
| `gallery.js` | galeria + lightbox | `[data-gallery]`, `#lightbox-*` | — |
| `audio.js` | player custom | `[data-audio]` | — |
| `share.js` | compartilhar / copiar link | `[data-share]`, `[data-copy-link]` | — |
| `mobile.js` | menu hambúrguer | `#menu-btn`, `#sidebar` | — |

**Teclado.** Só a palette (`Ctrl+K`, `Esc`, `↑↓`, `Enter`, `Tab`, `Alt+1..9`) e o menu mobile (`Esc`,
`Tab`, e só com o menu aberto) escutam em `document`. A **galeria escuta no próprio root**,
de propósito, para não colidir com o `Ctrl+K` — e ela ignora o evento inteiro se o alvo for
um campo de texto, para não sequestrar as setas de quem está digitando.

Na palette, `Tab` foi **reaproveitado** para alternar o TL;DR curto/longo do resultado
ativo. Isso é seguro porque o foco nunca sai do input e o `#page` está `inert` — mas tem um
efeito colateral registrado abaixo.

**Busca.** `palette.js` importa `/pagefind/pagefind.js` dinamicamente, só na primeira
tecla digitada. O índice é escrito pelo passo `npx pagefind` do build — então **sob
`hugo server` ele não existe**, e a palette degrada com "busca indisponível — rode o build
completo". Isso é esperado, não um bug. Use `just preview` para testar busca.

**Filtros de faceta.** As tags e a época já entram no índice como facetas
(`data-pagefind-filter` no `single.html`); a palette as expõe como chips toggle. O modelo é
**"filtros quietos"**: o foco nunca sai do input. Os chips têm `tabindex="-1"` (fora da ordem
de `Tab`, que segue no toggle do TL;DR) e alternam por **clique** ou por **`Alt+1..9`** a
partir do input. O `aria-pressed` do chip é a única fonte da verdade — `activeButtons()` lê o
DOM, sem estado paralelo.

Composição das facetas, **medida no índice** (não presumida): a Pagefind trata um array cru
como **E**, então `activeFilters()` emite `{ any: [...] }` por faceta — **OU dentro** de uma
faceta (somar tags amplia), **E entre** facetas (tag ∧ época). Faceta clássica.

Os chips são renderizados pelo Hugo (progressive enhancement) e começam `hidden`;
`syncFilters()` os revela e numera (`[1]..[9]`). `tag`: os 9 mais usados (`first 9 .ByCount`).
`época`: só as que **agrupam ≥ 2 posts** — com posts 1:1 por época, um chip casaria um único
post, então o caminho existe e liga sozinho quando uma época ganha o 2º post.

O status (`#palette-status`, `aria-live`) tem **um dono por transição**: a contagem carrega o
nome dos filtros ativos (`"3 posts · filtro: python"`) — é o texto final, sobrevive à
coalescência do `polite`; e `showZeroState(msg)` recebe a mensagem do caller (input limpo →
`""`; último filtro desligado → `"filtro X removido"`).

---

## Shortcodes

`pos` posiciona a mídia e aceita `inline-left | inline-right | break-full | break-box`. Vale
em `figure`, `gallery`, `audio` e `embed` — o `slide` herda a posição da galeria que o
contém, e o `clear` não tem parâmetro nenhum.

| Shortcode | Obrigatórios | Opcionais | Falha o build se… |
|---|---|---|---|
| `figure` | `src`, `alt` | `cap`, `pos`, `w` | falta `src`; `alt` não setado; `pos` inválido; **resource local não resolve** |
| `gallery` | `label` | `pos`, `w` | falta `label`; `pos` inválido |
| `slide` | `src`, `alt` | `cap` | não está dentro de `gallery`; falta `src`/`alt`; resource não resolve |
| `audio` | `src` | `cap`, `pos`, `w` | falta `src`; `pos` inválido; resource não resolve |
| `embed` | `title` + (`yt` **ou** `src`) | `ratio`, `pos`, `w`, `cap` | falta ambos `yt`/`src`; falta `title`; `pos` inválido |
| `clear` | — | — | — |
| `diagrama` | `src` | `cap` | falta `src`; resource não resolve; arquivo não começa com `<svg` |

Notas de desenho:

- O `figure` resolve a imagem como **resource do Hugo**, então emite `width`/`height`
  reais — CLS zero. O protótipo escrevia `<img>` à mão e não podia.
- `{{< embed yt="ID" >}}` monta a URL do `youtube-nocookie` sozinho. Ninguém esquece o
  domínio sem rastreio se não for possível escrevê-lo errado.
- A galeria é **shortcodes aninhados** (`gallery` + `slide`), não um blob de JSON. Os
  `aria-label` ("2 de 3") são gerados pelo JS, que sabe o total — escritos à mão, o
  primeiro slide adicionado depois deixaria todos os outros mentindo.
- O `diagrama` põe o SVG **inline**, não em `<img>`: só assim ele lê os tokens do tema e
  recolore junto. Em `<img>` ele cairia no fallback (fosforo) nos 8 temas. O SVG vem da
  skill `diagrama-blog` (fora do repo), que escreve as cores como `var(--accent, #eec35e)`.
  No celular ele não encolhe: o wrapper rola na horizontal e é focável pelo teclado.
- Bloco de código não é shortcode: use ``` cru. A moldura vem do render hook
  `_markup/render-codeblock.html`, e ```` ```python {file="x.py"} ```` gera o label
  `$ /usr/bin/env python x.py`.

---

## A ordem do CSS (não reordenar)

Bundle único, concatenado em `head.html` nesta ordem. **Há traps de especificidade** — a
cascata é 100% ordem-de-fonte, não há `@layer`.

```
fonts → tokens → themes → base → header → logo → layout → panels →
posts → post-body → code → footnotes → media → gallery → audio →
pagination → palette → mobile
```

Camadas: infra → base → chrome → conteúdo → mídia → overlays → **responsivo (sempre por
último**, para as `@media` vencerem por ordem de fonte).

Dois traps que já morderam:

- **`.sidebar.term-panel`** (seletor composto, 2 classes) existe porque `.term-panel` vem
  *depois* de `.sidebar` no bundle e seu `position: relative` venceria o `sticky` por
  ordem de fonte — a sidebar parava de grudar.
- **`#sidebar { display: none }`** no mobile usa `id` (1,0,0) justamente para bater o
  `.sidebar.term-panel` (0,2,0).

O bundle é **um só, servido em todas as páginas**. Por isso os seletores da página de post
são escopados em `.post-single` / `.post-body`: sem o escopo, a regra vazaria e engrossaria
os chips da home.

---

## Dívidas conhecidas

Registradas porque são contratos frágeis, não porque estão erradas.

1. **O markup de um resultado da palette existe em dois lugares**: `palette.html` (estado
   zero, e fallback sem JS) e `hitHTML()` no `palette.js`. Mexeu num, mexa no outro.
2. **`.palette-close` é focável mas inalcançável por `Tab`** enquanto a palette está aberta,
   porque `Tab` virou o toggle de TL;DR. Fecha-se por `Esc` ou clique.
3. **Nada medeia o menu mobile aberto e o `Ctrl+K`** — os dois modais podem coexistir.
4. **`LOGO_LOOP_MS` (`theme.js`) duplica à mão a duração de `stripe-cycle`** no `logo.css`.
5. **`/cronista/` é link morto** na sidebar: a página não existe.
6. **Paths absolutos hardcoded** (favicons, wordmark, ícones sociais) não passam por
   `relURL` — quebram se o site for servido num subpath.
7. **Três dos quatro ícones sociais são `href="#"`** — falta `[params.social]` no `hugo.toml`.
8. **`#nav.header-nav` é uma caixa vazia**, e `pagination` é o único componente de chrome
   sem `id`.
9. **Os chips de filtro além do 9º são só-clique**: `Alt+1..9` endereça os 9 primeiros, e os
   chips têm `tabindex="-1"`, então a cauda não tem alcance por teclado. Hoje há 8 tags; se
   passar de 9, curar o conjunto (o backstop é o `ver todas` da sidebar).

---

## Modelo de dados do post

```toml
title     = 'Título da crônica'
date      = 2026-07-06     # data de PUBLICAÇÃO
num       = 1234           # nº da entrada: vira #1234, o id #post-1234, e ORDENA tudo
epoca     = '1991–2016'    # período RETRATADO pelo post — distinto de `date`
tldr      = '…'            # resumo curto, sempre visível
tldr_long = '…'            # resumo longo, atrás do [ver mais]
tags      = ['python']
```

`date` e `epoca` são eixos diferentes de propósito: um é quando o texto saiu, o outro é a
época sobre a qual ele fala. Só `tags` é taxonomia — `categories` foi **desligada de
propósito** no `hugo.toml`, porque o default do Hugo gerava um `/categories/` órfão.

O `[ver mais]` da listagem é **CSS puro** (checkbox + label), sem JS. Na página do post não
há disclosure: os dois TL;DR aparecem juntos.

**O índice de busca é só metadado.** O `data-pagefind-body` existe apenas no `single.html`
— então só posts entram no índice — e o corpo é explicitamente excluído
(`data-pagefind-ignore` no `.post-body`). Busca-se por título, tags, datas, época e TL;DR.
`tag` e `época` também são **facetas** (`data-pagefind-filter`): os chips da palette filtram
por elas (ver `## JavaScript`).

---

## Comandos

| Comando | O quê |
|---|---|
| `just serve` | dev server (com drafts). **Sem índice de busca.** |
| `just build` | `rm -rf public` → hugo → pagefind |
| `just preview` | build + servidor estático — o mesmo bytes-a-bytes que o audit mede |
| `just audit [rota]` | gate Lighthouse (a11y, perf, best-practices, SEO) |
| `just swatches` | regenera `docs/themes/swatches.svg` e **falha se algum par de texto reprovar** |

`just build` faz `rm -rf public` explícito em vez de confiar no `--cleanDestinationDir` do
Hugo — a flag relatava "Cleaned 0" e deixava HTML velho para trás. E aborta se o diretório
sobreviver ao `rm`: melhor não ter build do que ter um build metade-velho.

**O Lighthouse só audita o tema ativo.** Um `a11y 100` não diz nada sobre os outros 7 temas
— é para isso que existe o `just swatches`.
