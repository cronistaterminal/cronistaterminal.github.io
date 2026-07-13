# Roadmap

O que está adiado **de propósito**, e o que destrava cada coisa.

Isto não é lista de tarefas — é o registro de decisões de *não fazer agora*, com o
gatilho que as reabre. Um item só sai daqui quando o gatilho acontece.

O scratchpad de porte do template (`TODO.txt`, gitignorado) é outra coisa: ele rastreia
o que falta *portar*. Este arquivo rastreia o que escolhemos *esperar*.

---

## Esperando o segundo post de uma mesma época

Dois itens que pareciam independentes têm **o mesmo gatilho**, e por isso viraram um só.

### 1. Corpo real nos posts

Hoje **1 dos 6 posts tem prosa real** — `basic-lingua-franca` (o post-vitrine dos
componentes de mídia). Os outros cinco seguem com o placeholder de 11 palavras.

**Decisão (2026-07-13): não escrever os cinco.** Escrever prosa para preencher lacuna é
trabalho editorial travestido de tarefa técnica.

O que *era* dado como bloqueio técnico dissolveu-se sozinho: a nota original dizia que o
Pagefind "indexaria seis vezes a mesma frase". Não indexa — a decisão do Bloco 2 foi
indexar **só metadado** (`data-pagefind-ignore` no `.post-body`), então o corpo nunca
entra no índice e o placeholder não polui busca nenhuma.

### 2. Sidebar contextual no single

Hoje a `sidebar.html` é única: navegação, tags em destaque, últimos posts — a mesma na
home e no post. No protótipo, a página de post mostrava **"relacionados"** e **"outros da
mesma época"**.

O segundo é o problema: com um único post por época, "outros da mesma época" é uma caixa
vazia. O componente não pode ser validado — nem sequer *visto* — antes de existir um par.

**Fork em aberto, a decidir quando o item voltar:** ramificar por `.Kind` dentro da
partial, ou manter duas partials distintas.

### O gatilho

> **Quando existir um segundo post retratando a mesma época.**

É o momento em que os dois itens deixam de ser hipotéticos ao mesmo tempo: há prosa real
para ler, e há um "outro da mesma época" para a sidebar apontar.

Há uma dependência a resolver junto: hoje `epoca` é **texto livre** (`'1980–1991'`,
`'1936'`). Para virar eixo navegável, precisa de vocabulário ou normalização — senão cada
post cria seu próprio termo órfão. Isso se cruza com o Bloco 8 (arquivo por data/período),
onde a pergunta "a época vira taxonomia?" já está em aberto. **Decidir os dois juntos.**

---

## Depois

Blocos ainda não abertos, em ordem. Detalhe no `TODO.txt`.

| | O quê | Nota |
|---|---|---|
| 6 | Páginas que faltam | `/cronista/` é **link morto** hoje; 404; `baseURL` ainda é placeholder |
| 7 | Categorias | Decidido: **uma** por post (o build tem que validar). Falta o vocabulário, a UI e o idioma das rotas |
| 8 | SEO + arquivo por data/época | Data e época são **links que apontam pro próprio post** — ou ganham destino real, ou perdem o `href` |
| 9 | Deploy (Cloudflare) | O comando de build **mudou no Bloco 2** e o Cloudflare não sabe: sem o passo do Pagefind, o site vai ao ar com a busca morta |
