# Os 8 temas

![swatches dos 8 temas](swatches.svg)

O `swatches.svg` acima é **gerado**, não desenhado: `tools/theme-swatches.py` reimplementa
em Python as mesmas fórmulas de cor do CSS (`color-mix(in oklab …)`, `oklch(from …)`), então
o que você vê é o que o browser vai renderizar. Se um token mudar no `tokens.css`, mude
também na ferramenta — senão a folha passa a mentir.

```
just swatches      # regenera o SVG e mede o contraste. Falha se um par de TEXTO reprovar.
```

---

## A regra: um tema declara três cores

Um tema sobrescreve **só o trio mestre** — `--background`, `--foreground`, `--accent`. Todo
o resto (`--accent-dim/line/mute/dark`, `--chip-text`, `--sidebar-bg`, `--code-bg` e as 6
faixas do logo) **recalcula sozinho**, porque as fórmulas em `tokens.css` releem o `--accent`
vencedor no seletor do tema.

É por isso que adicionar um tema custa três linhas:

```css
:root[data-theme="novo"] {
    color-scheme: dark;
    --background: #…;
    --foreground: #…;
    --accent: #…;
}
```

As misturas são feitas em **OKLab**, não em sRGB: misturar em sRGB passa por tons lamacentos
e a matiz do tema se perde pelo caminho.

### As duas exceções

**`high-contrast` fixa os derivados em hex.** Com accent branco sobre fundo quase-preto, a
mistura cairia em cinzas de baixo contraste — sobretudo o chip. A fórmula que serve sete
temas quebra no caso extremo, então ali os valores são cravados à mão.

**`bsod` descola o `--code-bg` do `--sidebar-bg`.** Nos outros temas o azul não existe; ali
o `#0000aa` é vivo e saturado, e um bloco de código inteiro sobre ele vibra. É o único
motivo pelo qual o token `--code-bg` existe separado.

---

## As cores

`default` é o `:root` base e **nunca seta `data-theme`** — por isso ele é o único que
mantém a TV do logo em arco-íris; qualquer tema nomeado cai num degradé monocromático do
seu accent.

As três primeiras colunas são **declaradas**; as demais são **derivadas** (exceto no
`high-contrast`, onde são fixas).

| tema | `--background` | `--foreground` | `--accent` | `--accent-quiet` | `--accent-line` | `--accent-mute` | `--accent-dark` | `--sidebar-bg` | `--code-bg` |
|---|---|---|---|---|---|---|---|---|---|
| **fosforo** *(default)* | `#1a170f` | `#eceae5` | `#eec35e` | `#eecf8c` | `#715e31` | `#5c4d2a` | `#845c00` | `#14110a` | `#14110a` |
| **alto-contraste** | `#0a0a0b` | `#f4f4f5` | `#ffffff` | `#fcfcfc` | `#8a8a91` | `#26262a` | `#cfcfd4` | `#050506` | `#050506` |
| **zuko** | `#160a08` | `#f5e3da` | `#ff4b3e` | `#ff8170` | `#752820` | `#5e211b` | `#9d0000` | `#120605` | `#120605` |
| **jabuticaba** | `#120a14` | `#f0e9ee` | `#d24a9e` | `#e07eb6` | `#61264d` | `#4e203f` | `#7d0055` | `#0e0610` | `#0e0610` |
| **ametista** | `#140e1c` | `#ece6f5` | `#b07bff` | `#c19dfe` | `#543b79` | `#453162` | `#5f20a1` | `#0f0917` | `#0f0917` |
| **bsod** | `#0000aa` | `#ffffff` | `#aecbff` | `#c6dbff` | `#416fd3` | `#2e5dca` | `#4b6492` | `#04009c` | `#12007d` |
| **c64** | `#0a0a16` | `#e6e3f5` | `#8f84ec` | `#a7a1f0` | `#403c6d` | `#333058` | `#463393` | `#070712` | `#070712` |
| **hacker** | `#0d0208` | `#bff5c8` | `#00ff41` | `#68fd76` | `#306529` | `#2b4c23` | `#008b00` | `#0a0106` | `#0a0106` |

### De onde vem cada um

| tema | referência | nota |
|---|---|---|
| fosforo | âmbar de fósforo dos monitores CRT | o default |
| alto-contraste | branco máximo | todos os pares ≥ 7:1 (AAA) |
| zuko | vermelho da Nação do Fogo (*Avatar*) | |
| jabuticaba | magenta da casca da fruta | |
| ametista | violeta (*Steven Universe*) | |
| bsod | a tela azul do Windows 9x | o único com fundo **azul** — a piada toda |
| c64 | azul do Commodore 64 | o azul autêntico (`#7c70da`) dava 2.3:1; o VIC-II era para CRT. Clareado para `#8f84ec` |
| hacker | verde Matrix (*digital rain*) | |

