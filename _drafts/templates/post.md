---
title:
epoca:
tags: []
recomendado: false
---

> [!tldr]
>

> [!tldr-long]
>

%%
GUIA — este bloco é um comentário do Obsidian: invisível na leitura, e o promote o
remove do post publicado. Apague se incomodar. Não use o marcador de comentário
dentro deste texto: o par de dentro fecharia o bloco antes da hora.

VOCÊ PREENCHE
  title        vira <h1> e o <title> da página. Também gera o slug da URL.
  epoca        o período RETRATADO pelo post — ano ('1936') ou intervalo
               ('1980–1991'). OPCIONAL: deixe vazio se o post não retrata um
               recorte. O travessão é "–" (en dash), não hífen.
  tags         em uso hoje: alan-turing, arquitetura-de-software, c64, django,
               python, quadrinhos, retrocomputacao, seguranca. Sem acento e sem
               maiúscula — a rota /tags/<nome>/ vem daqui. Tag nova cria uma
               página com um post só; pese antes.
  recomendado  curadoria do /cronista/. É FLAG, não tag (decisão de projeto).
  [!tldr]      resumo CURTO, sempre visível no card da listagem. 1–2 frases.
  [!tldr-long] resumo LONGO, atrás do "ver mais". Não repita o curto — complemente.

O PROMOTE GERA — não escreva estes à mão
  date   data de PUBLICAÇÃO = o dia em que você promover.
  num    número da crônica, incremental com 4 dígitos ('0000', '0001'…). É o que
         ORDENA todas as listagens e vira id do DOM (#post-0001). Sequência
         automática; escolher à mão arrisca colisão, que quebra o "ver mais".
  slug   4 caracteres aleatórios no fim da URL, cunhados UMA vez e imutáveis
         depois — URL é contrato. Não invente e não copie de outro post.

PUBLICAR
  just promote <slug> -n        # dry-run: mostra o TOML que sairia
  just promote <slug>           # escreve content/posts/<base>.md e copia
                                # <slug>/assets/ para assets/posts/<slug>/
  just check

Os dois callouts são EXTRAÍDOS para o front matter e REMOVIDOS do corpo — o
single.html já renderiza os dois no abstract, então deixá-los publicaria o resumo
duas vezes. O rascunho aqui NUNCA é apagado nem alterado pelo promote.
%%
