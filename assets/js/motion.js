// Movimento (issue #1): o toggle da fileira de a11y e a fonte única da verdade p/ o JS.
//
// O estado é o atributo data-motion na raiz ("reduce" | "full"), aplicado ANTES do render
// por theme-init.js: a escolha salva no localStorage vence; sem escolha, vale o
// prefers-reduced-motion do sistema. Assim o padrão continua sendo o do SO (a11y não
// regride) e o site consegue sobrepô-lo nos dois sentidos.
//
// Segundo arquivo do bundle (logo depois do i18n.js): motionReduced() é usado por
// prompt.js, theme.js e lost.js. Eles NÃO leem a media query direto — leriam o SO e
// ignorariam a escolha feita aqui. Quem tem loop vivo escuta o evento "motionchange"
// em document, disparado a cada troca.
const motionReduced = () => document.documentElement.getAttribute("data-motion") === "reduce";

(() => {
    const root = document.documentElement;
    const input = document.querySelector(".motion-input");
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");

    const apply = (value) => {
        root.setAttribute("data-motion", value);
        // checkbox "Animações": marcado = animações LIGADAS (o nome é o estado, não a ação).
        if (input) input.checked = value === "full";
        document.dispatchEvent(new CustomEvent("motionchange"));
    };

    const saved = () => {
        try {
            const v = localStorage.getItem("motion");
            return v === "reduce" || v === "full" ? v : null;
        } catch (e) {
            return null;
        }
    };

    if (input) {
        input.checked = !motionReduced();
        input.addEventListener("change", () => {
            const value = input.checked ? "full" : "reduce";
            apply(value);
            try {
                localStorage.setItem("motion", value);
            } catch (e) {
                /* sem persistência: a escolha vale só nesta página */
            }
        });
    }

    // Sem escolha salva, o site acompanha o SO ao vivo (a pessoa liga o reduced-motion
    // com a aba aberta). Com escolha salva, ela manda e a mudança do SO é ignorada.
    mq.addEventListener("change", () => {
        if (!saved()) apply(mq.matches ? "reduce" : "full");
    });
})();
