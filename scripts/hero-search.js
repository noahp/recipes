(function () {
    // Open the search bar on every page load without focusing (avoids mobile keyboard pop-up)
    document.addEventListener('DOMContentLoaded', function () {
        var btn = document.getElementById('mdbook-search-toggle');
        var searchbar = document.getElementById('mdbook-searchbar');
        if (btn) {
            btn.click();
            if (searchbar) {
                setTimeout(function () { searchbar.blur(); }, 0);
            }
        }
    });
})();
