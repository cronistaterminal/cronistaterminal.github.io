# dablog — build, preview, validação e auditoria.
#
# A regra da casa: se um comando foi digitado à mão duas vezes, ele vira receita. E se a
# receita cresce a ponto de precisar de shebang, ela vira um arquivo em tools/ — script
# escondido dentro de justfile é script sem lint, sem import e sem teste.
#
# CONVENÇÃO DOS COMENTÁRIOS: o `just --list` mostra apenas o bloco de comentário GRUDADO
# na receita. Por isso o racional longo vem primeiro, depois uma LINHA EM BRANCO, e só
# então o resumo de uma linha. Sem a linha em branco, o --list imprime o meio de um
# parágrafo e vira ruído.

# Binário Chromium usado pelo Lighthouse: o Brave Origin (do Nilton), apontado DIRETO no
# executável real — não em /usr/bin/brave-origin-nightly, que é um wrapper shell. O
# wrapper faz `exec brave-origin "$USER_FLAGS" "$BRAVE_FLAGS" "$FLAG" "$@"`: com essas
# vars vazias E entre aspas, elas viram argumentos VAZIOS, que o Chromium lê como
# URLs-alvo -> "Multiple targets are not supported in headless mode" e o Lighthouse não
# conecta.
chrome := "/opt/brave.com/brave-origin-nightly/brave-origin"
port   := "8099"

_default:
    @just --list

# ── build ────────────────────────────────────────────────────────────────────────────

# O Pagefind roda DEPOIS do Hugo, sobre o HTML já renderizado — ele é um crawler do
# próprio public/, não um plugin do Hugo. Por isso a ordem é rígida: `hugo` escreve o
# HTML, `pagefind` o lê e escreve public/pagefind/. Inverter (ou rodar só `hugo`) deixa o
# site com a palette sem índice. O que ele indexa é decidido por MARCAÇÃO no single.html
# (data-pagefind-body / -ignore / -meta / -filter), não aqui.
#
# `rm -rf public` em vez de --cleanDestinationDir: o Hugo NÃO limpa o public/ por padrão,
# só sobrescreve o que ele mesmo gera, e um public/ acumulado JÁ serviu HTML velho aqui
# mais de uma vez (datas antigas num post; e depois um <img> com o src do fallback num
# build em que o asset já existia). A flag deveria resolver, mas ela relata "Cleaned 0" e
# o resíduo continua lá — em vez de confiar no que ela promete, apagamos o diretório.
# Determinístico, e custa milissegundos. Vem ANTES do pagefind — se apagássemos depois,
# levaríamos junto o public/pagefind/ que o indexador acabou de escrever.

# Build de produção em public/ + índice de busca do Pagefind.
build:
    rm -rf public
    # O `rm` acima JÁ FALHOU ("Directory not empty", transitório e não reproduzido).
    # Quando isso acontece o build segue sobre um public/ sujo: o Hugo sobrescreve o que
    # gera e o resto fica VELHO — foi assim que um post apareceu com <img> do fallback
    # (src relativo, 404) num build em que o asset existia. Se o diretório sobreviver,
    # abortamos: melhor não ter build do que ter um build metade-velho.
    @test ! -d public || { echo "ERRO: public/ sobreviveu ao rm -rf — build abortado"; exit 1; }
    hugo --gc --minify
    npx --yes pagefind@latest --site public

# O mesmo gate que o pre-commit roda: compila templates, config e front matter INTEIROS em
# memória e não escreve nada em disco. Um partial quebrado ou um hugo.toml inválido morre
# aqui. É o check mais barato do repositório — rode à vontade.

# Compila o site em memória (o gate do pre-commit, à mão).
gate:
    hugo --renderToMemory --gc --logLevel error
    @echo "  [ok] o Hugo compila."

# Apaga os artefatos de build. Nenhum é versionado; todos se regeneram.
clean:
    rm -rf public .lighthouse tools/__pycache__
    @echo "  public/ .lighthouse/ tools/__pycache__/ removidos."

# ── servir ───────────────────────────────────────────────────────────────────────────

