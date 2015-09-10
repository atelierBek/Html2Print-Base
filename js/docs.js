window.HTML2print = window.HTML2print || {};


(function(undefined) {
    'use strict';

    HTML2print.Docs = function() {};

    HTML2print.Docs.prototype.initialize = function(src) {
        this.src = src || {};

        var viewport = document.getElementById("viewport");
        var toolbar = document.getElementById("toolbar");
        var select = document.createElement('select');
        select.setAttribute('name', 'documents');

        for (var key in this.src) {
            var elt = document.createElement("option");
            elt.setAttribute('value', this.src[key]);
            var txt = document.createTextNode(key);
            elt.appendChild(txt);
            select.appendChild(elt);
        }

        toolbar.insertBefore(select, toolbar.firstChild);

        select.addEventListener("change", function(event) {
            var stateObj = { doc: this.value };
            history.pushState(stateObj, "", "#!" + this.value);
            viewport.src = this.value;
        });

        var currentState = history.state;
        if (currentState) { viewport.src = currentState.doc; }
    }
})();
