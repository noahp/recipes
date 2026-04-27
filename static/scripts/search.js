(function () {
    var input = document.getElementById('search-input');
    var results = document.getElementById('search-results');
    var index = null;
    var docMap = {};

    function loadIndex() {
        var s = document.createElement('script');
        s.src = window.SEARCH_INDEX_URL;
        s.onload = function () {
            if (window.searchIndex) {
                index = elasticlunr.Index.load(window.searchIndex);
                // Build docMap for fast lookup
                Object.values(window.searchIndex.documentStore.docs).forEach(function (doc) {
                    docMap[doc.id] = doc;
                });
            }
        };
        document.head.appendChild(s);
    }

    function renderResults(hits) {
        results.innerHTML = '';
        if (!hits.length) {
            results.classList.add('hidden');
            return;
        }
        hits.slice(0, 10).forEach(function (hit) {
            var doc = docMap[hit.ref];
            if (!doc) return;
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = hit.ref;
            a.textContent = doc.title || hit.ref;
            li.appendChild(a);
            if (doc.body) {
                var teaser = document.createElement('span');
                teaser.className = 'teaser';
                teaser.textContent = doc.body.slice(0, 120).trim();
                li.appendChild(teaser);
            }
            results.appendChild(li);
        });
        results.classList.remove('hidden');
    }

    input.addEventListener('input', function () {
        var q = input.value.trim();
        if (!q) {
            results.classList.add('hidden');
            return;
        }
        if (!index) { return; }
        var hits = index.search(q, { expand: true, fields: { title: { boost: 2 }, body: { boost: 1 } } });
        renderResults(hits);
    });

    document.addEventListener('click', function (e) {
        if (!input.contains(e.target) && !results.contains(e.target)) {
            results.classList.add('hidden');
        }
    });

    input.addEventListener('focus', function () {
        if (input.value.trim() && results.children.length) {
            results.classList.remove('hidden');
        }
    });

    loadIndex();
})();
