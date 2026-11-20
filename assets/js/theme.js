// Tema + persistência de fonte (M1). O estado inicial já foi aplicado por theme-init.js
// (head, antes do render); aqui só sincronizamos os controles com esse estado e ligamos
// os eventos de troca. defer: roda após o parse, os elementos já existem.
(() => {
    const root = document.documentElement;

    // --- Ciclo de loading da TV do logo (M2) ---
    // .is-loading faz as 6 faixas ciclarem pelas cores ATUAIS do tema (stripe-cycle em
    // logo.css). DOIS gatilhos o disparam, com semânticas distintas:
    //   - troca de FONTE (Aa): progresso indeterminado — cicla ENQUANTO as fontes do modo
    //     carregam, com um piso p/ ser perceptível;
    //   - troca de TEMA (swatch): one-shot — toca exatamente UM ciclo completo p/ "assentar"
    //     a cor nova.
    // Máquina compartilhada (definida ANTES dos dois handlers que a usam). Movimento
    // reduzido (motionReduced, de motion.js) -> sem ciclo (o estado estático já é o tema
    // vigente). Lido a cada troca, não no carregamento: o toggle pode mudar no meio.
    const logo = document.querySelector(".logo-tv");

    // = duração de stripe-cycle (1.2s) em logo.css: UM ciclo inteiro do padrão, no fim do
    // qual todas as faixas voltam à fase de repouso ao MESMO tempo (graças ao período
    // comum). Remover .is-loading nesse instante é imperceptível (animado == estático).
    // Manter em sincronia com a animação no CSS se a duração mudar lá.
    const LOGO_LOOP_MS = 1200;

    let loadingTimer = null;
    // Mostra o ciclo enquanto `task` não resolve, com piso de minMs (a duração mínima
    // visível). Task instantânea + minMs = LOGO_LOOP_MS -> exatamente um loop. Toggle/troca
    // rápida não corta cedo: clearTimeout reseta a remoção e o ciclo segue contínuo.
    const showLoading = (task, minMs = 750) => {
        if (!logo || motionReduced()) return;
        clearTimeout(loadingTimer);
        logo.classList.add("is-loading");
        const start = performance.now();
        Promise.resolve(task).catch(() => {}).then(() => {
            const wait = Math.max(0, minMs - (performance.now() - start));
            loadingTimer = setTimeout(() => logo.classList.remove("is-loading"), wait);
        });
    };

    // --- Tema: radios refletem o data-theme vigente; trocar aplica + persiste + 1 ciclo ---
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
            // Toca UM ciclo completo da TV p/ assentar a cor nova. data-theme já foi setado
            // acima -> as faixas leem var(--stripe-N) ao vivo e o ciclo já mostra a paleta
            // recém-aplicada. Task instantânea: o piso LOGO_LOOP_MS define exatamente um loop.
            showLoading(Promise.resolve(), LOGO_LOOP_MS);
        });
    });

    // --- Fonte (toggle Aa): persiste a escolha entre sessões (pendência do README).
    // O toggle continua CSS-only via :has p/ resposta instantânea; aqui mantemos o
    // atributo data-font em sincronia com o checkbox p/ (a) restaurar antes do render
    // (theme-init) e (b) gravar a escolha. Os dois gatilhos (:has e [data-font]) setam
    // a MESMA coisa -> idempotentes, nunca conflitam. ---
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
            // Espera as duas fontes do modo de destino carregarem (corpo + título). Progresso
            // indeterminado: cicla até as fontes resolverem, com o piso padrão (750ms).
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
