(function($, undefined) {
    'use strict';

    $('#viewport')[0].addEventListener("load", function(event) {
        var doc = this.contentDocument.getElementsByTagName('html')[0];
        
        $('[name="preview"]')[0].addEventListener("change", function(event) {
            if(this.checked) {
                doc.classList.add("preview");
                doc.classList.remove("normal");
            } else {
                doc.classList.add("normal");
                doc.classList.remove("preview");
            }
        });

        $('[name="grid"]')[0].addEventListener("change", function(event) {
            if(this.checked) {
                doc.classList.add("grid");
            } else {
                doc.classList.remove("grid");
            }
        });

        $('[name="debug"]')[0].addEventListener("change", function(event) {
            if(this.checked) {
                doc.classList.add("debug");
            } else {
                doc.classList.remove("debug");
            }
        });

        $('[name="spread"]')[0].addEventListener("change", function(event) {
            if(this.checked) {
                doc.classList.add("spread");
            } else {
                doc.classList.remove("spread");
            }
        });

        $('[name="zoom"]')[0].addEventListener("change", function(event) {
            var zoomLevel = this.value / 100;
            var elt = doc.querySelector("#pages");
            
            elt.style.webkitTransform = "scale(" + zoomLevel + ")";
            elt.style.webkitTransformOrigin = "0 0";
        });

        $('[name="page"]')[0].addEventListener("change", function(event) {
            var pageNumber = this.value - 1;

            var target = doc.querySelectorAll('.paper')[pageNumber];
            var offsetTop = target.offsetTop;

            doc.querySelector('body').scrollTop = offsetTop;
        });

        $('#reload')[0].addEventListener("click", function(event) {
            $("#viewport")[0].contentWindow.location.reload();
        });

        $('#print')[0].addEventListener("click", function(event) {
            $("#viewport")[0].contentWindow.print();
        });
    }, false);
})(document.querySelectorAll.bind(document));
