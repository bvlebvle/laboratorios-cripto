// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  CrytpoJS
// @author       You
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==

// ==/UserScript==

(function() {
    'use strict';

    var nuevo = 'Vamos de excursión a la montaña este fin de semana. Ayer fuimos a un concierto de música clásica. La casa en el lago es un lugar tranquilo y relajante. Inmediatamente después de la lluvia, salimos a dar un paseo. Toda la familia se reunió para celebrar el cumpleaños. Al atardecer, disfrutamos de una cena al aire libre.Vamos de excursión a la montaña este fin de semana. Ayer fuimos a un concierto de música clásica. La casa en el lago es un lugar tranquilo y relajante. Inmediatamente después de la lluvia, salimos a dar un paseo. Toda la familia se reunió para celebrar el cumpleaños. Al atardecer, disfrutamos de una cena al aire libre.Vamos de excursión a la montaña este fin de semana. Ayer fuimos a un concierto de música clásica. La casa en el lago es un lugar tranquilo y relajante. Inmediatamente después de la lluvia, salimos a dar un paseo. Toda la familia se reunió para celebrar el cumpleaños. Al atardecer, disfrutamos de una cena al aire libre.Vamos de excursión a la montaña este fin de semana. Ayer fuimos a un concierto de música clásica. La casa en el lago es un lugar tranquilo y relajante. Inmediatamente después de la lluvia, salimos a dar un paseo. Toda la familia se reunió para celebrar el cumpleaños. Al atardecer, disfrutamos de una cena al aire libre.'
    var ids_nuevos = ['73w77NXoMc4=', 'r1JX/O/zsVM=', '/P4EHJknl7Y=', 'IiVqmoX5tCc=', 'EHtHm26ZE9k=', 'jvthEyTQvYk=', 'RgGPSAdemtE='];
    var parrafo = document.querySelector('p');
    parrafo.textContent = nuevo;

    var divs = document.querySelectorAll('div');
    for (var i = 0; i < divs.length; i++) {
        var div = divs[i];
        var clase = div.className;
        if(clase[0]=='M'){
            div.id = ids_nuevos[i];
        }
    }
    var nuevoDiv = document.createElement('div');
    nuevoDiv.className = 'M7';
    nuevoDiv.id = ids_nuevos[6];
    document.body.appendChild(nuevoDiv);


})();
