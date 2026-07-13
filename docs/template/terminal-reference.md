# Nota histórica: de onde veio a estética

> **Isto não é a especificação do template.** É o registro da referência que serviu de ponto
> de partida. A especificação viva é [`docs/template/README.md`](README.md), escrita
> a partir do código. Onde este documento e o código discordarem, **o código está certo** —
> o layout deixou de ser uma releitura e virou coisa própria.
>
> O documento existe para responder "por que o fundo é marrom?" e "de onde veio o
> `--radius: 0`?", não para dizer como o template funciona hoje.

## A referência

[`panr/hugo-theme-terminal`](https://github.com/panr/hugo-theme-terminal) — estudado como
referência estética, **nunca consumido como tema**. O visual foi reconstruído do zero em
HTML/CSS próprio.

O que ele estabeleceu, e que sobreviveu:

- **Duotone quente + um único acento.** Fundo quase-preto amarronzado (`#1a170f`), texto
  off-white (`#eceae5`), um dourado (`#eec35e`) carregando toda a hierarquia — links,
  bordas, destaques.
- **Cantos retos.** `--radius: 0` como assinatura, não como economia.
- **Monoespaçado inclusive no corpo do texto.**
- **864px de largura de leitura** — hoje é o `--content-width`.
- Os nomes `--background` / `--foreground` / `--accent`.

## O que divergiu, e por quê

O trio de cores original virou o **tema `default`** entre oito. Tudo o mais mudou de
natureza:

| A referência | O dablog hoje | Por quê |
|---|---|---|
| três cores fixas | **trio mestre + derivados calculados** em OKLab | trocar o tema recolore o site inteiro; adicionar um tema custa 3 linhas |
| uma coluna | dois painéis irmãos (`#main` \| `#sidebar`) + overlays | a sidebar é navegação e meta; a busca é uma *command palette*, não um campo |
| `Fira Code` | dois pares de fontes, alternáveis | acessibilidade cognitiva: um modo convencional e um acessível (Lexend / Comic Relief) |
| accent translúcido em sRGB | `color-mix(in oklab …)` | sRGB atravessa tons lamacentos e perde a matiz do tema |
| listagem data + título + resumo | crônica **numerada** (`num`), com **época** e dois TL;DR | o eixo do blog é a época retratada, não a data de publicação |
| tempo de leitura, TOC, cover | nada disso | não é o gênero do texto |
| — | 8 temas, WCAG 1.4.1, contrato de modal, `inert`, focus-trap | acessibilidade é a restrição primária, não um verniz |

A dívida estética foi paga. O que resta dela é a paleta do `default` e a ideia de que um
terminal pode ser bonito.
