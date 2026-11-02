// Prueba de velocidad de lectura: mismos textos, preguntas y cálculo que la app
// (src/speedtest/passage.ts, speed.ts y src/app/prueba.tsx). Todo ocurre en el navegador: no se envía nada.
(function () {
  var caja = document.querySelector('[data-prueba]');
  if (!caja) return;
  var datos = JSON.parse(document.getElementById('prueba-datos').textContent);
  var t = datos.textos, pruebas = datos.pruebas;
  var MAX_CREIBLE = 800, MIN = 150, MAX_SUGERIDA = 600;
  var ronda = Math.floor(Math.random() * pruebas.length);
  var prueba, palabras, inicio, ppm, pregunta, aciertos;

  function el(tag, clase, texto) {
    var n = document.createElement(tag);
    if (clase) n.className = clase;
    if (texto !== undefined) n.textContent = texto;
    return n;
  }
  function boton(texto, fn, clase) {
    var b = el('button', clase || 'boton', texto);
    b.type = 'button';
    b.addEventListener('click', fn);
    return b;
  }
  function pantalla() {
    caja.textContent = '';
    for (var i = 0; i < arguments.length; i++) caja.appendChild(arguments[i]);
    caja.scrollIntoView({ block: 'start' });
  }
  function sugerida(base) {
    return Math.min(MAX_SUGERIDA, Math.max(MIN, Math.round((base * 1.25) / 10) * 10));
  }
  function empezar() {
    prueba = pruebas[ronda++ % pruebas.length];
    palabras = prueba.passage.split(/\s+/).filter(Boolean).length;
    var texto = el('div', 'prueba-texto');
    prueba.passage.split(/\n+/).forEach(function (p) { texto.appendChild(el('p', '', p)); });
    pantalla(texto, boton(t.termine, terminar));
    inicio = Date.now();
  }
  function terminar() {
    ppm = Math.round(palabras / ((Date.now() - inicio) / 60000));
    pregunta = 0; aciertos = 0;
    preguntar();
  }
  function preguntar() {
    var q = prueba.questions[pregunta];
    var lista = el('div', 'prueba-opciones');
    q.options.forEach(function (o, i) {
      lista.appendChild(boton(o, function () {
        if (i === q.correct) aciertos++;
        pregunta++;
        if (pregunta < prueba.questions.length) preguntar(); else resultado();
      }, 'boton secundario'));
    });
    pantalla(el('p', 'nota', t.pregunta.replace('{n}', pregunta + 1).replace('{t}', prueba.questions.length)), el('h3', '', q.question), lista);
  }
  function resultado() {
    var otra = boton(t.otra, empezar, 'boton secundario');
    if (ppm > MAX_CREIBLE) {
      pantalla(el('h3', '', t.muyRapido), el('p', '', t.muyRapidoTexto.replace('{ppm}', ppm)), otra);
      return;
    }
    var hoja = [el('p', 'prueba-numero', String(ppm)), el('p', 'nota', t.unidad.replace('{c}', aciertos).replace('{t}', prueba.questions.length))];
    if (aciertos < 2) hoja.push(el('p', '', t.bajaComprension));
    else hoja.push(el('p', '', t.sugerencia.replace('{ppm}', sugerida(ppm))));
    var enlace = el('a', 'boton', t.descargar);
    enlace.href = datos.play;
    var botones = el('div', 'botones');
    botones.appendChild(enlace);
    botones.appendChild(otra);
    hoja.push(botones);
    pantalla.apply(null, hoja);
  }

  caja.querySelector('button').addEventListener('click', empezar);
})();
