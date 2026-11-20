---
name: blog-proof
description: Revisão (proofing) de um rascunho do blog em _drafts/posts/<slug>/post.md. Roda a checagem mecânica (notas, shortcodes, callouts, tags); executa os pedidos que o autor deixou no texto entre chaves duplas ({{ … }}); corrige sozinho só a mecânica (acento, grafia, vírgula, hífen); pergunta tudo o que move palavra (regência, ordem, coesão, coerência) com aceitar/recusar; marca as referências no padrão do cronistaterminal; preenche época, tags e os dois TL;DR que estiverem vazios. Usar quando o usuário pedir "/blog-proof", "revisa o post", "faz o proofing do post".
argument-hint: "[slug do post]"
---

# blog-proof

Revisa `_drafts/posts/<slug>/post.md`, o rascunho de um post do cronistaterminal.
Edita só o rascunho: levar o post para `content/` é tarefa do `just promote <slug>`.

**A prosa é do Nilton.** O papel aqui tem quatro formas, e só quatro: cumprir os pedidos
que ele deixou no texto, corrigir a mecânica, escrever as referências, apontar estrutura. Texto novo é sempre proposta que ele aceita,
nunca edição direta. Editar sem avisar faz ele se perder na própria escrita: ele volta ao
texto e não reconhece o que leu. Esse custo é maior que o erro que se ia consertar.

- **Sem slug:** o rascunho com o `post.md` modificado mais recentemente (`ls -t _drafts/posts/*/post.md`).
  Mais de um candidato plausível: AskUserQuestion.
- **Leia antes:** o `post.md` inteiro, `pesquisa/index.md` e as notas de `pesquisa/*.md`, quando houver.
  A pesquisa é a base da checagem de fato (passo 3) e das referências (passo 4).

## Ordem

0. Checagem mecânica (script) → anota os ERROs para o relatório.
1. Pedidos `{{ … }}` → executa cada um, no lugar do marcador.
2. Mecânica (automático) → tabela `antes → depois` → pergunta se commita separado.
3. O que move palavra: estrutura, coesão, coerência, fato (pergunta) → aplica o aceito.
4. Referências.
5. Front matter: época, tags, `[!tldr]`, `[!tldr-long]`. Por último: os resumos dependem do texto final.
6. Checagem de novo + `just promote <slug> -n` (se o post não está publicado).
7. Relatório no chat.

## 0. Checagem mecânica

```bash
python3 .claude/skills/blog-proof/checar.py <slug>
```

Mede o que dá para medir sem ler a prosa, e que quebra o build ou some em silêncio:

| O que pega | Por que importa |
|---|---|
| `[^x]` sem definição | O Goldmark não avisa: sai como **texto literal** no post |
| definição sem uso, rótulo repetido, rótulo numérico | Some de Referências, ou briga com a numeração que o layout gera |
| `figure`/`slide` sem `alt`, `embed` sem `title` | O build **falha** (o shortcode dá `errorf`) |
| `src` que não resolve | O build falha. Procura em `assets/<src>` e em `<slug>/assets/` (o promote copia de lá) |
| `%%` em número ímpar | O promote aborta |
| pedido `{{ … }}` pendente | O Hugo não processa: sai como **texto literal** no post |
| callout ausente, vazio ou longo | Ausente aborta o promote; longo estoura o card da listagem |
| `epoca` com hífen, tag fora do formato, tag nova | Formato do site; cada tag nova cria uma página `/tags/` com um post só |
| post já publicado | Corrigir o rascunho **não** atualiza `content/posts/` (ver abaixo) |

**Post já publicado.** O promote recusa sobrescrever. Toda correção feita no rascunho precisa
ser espelhada à mão em `content/posts/<base>.md`, ou o rascunho e o site divergem em silêncio.
Isso já aconteceu: os créditos de Caubet/Mollin e o ORCID do Diepenbroek foram corrigidos só
em `content/`. Nesse caso, ao fim, liste as diferenças e pergunte se espelha (e em que direção).

## 1. Pedidos: o que o autor deixou entre chaves duplas

