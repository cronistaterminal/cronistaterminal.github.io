// Aplica tema + fonte + movimento ANTES do render (evita flash de tema/fonte errados). Mínimo e
// BLOCKING no <head> — por isso fica fora do prompt.js/palette.js (que são defer).
// Precedência do tema: ?theme= na URL (deep-link / teste Lighthouse) > localStorage >
// default. A fonte (toggle Aa) restaura do localStorage. Os eventos/sincronia dos
// controles ficam em theme.js (defer). try/catch: localStorage pode lançar (modo
// privado/cookies bloqueados) — degradar pro default sem quebrar a página.
(function () {
    try {
        var root = document.documentElement;
        var qs = new URLSearchParams(location.search);
        var theme = qs.get("theme") || localStorage.getItem("theme");
        // Whitelist: só temas conhecidos viram atributo (bloqueia injeção via ?theme=).
        // `default` não tem atributo (é o :root base) -> ausente da lista de propósito.
        var THEMES = ["high-contrast", "zuko", "jabuticaba", "ametista", "bsod", "c64", "hacker"];
        if (THEMES.indexOf(theme) !== -1) {
            root.setAttribute("data-theme", theme);
        }
        if (localStorage.getItem("font") === "accessible") {
            root.setAttribute("data-font", "accessible");
        }
    } catch (e) {
        /* sem persistência: segue no default */
    }
    // Movimento (issue #1): escolha salva ("reduce"/"full") > prefers-reduced-motion do SO.
    // SEMPRE seta o atributo, mesmo se o localStorage lançar: o CSS e o JS leem só o
    // data-motion, e a ausência dele fica reservada para "sem JS" (fallback na media query).
    var motion = null;
    try {
        motion = localStorage.getItem("motion");
    } catch (e) {
        /* sem persistência: cai no SO */
    }
    if (motion !== "reduce" && motion !== "full") {
        motion = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "reduce" : "full";
    }
    document.documentElement.setAttribute("data-motion", motion);
})();
