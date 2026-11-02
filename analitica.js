// Visitas anónimas a PostHog, sin cookies ni librería (la oficial pesa 100 KB). El identificador es aleatorio
// y dura solo la sesión del navegador. Se apaga con "no rastrear". No se carga en privacidad ni borrar cuenta.
(function () {
  if (location.hostname !== 'lincereader.com' || navigator.webdriver) return;
  if (navigator.doNotTrack === '1' || navigator.globalPrivacyControl) return;
  var sesion;
  try {
    sesion = sessionStorage.getItem('lince_sesion');
    if (!sesion) {
      sesion = crypto.randomUUID();
      sessionStorage.setItem('lince_sesion', sesion);
    }
  } catch (e) {
    sesion = crypto.randomUUID();
  }

  function evento(nombre, datos) {
    var propiedades = {
      $process_person_profile: false,
      $lib: 'lince-web',
      $current_url: location.origin + location.pathname,
      $pathname: location.pathname,
      $host: location.hostname,
      idioma: document.documentElement.lang,
    };
    for (var clave in datos) propiedades[clave] = datos[clave];
    fetch('https://us.i.posthog.com/capture/', {
      method: 'POST',
      keepalive: true,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        api_key: 'phc_BhURRzXthiXhwrBcJWYnzukkjVmsdsu23wqfjywkuvWh',
        event: nombre,
        distinct_id: sesion,
        properties: propiedades,
      }),
    }).catch(function () {});
  }
  window.linceEvento = evento;

  var visita = {};
  var url = new URLSearchParams(location.search);
  ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (clave) {
    if (url.get(clave)) visita[clave] = url.get(clave);
  });
  if (document.referrer) {
    var origen = new URL(document.referrer).hostname;
    if (origen !== location.hostname) visita.$referring_domain = origen;
  }
  evento('$pageview', visita);

  document.addEventListener('click', function (e) {
    var enlace = e.target.closest && e.target.closest('a[href*="play.google.com/store/apps"]');
    if (enlace) evento('clic_play', { campana: (enlace.href.match(/utm_campaign%3D([\w-]+)/) || [])[1] });
  });
})();
