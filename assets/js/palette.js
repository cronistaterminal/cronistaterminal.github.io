// ── Command palette (busca) ───────────────────────────────────────────
// Overlay invocável, arquitetado como command palette: "search" é o comando
// DEFAULT (e, por ora, o único). open(command) cai no default quando chamado
// sem argumento (Ctrl+K) e direto no comando pedido por um gatilho
// (data-command="search" na sidebar/pagination). Contrato de a11y: o foco ENTRA
// no input e VOLTA pro gatilho ao fechar; Tab fica preso dentro; Esc/clique-fora
// fecham; o fundo (#page) vira inert + sem scroll.
//
// ── MOTOR DE BUSCA ────────────────────────────────────────────────────
// Campo VAZIO: a lista renderizada pelo Hugo (posts recentes) — o estado zero,
//              que também é o fallback de quem está sem JS.
// Campo CHEIO: o Pagefind assume. Ele é carregado SOB DEMANDA (import dinâmico
//              na primeira tecla): o WASM não pesa em quem nunca busca.
//
// O que é buscável (tags, título, datas, época, tl;dr — e NÃO o corpo) é decidido
// por marcação no single.html, não aqui. Ver layouts/_default/single.html.
//
// ── O FUZZY É ESPERADO, NÃO É BUG ─────────────────────────────────────
// O Pagefind casa por DISTÂNCIA DE EDIÇÃO, tolerante ao tamanho da palavra: uma
// busca por um termo que NÃO existe no arquivo cola no vizinho mais próximo em
// vez de devolver vazio. Medido neste índice:
//     "commodore"  -> 3 posts (colou em "com…": computador, compartilhado, como)
//     "pythonzzzz" -> os mesmos 3 posts de "python"
//     "xyz"        -> 0 (a tolerância tem limite)
// Cortar por score NÃO resolve: o Pagefind pontua por RARIDADE (TF-IDF), então o
// ruído de uma palavra rara ("compartilhado", 1.38) supera o acerto de uma comum
// ("python", 1.21) — um limiar derrubaria os bons junto com os maus.
// DECISÃO DO NILTON (2026-07-12): aceitar. O outro lado da moeda é a tolerância a
// erro de digitação, que é justamente o que se quer numa busca. Se um dia isso
// incomodar, o caminho é um pós-filtro por prefixo aqui no cliente — não mexer
// no ranking do Pagefind.
(() => {
    const backdrop = document.getElementById("palette-backdrop");
    const input = document.getElementById("palette-input");
    const list = document.getElementById("palette-results");
    const status = document.getElementById("palette-status");
    const page = document.getElementById("page");
    const filtersRegion = document.getElementById("palette-filters");
    if (!backdrop || !input || !list) return;

    const DEFAULT_COMMAND = "search"; // buscar é o default — novos comandos entram aqui
    let opener = null;                // quem abriu, p/ devolver o foco

    const isOpen = () => !backdrop.hidden;

    // O HTML do estado zero, guardado ANTES de qualquer busca: é para cá que a
    // lista volta quando o campo é limpo E nenhum filtro está ligado.
    const zeroStateHTML = list.innerHTML;

    // ── Filtros de faceta (tag/época) ─────────────────────────────────────
    // "Filtros quietos" (decisão do Nilton, 2026-07-19): o foco fica no input;
    // os chips (tabindex=-1) alternam por clique ou por Alt+N. O aria-pressed do
    // botão é a ÚNICA fonte da verdade — activeFilters() lê o DOM, sem estado
    // paralelo para dessincronizar. Vazio se nada estiver ligado.
    const filterBtns = filtersRegion
        ? Array.from(filtersRegion.querySelectorAll(".palette-filter"))
        : [];

    const activeFilters = () => {
        const byType = {};
        filterBtns.forEach((b) => {
            if (b.getAttribute("aria-pressed") === "true") {
                (byType[b.dataset.filterType] ||= []).push(b.dataset.filterValue);
            }
        });
        // { any: [...] } = OU DENTRO da faceta (somar tags amplia o conjunto). A
        // Pagefind combina chaves diferentes (tag vs época) com E — faceta clássica:
        // OU dentro, E entre. MEDIDO no índice: o array cru default seria E (o
        // oposto do que se quer), então o { any } é obrigatório, não estilo.
        const f = {};
        for (const t in byType) f[t] = { any: byType[t] };
        return f;
    };

    // ── Navegação por teclado (combobox + aria-activedescendant) ──────────
    // O foco FICA no input; ↑/↓ movem um "ativo" virtual; Enter abre o post.
    //
    // ATENÇÃO: `options` NÃO pode ser capturado uma vez só. A lista é reescrita a
    // cada busca, e uma referência velha apontaria para <li>s que já saíram do
    // DOM — as setas navegariam numa lista fantasma. Por isso ele é `let`, e
    // syncOptions() o reconstrói depois de todo render.
    let options = [];
    let active = -1;

    const syncOptions = () => {
        options = Array.from(list.querySelectorAll('[role="option"]'));
        // Mouse e teclado dividem UM destaque: passar o mouse pré-seleciona.
        options.forEach((o, i) => o.addEventListener("mouseenter", () => setActive(i)));
        active = -1;
        input.removeAttribute("aria-activedescendant");
        if (options.length) setActive(0); // 1º hit pré-selecionado -> Enter abre direto
    };

    const setActive = (i) => {
        if (!options.length) return;
        active = (i + options.length) % options.length; // wrap nas pontas
        options.forEach((o, k) => o.setAttribute("aria-selected", k === active));
        const el = options[active];
        input.setAttribute("aria-activedescendant", el.id);
        el.scrollIntoView({ block: "nearest" });
    };

    const move = (d) => setActive(active + d);
    const activate = () => { if (active >= 0) options[active]?.querySelector(".hit-head")?.click(); };

    // Tab alterna o tl;dr do resultado ativo: tldr-1 ⇄ tldr-1 + tldr-2 (CSS via
    // aria-expanded no li). É seguro num modal — o foco fica no input e o Esc
    // continua sendo a saída.
    const toggleHit = () => {
        if (active < 0) return;
        const li = options[active];
        li.setAttribute("aria-expanded", li.getAttribute("aria-expanded") === "true" ? "false" : "true");
    };

    // ── Render dos resultados do Pagefind ─────────────────────────────────
    // Espelha o markup que o palette.html gera no build. Se um mudar, o outro
    // muda junto: a estrutura li[role=option] > a.hit-head > .hit-id/.hit-title
    // é contrato do CSS e da navegação por teclado.
    const esc = (s) => {
        const d = document.createElement("div");
        d.textContent = s ?? "";
        return d.innerHTML;
    };

    // Escapar HTML não basta num href: `javascript:...` passaria intacto pelo
    // esc(). As URLs vêm do nosso próprio índice, mas "é do meu site" é premissa
    // que envelhece mal — só aceitamos caminho interno.
    const safeURL = (u) => (typeof u === "string" && u.startsWith("/") ? u : "#");

    const hitHTML = (r) => {
        const m = r.meta || {};
        const href = safeURL(r.url);
        // Sem `num` não há id estável — cai na própria URL.
        const id = m.num ? `hit-${esc(m.num)}` : `hit-${esc(href)}`;
        const idChip = m.num ? `<span class="hit-id">#${esc(m.num)}</span>` : "";
        // Usamos o tl;dr (metadado limpo) e NÃO o r.excerpt do Pagefind: como o
        // índice é só de metadados, o excerpt sairia costurando tags e datas
        // ("retrocomputacao c64 22 Junho 2026…"). Destacar os termos no hit fica
        // para quando o corpo do post entrar no índice.
        return `
      <li class="palette-hit" role="option" id="${id}" aria-selected="false" aria-expanded="false">
        <a class="hit-head" href="${esc(href)}" tabindex="-1">${idChip}<span class="hit-title">${esc(m.title)}</span></a>
        ${m.tldr ? `<p class="hit-tldr">${esc(m.tldr)}</p>` : ""}
        ${m.tldr_long ? `<p class="hit-tldr-long">${esc(m.tldr_long)}</p>` : ""}
      </li>`;
    };

    const say = (msg) => { if (status) status.textContent = msg; };

    // ── Pagefind: carregado na PRIMEIRA busca, uma vez só ─────────────────
    // Guardamos a promessa (não o módulo): chamadas concorrentes durante o
    // carregamento compartilham o mesmo import em vez de dispararem vários.
    let enginePromise = null;
    const engine = () => {
        if (!enginePromise) {
            // Caminho absoluto: o índice é escrito em public/pagefind/ pelo passo
            // `pagefind --site public` do build. Sob `hugo server` ele NÃO existe
            // (ver justfile) — o catch abaixo transforma isso em degradação suave.
            enginePromise = import("/pagefind/pagefind.js").then(async (pf) => {
                await pf.init();
                return pf;
            });
        }
        return enginePromise;
    };

    // Toda busca carrega um token. Só a MAIS RECENTE tem direito de escrever na
    // tela: sem isso, digitar "com" e depois "commodore" pode terminar exibindo
    // os resultados de "com", se a resposta dele chegar por último.
    let token = 0;

    const showZeroState = () => {
        list.innerHTML = zeroStateHTML;
        say("");
        syncOptions();
    };

    const runSearch = async () => {
        const mine = ++token;
        const q = input.value.trim();
        const filters = activeFilters();
        const filtered = Object.keys(filters).length > 0;

        // Sem termo E sem filtro: volta ao estado zero (a lista do Hugo).
        if (!q && !filtered) { showZeroState(); return; }

        let pf;
        try {
            pf = await engine();
        } catch {
            // Índice ausente (dev server) ou falha de rede: a palette continua
            // usável com o estado zero em vez de virar uma caixa morta.
            if (mine !== token) return;
            say("busca indisponível — rode o build completo (just preview).");
            return;
        }
        if (mine !== token) return; // já fui superado enquanto carregava

        // Termo vazio + filtro ligado: passar null como termo devolve TODOS os
        // docs que batem no filtro (a Pagefind aceita busca só-por-filtro). Sem
        // filtro, não mandamos a chave — search(q) puro preserva o ranking fuzzy.
        const search = await pf.search(q || null, filtered ? { filters } : undefined);
        if (mine !== token) return; // idem, enquanto buscava

        // Só pedimos os dados dos hits que vamos DESENHAR: o data() de cada
        // resultado é uma requisição à parte. 20 é o teto da lista.
        const hits = await Promise.all(search.results.slice(0, 20).map((r) => r.data()));
        if (mine !== token) return;

        // Sufixo com os filtros ligados: a contagem sozinha não diz POR QUE o
        // conjunto encolheu. Como é o texto FINAL do status, sobrevive à
        // coalescência do aria-live polite (o ponto do achado do review).
        const on = filterBtns
            .filter((b) => b.getAttribute("aria-pressed") === "true")
            .map((b) => b.dataset.filterValue);
        const suffix = on.length ? ` · filtro: ${on.join(", ")}` : "";

        if (!hits.length) {
            list.innerHTML = "";
            const base = q ? `nenhum post encontrado para “${q}”` : "nenhum post com esse filtro";
            say(`${base}${suffix}.`);
            syncOptions();
            return;
        }

        list.innerHTML = hits.map(hitHTML).join("");
        const n = search.results.length;
        say(`${n} ${n === 1 ? "post encontrado" : "posts encontrados"}${suffix}.`);
        syncOptions();
    };

    // Debounce: não dispara uma busca por tecla. 120ms é curto o bastante para
    // parecer instantâneo e longo o bastante para engolir a digitação rápida.
    let timer = null;
    input.addEventListener("input", () => {
        clearTimeout(timer);
        timer = setTimeout(runSearch, 120);
    });

    // ── Toggle de filtro ──────────────────────────────────────────────────
    // Alterna o aria-pressed do chip e re-roda a busca. O foco VOLTA pro input:
    // clicar um <button> o roubaria, e o contrato é "foco sempre no input".
    // Anuncia o estado no status (região viva) — o único sinal para quem não vê
    // a cor do chip mudar.
    const anyFilterOn = () => filterBtns.some((b) => b.getAttribute("aria-pressed") === "true");

    const toggleFilter = (btn) => {
        const on = btn.getAttribute("aria-pressed") === "true";
        btn.setAttribute("aria-pressed", on ? "false" : "true");
        runSearch();
        input.focus();
        // Anunciar DEPOIS do trecho síncrono do runSearch: ao desligar o ÚLTIMO
        // filtro (sem termo), o runSearch cai no estado zero e faz say("") na
        // mesma pilha — um anúncio ANTES seria apagado antes do leitor de tela
        // vê-lo. No caminho de busca, o say(count) nomeia os filtros ativos; aqui
        // só cobrimos a volta ao estado zero, onde não há count para carregá-los.
        if (!input.value.trim() && !anyFilterOn()) {
            say(`filtro ${btn.dataset.filterValue} removido.`);
        }
    };

    filterBtns.forEach((b) => {
        // preventDefault no mousedown: um <button> rouba o foco no mousedown
        // (mesmo com tabindex=-1). Impedi-lo mantém o foco no input DE FATO — o
        // contrato "foco sempre no input" literal, não só restaurado depois.
        b.addEventListener("mousedown", (e) => e.preventDefault());
        b.addEventListener("click", () => toggleFilter(b));
    });

    // Numera os 9 primeiros chips ([1]..[9]) e anuncia o atalho via
    // aria-keyshortcuts, e revela a região (começa [hidden] no template: o
    // filtro é um recurso JS+Pagefind). O número é aria-hidden — dica de mouse
    // redundante; quem lê tela ouve o atalho pelo aria-keyshortcuts.
    const syncFilters = () => {
        if (!filterBtns.length) return;
        filtersRegion.hidden = false;
        filterBtns.forEach((b, i) => {
            if (i >= 9) return; // Alt+1..9 cobre os 9 primeiros; a cauda é só-clique
            b.setAttribute("aria-keyshortcuts", `Alt+${i + 1}`);
            const num = document.createElement("span");
            num.className = "filter-num";
            num.setAttribute("aria-hidden", "true");
            num.textContent = i + 1;
            b.prepend(num);
        });
    };

    const open = (command = DEFAULT_COMMAND) => {
        if (isOpen()) return;
        opener = document.activeElement;          // lembra o gatilho
        backdrop.hidden = false;
        if (page) page.inert = true;              // fundo fora do foco/leitor
        document.body.style.overflow = "hidden";  // scroll lock
        // (command só diferencia quando houver >1; hoje todos caem na busca)
        input.value = "";
        // reabre limpa: sem termo E sem filtro ligado, senão o estado zero mentiria
        filterBtns.forEach((b) => b.setAttribute("aria-pressed", "false"));
        showZeroState();                          // reabre sempre no estado zero
        input.focus();
    };

    const close = () => {
        if (!isOpen()) return;
        backdrop.hidden = true;
        if (page) page.inert = false;
        document.body.style.overflow = "";
        if (opener && opener.focus) opener.focus(); // foco VOLTA pro gatilho
    };

    // Ctrl+K (Cmd+K no Mac) alterna. preventDefault assume o atalho do browser
    // DE PROPÓSITO — convenção de palette; Ctrl+K é seguro (≠ Ctrl+P/imprimir).
    document.addEventListener("keydown", (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
            e.preventDefault();
            isOpen() ? close() : open();
        } else if (e.key === "Escape" && isOpen()) {
            close();
        } else if (isOpen()) {
            // Alt+1..9: liga/desliga o chip de filtro N sem tirar o foco do input.
            // e.code (tecla física) em vez de e.key: com Alt segurado alguns
            // layouts trocam o e.key do dígito, mas Digit1..9 é estável.
            // !ctrlKey && !metaKey exclui o AltGr (= ctrl+alt), que em ABNT2 e
            // layouts EU compõe caractere — sem o guard, eu comeria a digitação.
            if (e.altKey && !e.ctrlKey && !e.metaKey && /^Digit[1-9]$/.test(e.code)) {
                const btn = filterBtns[Number(e.code.slice(5)) - 1];
                if (btn) { e.preventDefault(); toggleFilter(btn); return; }
            }
            // Foco fica no input (modal + #page inert -> sem escape). ↑/↓ movem a
            // seleção; Tab alterna o tl;dr do resultado ativo; Enter abre o post.
            // ←/→ ficam livres p/ editar o texto da busca.
            if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
            else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
            else if (e.key === "Enter") { e.preventDefault(); activate(); }
            else if (e.key === "Tab") { e.preventDefault(); toggleHit(); }
        }
    });

    // Botão X (canto do painel) fecha.
    const closeBtn = backdrop.querySelector(".palette-close");
    if (closeBtn) closeBtn.addEventListener("click", close);

    // A dica "Esc fechar" na legenda também fecha (clique de mouse).
    const hintClose = backdrop.querySelector(".hint-close");
    if (hintClose) hintClose.addEventListener("click", close);

    // Clique no backdrop (fora do painel) fecha.
    backdrop.addEventListener("click", (e) => {
        if (e.target === backdrop) close();
    });

    // Gatilhos: qualquer [data-command] abre direto naquele comando.
    document.querySelectorAll("[data-command]").forEach((el) => {
        el.addEventListener("click", (e) => {
            e.preventDefault();
            open(el.dataset.command);
        });
    });

    syncFilters(); // numera/revela os chips de filtro
    syncOptions(); // liga o teclado à lista do estado zero
})();
