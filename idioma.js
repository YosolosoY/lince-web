// Sugerencia de idioma: no redirige (Google lo desaconseja). Si el navegador está en español, ofrece la
// versión en español una vez; al elegir o cerrar, no vuelve a aparecer.
(function () {
  var clave = 'lince_idioma_visto';
  try { if (localStorage.getItem(clave)) return; } catch (e) { return; }
  if (!/^es\b/i.test(navigator.language || '')) return;
  var destino = document.querySelector('a[hreflang="es"]');
  if (!destino) return;
  function guardar() { try { localStorage.setItem(clave, '1'); } catch (e) {} }
  var aviso = document.createElement('div');
  aviso.className = 'aviso-idioma';
  aviso.lang = 'es';
  var enlace = document.createElement('a');
  enlace.href = destino.getAttribute('href');
  enlace.textContent = 'Ver en español';
  enlace.addEventListener('click', guardar);
  var cerrar = document.createElement('button');
  cerrar.type = 'button';
  cerrar.textContent = '✕';
  cerrar.setAttribute('aria-label', 'Cerrar');
  cerrar.addEventListener('click', function () { guardar(); aviso.remove(); });
  aviso.appendChild(enlace);
  aviso.appendChild(cerrar);
  document.body.appendChild(aviso);
})();
