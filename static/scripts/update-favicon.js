var emoji = '🥘';
var h1 = document.querySelector('#main-content h1');
if (h1) {
    var glyphs = [...h1.textContent];
    if (glyphs.length) emoji = glyphs[0];
}
var favicon = document.getElementById('favicon');
if (favicon) {
    favicon.setAttribute(
        'href',
        'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>' +
        '<text y=%22.9em%22 font-size=%2290%22>' + emoji + '</text></svg>'
    );
}
