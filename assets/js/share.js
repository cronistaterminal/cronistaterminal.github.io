// Ações do post: compartilhar + copiar link (M5, round de ajustes). Standalone;
// no Hugo vira o mesmo script no rodapé com `defer`.
//
// [data-share]      -> Web Share API nativa (navigator.share) quando disponível;
//                      fallback = copia o link e dá feedback no próprio botão.
// [data-copy-link]  -> copia location.href via Clipboard API e troca o rótulo
//                      pra "copiado!" por ~1,6s (affordance de sucesso).
//
// Robustez: clipboard pode falhar (permissão/HTTP não-seguro) — try/catch dá
// feedback de erro em vez de exceção solta. O label original é restaurado sempre.
(() => {
    "use strict";

    const pageUrl = () => window.location.href;

    // Troca o texto de um elemento por `msg` e restaura o original após `ms`.
    const flash = (el, msg, ms = 1600) => {
        if (!el) return;
        if (el.dataset.flashing === "1") return; // ignora cliques repetidos no meio
        const original = el.textContent;
        el.dataset.flashing = "1";
        el.textContent = msg;
        window.setTimeout(() => {
            el.textContent = original;
            delete el.dataset.flashing;
        }, ms);
    };

    const copy = async (text) => {
        if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(text);
            return true;
        }
        // Fallback legado (http://localhost não é secure context em alguns setups).
        try {
            const ta = document.createElement("textarea");
            ta.value = text;
            ta.setAttribute("readonly", "");
            ta.style.position = "absolute";
            ta.style.left = "-9999px";
            document.body.appendChild(ta);
            ta.select();
            const ok = document.execCommand("copy");
            document.body.removeChild(ta);
            return ok;
        } catch {
            return false;
        }
    };

    // Rótulo de texto do botão (o <span> de texto, ou o próprio botão).
    const labelOf = (btn) => btn.querySelector(".post-action-txt") || btn;

    document.querySelectorAll("[data-share]").forEach((btn) => {
        btn.addEventListener("click", async () => {
            const data = { title: document.title, url: pageUrl() };
            if (navigator.share) {
                try {
                    await navigator.share(data);
                } catch {
                    // usuário cancelou o sheet nativo — silencioso, sem feedback.
                }
                return;
            }
            // Sem Web Share: cai pra copiar o link.
            const ok = await copy(pageUrl());
            flash(labelOf(btn), tr(ok ? "js_link_copied" : "js_failed"));
        });
    });

    document.querySelectorAll("[data-copy-link]").forEach((btn) => {
        btn.addEventListener("click", async () => {
            const ok = await copy(pageUrl());
            flash(labelOf(btn), tr(ok ? "js_copied" : "js_failed"));
        });
    });
})();
