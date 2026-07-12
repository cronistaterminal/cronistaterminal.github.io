// Extraído de layouts/index.html (M3).

// ── Command palette (busca) ───────────────────────────────────────────
// Overlay invocável, arquitetado como command palette: "search" é o comando
// DEFAULT (e, por ora, o único). open(command) cai no default quando chamado
// sem argumento (Ctrl+K) e direto no comando pedido por um gatilho
// (data-command="search" no chip "buscar"; futura sidebar/header só repetem
// o atributo — zero JS novo). Contrato de a11y: o foco ENTRA no input e
// VOLTA pro gatilho ao fechar; Tab fica preso dentro; Esc/clique-fora fecham;
// o fundo (#page) vira inert + sem scroll. Standalone: resultados são mock.
(() => {
    const backdrop = document.getElementById("palette-backdrop");
    const input = document.getElementById("palette-input");
    const page = document.getElementById("page");
    if (!backdrop || !input) return;

    const DEFAULT_COMMAND = "search"; // buscar é o default — novos comandos entram aqui
    let opener = null;                // quem abriu, p/ devolver o foco

    const isOpen = () => !backdrop.hidden;

    // Navegação por teclado nos resultados (combobox + aria-activedescendant):
    // o foco FICA no input; ↑/↓ movem um "ativo" virtual; Enter abre o post.
    const options = Array.from(backdrop.querySelectorAll('[role="option"]'));
    let active = -1;

    const setActive = (i) => {
        if (!options.length) return;
        active = (i + options.length) % options.length; // wrap nas pontas
        options.forEach((o, k) => o.setAttribute("aria-selected", k === active));
        const el = options[active];
        input.setAttribute("aria-activedescendant", el.id);
        el.scrollIntoView({ block: "nearest" });
    };

    const move = (d) => setActive(active + d);
    const activate = () => { if (active >= 0) options[active].querySelector(".hit-head")?.click(); };

    // Tab alterna o tl;dr do resultado ativo: tldr-1 ⇄ tldr-1 + tldr-2 (CSS via
    // aria-expanded no li). É seguro num modal — o foco fica no input e o Esc
    // continua sendo a saída.
    const toggleHit = () => {
        if (active < 0) return;
        const li = options[active];
        li.setAttribute("aria-expanded", li.getAttribute("aria-expanded") === "true" ? "false" : "true");
    };

    // Mouse e teclado dividem UM destaque: passar o mouse pré-seleciona o item.
    options.forEach((o, i) => o.addEventListener("mouseenter", () => setActive(i)));

    const open = (command = DEFAULT_COMMAND) => {
        if (isOpen()) return;
        opener = document.activeElement;          // lembra o gatilho
        backdrop.hidden = false;
        if (page) page.inert = true;              // fundo fora do foco/leitor
        document.body.style.overflow = "hidden";  // scroll lock
        // (command só diferencia quando houver >1; hoje todos caem na busca)
        input.value = "";
        input.focus();
        setActive(0); // pré-seleciona o 1º resultado (Enter abre direto)
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
})();
