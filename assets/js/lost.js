/* lost.js — a página 404.
 *
 * Sorteia um vídeo, apodrece a frase, e leva o visitante de volta para casa se ele ficar
 * parado. Todo o conteúdo e o ritmo vêm de data/404.toml, via dois <script type=json> que
 * o layouts/404.html emite. Sem esses ganchos o arquivo sai calado (é o caso em todas as
 * outras páginas do site: o bundle é único).
 *
 * Hooks do DOM (contrato com layouts/404.html):
 *   [data-lost-config]  json: redirectAfter, decayStarts, decaySteps[], home
 *   [data-videos]       json: a lista inteira (o sorteio acontece AQUI, no cliente)
 *   [data-decay]        o trecho da frase que apodrece (aria-hidden)
 *   [data-timer]        a caixa do contador (hidden até o JS assumir)
 *   [data-timer-txt]    o texto do contador (visual)
 *   [data-timer-sr]     region role=status — anuncia UMA vez, não a cada segundo
 *   [data-stay]         botão "ficar aqui" — o escape exigido pela WCAG 2.2.1
 *   [data-video]        a caixa do vídeo (hidden até haver um sorteado)
 *   [data-play]         o botão que injeta o iframe (o play é sempre um ato humano)
 *   [data-canal] [data-titulo] [data-msg]   preenchidos do vídeo sorteado
 */
(() => {
  const cfgEl = document.querySelector("[data-lost-config]");
  if (!cfgEl) return; // não é a 404

  const cfg = JSON.parse(cfgEl.textContent);
  const decayEl = document.querySelector("[data-decay]");
  const timerBox = document.querySelector("[data-timer]");
  const timerTxt = document.querySelector("[data-timer-txt]");
  const timerSR = document.querySelector("[data-timer-sr]");
  const stayBtn = document.querySelector("[data-stay]");
  const videoBox = document.querySelector("[data-video]");
  const playBtn = document.querySelector("[data-play]");

  /* Quem pediu menos movimento (no SO ou no toggle do header) não leva texto se contorcendo NEM teleporte. A página vira
     estática: a frase original, o link e o vídeo continuam ali — só o easter egg dorme.
     (Decisão do Nilton, 2026-07-13.) */
  const calm = motionReduced();

  // --- o vídeo ---------------------------------------------------------------
  // Sorteado aqui e não no build: o Hugo congelaria o "aleatório" até o próximo deploy.
  const videosEl = document.querySelector("[data-videos]");
  let video = null;
  if (videosEl && videoBox) {
    const videos = JSON.parse(videosEl.textContent) || [];
    if (videos.length) {
      video = videos[Math.floor(Math.random() * videos.length)];
      videoBox.querySelector("[data-canal]").textContent = video.canal || "";
      videoBox.querySelector("[data-titulo]").textContent = video.titulo || "";
      videoBox.querySelector("[data-msg]").textContent = video.mensagem || "";
      /* Sem aria-label aqui de propósito: o nome acessível do botão é o próprio conteúdo
         (o sr-only "Reproduzir vídeo:" + canal + título). Sobrescrever com aria-label
         quebraria a WCAG 2.5.3 — ver o comentário no layouts/404.html. */
      videoBox.hidden = false;
    }
  }

  /* O id do YouTube a partir da URL normal (watch?v=… ou youtu.be/…). O autor cola o link
     que copiou; montar a URL sem rastreio é problema nosso, não dele — mesma regra do
     shortcode embed. Se não reconhecermos o formato, o play não aparece: melhor sem vídeo
     do que um iframe apontando para lugar nenhum. */
  const ytId = (url) => {
    try {
      const u = new URL(url);
      if (u.hostname === "youtu.be") return u.pathname.slice(1) || null;
      if (u.hostname.endsWith("youtube.com")) return u.searchParams.get("v");
    } catch {
      /* url inválida no data — cai fora */
    }
    return null;
  };

  const play = () => {
    const id = video && ytId(video.link);
    if (!id) return;
    stop("play"); // dar play É o gesto deliberado que cancela o redirect
    const frame = document.createElement("iframe");
    frame.className = "lost-frame";
    frame.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1`;
    frame.title = `${video.titulo || "vídeo"} — ${video.canal || ""}`.trim();
    frame.loading = "lazy";
    frame.referrerPolicy = "strict-origin-when-cross-origin";
    frame.allow = "accelerometer; autoplay; encrypted-media; picture-in-picture";
    frame.allowFullscreen = true;
    playBtn.replaceWith(frame);
    frame.focus({ preventScroll: true }); // o foco segue o que o usuário abriu
  };

  if (playBtn) playBtn.addEventListener("click", play);

  // --- o relógio -------------------------------------------------------------
  let t = 0;
  let tick = null;

  const stop = (why) => {
    if (!tick) return;
    clearInterval(tick);
    tick = null;
    // Ao cancelar, a frase VOLTA ao original: as coisas param de ficar estranhas
    // porque você agiu. É o prêmio por não ter ficado parado.
    if (decayEl && decayEl.dataset.original) decayEl.textContent = decayEl.dataset.original;
    if (timerBox) timerBox.hidden = true;
    if (timerSR) {
      timerSR.textContent =
        why === "play" ? "Redirecionamento cancelado. Reproduzindo o vídeo." : "Redirecionamento cancelado. Você ficou.";
    }
  };

  if (stayBtn) stayBtn.addEventListener("click", () => stop("stay"));
  // Desligar as animações com o relógio correndo = ficar: a frase volta ao original e o
  // redirect cai. Religar não recomeça — o apodrecimento é de uma vez só.
  document.addEventListener("motionchange", () => {
    if (motionReduced()) stop("stay");
  });

  if (!calm && decayEl && timerBox && timerTxt) {
    decayEl.dataset.original = decayEl.textContent;
    timerBox.hidden = false;

    /* Anuncia UMA vez, não a cada segundo: um contador tagarela repetiria dez vezes e
       viraria ruído — o leitor de tela precisa saber que há um prazo e como escapar,
       não ouvir a contagem. */
    if (timerSR) {
      timerSR.textContent = `Você voltará para a página inicial em ${cfg.redirectAfter} segundos. Use o botão "ficar aqui" para cancelar.`;
    }

    const restante = () => cfg.redirectAfter - t;
    timerTxt.textContent = `voltando em ${restante()}…`;

    tick = setInterval(() => {
      t += 1;

      if (t >= cfg.redirectAfter) {
        clearInterval(tick);
        tick = null;
        window.location.href = cfg.home;
        return;
      }

      timerTxt.textContent = `voltando em ${restante()}…`;

      // O apodrecimento: um passo por segundo, a partir de decayStarts.
      const i = t - cfg.decayStarts;
      if (i >= 0 && i < cfg.decaySteps.length) {
        decayEl.textContent = cfg.decaySteps[i];
      }
    }, 1000);
  }
})();
