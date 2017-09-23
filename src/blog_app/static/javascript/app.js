(function() {
    Ink.requireModules(
        ['Ink.Dom.Loaded_1', 'Ink.Dom.Selector_1'],
        function(Loaded, Selector) {

            function loadHighlightJs() {
                var elements = Selector.select('code');
                for (var i = 0; i < elements.length; i++) {
                    hljs.highlightBlock(elements[i]);
                }
            }

            Loaded.run(function() {
                loadHighlightJs();
            });
        }
    );
})();
