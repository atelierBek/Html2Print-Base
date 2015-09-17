;(function(undefined) {
    // http://stackoverflow.com/questions/8567114/how-to-make-an-ajax-call-without-jquery
    function callAjax(url, callback){
        var xmlhttp;
        // compatible with IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
        xmlhttp.withCredentials = true;
        xmlhttp.onreadystatechange = function(){
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
                callback(xmlhttp.responseText);
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    }

    // loads stories
    var stories = document.querySelectorAll('article[data-src]');

    for (var i = 0, l = stories.length; i < l; i ++) {
        var v = stories[i];
        var src = v.dataset.src;

        callAjax(src, function(data) {
            v.innerHTML = data;
        });
    }
})();
