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

(function () {
	"use strict";

	var divs = document.querySelectorAll("div");

	function obtener_key() {
		var regex = /[A-Z]/;
		var key = "";
		var text = document.body.textContent;
		for (var i = 0; i < text.length; i++) {
			if (regex.test(text[i])) {
				key += text[i];
			}
		}
		return key;
	}

	function cont_msg() {
		var cont = 0;
		var divs = document.querySelectorAll("div");
		for (var i = 0; i < divs.length; i++) {
			var div = divs[i];
			var clase = div.className;
			if (clase[0] == "M") {
				cont++;
			}
		}
		return cont;
	}
	var cont = cont_msg();
	console.log("Cantidad de mensaje cifrados: " + cont);

	var key = obtener_key();
	console.log("Password: " + key);

	for (var i = 0; i < divs.length; i++) {
		var div = divs[i];
		var clase = div.className;
		if (clase[0] == "M") {
			var id = div.id;

			var bytesDescifrados = CryptoJS.TripleDES.decrypt(
				{
					ciphertext: CryptoJS.enc.Base64.parse(id)
				},
				CryptoJS.enc.Utf8.parse(key),
				{
					mode: CryptoJS.mode.ECB,
					padding: CryptoJS.pad.Pkcs7
				}
			);

			var textoDescifrado = bytesDescifrados.toString(CryptoJS.enc.Utf8);
			console.log(clase + " Texto cifrado: " + id + " Texto descifrado: " + textoDescifrado);

			var h3 = document.createElement("h3");
			h3.textContent = textoDescifrado;
			document.body.appendChild(h3);
		}
	}
})();
