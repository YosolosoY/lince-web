// Demostración del lector de Lince: misma letra guía (ORP) y mismas pausas que la app
// (src/reader/text.ts: splitOrp y wordDelay). La letra guía queda al 40 % del ancho.
(function () {
  var caja = document.querySelector('[data-demo]');
  if (!caja) return;
  var texto = caja.getAttribute('data-texto');
  var palabras = texto.split(/\s+/).filter(Boolean);
  var zona = caja.querySelector('.demo-zona');
  var pre = caja.querySelector('.pre');
  var piv = caja.querySelector('.piv');
  var suf = caja.querySelector('.suf');
  var palabra = caja.querySelector('.demo-texto');
  var boton = caja.querySelector('button');
  var barra = caja.querySelector('input[type=range]');
  var ppm = caja.querySelector('.demo-ppm');
  var etiquetas = { leer: boton.getAttribute('data-leer'), pausa: boton.getAttribute('data-pausa'), otra: boton.getAttribute('data-otra') };
  var i = 0, reloj = null;
  var letra = /[\p{L}\p{N}]/u;

  function partes(w) {
    var c = Array.from(w), ini = 0, fin = c.length - 1;
    while (ini < c.length && !letra.test(c[ini])) ini++;
    while (fin > ini && !letra.test(c[fin])) fin--;
    if (ini >= c.length) return ['', c[0] || '', c.slice(1).join('')];
    var n = fin - ini + 1;
    var orp = n <= 2 ? 0 : n <= 5 ? 1 : n <= 9 ? 2 : n <= 13 ? 3 : 4;
    var p = ini + orp;
    return [c.slice(0, p).join(''), c[p], c.slice(p + 1).join('')];
  }

  function demora(w) {
    var base = 60000 / Number(barra.value);
    var limpia = w.replace(/["'”’»)\]]+$/, ''), ultima = limpia.slice(-1), extra = 0;
    if ('.!?…'.indexOf(ultima) >= 0) extra += 2.5;
    else if (',;:—–'.indexOf(ultima) >= 0) extra += 1.2;
    if (Array.from(limpia).filter(function (ch) { return letra.test(ch); }).length >= 10) extra += 0.4;
    return base * (1 + extra);
  }

  function mostrar(w) {
    var p = partes(w);
    pre.textContent = p[0]; piv.textContent = p[1]; suf.textContent = p[2];
    // Centro de la letra guía sobre la marca del 40 %.
    var x = zona.clientWidth * 0.4 - pre.offsetWidth - piv.offsetWidth / 2;
    palabra.style.transform = 'translateX(' + x + 'px)';
  }

  function paso() {
    if (i >= palabras.length) { parar(true); return; }
    var w = palabras[i++];
    mostrar(w);
    reloj = setTimeout(paso, demora(w));
  }

  function parar(fin) {
    clearTimeout(reloj); reloj = null;
    boton.textContent = fin ? etiquetas.otra : etiquetas.leer;
    if (fin) i = 0;
  }

  boton.addEventListener('click', function () {
    if (reloj) { parar(false); return; }
    boton.textContent = etiquetas.pausa;
    paso();
  });
  zona.addEventListener('click', function () { boton.click(); });
  barra.addEventListener('input', function () { ppm.textContent = barra.value; });
  window.addEventListener('resize', function () { mostrar(palabras[Math.max(0, i - 1)]); });
  ppm.textContent = barra.value;
  mostrar(palabras[0]);
})();
