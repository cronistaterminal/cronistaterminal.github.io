---
title:
epoca:
traducao: maquina
---

> [!tldr]
>

> [!tldr-long]
>

%%
GUIA — a tradução em inglês. Mora ao lado do post.md, na mesma pasta, como post.en.md.

VOCÊ PREENCHE
  title        o título em inglês. Gera a parte legível do slug em inglês; o sufixo
               de 4 caracteres é o MESMO do original.
  epoca        OPCIONAL. Vazio = a do original. Preencha só se a notação muda
               ('a.C.' -> 'BC').
  traducao     maquina (tradução por IA, mostra o aviso) | humana (revisada, sem aviso).
  [!tldr] / [!tldr-long]   os dois resumos, em inglês.

NÃO ESCREVA
  tags   saem de data/tags.toml (o promote recusa se houver tags aqui).
  date, num, slug   herdados do original.

PUBLICAR
  just promote <slug>   — se o original já está no ar, promove só a tradução.
%%
