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

        // restores last document or loads the first one
        var hash = window.location.hash;
        if (hash && hash.substring(0,2) === "#!") {
            var src = hash.substring(2);
            viewport.src = src; 
            select.value = src;
        } else {
            var stateObj = { doc: select.value };
            window.history.pushState(stateObj, "", "#!" + select.value);
            viewport.src = select.value;
        };

        // push to history when on changes document
        select.addEventListener("change", function(event) {
            var stateObj = { doc: this.value };
            window.history.pushState(stateObj, "", "#!" + this.value);
            viewport.src = this.value;
        });
    }
})();
