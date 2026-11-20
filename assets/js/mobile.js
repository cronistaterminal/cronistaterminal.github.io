// Menu mobile (M4): o botão hambúrguer abre/fecha o #sidebar como menu modal. Como ele
// cobre a viewport com backdrop, segue o contrato de modal do projeto (ver memória
// modal-a11y-contract): ao abrir, o foco ENTRA no menu, fica preso (focus-trap), o scroll
// do body trava; ao fechar (Esc / clique-fora / link / botão), o foco VOLTA pro botão.
// Estado canônico = aria-expanded no botão + #page.menu-open (dispara o CSS).
(() => {
    const btn = document.getElementById("menu-btn");
    const page = document.getElementById("page");
    const sidebar = document.getElementById("sidebar");
    if (!btn || !page || !sidebar) return;

    const mq = window.matchMedia("(max-width: 768px)");
    const isOpen = () => btn.getAttribute("aria-expanded") === "true";

    // Focáveis dentro do "modal" = o botão (p/ fechar) + os links/botões da sidebar.
    const SEL = 'a[href], button, input:not([type="hidden"]), [tabindex]:not([tabindex="-1"])';
    const focusables = () => [btn, ...sidebar.querySelectorAll(SEL)];

    const setOpen = (open) => {
        page.classList.toggle("menu-open", open);
        document.body.classList.toggle("menu-locked", open);
        btn.setAttribute("aria-expanded", open ? "true" : "false");
        btn.setAttribute("aria-label", tr(open ? "menu_close" : "menu_open"));
        if (open) {
            const first = sidebar.querySelector(SEL);
            if (first) first.focus();
        }
    };

    btn.addEventListener("click", () => setOpen(!isOpen()));

    // Teclado: Esc fecha (foco volta ao botão); Tab fica preso no menu (focus-trap).
    document.addEventListener("keydown", (e) => {
        if (!isOpen()) return;
        if (e.key === "Escape") {
            setOpen(false);
            btn.focus();
            return;
        }
        if (e.key === "Tab") {
            const items = focusables();
            if (!items.length) return;
            const first = items[0];
            const last = items[items.length - 1];
            if (e.shiftKey && document.activeElement === first) {
                e.preventDefault();
                last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
                e.preventDefault();
                first.focus();
            }
        }
    });

    // Clique fora do menu E do botão fecha (cobre o backdrop, sem coordenada hardcoded).
    page.addEventListener("click", (e) => {
        if (isOpen() && !sidebar.contains(e.target) && !btn.contains(e.target)) {
            setOpen(false);
        }
    });

    // Clicar num link do menu navega -> fecha.
    sidebar.addEventListener("click", (e) => {
        if (e.target.closest("a")) setOpen(false);
    });

    // Cruzar o breakpoint pra desktop reseta o estado órfão (menu-open + aria-expanded).
    mq.addEventListener("change", (e) => {
        if (!e.matches && isOpen()) setOpen(false);
    });
})();
