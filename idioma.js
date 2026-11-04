// Sugerencia de idioma: no redirige (Google lo desaconseja). Si el navegador está en otro idioma que tiene versión
// de esta página, la ofrece una vez; al elegir o cerrar, no vuelve a aparecer.
(function () {
  var clave = 'lince_idioma_visto';
  try { if (localStorage.getItem(clave)) return; } catch (e) { return; }
  var textos = { en: 'View in English', es: 'Ver en español', pt: 'Ver em português', fr: 'Voir en français', de: 'Auf Deutsch ansehen', it: 'Vedi in italiano' };
  var cerrarTexto = { en: 'Close', es: 'Cerrar', pt: 'Fechar', fr: 'Fermer', de: 'Schließen', it: 'Chiudi' };
  var navegador = (navigator.language || '').slice(0, 2).toLowerCase();
  var pagina = (document.documentElement.lang || '').slice(0, 2).toLowerCase();
  if (!textos[navegador] || navegador === pagina) return;
  var destino = document.querySelector('a[hreflang="' + navegador + '"]');
  if (!destino) return;
  function guardar() { try { localStorage.setItem(clave, '1'); } catch (e) {} }
  var aviso = document.createElement('div');
  aviso.className = 'aviso-idioma';
  aviso.lang = navegador;
  var enlace = document.createElement('a');
  enlace.href = destino.getAttribute('href');
  enlace.textContent = textos[navegador];
  enlace.addEventListener('click', guardar);
  var cerrar = document.createElement('button');
  cerrar.type = 'button';
  cerrar.textContent = '✕';
  cerrar.setAttribute('aria-label', cerrarTexto[navegador]);
  cerrar.addEventListener('click', function () { guardar(); aviso.remove(); });
  aviso.appendChild(enlace);
  aviso.appendChild(cerrar);
  document.body.appendChild(aviso);
})();
