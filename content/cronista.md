+++
# A página "sobre mim". O LAYOUT está pronto; o conteúdo abaixo é PLACEHOLDER —
# troque à vontade sem tocar no template (layouts/_default/cronista.html).
title = "O Cronista"
layout = "cronista"

# ── bloco de identidade (tudo opcional) ───────────────────────────────────────
# role     : a linha de papel sob o nome. Vazio -> some.
# since     : "desde …". Vazio -> some. É string livre (pode ser "1998", "sempre").
# portrait  : caminho de uma imagem (ex.: "/img/cronista.png", de static/).
#             Não definido -> mostra um placeholder de moldura (útil enquanto não há foto).
#             portrait = false -> remove o slot inteiro; o texto ocupa a largura toda.
role = "historiador lírico, metódico"
since = "20XX"
# portrait = "/img/cronista.png"

# A contagem de crônicas NÃO é campo: o template a calcula das páginas em /posts/,
# então nunca envelhece.
+++

<!-- PLACEHOLDER — a prosa real entra aqui. Markdown normal: parágrafos, listas,
     ênfase, links (viram .content-link automático dentro do .post-body), e até
     notas de rodapé se um dia precisar. -->

Aqui é onde o Cronista se apresenta. Um parágrafo de abertura que diz quem
escreve, de que lugar, e por quê — o tom que o resto do blog vai confirmar.

Um segundo parágrafo, porque um bloco só de texto já revela como a prosa
respira: o espaçamento entre linhas, a medida da coluna, a cor do link quando
ele aparece [no meio de uma frase](/posts/).

> E uma citação, para ver como a régua lateral e o recuo se comportam — o
> Cronista gosta de deixar uma frase de outro alguém falar por ele de vez em
> quando.
