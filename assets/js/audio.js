// ── Player de audio custom (self-hosted) ──────────────────────────────
// Substitui o controle nativo do <audio> (que destoa do visual terminal/CRT)
// por uma UI propria, tematizada via tokens. Cada figura [data-audio] e um
// player INDEPENDENTE (factory por elemento) — varios na mesma pagina nao se
// atrapalham. Defer-safe: roda no fim do <body> ou com defer.
//
// Markup esperado (o JS so LE; o CSS pinta):
//   <figure class="media-figure media-audio" data-audio>
//     <audio preload="none" src="..."></audio>           <- SEM controls
//     <div class="audio-ui">
//       <button class="audio-play" aria-label="Reproduzir">
//         <span class="audio-ico" aria-hidden="true"></span>   <- icone via CSS mask
//       </button>
//       <input type="range" class="audio-seek" min="0" max="100" value="0" step="0.1"
//              aria-label="Progresso do audio">
//       <span class="audio-time" aria-hidden="true">
//         <span data-audio-cur>0:00</span> / <span data-audio-dur>0:00</span>
//       </span>
//     </div>
//     <figcaption class="media-cap">...</figcaption>
//   </figure>
//
// Troca play<->pause: o JS so liga/desliga a classe .is-playing no <figure>.
// O CSS faz o resto — .audio-ico usa play.svg como mask por padrao e
// .is-playing .audio-ico troca pra pause.svg. Zero manipulacao de SVG aqui.
(() => {
    "use strict";

    // Formata segundos -> "M:SS" (ex.: 75 -> "1:15"). NaN/Infinity (metadata
    // ainda nao carregada) caem em "0:00".
    const fmt = (secs) => {
        if (!Number.isFinite(secs) || secs < 0) return "0:00";
        const m = Math.floor(secs / 60);
        const s = Math.floor(secs % 60);
        return m + ":" + String(s).padStart(2, "0");
    };

    // Monta UM player sobre uma <figure data-audio>. Tudo encapsulado: cada
    // chamada tem seu proprio audio/estado, sem variaveis compartilhadas.
    const setup = (figure) => {
        const audio = figure.querySelector("audio");
        const btn = figure.querySelector(".audio-play");
        const seek = figure.querySelector(".audio-seek");
        const curEl = figure.querySelector("[data-audio-cur]");
        const durEl = figure.querySelector("[data-audio-dur]");
        // Sem <audio> ou sem botao nao da pra montar nada — sai quieto.
        if (!audio || !btn) return;

        // Garante que o controle nativo nunca aparece (o markup ja omite, mas
        // se alguem colar com controls=true a UI custom continua sendo a unica).
        audio.removeAttribute("controls");

        // Enquanto o usuario arrasta a barra NAO sobrescrevemos a posicao dela
        // com o timeupdate do audio — senao o thumb "briga" com o dedo.
        let scrubbing = false;

        // Sincroniza botao + aria-label com o estado real do audio. Fonte de
        // verdade = audio.paused (nao um flag nosso): os eventos play/pause/ended
        // chamam isto, entao teclado/legenda/fim-da-faixa convergem no mesmo lugar.
        const syncPlayState = () => {
            const playing = !audio.paused && !audio.ended;
            figure.classList.toggle("is-playing", playing);
            btn.setAttribute("aria-label", playing ? "Pausar" : "Reproduzir");
        };

        // Atualiza barra + tempo decorrido. Pula a barra durante o scrub.
        const syncProgress = () => {
            const dur = audio.duration;
            if (curEl) curEl.textContent = fmt(audio.currentTime);
            if (!scrubbing && seek && Number.isFinite(dur) && dur > 0) {
                seek.value = String((audio.currentTime / dur) * 100);
            }
        };

        // ── Eventos do <audio> ────────────────────────────────────────────
        // Duracao so existe depois do metadata (preload="none" => so carrega
        // ao tocar / dar play). Preenche o "/ M:SS" da direita.
        audio.addEventListener("loadedmetadata", () => {
            if (durEl) durEl.textContent = fmt(audio.duration);
            syncProgress();
        });
        audio.addEventListener("timeupdate", syncProgress);
        // play/pause/ended: estado pode mudar por fora do nosso botao (ex.: outra
        // aba de midia, fim da faixa) — reconciliamos sempre.
        audio.addEventListener("play", syncPlayState);
        audio.addEventListener("pause", syncPlayState);
        audio.addEventListener("ended", () => {
            // No fim, volta o ponteiro pro inicio pra um novo play recomecar limpo.
            if (seek) seek.value = "0";
            syncPlayState();
            syncProgress();
        });

        // ── Botao play/pause ──────────────────────────────────────────────
        // So alterna play()/pause(); a UI segue pelos eventos acima (nao
        // adivinhamos o estado aqui). play() pode rejeitar (autoplay policy):
        // como o clique e um gesto do usuario costuma resolver; o catch evita
        // unhandled rejection no console.
        btn.addEventListener("click", () => {
            if (audio.paused) {
                const p = audio.play();
                if (p && typeof p.catch === "function") p.catch(() => {});
            } else {
                audio.pause();
            }
        });

        // ── Barra de seek ─────────────────────────────────────────────────
        // input => arrastando AGORA: marca scrubbing e move o currentTime
        // proporcional (so quando ja sabemos a duracao). Atualiza o tempo
        // decorrido na hora pra dar feedback enquanto arrasta.
        if (seek) {
            const applySeek = () => {
                const dur = audio.duration;
                if (Number.isFinite(dur) && dur > 0) {
                    audio.currentTime = (Number(seek.value) / 100) * dur;
                }
                if (curEl) curEl.textContent = fmt(audio.currentTime);
            };
            seek.addEventListener("input", () => {
                scrubbing = true;
                applySeek();
            });
            // change => soltou o controle: aplica a posicao final e libera o
            // timeupdate pra voltar a comandar a barra.
            seek.addEventListener("change", () => {
                applySeek();
                scrubbing = false;
            });
        }

        // Estado inicial coerente (audio comeca pausado em 0:00).
        syncPlayState();
        syncProgress();
    };

    // Monta todos os players da pagina.
    document.querySelectorAll("[data-audio]").forEach(setup);
})();
