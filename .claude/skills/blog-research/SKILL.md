---
name: blog-research
description: Pesquisa com rigor acadêmico e jornalístico para um rascunho do blog (_drafts/posts/<slug>/pesquisa/). Uma nota por pergunta, fonte o mais primária possível, divergências lado a lado, cópia de cada fonte (lei, PDF, página) com link original e Wayback. Entrega o achado, não mexe no post. Usar quando o usuário pedir "/blog-research", "pesquisa para o post", "faz umas pesquisas pro post".
argument-hint: "<slug do post> — <pergunta 1>; <pergunta 2>; ..."
---

# blog-research

Pesquisa para um rascunho em `_drafts/posts/<slug>/`. Entregável: arquivos em `pesquisa/`.
No chat, só o resumo.

**A entrega é o achado, não a solução.** Esta skill **não edita `post.md`**. Levar o achado
para o texto é decisão do autor, e o `/blog-proof` é quem cruza texto com pesquisa.

## Onde fica

`_drafts/` é um vault Obsidian: **a raiz dos wikilinks é `_drafts/`**, não a raiz do repo.

```
_drafts/posts/<slug>/pesquisa/
  index.md                ← hub: perguntas, status de cada nota, divergências, o que ler à mão
  <tema>.md               ← uma nota por pergunta
  fontes/
    index.md              ← fontes por assunto (gerado por indice.py; não editar à mão)
    <assunto>/
      resumo.md           ← resumo do conteúdo de cada fonte da pasta
      <ano>-<id>.md       ← cópia da fonte em Markdown (frontmatter com url, wayback, acessado)
      <ano>-<id>.pdf      ← lei, artigo, ebook ou PDF, quando o acesso é livre (vai para o LFS)
```

- **Nome: ano primeiro.** `<ano>-<id>`: `1975-saltzer-schroeder-protection`, `2018-lgpd-lei-13709`.
  Kebab, sem acento.
  - Ano = quando o texto foi escrito/promulgado (lei: ano da lei, mesmo com redação atual).
  - Texto antigo: data da obra, não da tradução, com 4 dígitos. Antes de Cristo leva `ac`:
    `0430ac-herodoto-historias-5-30-macaulay-1890`. Depois de Cristo: `0100-plutarco-...`.
  - Sem data conhecida: `sd-<id>`.
- **Pasta por assunto**, kebab, com prefixo do tema: `seguranca-normas-eua/`,
  `dados-pessoais-brasil-leis/`, `cripto-grecia-roma/`. Antes de criar, veja se uma existente serve.
- `fontes/` é compartilhada entre as notas do post: antes de capturar, veja se a fonte já existe
  (`fontes/index.md`). **Entre posts também:** `ls _drafts/posts/*/pesquisa/fontes/*/` — se outro
  post já capturou a lei ou o paper, copie de lá em vez de baixar de novo.
- Link para fonte: `[[posts/<slug>/pesquisa/fontes/<assunto>/<ano>-<id>]]`.
- Sem slug no argumento: o rascunho com `post.md` mais recente (`ls -t _drafts/posts/*/post.md`).
  Mais de um candidato: AskUserQuestion.

## Regras de rigor

1. **Fonte primária primeiro.** Ordem: texto original (lei, paper, carta, inscrição, tradução de
   texto antigo) → acadêmica revisada por pares e livro de historiador → jornalismo e referência
   → Wikipedia. **Wikipedia só serve de pista** para chegar à fonte; nunca é citada.
2. Toda afirmação do achado tem footnote. A footnote diz o **tipo** (`primária`, `secundária`,
   `terciária`).
3. **Afirmar exige ter lido a fonte**, a cópia capturada, não o snippet de busca nem a memória.
   Snippet e resumo de modelo (WebFetch resume) são pista: para afirmar, leia o texto cru.
   Achou só o snippet: escreva "não confirmado" e registre em "Em aberto".
4. **Duas fontes discordam: as duas entram**, numa tabela de divergências, com o que cada uma diz
   e por quê. Sem desempate inventado: se uma é mais confiável, diga o critério (mais antiga,
   primária, revisada).
5. Atribuição popular sem fonte ("quem inventou X foi Y") vira divergência ou "não confirmado".
   Nunca fato.
6. **Atribuição de trabalho alheio é o erro mais caro.** Quem leu a cifra, quem traduziu, quem
   cunhou o termo: confira no texto da fonte, com página. O primeiro post precisou de dois commits
   de correção de crédito (Caubet/Mollin, ORCID do Diepenbroek) depois de publicado.
7. Datas antigas: diga a datação e quem datou (ex.: "c. 1900 a.C., segundo Kahn").
8. Citação literal entre aspas, no idioma original, com tradução logo abaixo quando não for pt-br.
9. Registre identificadores persistentes quando existirem: DOI da fonte, ORCID do autor.
   O `/blog-proof` usa nas referências.

## Captura de fontes

```bash
python3 -u .claude/skills/blog-research/capturar.py <url> <pesquisa>/fontes/<assunto> <ano>-<id> [--titulo T] [--completo]
```

- Baixa, arquiva no Wayback (snapshot novo; se falhar, o mais recente) e converte:
  PDF → `<id>.pdf` + texto (pdftotext); HTML → texto principal via trafilatura (cai para pandoc).
- **Recuo em cadeia quando o site barra:** urllib → `curl_cffi` (fingerprint de browser, via
  `uv run`) → snapshot cru do Wayback (`<ts>id_/<url>`). O `aviso` do JSON diz qual rodou.
  Conteúdo vindo do Wayback é cópia arquivada: registre isso na footnote.
  Se as três falham, o script sai com erro: a fonte vai para "ler à mão" no `index.md`.
