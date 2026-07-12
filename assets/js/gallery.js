// Galeria de imagens do post (M5). Standalone por enquanto; quando portar pro
// Hugo, vira partial + este script no rodapé com `defer`.
//
// ── Galeria por <figure data-gallery> ─────────────────────────────────
// Cada [data-gallery] é uma galeria INDEPENDENTE (factory por elemento):
// estado próprio, próprios botões, próprio listener de teclado escopado ao
// root. Slides alternam via atributo `hidden` (um visível por vez). Os
// controles (primeiro/anterior/próxima/último) ficam no canto inferior-direito
// da caixa, clampam nos extremos e ficam `disabled` quando não há pra onde ir;
// o contador mostra "N de total". A legenda fica SEMPRE visível (overlay).
//
// Clicar na imagem (botão .gallery-zoom) abre o LIGHTBOX: overlay modal irmão
// do #page (mesmo contrato da command palette — #page inert, foco preso, Esc/
// clique-fora/X fecham, foco volta ao gatilho).
//
// Contrato de teclado (espelha palette.js, MAS sem listener global p/ não
// colidir com Ctrl+K): keydown ESCOPADO no root; ←/→/Home/End navegam SÓ com o
// foco dentro e fora de campo de texto.
(() => {
    "use strict";

    const isTextField = (el) =>
        el &&
        (el.tagName === "INPUT" ||
            el.tagName === "TEXTAREA" ||
            el.isContentEditable);

    // ── Lightbox compartilhado ────────────────────────────────────────────
    // Um único overlay no DOM, reusado por todas as galerias. Recebe a lista de
    // slides {src, alt, cap} + índice inicial + a galeria de origem (p/ sincronizar
    // o slide ativo e devolver o foco ao botão de zoom certo ao fechar).
    const buildLightbox = () => {
        const backdrop = document.getElementById("lightbox-backdrop");
        if (!backdrop) return null;

        const dialog = backdrop.querySelector(".lightbox");
        const img = backdrop.querySelector(".lightbox-img");
        const cap = backdrop.querySelector(".lightbox-cap");
        const idxOut = backdrop.querySelector("[data-lb-index]");
        const totalOut = backdrop.querySelector("[data-lb-total]");
        const btnPrev = backdrop.querySelector("[data-lb-prev]");
        const btnNext = backdrop.querySelector("[data-lb-next]");
        const btnClose = backdrop.querySelector(".lightbox-close");
        const page = document.getElementById("page");

        let data = [];
        let i = 0;
        let originRoot = null; // galeria de origem (p/ sincronizar + devolver foco)
        let onSync = null; // callback que move o slide ativo da galeria

        const paint = () => {
            const s = data[i];
            if (!s) return;
            img.src = s.src;
            img.alt = s.alt || "";
            cap.textContent = s.cap || "";
            cap.hidden = !s.cap;
            if (idxOut) idxOut.textContent = String(i + 1);
            if (totalOut) totalOut.textContent = String(data.length);
            btnPrev.disabled = i === 0;
            btnNext.disabled = i === data.length - 1;
            if (onSync) onSync(i); // mantém a galeria de fundo no mesmo slide
        };

        const go = (n) => {
            i = Math.max(0, Math.min(data.length - 1, n));
            paint();
        };

        const open = (slides, start, root, sync) => {
            data = slides;
            i = start;
            originRoot = root;
            onSync = sync;
            paint();
            backdrop.hidden = false;
            page.inert = true;
            document.body.style.overflow = "hidden";
            btnClose.focus();
        };

        const close = () => {
            backdrop.hidden = true;
            page.inert = false;
            document.body.style.overflow = "";
            onSync = null;
            // Devolve o foco ao botão de zoom do slide VISÍVEL (a galeria já foi
            // sincronizada), não ao que abriu — assim o foco segue o que o usuário vê.
            const back =
                originRoot &&
                originRoot.querySelector(".gallery-slide:not([hidden]) .gallery-zoom");
            if (back) back.focus();
            originRoot = null;
        };

        // Focus-trap: Tab circula só entre os controles habilitados do diálogo.
        const trap = (e) => {
            const focusable = Array.from(
                dialog.querySelectorAll("button:not([disabled])"),
            );
            if (!focusable.length) return;
            const first = focusable[0];
            const last = focusable[focusable.length - 1];
            if (e.shiftKey && document.activeElement === first) {
                e.preventDefault();
                last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
                e.preventDefault();
                first.focus();
            }
        };

        btnPrev.addEventListener("click", () => go(i - 1));
        btnNext.addEventListener("click", () => go(i + 1));
        btnClose.addEventListener("click", close);
        // Clique no fundo (fora do diálogo) fecha.
        backdrop.addEventListener("click", (e) => {
            if (e.target === backdrop) close();
        });
        backdrop.addEventListener("keydown", (e) => {
            switch (e.key) {
                case "Escape":
                    e.preventDefault();
                    close();
                    break;
                case "ArrowLeft":
                    e.preventDefault();
                    go(i - 1);
                    break;
                case "ArrowRight":
                    e.preventDefault();
                    go(i + 1);
                    break;
                case "Tab":
                    trap(e);
                    break;
            }
        });

        return { open };
    };

    const lightbox = buildLightbox();

    // ── Factory: monta UMA galeria a partir do seu <figure root> ───────────
    const makeGallery = (root) => {
        const slides = Array.from(root.querySelectorAll(".gallery-slide"));
        if (slides.length < 2) return; // 0–1 slide: nada a navegar, sai.

        const btnFirst = root.querySelector("[data-gallery-first]");
        const btnPrev = root.querySelector("[data-gallery-prev]");
        const btnNext = root.querySelector("[data-gallery-next]");
        const btnLast = root.querySelector("[data-gallery-last]");
        const idxOut = root.querySelector("[data-gallery-index]");
        const totalOut = root.querySelector("[data-gallery-total]");

        const last = slides.length - 1;
        let index = 0; // estado: slide atual (0-based)

        if (totalOut) totalOut.textContent = String(slides.length);

        // Dados dos slides p/ o lightbox (src/alt/legenda), colhidos uma vez.
        const data = slides.map((slide) => {
            const im = slide.querySelector("img");
            const c = slide.querySelector(".gallery-cap");
            return {
                src: (im && (im.currentSrc || im.src)) || "",
                alt: (im && im.alt) || "",
                cap: c ? c.textContent.trim() : "",
            };
        });

        const render = () => {
            // O foco estava DENTRO da galeria antes da troca? Guardar isto antes
            // de mexer nos slides — logo abaixo o elemento focado pode sumir.
            const hadFocus = root.contains(document.activeElement);

            slides.forEach((slide, i) => {
                slide.hidden = i !== index;
            });
            if (idxOut) idxOut.textContent = String(index + 1);

            const atStart = index === 0;
            const atEnd = index === last;
            if (btnFirst) btnFirst.disabled = atStart;
            if (btnPrev) btnPrev.disabled = atStart;
            if (btnNext) btnNext.disabled = atEnd;
            if (btnLast) btnLast.disabled = atEnd;

            // Resgate do foco. Navegando pelas SETAS, o foco está no .gallery-zoom
            // do slide visível — e a linha acima acabou de escondê-lo, o que joga o
            // foco no <body>. Duas consequências, ambas ruins: o usuário de teclado
            // perde o lugar (o próximo Tab recomeça do topo da página) e, como o
            // listener de setas é ESCOPADO no root, a navegação simplesmente morre
            // depois de uma tecla. Devolvemos o foco ao zoom do slide que entrou.
            // (Clicando nos botões isto não dispara: o botão não fica hidden, então
            // o foco continua dentro do root e nada é movido.)
            if (hadFocus && !root.contains(document.activeElement)) {
                const zoom = slides[index].querySelector(".gallery-zoom");
                if (zoom) zoom.focus();
            }
        };

        const go = (i) => {
            const clamped = Math.max(0, Math.min(last, i));
            if (clamped === index) return;
            index = clamped;
            render();
        };

        if (btnFirst) btnFirst.addEventListener("click", () => go(0));
        if (btnPrev) btnPrev.addEventListener("click", () => go(index - 1));
        if (btnNext) btnNext.addEventListener("click", () => go(index + 1));
        if (btnLast) btnLast.addEventListener("click", () => go(last));

        // Clicar na imagem abre o lightbox no slide atual. Navegar no lightbox
        // sincroniza o slide da galeria de fundo (onSync chama go()).
        if (lightbox) {
            slides.forEach((slide) => {
                const zoom = slide.querySelector(".gallery-zoom");
                if (zoom) {
                    zoom.addEventListener("click", () =>
                        lightbox.open(data, index, root, (n) => go(n)),
                    );
                }
            });
        }

        root.addEventListener("keydown", (e) => {
            if (isTextField(e.target)) return;
            switch (e.key) {
                case "ArrowLeft":
                    e.preventDefault();
                    go(index - 1);
                    break;
                case "ArrowRight":
                    e.preventDefault();
                    go(index + 1);
                    break;
                case "Home":
                    e.preventDefault();
                    go(0);
                    break;
                case "End":
                    e.preventDefault();
                    go(last);
                    break;
            }
        });

        // "N de total" em cada slide: quem conta é o JS, não o autor. No markup
        // do protótipo esse rótulo era escrito à mão (aria-label="1 de 3") — o
        // primeiro slide adicionado depois deixaria todos os outros mentindo.
        slides.forEach((slide, i) => {
            slide.setAttribute("aria-label", `${i + 1} de ${slides.length}`);
        });

        render(); // estado inicial (slide 0 visível, first/prev disabled)

        // Só agora os controles aparecem (gallery.css os esconde até aqui):
        // botão de navegação só é honesto depois que existe quem o escute.
        root.dataset.galleryReady = "";
    };

    document.querySelectorAll("[data-gallery]").forEach(makeGallery);
})();
