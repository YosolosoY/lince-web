// Calculadora de tiempo de lectura. Usa la velocidad de la prueba si ya se hizo en este navegador.
(function () {
  var caja = document.querySelector('[data-calculadora]');
  if (!caja) return;
  var ppm = document.getElementById('ppm');
  var paginas = document.getElementById('paginas');
  var resultado = document.getElementById('resultado');
  var plantilla = caja.getAttribute('data-resultado');
  var filas = document.querySelectorAll('[data-palabras]');
  try {
    var guardada = Number(localStorage.getItem('lince_ppm'));
    if (guardada >= 50 && guardada <= 1000) ppm.value = guardada;
  } catch (e) {}

  function tiempo(palabras, velocidad) {
    var m = Math.round(palabras / velocidad);
    return m >= 60 ? Math.floor(m / 60) + ' h ' + String(m % 60).padStart(2, '0') + ' min' : m + ' min';
  }
  function actualizar() {
    var v = Number(ppm.value);
    if (!(v >= 50 && v <= 1000)) return;
    filas.forEach(function (f) {
      f.querySelector('.tiempo').textContent = tiempo(Number(f.getAttribute('data-palabras')), v);
    });
    var p = Number(paginas.value);
    resultado.textContent = p > 0 ? plantilla.replace('{t}', tiempo(p * 300, v)).replace('{p}', v) : '';
  }
  ppm.addEventListener('input', actualizar);
  paginas.addEventListener('input', actualizar);
  actualizar();
})();
