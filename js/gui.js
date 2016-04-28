(function($, undefined) {
    'use strict';

    var $viewport = $("#viewport")[0]
        , $previewBtn = $('[name="preview"]')[0]
        , $gridBtn = $('[name="grid"]')[0]
        , $debugBtn = $('[name="debug"]')[0]
        , $spreadBtn = $('[name="spread"]')[0]
        , $zoomBtn = $('[name="zoom"]')[0]
        , $pageBtn = $('[name="page"]')[0]
        , $displayBtn = $('[name="display"]')[0]
        , $reloadBtn = $('#reload')[0]
        , $printBtn = $('#print')[0]
        , $designmodeBtn = $('[name="designmode"]')[0]
    ;

    $viewport.addEventListener("load", function(event) {
        var $contentDoc = this.contentDocument;
        var $doc = this.contentDocument.getElementsByTagName('html')[0]
        
        function switchPreview(event) {
            if(this.checked) {
                $doc.classList.add("preview");
                $doc.classList.remove("normal");
            } else {
                $doc.classList.add("normal");
                $doc.classList.remove("preview");
            }
        }

        function switchGrid(event) {
            console.log(event);
            if (this.checked) {
                $doc.classList.add("grid");
            } else {
                $doc.classList.remove("grid");
            }
        }

        function switchDebug(event) {
            if(this.checked) {
                $doc.classList.add("debug");
            } else {
                $doc.classList.remove("debug");
            }
        }

        function switchSpread(event) {
            if(this.checked) {
                $doc.classList.add("spread");
            } else {
                $doc.classList.remove("spread");
            }
        }

        function switchDesignMode(event) {
            if(this.checked) {
                $contentDoc.designMode = "on";
            } else {
                $contentDoc.designMode = "off";
            }
        }

        function setZoom(event) {
            var zoomLevel = this.value / 100;
            var elt = $doc.querySelector("#pages");
            
            elt.style.webkitTransform = "scale(" + zoomLevel + ")";
            elt.style.webkitTransformOrigin = "0 0";
        }

        function changePage(event) {
            var pageNumber = this.value - 1;

            var target = $doc.querySelectorAll('.paper')[pageNumber];
            var offsetTop = target.offsetTop;

            $doc.querySelector('body').scrollTop = offsetTop;
        }

        function changeDisplay(event) {
            var htmlelt = $doc.querySelectorAll('html')[0];
            var elts = $doc.querySelectorAll('img');

            $doc.classList.remove("low");
            $doc.classList.remove("bw");
            $doc.classList.remove("color");
            $doc.classList.add(this.value);

            for (var i = 0, l = elts.length; i < l; i ++) {
                var elt = elts[i];

                if (!elt.dataset.low) { elt.dataset.low = elt.src; }

                elt.style.visibility = 'visible';

                if (elt.dataset[this.value]) {
                    elt.src = elt.dataset[this.value];
                } else {
                    elt.src = "";
                    elt.style.visibility = 'hidden'
                }
            }
        }

        function reload(event) {
           $viewport.contentWindow.location.reload();
        }

        function print(event) {
            $viewport.contentWindow.print();
        }


        $previewBtn.addEventListener("change", switchPreview);
        $gridBtn.addEventListener("change", switchGrid);
        $debugBtn.addEventListener("change", switchDebug);
        $spreadBtn.addEventListener("change", switchSpread);
        $zoomBtn.addEventListener("change", setZoom);
        $pageBtn.addEventListener("change", changePage);
        $reloadBtn.addEventListener("click", reload);
        $printBtn.addEventListener("click", print);
        $displayBtn.addEventListener("change", changeDisplay);
        $designmodeBtn.addEventListener("change", switchDesignMode);


        switchPreview.bind($previewBtn)();
        switchGrid.bind($gridBtn)();
        switchDebug.bind($debugBtn)();
        switchSpread.bind($spreadBtn)();
        setZoom.bind($zoomBtn)();
        //changePage.bind($pageBtn)();
    }, false);
})(document.querySelectorAll.bind(document));
