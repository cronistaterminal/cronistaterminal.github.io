// Tema + persistência de fonte (M1). O estado inicial já foi aplicado por theme-init.js
// (head, antes do render); aqui só sincronizamos os controles com esse estado e ligamos
// os eventos de troca. defer: roda após o parse, os elementos já existem.
(() => {
    const root = document.documentElement;

    // --- Tema: radios refletem o data-theme vigente; trocar aplica + persiste ---
    const current = root.getAttribute("data-theme") || "default";
    const active = document.querySelector(`.theme-input[value="${current}"]`);
    if (active) active.checked = true;

    document.querySelectorAll(".theme-input").forEach((radio) => {
        radio.addEventListener("change", () => {
            if (!radio.checked) return;
            if (radio.value === "default") {
                root.removeAttribute("data-theme");
            } else {
                root.setAttribute("data-theme", radio.value);
            }
            try {
                localStorage.setItem("theme", radio.value);
            } catch (e) {
                /* sem persistência: o tema vale só nesta sessão */
            }
        });
    });

    // --- Fonte (toggle Aa): persiste a escolha entre sessões (pendência do README).
    // O toggle continua CSS-only via :has p/ resposta instantânea; aqui mantemos o
    // atributo data-font em sincronia com o checkbox p/ (a) restaurar antes do render
    // (theme-init) e (b) gravar a escolha. Os dois gatilhos (:has e [data-font]) setam
    // a MESMA coisa -> idempotentes, nunca conflitam. ---
    // Ciclo de loading na TV do logo (M2): enquanto a fonte de destino carrega, as faixas
    // ciclam as cores atuais. A fonte é prefetched -> resolve em ms, então um PISO de
    // duração garante que o ciclo seja perceptível. prefers-reduced-motion -> sem ciclo
    // (o estado estático já é o tema vigente). Layer transitória: só adiciona/remove a
    // classe .is-loading; a cor do tema (fill estático) fica intacta por baixo.
    const logo = document.querySelector(".logo-tv");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let loadingTimer = null;
    const showLoading = (task, minMs = 750) => {
        if (!logo || reduceMotion) return;
        clearTimeout(loadingTimer); // toggle rápido não remove a classe cedo
        logo.classList.add("is-loading");
        const start = performance.now();
        Promise.resolve(task).catch(() => {}).then(() => {
            const wait = Math.max(0, minMs - (performance.now() - start));
            loadingTimer = setTimeout(() => logo.classList.remove("is-loading"), wait);
        });
    };

    const aa = document.querySelector(".aa-input");
    if (aa) {
        aa.checked = root.getAttribute("data-font") === "accessible";
        aa.addEventListener("change", () => {
            if (aa.checked) {
                root.setAttribute("data-font", "accessible");
            } else {
                root.removeAttribute("data-font");
            }
            try {
                localStorage.setItem("font", aa.checked ? "accessible" : "conventional");
            } catch (e) {
                /* sem persistência: a fonte vale só nesta sessão */
            }
            // Espera as duas fontes do modo de destino carregarem (corpo + título).
            const body = aa.checked ? "Lexend" : "IBM Plex Mono";
            const head = aa.checked ? "Comic Relief" : "Space Mono";
            const task = document.fonts && document.fonts.load
                ? Promise.all([
                    document.fonts.load(`1em "${body}"`),
                    document.fonts.load(`700 1em "${head}"`),
                ])
                : Promise.resolve();
            showLoading(task);
        });
    }
})();
