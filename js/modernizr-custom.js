/*! modernizr 3.0.0 (Custom Build) | MIT *
 * http://modernizr.com/download/?-regions-prefixed !*/
!function(e,n,t){function r(e,n){return typeof e===n}function i(){var e,n,t,i,o,s,a;for(var l in v){if(e=[],n=v[l],n.name&&(e.push(n.name.toLowerCase()),n.options&&n.options.aliases&&n.options.aliases.length))for(t=0;t<n.options.aliases.length;t++)e.push(n.options.aliases[t].toLowerCase());for(i=r(n.fn,"function")?n.fn():n.fn,o=0;o<e.length;o++)s=e[o],a=s.split("."),1===a.length?Modernizr[a[0]]=i:(!Modernizr[a[0]]||Modernizr[a[0]]instanceof Boolean||(Modernizr[a[0]]=new Boolean(Modernizr[a[0]])),Modernizr[a[0]][a[1]]=i),x.push((i?"":"no-")+a.join("-"))}}function o(e){var n=C.className,t=Modernizr._config.classPrefix||"";if(_&&(n=n.baseVal),Modernizr._config.enableJSClass){var r=new RegExp("(^|\\s)"+t+"no-js(\\s|$)");n=n.replace(r,"$1"+t+"js$2")}Modernizr._config.enableClasses&&(n+=" "+t+e.join(" "+t),_?C.className.baseVal=n:C.className=n)}function s(){return"function"!=typeof n.createElement?n.createElement(arguments[0]):_?n.createElementNS.call(n,"http://www.w3.org/2000/svg",arguments[0]):n.createElement.apply(n,arguments)}function a(e){return e.replace(/([a-z])-([a-z])/g,function(e,n,t){return n+t.toUpperCase()}).replace(/^-/,"")}function l(e,n){return!!~(""+e).indexOf(n)}function f(e,n){return function(){return e.apply(n,arguments)}}function u(e,n,t){var i;for(var o in e)if(e[o]in n)return t===!1?e[o]:(i=n[e[o]],r(i,"function")?f(i,t||n):i);return!1}function d(e){return e.replace(/([A-Z])/g,function(e,n){return"-"+n.toLowerCase()}).replace(/^ms-/,"-ms-")}function p(){var e=n.body;return e||(e=s(_?"svg":"body"),e.fake=!0),e}function c(e,t,r,i){var o,a,l,f,u="modernizr",d=s("div"),c=p();if(parseInt(r,10))for(;r--;)l=s("div"),l.id=i?i[r]:u+(r+1),d.appendChild(l);return o=s("style"),o.type="text/css",o.id="s"+u,(c.fake?c:d).appendChild(o),c.appendChild(d),o.styleSheet?o.styleSheet.cssText=e:o.appendChild(n.createTextNode(e)),d.id=u,c.fake&&(c.style.background="",c.style.overflow="hidden",f=C.style.overflow,C.style.overflow="hidden",C.appendChild(c)),a=t(d,e),c.fake?(c.parentNode.removeChild(c),C.style.overflow=f,C.offsetHeight):d.parentNode.removeChild(d),!!a}function h(n,r){var i=n.length;if("CSS"in e&&"supports"in e.CSS){for(;i--;)if(e.CSS.supports(d(n[i]),r))return!0;return!1}if("CSSSupportsRule"in e){for(var o=[];i--;)o.push("("+d(n[i])+":"+r+")");return o=o.join(" or "),c("@supports ("+o+") { #modernizr { position: absolute; } }",function(e){return"absolute"==getComputedStyle(e,null).position})}return t}function g(e,n,i,o){function f(){d&&(delete z.style,delete z.modElem)}if(o=r(o,"undefined")?!1:o,!r(i,"undefined")){var u=h(e,i);if(!r(u,"undefined"))return u}for(var d,p,c,g,m,v=["modernizr","tspan"];!z.style;)d=!0,z.modElem=s(v.shift()),z.style=z.modElem.style;for(c=e.length,p=0;c>p;p++)if(g=e[p],m=z.style[g],l(g,"-")&&(g=a(g)),z.style[g]!==t){if(o||r(i,"undefined"))return f(),"pfx"==n?g:!0;try{z.style[g]=i}catch(y){}if(z.style[g]!=m)return f(),"pfx"==n?g:!0}return f(),!1}function m(e,n,t,i,o){var s=e.charAt(0).toUpperCase()+e.slice(1),a=(e+" "+S.join(s+" ")+s).split(" ");return r(n,"string")||r(n,"undefined")?g(a,n,i,o):(a=(e+" "+E.join(s+" ")+s).split(" "),u(a,n,t))}var v=[],y={_version:"3.0.0",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,n){var t=this;setTimeout(function(){n(t[e])},0)},addTest:function(e,n,t){v.push({name:e,fn:n,options:t})},addAsyncTest:function(e){v.push({name:null,fn:e})}},Modernizr=function(){};Modernizr.prototype=y,Modernizr=new Modernizr;var C=n.documentElement,x=[],_="svg"===C.nodeName.toLowerCase();Modernizr.addTest("regions",function(){if(_)return!1;var e=Modernizr.prefixed("flowFrom"),n=Modernizr.prefixed("flowInto"),r=!1;if(!e||!n)return r;var i=s("iframe"),o=s("div"),a=s("div"),l=s("div"),f="modernizr_flow_for_regions_check";a.innerText="M",o.style.cssText="top: 150px; left: 150px; padding: 0px;",l.style.cssText="width: 50px; height: 50px; padding: 42px;",l.style[e]=f,o.appendChild(a),o.appendChild(l),C.appendChild(o);var u,d,p=a.getBoundingClientRect();return a.style[n]=f,u=a.getBoundingClientRect(),d=parseInt(u.left-p.left,10),C.removeChild(o),42==d?r=!0:(C.appendChild(i),p=i.getBoundingClientRect(),i.style[n]=f,u=i.getBoundingClientRect(),p.height>0&&p.height!==u.height&&0===u.height&&(r=!0)),a=l=o=i=t,r});var w="Moz O ms Webkit",S=y._config.usePrefixes?w.split(" "):[];y._cssomPrefixes=S;var b=function(n){var r,i=prefixes.length,o=e.CSSRule;if("undefined"==typeof o)return t;if(!n)return!1;if(n=n.replace(/^@/,""),r=n.replace(/-/g,"_").toUpperCase()+"_RULE",r in o)return"@"+n;for(var s=0;i>s;s++){var a=prefixes[s],l=a.toUpperCase()+"_"+r;if(l in o)return"@-"+a.toLowerCase()+"-"+n}return!1};y.atRule=b;var E=y._config.usePrefixes?w.toLowerCase().split(" "):[];y._domPrefixes=E;var T={elem:s("modernizr")};Modernizr._q.push(function(){delete T.elem});var z={style:T.elem.style};Modernizr._q.unshift(function(){delete z.style}),y.testAllProps=m;y.prefixed=function(e,n,t){return 0===e.indexOf("@")?b(e):(-1!=e.indexOf("-")&&(e=a(e)),n?m(e,n,t):m(e,"pfx"))};i(),o(x),delete y.addTest,delete y.addAsyncTest;for(var R=0;R<Modernizr._q.length;R++)Modernizr._q[R]();e.Modernizr=Modernizr}(window,document);