Texto entre chaves duplas, como `{{exemplo}}` ou `{{ acha a fonte do Kahn pra isso }}`, é um
**pedido do Nilton para o revisor**, deixado no ponto exato do texto em que ele se aplica. Não
é prosa nem erro de digitação, e o revisor cumpre o pedido durante o proofing.

**Não confundir com shortcode.** `{{< … >}}` e `{{% … %}}` são shortcodes do Hugo: não são
pedidos e não se tocam. Pedido é `{{` seguido de qualquer coisa que **não** seja `<` ou `%`.
O script do passo 0 lista os pedidos com a linha de cada um.

- **Ordem:** na ordem do texto, antes da mecânica. Assim a mecânica e o resto da revisão
  correm sobre o texto já com os pedidos cumpridos.
- **O contexto vale:** o pedido se refere ao trecho em volta dele. "Pesquisa isso" é a frase
  anterior, não o post inteiro.
- **Executar:** o resultado entra **no lugar do marcador**, e o marcador sai. Pedido que é
  instrução sobre o trecho ("reescreve mais curto", "confere essa data") altera o trecho e
  some sem deixar rastro no texto.
- **Pedido que gera prosa** (escrever, reescrever, expandir): escreve nas palavras e nos vícios
  do autor (o perfil de escrita do passo 5 vale aqui também), e o trecho vai por extenso no
  relatório, com o pedido original ao lado. Assim ele reconhece o que é dele e o que não é.
- **Pedido que precisa de pesquisa:** o que já está em `pesquisa/`, usa. O que não está, faz
  com o rigor do `/blog-research` (fonte primária, nunca o plausível). Se não achar, o marcador
  **fica** e vai para o relatório com o motivo.
- **Pedido ambíguo, ou com mais de uma saída real:** AskUserQuestion antes de executar
  (`header: Pedido 1/N`, a pergunta cita o pedido entre aspas). Não adivinhar.
- **Pedido fora do escopo do proofing** (mexer no layout, no site, em outro post): não executa
  nem apaga. Fica no texto e vai para o relatório como pendente.

## 2. Mecânica: corrigir sem perguntar

A linha de corte é **mover palavra**. O que não move palavra, corrige direto com Edit:

- acentuação, grafia, crase;
- vírgula (inclusive a que separa sujeito de verbo, e a que falta antes de vocativo);
- caixa: minúscula depois de dois-pontos, maiúscula de nome próprio, e capitalização de nome
  estrangeiro conforme o original (`Journal Des Débats` → `Journal des Débats`);
- hífen vs. espaço (`redes-sociais` → `redes sociais`), hífen vs. travessão (`-` → `—`);
- letra trocada, palavra repetida por acidente, espaço duplo.

**Não toca:** blocos e trechos de código; shortcodes `{{< … >}}`/`{{% … %}}` e blocos `%% … %%`; citações
literais de fonte; títulos de obras; nomes próprios; palavra estrangeira usada de propósito.

**O registro é blog, não paper.** Oralidade ("pra", "tá", "dá pra"), "responder essas
perguntas" sem o `a`, frase que começa com "E" ou "Mas", fragmento de efeito, anglicismo
de dev: está certo para o veículo. Não é erro. No máximo vira opção no relatório, nunca correção.

**O viés do revisor: pensar em inglês e traduzir.** Isso fabrica erro onde não tem. Antes de
marcar, teste se é maneirismo: `deus das Fronteiras` com maiúscula é epíteto, não descuido.
**Na dúvida entre erro e voz, é voz.** Deixa como está e menciona no relatório que deixou.

Guarde a lista `antes → depois`. Depois pergunte (AskUserQuestion, `header: Commit`):
"Commitar a mecânica separada, para poder reverter só ela?". Sim: `docs(drafts): fix mechanics
in <slug>`. Não: segue, e a tabela do relatório é o registro. **Nunca commita sem esse sim**,
e nunca dá push.

## 3. O que move palavra: perguntar

Vira pergunta, com a correção sugerida e sem aplicá-la:

