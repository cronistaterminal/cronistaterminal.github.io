// Strings de interface para o JS. Os textos moram em i18n/<lang>.toml, como os dos
// templates; o baseof serializa as chaves que o JS usa num <script type="application/json"
// id="i18n-js">, e este arquivo as expõe por tr().
//
// É o PRIMEIRO do bundle: os outros scripts chamam tr() já no carregamento. O bundle não
// é módulo (é concatenação), então `tr` é global de propósito, como o mountPrompt.
//
// Placeholder no formato {nome}: tr("js_slide_of", { i: 2, n: 5 }) -> "2 de 5".
// Chave ausente devolve a própria chave: aparece na tela, em vez de sumir em silêncio.
const I18N = (() => {
    try {
        return JSON.parse(document.getElementById("i18n-js").textContent);
    } catch {
        return {};
    }
})();

function tr(key, vars) {
    const s = Object.prototype.hasOwnProperty.call(I18N, key) ? I18N[key] : key;
    if (!vars) return s;
    return s.replace(/\{(\w+)\}/g, (m, k) => (k in vars ? String(vars[k]) : m));
}
