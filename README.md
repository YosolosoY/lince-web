# lince-web

Sitio de Lince: lincereader.com (GitHub Pages). Inglés en la raíz, español en /es/, y portugués, francés, alemán e
italiano en /pt/, /fr/, /de/ y /it/. Las rutas de cada página en cada idioma están en `idiomas.py`.

## Qué se edita a mano y qué se genera

- A mano: portada en inglés (`index.html`) y en español (`es/index.html`), prueba de velocidad en inglés y español,
  privacidad y borrar cuenta en inglés y español, prensa, 404.
- Generado (no editar el HTML, editar el script y volver a correrlo):
  - `python3 generar_inicio.py`: portadas pt/fr/de/it (misma estructura que `index.html`).
  - `python3 generar_prueba.py`: prueba de velocidad pt/fr/de/it. Textos de `datos/pruebas.json`, que sale de
    `src/speedtest/tests-*.ts` de la app.
  - `python3 generar_guias.py`: "¿Cuánto tarda leer?" y "¿Qué es RSVP?" en los seis idiomas. Libros de
    `datos/clasicos.json` (sale de `src/catalog/books.ts` de la app).
  - `python3 generar_legales.py`: privacidad y borrar cuenta pt/fr/de/it. Si cambia la versión en inglés o español,
    cambiar también estos textos y la fecha.
  - `python3 generar_sitemap.py`: `sitemap.xml` con todas las páginas y sus alternativas de idioma.

Cada página enlaza sus versiones en los seis idiomas (hreflang, selector de la barra y pie). `idioma.js` sugiere una
vez la versión en el idioma del navegador, sin redirigir.

## Imágenes

Capturas en `img/<idioma>-<nombre>.webp` (540×1200; acostado 1200×540; tablet 1200×750), sacadas del emulador con la app
en ese idioma. Video de la portada: `img/demo-<idioma>.{mp4,webm}` y su póster (en español: `demo.*`).
