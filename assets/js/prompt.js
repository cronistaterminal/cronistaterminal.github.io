// Extraído de layouts/index.html (M3).
// Monta um prompt vivo. target = id (string) -> escreve em .textContent (com
// .cursor ao lado, p/ footer/body); ou {input: el} -> escreve no PLACEHOLDER
// do input (a busca da palette). write() unifica os dois destinos; o motor é
// o mesmo. commands = array em loop. opts sobrescreve os tempos (ms). Retorna
// cedo se o alvo não existir — seguro chamar pra alvos talvez ausentes.
const mountPrompt = (target, commands, opts = {}) => {
    let write;
    if (typeof target === "string") {
        const out = document.getElementById(target);
        if (!out) return;
        write = (t) => { out.textContent = t; };
    } else if (target && target.input) {
        const el = target.input;
        write = (t) => { el.placeholder = t; };
    } else {
        return;
    }

    const {
        TYPE = 75,         // base por caractere ao digitar
        TYPE_JITTER = 55,  // variação aleatória somada ao TYPE
        ERASE = 35,        // apagar: mais rápido e mais regular que digitar
        HOLD = 1600,       // pausa com o comando inteiro na tela
        GAP = 500,         // respiro depois de apagar, antes do próximo
        PUNCT_PAUSE = 220, // hesitação extra após espaço/pontuação
    } = opts;

    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    const rand = (n) => Math.random() * n;

    // Delay de um caractere: base + jitter, com hesitação após espaço/pontuação
    // (quem digita "pensa" entre palavras). for..of itera code points correto
    // (o "é" de café é 1 caractere, não 2 surrogates).
    const typeDelay = (ch) =>
        TYPE + rand(TYPE_JITTER) + (" .,/'".includes(ch) ? PUNCT_PAUSE : 0);

    // Buffer local (cur/chars) em vez de ler do destino: placeholder não dá
    // pra "ler de volta" como textContent, então a fonte da verdade é local.
    const type = async (text) => {
        let cur = "";
        for (const ch of text) {
            cur += ch;
            write(cur);
            await sleep(typeDelay(ch));
        }
    };

    const erase = async (text) => {
        let chars = Array.from(text);
        while (chars.length) {
            chars.pop();
            write(chars.join(""));
            await sleep(ERASE + rand(20));
        }
    };

    const run = async () => {
        for (let i = 0; ; i = (i + 1) % commands.length) {
            await type(commands[i]);
            await sleep(HOLD);
            await erase(commands[i]);
            await sleep(GAP);
        }
    };

    // prefers-reduced-motion: sem loop; mostra só o 1º comando, parado.
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        write(commands[0]);
    } else {
        run();
    }
};

// Footer: o prompt enxuto na borda.
// As listas moram em i18n/<lang>.toml (js_prompt_*), separadas por "|".
mountPrompt("footer-typed", tr("js_prompt_footer").split("|"));

// #layout-body: prompt na borda do painel da região de conteúdo — trocar à vontade.
// HOLD um pouco maior dessincroniza do footer ("duas sessões abertas").
mountPrompt("body-typed", tr("js_prompt_body").split("|"), { HOLD: 2000 });

// #sidebar: prompt na borda do painel lateral. Comandos com cara de "quem é
// este lugar" (identidade/índice), distintos dos posts (#main) e do perfil
// (footer). HOLD próprio (1400) dessincroniza dos outros dois — 3 sessões
// independentes piscando.
mountPrompt("sidebar-typed", tr("js_prompt_sidebar").split("|"), { HOLD: 1400 });

// Placeholder vivo do input da palette: cicla exemplos de busca (mesmos temas
// dos posts) — convida a buscar. Escreve no placeholder, então só aparece com
// o campo vazio (some assim que o usuário digita). Respeita reduced-motion.
mountPrompt({ input: document.getElementById("palette-input") }, tr("js_prompt_search").split("|"), { HOLD: 1800 });