### As faixas do logo

A TV do logo tem 6 faixas. No `default` elas são o arco-íris da identidade:

| | | | | | |
|---|---|---|---|---|---|
| `#E5141E` | `#D60270` | `#9B4F96` | `#0038A8` | `#3E31A2` | `#008F11` |
| atari | rosa | roxo | azul | c64 | hacker |

Em **qualquer** tema nomeado, uma regra única as substitui por um degradé do accent —
luminosidade fixa em `0.96 / 0.82 / 0.67 / 0.52 / 0.40 / 0.29`, matiz e croma preservados.
Seis tons do accent, claro para escuro, imitando a iluminação de um CRT colorido. Nenhum
tema declara `--stripe-*`: a recoloração é automática.

No alto-contraste, o accent é branco (croma ≈ 0), então o degradé cai em cinzas de graça.

---

## Contraste

Os pares medidos e o alvo de cada um. **Alvo 4.5:1** vale para texto (WCAG 1.4.3) e
**reprova** o `just swatches`. A borda é medida mas não é gate: contorno decorativo não está
sujeito a mínimo de contraste, e um gate que mente ensina a ignorá-lo.

| par | o que é | alvo |
|---|---|---|
| `fg/bg` | texto do corpo | 4.5 |
| `accent/bg` | link, título, prompt | 4.5 |
| `chip/mute` | texto do chip de tag em repouso | 4.5 |
| `code-fn/code-bg` | nome de função no bloco de código | 4.5 |
| `fg/code-bg` | corpo do código | 4.5 |
| `quiet/bg` | `--accent-quiet` sobre a página | 4.5 |
| `quiet/sidebar-bg` | `--accent-quiet` sobre a sidebar | 4.5 |
| `hit-head/mute` | título do resultado **selecionado** da busca | 4.5 |
| `hit-tldr/mute` | resumo do resultado **selecionado** | 4.5 |
| `line/bg` | borda dos painéis | informativo |

Hoje todos passam, nos 8 temas. Foi preciso remover um token para chegar lá.

### O token que foi removido: `--accent-dim`

Existia um `--accent-dim` = `color-mix(accent 70%, background)`. Ele misturava o accent com o
**fundo** — ou seja, **escurecia**. Como cor de texto sobre fundo escuro, ele *afundava*:
reprovava 4.5:1 em quatro dos oito temas (jabuticaba 2.76, zuko 3.21, c64 3.34, ametista 3.49
sobre o `--background`).

O bug mordeu **quatro vezes** — no bloco de código, no contador da galeria, no tempo do áudio
e nos rótulos da sidebar — sempre pela mesma razão: **o nome prometia "accent mais quieto" e a
fórmula entregava "accent mais perto do fundo"**. Toda vez, a correção local foi a mesma, e
toda vez o token seguiu ali, esperando o próximo uso.

Por isso ele foi **removido, não corrigido**. Enquanto existisse, alguém o usaria de novo. No
lugar entrou o `--accent-quiet`:

```css
--accent-quiet: color-mix(in oklab, var(--accent) 70%, var(--foreground));
```

Aqui "quieto" é por **dessaturação** — puxa o accent na direção do texto — e não por
escurecimento. Pior caso: 7.25:1 sobre `--background`, 7.44:1 sobre `--sidebar-bg`.

O custo estético é real e vale saber: a hierarquia entre `h2` e `h3` deixa de ser "um âmbar
mais escuro" e passa a ser "um âmbar mais lavado". A distinção continua, mas peso e tamanho
carregam mais do trabalho do que antes.

### O outro fundo: `--accent-mute`

`--accent-quiet` resolve o texto sobre a **página**. Não resolve o texto sobre um **chip**.

`--accent-mute` é o fundo dos chips em repouso — e também o do **resultado selecionado da
palette**. Sobre ele, *nenhuma* mistura de accent passa: mesmo puxando 90% na direção do
foreground, o pior caso fica em 3.75:1. E não é um canto raro: o primeiro resultado da busca
já nasce selecionado, então esse é o estado normal.

Regra: **mudou o fundo, muda a cor.** Sobre `--accent-mute`, o texto sobe para `--foreground`
cheio (títulos) ou usa `--chip-text` (que é, por definição, o tom calibrado contra esse fundo).
É o mesmo padrão do `li:target` nas notas de rodapé, onde o realce troca o fundo e o texto
acompanha.

**Nada disso aparece no Lighthouse**, porque ele só audita o tema ativo — e no tema ativo
(fosforo) três desses quatro casos passavam. Um `a11y 100` não diz nada sobre os outros sete.
É essa a lacuna que o `just swatches` fecha.