- regência e preposição; concordância que exige trocar a palavra (não só a desinência);
- ordem invertida, frase que não fecha, sujeito solto, paralelismo quebrado;
- palavra cujo sentido não se recuperou;
- **coesão:** referente ambíguo ("isso", "ele" sem antecedente), conector errado ("portanto"
  sem causa, "mas" sem oposição), tempo verbal que oscila, termo técnico em dois sentidos;
- **coerência:** contradição entre trechos, salto lógico, repetição de ideia;
- **fato:** afirmação que a pesquisa do post contradiz, ou que a pesquisa marca como divergente
  e o texto afirma como certa;
- **estrutura:** ordem de seções que quebra o fio, hierarquia de títulos, corte sugerido.

**Toda correção sugerida tem mais de uma saída.** Mostre a que você recomenda e cite a outra
plausível. Em `através do códigos`, as saídas eram `do código`, `dos códigos` e `de código`,
e a intenção do autor era a terceira. Não decida pela "óbvia".

Formato: AskUserQuestion, uma pergunta por problema, até 4 por chamada, na ordem do texto.

- `header`: `Regência 1/N`, `Coesão 2/N`, `Fato 3/N`…
- `question`: o problema em 1 frase, com o começo do trecho entre aspas. Precisa se entender sozinha.
- Opções, com `preview`:
  - **Aceitar** (sem "Recomendado": a escolha é dele). Preview:
    ```
    ANTES
    <trecho atual, contexto mínimo>

    DEPOIS
    <reescrita mínima, nas palavras e vícios do autor>

    OUTRA SAÍDA
    <a segunda leitura plausível, se houver>

    POR QUÊ
    <1 linha>
    ```
  - **Recusar**. Preview: `Fica como está:` + o trecho.
- Aceitou → aplica. Aceitou com nota → aplica com a nota. "Other" → usa o texto dele.
  Recusou → não mexe. Esc → não repete, conta no relatório.

**Rodada seguinte, depois de ele mexer à mão:** deslize novo continua sendo pergunta, inclusive
quando nasceu de uma sugestão aceita e a correção parece ter uma saída só.

### Fato contra a pesquisa

O blog é de historiador metódico: o tom é narrativo, mas o contrato é factual. Cruze cada
afirmação datável, atribuível ou numérica com `pesquisa/`:

- a pesquisa contradiz → pergunta `Fato`;
- a pesquisa marca como divergência ou "não confirmado" e o texto afirma como fato → pergunta
  `Fato`, sugerindo a forma hedgeada ("segundo Kahn", "atribui-se a");
- a pesquisa não cobre → vai para "sem fonte" no relatório, com sugestão de `/blog-research`.
  **Nunca** preencher com o plausível.

## 4. Referências: padrão do cronistaterminal

Nota de rodapé nativa do Goldmark. O `single.html` troca o `<hr>` das notas por um
`<h2>Referências</h2>` e o layout numera. Não escreva título nem número.

- **Marca no texto:** `[^rotulo]` colado na palavra, antes da pontuação: `direto no interpretador[^basic].`
- **Rótulo:** curto, kebab, sem acento, pelo autor ou pela obra: `[^saltzer]`, `[^lgpd]`. Nunca número.
  Dois textos do mesmo autor: `[^kahn-1967]`, `[^kahn-1996]`.
- **Definição:** no fim do post, uma por bloco, separadas por linha em branco. A continuação
  é indentada com 4 espaços. Formato ABNT:

```markdown
[^goto]: DIJKSTRA, Edsger W. "Go To Statement Considered Harmful". *Communications
    of the ACM*, v. 11, n. 3, mar. 1968, p. 147–148. Disponível em
    [cs.utexas.edu](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD215.html).

[^lgpd]: BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de
    Dados Pessoais (LGPD). Disponível em
    [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).
```

| Tipo | Forma |
|---|---|
| Livro | `SOBRENOME, Nome. *Título*. Editora, ano.` (+ `, p. X` se a afirmação é pontual) |
| Capítulo | `SOBRENOME, Nome. "Capítulo". In: SOBRENOME, Nome (ed.). *Livro*. Editora, ano, p. a–b.` |
| Artigo | `SOBRENOME, Nome. "Título". *Periódico*, v. X, n. Y, mês ano, p. a–b.` |
| Lei/norma | `PAÍS ou ÓRGÃO. Tipo nº X, de <data>. Ementa curta.` |
| Texto antigo | `AUTOR. *Obra*, livro.capítulo. Trad. Nome, ano.` |
| Página web | `AUTOR ou SITE. "Título". Ano.` |