# ATENÇÃO: o `hugo server` NÃO gera o índice do Pagefind (ele serve de memória, sem passar
# pelo public/). A palette cai no estado inicial (posts recentes, renderizados pelo Hugo)
# e a busca por digitação não responde. Para exercitar a busca de verdade, use `preview`.
#
# O `--renderToMemory` é EXPLÍCITO desde o Hugo 0.170: lá o `hugo server` passou a servir
# "from disk", escrevendo no public/ — com drafts e o script do livereload. Rodando ao lado
# de um `just build`, ele sujou o public/ recém-limpo e o `just links` acusou o
# /livereload.js como link morto (2026-11-19).

# Servidor de desenvolvimento: live reload, inclui drafts, SEM busca.
serve:
    hugo server -D --disableFastRender --renderToMemory

# Preview do build de produção — o mesmo bytes-a-bytes que o audit mede. Roda em PRIMEIRO
# PLANO; Ctrl-C encerra. Para deixar o servidor de pé enquanto você continua trabalhando
# (validar no browser, por exemplo), use `just up`.

# Serve o build de produção em primeiro plano.
preview: build
    @echo "→ http://localhost:{{ port }}"
    python3 -m http.server {{ port }} --directory public

# Sobrevive ao fim do comando (setsid), então dá para dirigir o browser contra ele.
# Idempotente: mata o anterior antes de subir, porque um servidor esquecido de uma sessão
# passada aponta para um public/ que já não existe — e aí você valida um site fantasma.
# (Era, de longe, o comando mais reescrito à mão nesta base.)

# Serve o build de produção EM FUNDO. `just down` encerra.
up: build
    #!/usr/bin/env bash
    set -euo pipefail
    pkill -f "http.server {{ port }}" 2>/dev/null || true
    sleep 0.3
    (setsid python3 -m http.server {{ port }} --directory public >/dev/null 2>&1 </dev/null &)
    for _ in $(seq 1 40); do
        curl -sf -o /dev/null "http://localhost:{{ port }}/" && break || sleep 0.1
    done
    echo "  → http://localhost:{{ port }}   (just down encerra)"

# PRECISA da shebang, e isso não é estilo. Numa receita comum o just roda
# `sh -c 'pkill -f "http.server 8099" …'` — e a linha de comando DESSE sh contém o padrão.
# O pkill -f casa contra a cmdline inteira de cada processo: ele poupa a si mesmo, mas
# mata o pai, e a receita morre antes de terminar. (Aconteceu: o `down` matava o servidor
# e sumia sem imprimir nada.) Com a shebang, o corpo vira um ARQUIVO temporário e a
# cmdline passa a ser `bash /tmp/just-xxxx` — que não casa com nada.

# Encerra o servidor de fundo.
down:
    #!/usr/bin/env bash
    if pkill -f "http.server {{ port }}" 2>/dev/null; then
        echo "  servidor encerrado."
    else
        echo "  nada rodando na porta {{ port }}."
    fi

# Status HTTP de uma rota do servidor de fundo. Ex.: just hit cronista/
hit path="":
    @curl -s -o /dev/null -w "  %{http_code}  /{{ path }}\n" --max-time 3 "http://localhost:{{ port }}/{{ path }}" || echo "  servidor fora do ar — rode 'just up'."

# ── validação ────────────────────────────────────────────────────────────────────────

# Tudo o que dá para verificar sem um olho humano. É o que roda antes de fechar um bloco.
# Depende do build porque metade dos checks olha para o public/.

# Roda TODOS os checks: gate, xml, links, svg, js, contraste dos temas.
check: build gate xml links svg js i18n swatches
    @echo ""
    @echo "  [ok] tudo verde."
    @echo ""

# O Hugo NÃO checa isto: um href digitado à mão é texto para ele, não uma referência. Foi
# assim que /cronista/ ficou morto na sidebar de TODA página por semanas — com o build
# verde o tempo inteiro.

# Links internos que apontam para o vazio.
links:
    @python3 tools/links.py

# Mesmo buraco, outro lugar: `i18n "chave"` sem tradução renderiza VAZIO, sem erro.