- `--completo`: página inteira via pandoc. **Obrigatório para lei e norma**: o trafilatura pode cortar artigos.
- `trafilatura` não instalado: o script roda via `uvx`. O primeiro uso resolve o pacote (mais lento).
- Leva até ~3 min por fonte (o Wayback é lento). Várias de uma vez: em background, com saída
  em arquivo (`> log 2>&1`), nunca `| tail` (esconde o progresso até o fim).
- Saída JSON: use `url`, `wayback` e `aviso` na footnote. **`aviso` não vazio é degradação real**
  (sem snapshot, PDF escaneado sem texto, trafilatura caiu para pandoc): leia antes de seguir.
- Confira o `.md` gerado: se veio só menu ou ficou vazio, recapture com `--completo`.
  Pode tirar sobra de navegação do começo e do fim; o corpo fica como veio.
- **Copie o arquivo só quando o acesso é livre e legal**: lei, documento de governo, domínio público,
  open access, PDF publicado pelo autor ou pela editora. Livro protegido: cite com página, sem arquivo.
  Nunca baixe de site de pirataria (Library Genesis, Sci-Hub, Anna's Archive etc.).
- PDF, JPG e PNG de `_drafts/` vão para o Git LFS sozinhos (`.gitattributes`). Não precisa fazer nada,
  mas não renomeie a extensão para fugir dele.

## Nota por pergunta (`<tema>.md`)

```markdown
---
title: "<pergunta curta>"
type: research
status: em-andamento | concluida
created: <hoje>
post: "[[posts/<slug>/post]]"
---

> [!tldr] TL;DR
> 3 a 5 bullets. Preencher por último.

## Pergunta
## Resposta curta          ← o que dá para afirmar no post, com footnotes
## Linha do tempo          ← quando a pergunta é histórica (tabela: data · fato · fonte)
## Divergências            ← tabela: tema · fonte A diz · fonte B diz · nota
## Para o post             ← frases seguras de usar, e armadilhas (mitos comuns)
## Em aberto               ← o que não foi confirmado, e por quê
## Fontes
[^1]: Autor. *Título*. Ano. Tipo: primária. DOI: <doi, se houver> · Original: <url> · Wayback: <url> · Cópia: [[posts/<slug>/pesquisa/fontes/<assunto>/<ano>-<id>]] · Acessado em <data>.
```

- Fonte sem cópia possível (livro protegido): `Cópia: não disponível (protegido)` e a página citada.
- Aqui footnote numerada é certa: a nota de pesquisa não é publicada. Rótulo kebab é regra só do post.
- **"Para o post" é a ponte com o `/blog-proof`.** Escreva a frase segura **e** o nível de
  certeza ("confirmado na primária", "segundo X", "não confirmado"). É isso que vira a pergunta
  de `Fato` quando o texto afirma mais do que a pesquisa sustenta.

## Execução

1. Leia o `post.md` para entender o ângulo, e o `pesquisa/index.md`, se já existe (pergunta
   repetida: atualiza a nota existente, não cria outra).
2. Um subagente (`general-purpose`) por pergunta, **em paralelo**, até 4 por leva (mais que isso,
   em levas). Cada um recebe: slug, pergunta, caminho da nota, ângulo do post, este SKILL.md para
   ler e as pastas de assunto já existentes (deste post e dos outros). Cada um escreve a própria
   nota e captura as próprias fontes, já com nome e pasta finais. Devolve: TL;DR, divergências,
   fontes sem Wayback, fontes para ler à mão.
   - **Os subagentes gravam no repo.** Diga isso ao lançar. Ao fim, confira com
     `git status --short _drafts/` o que de fato foi escrito, em vez de confiar no relato.
3. **Resumo por pasta:** cada `fontes/<assunto>/` nova ou alterada ganha/atualiza o `resumo.md`.
   Um subagente por assunto, em paralelo (mesma regra de levas). Formato abaixo. **Só o conteúdo
   da fonte**: sem dizer se serve para o post, sem pontos de interesse, sem recomendação.
4. **Índice:** `python3 .claude/skills/blog-research/indice.py _drafts/posts/<slug>/pesquisa`
   regera `fontes/index.md`.
5. Ao final, quem invocou:
   - escreve/atualiza `pesquisa/index.md` (tabela: nota · pergunta · status · nº de fontes ·
     divergências; e a seção "Em aberto que exige leitura à mão");
   - confere que toda footnote tem original, Wayback (ou o aviso) e cópia, e que todo wikilink
     resolve: `[[posts/...]]` tem que existir sob `_drafts/` como `<caminho>.md` ou `<caminho>`;
   - tira o `.gitkeep` de `pesquisa/` se ficou com conteúdo (`gio trash`);
   - **não commita sozinho**: pergunta (AskUserQuestion, sim/não) se commita a pesquisa, com a
     mensagem `docs(drafts): research <tema> for <slug>`. Push, nunca.
6. No chat: TL;DR de cada pergunta, as divergências que o autor precisa decidir, e o que ficou
   para leitura à mão.

### `resumo.md` de cada pasta

```markdown
---
title: "Resumo — <assunto em pt-br>"
type: resumo-fontes
updated: <hoje>
---

# <assunto em pt-br>

## <ano legível> · <título curto da fonte>

- **Autor/órgão:** … · **Tipo:** lei | artigo | texto antigo (tradução de X, ano) | … · **Idioma:** …
- **Cópia:** [[posts/<slug>/pesquisa/fontes/<assunto>/<ano>-<id>]] · **Original:** <url>
- **Do que trata:** 1 frase.
- **Conteúdo:** 3 a 6 bullets com o que o texto diz. Trecho literal curto, se uma definição for central.
```

- Uma seção por fonte, em ordem cronológica. O `title` sem o "Resumo — " vira o nome do assunto
  no `fontes/index.md`.