- **Link:** `Disponível em [domínio](url)`, o domínio sem `www.`. Link em `.post-body` já sai
  com o contraste certo; não precisa de classe.
- **URL:** a original. Original fora do ar: o Wayback (está no front matter da cópia em `pesquisa/fontes/`).
- **Identificador persistente:** se a fonte tem DOI ou o autor tem ORCID na pesquisa, use-o:
  é o que não apodrece.
- **De onde vem:** das notas em `pesquisa/`, preferindo a fonte primária. A nota já tem autor,
  ano e URL; a cópia em `fontes/` tem o texto para conferir a página. **Confira no texto da
  cópia, não na memória**: atribuição errada (quem leu a cifra, quem disse a frase) é o erro
  que mais custou no primeiro post.
- **O que marcar:** data, atribuição ("X criou Y"), número, citação, artigo de lei, fato
  histórico contestável. Opinião do autor não leva nota.
- Nota que já existe: confere formato e link; não duplica rótulo.

## 5. Front matter e resumos

Campos que o `promote` lê (YAML plano, porque é o que o Obsidian edita e o promote converte para TOML):
`title`, `epoca`, `tags`, `recomendado`, e os dois callouts. Outros campos (herança do vault,
como `status`, `created`) são ignorados pelo promote: não mexa, não remova.

**Só preenche o que está vazio.** Campo já preenchido é do autor: se discordar, vira pergunta do passo 3.

**Perfil de escrita primeiro.** Antes dos resumos, anote de 4 a 6 traços do autor: tamanho de
frase; pessoa (eu, a gente, você); pontuação preferida; oralidade e gíria; humor ou ironia;
vícios. Os resumos **imitam esses traços, inclusive os vícios**: soam como ele, não como revisor.

| Campo | Regra |
|---|---|
| `epoca` | Período **retratado**, não a data do post. `'1936'`, `'1980–1991'` (travessão curto –), `'c. 1900 a.C.–2026'`. **Opcional**: post sem recorte histórico fica vazio. A `date` de publicação quem gera é o promote |
| `tags` | 2 a 4, kebab, sem acento, em linha: `[seguranca, python]`. Reaproveite antes de criar (a checagem lista as novas). Tag nova cria página com um post só: pese |
| `recomendado` | **Não toca.** É curadoria do `/cronista/`, decisão dele |
| `> [!tldr]` | 1 ou 2 frases, até ~140 caracteres. Sempre visível no card: precisa fisgar |
| `> [!tldr-long]` | 2 ou 3 frases, até ~260. Atrás do "ver mais": **complementa** o curto, não repete; conta o arco sem entregar o fim |

## 6. Verificação final

- `python3 .claude/skills/blog-proof/checar.py <slug>` de novo: zero ERRO.
- Post **não** publicado: `just promote <slug> -n`. É o parser real; o dry-run não escreve nada.
- Post publicado: liste o que mudou no rascunho e ainda não está em `content/posts/`.

## 7. Relatório (no chat)

Com headings, nesta ordem:

1. **Checagem:** ERROs e AVISOs restantes.
2. **Pedidos:** cada `{{ … }}` com o que foi feito; a prosa gerada por extenso,
   com o pedido ao lado. Os que ficaram no texto, com o motivo.
3. **Mecânica:** nº de correções e tabela `antes → depois` (até 10; o resto, "ver o diff").
   E o que foi deixado como voz, com o porquê de cada um.
4. **Perguntas:** aceitas, recusadas, com nota, puladas.
5. **Referências:** notas adicionadas; lista "sem fonte", com a sugestão de `/blog-research`.
6. **Front matter:** os valores escritos, com os dois resumos por extenso.
7. **Perfil de escrita usado:** os traços, 1 linha cada, para ele corrigir se a imitação errou.
8. **Publicado?** Se sim, a lista do que precisa ser espelhado em `content/`.
9. tl;dr.