# Strings de interface: paridade pt-br/en e toda chave usada existe.
i18n:
    @python3 tools/i18n.py

# O xmllint aceita vários arquivos e falha se QUALQUER um reprovar. Já pegou aqui: um
# CDATA que não sobrevive ao template do Hugo, e uma entidade HTML nomeada (&lsquo;) que o
# XML não define — as duas invalidam o documento INTEIRO, não só a linha.

# Feeds e sitemap bem-formados.
xml:
    @xmllint --noout $(find public -name '*.xml')
    @echo "  [ok] $(find public -name '*.xml' | wc -l) XML bem-formados."

# Não é preciosismo: um `--` dentro de um comentário XML é PROIBIDO pela spec e derruba o
# parser — o navegador simplesmente não desenha o ícone, sem erro no console. Já aconteceu
# com o logo. O xmllint pega, e é o único que pega.

# SVGs do repositório bem-formados.
svg:
    @xmllint --noout $(git ls-files '*.svg')
    @echo "  [ok] $(git ls-files '*.svg' | wc -l) SVGs bem-formados."

# O bundle é CONCATENADO: um erro de sintaxe em UM arquivo derruba todos os outros, e o
# sintoma é "o site inteiro parou de responder", não "o gallery.js quebrou".

# Sintaxe do JS de assets/js/.
js:
    @git ls-files -z 'assets/js/*.js' | xargs -0 -n1 node --check
    @echo "  [ok] $(git ls-files 'assets/js/*.js' | wc -l) arquivos JS sem erro de sintaxe."

# Existe porque o Lighthouse só audita o TEMA ATIVO: um a11y 100 não diz nada sobre os
# outros 7. A ferramenta reimplementa as fórmulas de cor do tokens.css/themes.css em
# Python, então o SVG é preview fiel do que o browser renderiza — não um mock pintado à
# mão. Sai com código 1 se algum par de TEXTO reprovar 4.5:1 (bordas são informativas).
# Se um token mudar no CSS, mude também em tools/theme-swatches.py, senão a folha mente.

# Regenera docs/themes/swatches.svg e mede o contraste dos 8 temas.
swatches:
    @python3 tools/theme-swatches.py

# Gate de a11y/perf. Sobe um servidor efêmero, mede com o Lighthouse e imprime só o que
# importa: as notas, os audits BINÁRIOS reprovados, e as métricas. Sem argumento, a home.

# Lighthouse numa página. Ex.: just audit posts/algum-post/
audit path="": build
    @bash tools/audit.sh "{{ path }}" "{{ port }}" "{{ chrome }}"

# ── conteúdo ─────────────────────────────────────────────────────────────────────────

# Abre os passos do apodrecimento da 404 em texto legível (.decay.txt, fora do git).
decay-edit:
    python3 tools/decay.py decode

# Zalgo cru NÃO entra no repositório: combining marks sangram para as linhas vizinhas do
# editor e destroem o diff. O base64 é o artefato versionado; o .decay.txt é a vista
# efêmera. Se esquecer o `decay-save`, o site vai ao ar com o Zalgo ANTERIOR — o TOML é a
# fonte da verdade, não o scratch.

# Recodifica .decay.txt -> data/decay.toml (base64), com round-trip verificado.
decay-save:
    python3 tools/decay.py encode

# Cria um post com o slug já congelado (kebab do título + 4 chars aleatórios). Os 4
# chars são gerados AQUI, uma vez — o Hugo não tem random no permalink. Ver tools/new-post.py.
new-post title:
    @python3 tools/new-post.py "{{ title }}"

# Promove _drafts/posts/<slug>/post.md para content/posts/. Converte o front matter
# YAML (Obsidian) para TOML, cunha o slug, atribui o num incremental ('0000', '0001'…),
# extrai os dois TL;DR dos callouts (removendo-os do corpo) e copia <slug>/assets/ para
# assets/posts/<slug>/. O rascunho NÃO é apagado. `-n` faz dry-run. Ver tools/promote-draft.py.
promote slug *flags:
    @python3 tools/promote-draft.py "{{ slug }}" {{ flags }}
