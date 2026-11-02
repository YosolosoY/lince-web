#!/usr/bin/env python3
"""Páginas de guía en inglés y español. datos/clasicos.json sale del catálogo de la app."""
import html, json
from pathlib import Path

B = 'https://lincereader.com'
HOY = '2026-11-02'
PLAY = 'https://play.google.com/store/apps/details?id=co.com.monsalve.lince&referrer=utm_source%3Dsitio%26utm_medium%3Dweb%26utm_campaign%3D'
ESTUDIO = 'https://doi.org/10.1177/1529100615623267'
BRYSBAERT = 'https://doi.org/10.1016/j.jml.2019.104047'
LIBROS = json.loads(Path('datos/clasicos.json').read_text())


def tiempo(words, wpm):
    m = round(words / wpm)
    return f'{m // 60} h {m % 60:02d} min' if m >= 60 else f'{m} min'


def pagina(p):
    es, en = p['es'], p['en']
    url, otro = (es, en) if p['lang'] == 'es' else (en, es)
    home = '/es/' if p['lang'] == 'es' else '/'
    ld = {'@context': 'https://schema.org', **p['ld'], 'url': B + url, 'inLanguage': p['lang'],
          'headline': p['h1'], 'description': p['desc']}
    pie = p['pie']
    return f'''<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{B + url}">
<link rel="alternate" hreflang="en" href="{B + en}">
<link rel="alternate" hreflang="es" href="{B + es}">
<link rel="alternate" hreflang="x-default" href="{B + en}">
<link rel="icon" href="/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/icono-180.png">
<meta name="theme-color" content="#FDF6E3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#151515" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Lince">
<meta property="og:locale" content="{'es_LA' if p['lang'] == 'es' else 'en_US'}">
<meta property="og:title" content="{html.escape(p['h1'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{B + url}">
<meta property="og:image" content="{B}/prensa/img/grafico-{p['lang']}.png">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta property="og:image:alt" content="{html.escape(p['alt'])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/estilo.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
<main class="sitio">
  <header class="barra">
    <a href="{home}" class="logo">L<span>i</span>nce</a>
    <nav>
      <a href="{home}" class="secundario">Lince</a>
      <a href="{otro}" hreflang="{'en' if p['lang'] == 'es' else 'es'}" lang="{'en' if p['lang'] == 'es' else 'es'}">{'English' if p['lang'] == 'es' else 'Español'}</a>
    </nav>
  </header>
{p['cuerpo']}
  <section class="cierre">
    <h2>{p['cta']}</h2>
    <p class="intro" style="margin: 0 auto 24px;">{p['ctap']}</p>
    <div class="botones"><a class="boton" href="{PLAY + p['camp']}">{p['boton']}</a></div>
  </section>

  <footer class="pie">
    <span>© 2026 Lince</span>
    <nav>
      <a href="{pie[0][0]}">{pie[0][1]}</a>
      <a href="{pie[1][0]}">{pie[1][1]}</a>
      <a href="{pie[2][0]}">{pie[2][1]}</a>
      <a href="mailto:lince.revision@gmail.com">{pie[3]}</a>
    </nav>
  </footer>
</main>
{p.get('script', '')}
</body>
</html>
'''


def tabla(lang, t):
    filas = sorted((b for b in LIBROS if b['l'] == lang), key=lambda b: b['w'])
    cuerpo = '\n'.join(
        f'''        <tr data-palabras="{b['w']}"><td>{html.escape(b['t'])}<br><small>{html.escape(b['a'])}</small></td><td>{f"{b['w']:,}".replace(',', '.' if lang == 'es' else ',')}</td><td class="tiempo">{tiempo(b['w'], 238)}</td></tr>'''
        for b in filas)
    return f'''<table class="tabla-libros">
      <thead><tr><th scope="col">{t[0]}</th><th scope="col">{t[1]}</th><th scope="col">{t[2]}</th></tr></thead>
      <tbody>
{cuerpo}
      </tbody>
    </table>'''


CALC = {
 'en': dict(ppm='Your speed (words per minute)', pag='Any other book: number of pages', res='About {t} at {p} wpm, counting 300 words per page.',
   col=('Book', 'Words', 'Time'), ph='320'),
 'es': dict(ppm='Tu velocidad (palabras por minuto)', pag='Cualquier otro libro: número de páginas', res='Unas {t} a {p} ppm, contando 300 palabras por página.',
   col=('Libro', 'Palabras', 'Tiempo'), ph='320'),
}


def calculadora(lang):
    c = CALC[lang]
    return f'''<div class="prueba articulo" data-calculadora data-resultado="{html.escape(c['res'])}">
    <label class="campo">{c['ppm']} <input type="number" id="ppm" min="50" max="1000" step="10" value="238" inputmode="numeric"></label>
    <label class="campo">{c['pag']} <input type="number" id="paginas" min="1" max="10000" placeholder="{c['ph']}" inputmode="numeric"></label>
    <p class="nota" id="resultado" aria-live="polite"></p>
  </div>'''


GUIAS = [
 dict(lang='en', en='/how-long-to-read/', es='/es/cuanto-tarda-leer/', archivo='how-long-to-read',
  title='How Long Does It Take to Read a Book? Classics Calculator',
  desc='See how long 25 classic books take at your reading speed, from real word counts. Change your words per minute, or enter the pages of any book.',
  h1='How long does it take to read a book?', alt='Lince feature graphic', camp='calculadora-en',
  ld={'@type': 'WebApplication', 'name': 'Book reading time calculator', 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Any', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}},
  cuerpo=lambda: f'''
  <div class="articulo">
    <h1>How long does it take to read a book?</h1>
    <p class="bajada">An average adult reads a 300-page book in about 6 hours. For the classics below we counted the real words, so you can see the time at your own speed.</p>
  </div>
  {calculadora('en')}
  <div class="articulo">
    <p>Don't know your speed? <a href="/reading-speed-test/">Take the 1-minute reading speed test</a> and it will appear here.</p>
    <h2>Reading time for 25 classics</h2>
    <p>Word counts come from the public domain editions included in Lince. Times are pure reading: no breaks.</p>
    {tabla('en', CALC['en']['col'])}
    <h2>How we calculate it</h2>
    <p>Time is the number of words divided by your words per minute. We start at 238 words per minute, the estimate for silent reading of non-fiction in English from a <a href="{BRYSBAERT}" rel="noopener">review of 190 studies</a>. Fiction averaged about 260, and your real speed changes with the book and how tired you are.</p>
    <h2>Why pages are only an estimate</h2>
    <p>A page can hold anywhere from 200 to 400 words depending on the edition, so we count 300. If you know a book's word count, that gives a better answer.</p>
  </div>''',
  cta='Read your next book with Lince', ctap='A speed reading app that shows how long each classic takes at your speed, one word at a time.', boton='Get it on Google Play',
  pie=[('/', 'Lince'), ('/reading-speed-test/', 'Speed test'), ('/what-is-rsvp-reading/', 'What is RSVP?'), 'Contact'],
  script='<script src="/calculadora.js"></script>\n<script src="/idioma.js" defer></script>'),
 dict(lang='es', en='/how-long-to-read/', es='/es/cuanto-tarda-leer/', archivo='es/cuanto-tarda-leer',
  title='¿Cuánto se tarda en leer un libro? Calculadora de clásicos',
  desc='Mira cuánto toman 25 clásicos a tu velocidad de lectura, con el conteo real de palabras. Cambia tus palabras por minuto o escribe las páginas de cualquier libro.',
  h1='¿Cuánto se tarda en leer un libro?', alt='Gráfico de presentación de Lince', camp='calculadora-es',
  ld={'@type': 'WebApplication', 'name': 'Calculadora de tiempo de lectura', 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Any', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}},
  cuerpo=lambda: f'''
  <div class="articulo">
    <h1>¿Cuánto se tarda en leer un libro?</h1>
    <p class="bajada">Un adulto promedio lee un libro de 300 páginas en unas 6 horas. En los clásicos de abajo contamos las palabras reales, para que veas el tiempo a tu propia velocidad.</p>
  </div>
  {calculadora('es')}
  <div class="articulo">
    <p>¿No sabes tu velocidad? <a href="/es/prueba-velocidad-lectura/">Haz la prueba de velocidad de lectura de 1 minuto</a> y aparecerá aquí.</p>
    <h2>Tiempo de lectura de 25 clásicos</h2>
    <p>Las palabras se contaron en las ediciones de dominio público incluidas en Lince. Los tiempos son de lectura pura, sin descansos.</p>
    {tabla('es', CALC['es']['col'])}
    <h2>Cómo lo calculamos</h2>
    <p>El tiempo es el número de palabras dividido por tus palabras por minuto. Partimos en 238 palabras por minuto, la estimación para lectura silenciosa de no ficción en inglés de una <a href="{BRYSBAERT}" rel="noopener">revisión de 190 estudios</a>. En ficción el promedio fue de unas 260, y tu velocidad real cambia según el libro y lo cansado que estés.</p>
    <h2>Por qué las páginas son solo una estimación</h2>
    <p>Una página puede tener entre 200 y 400 palabras según la edición, así que contamos 300. Si conoces las palabras de un libro, el resultado es mejor.</p>
  </div>''',
  cta='Lee tu próximo libro con Lince', ctap='Una app de lectura rápida que te muestra cuánto toma cada clásico a tu velocidad, una palabra a la vez.', boton='Descárgala en Google Play',
  pie=[('/es/', 'Lince'), ('/es/prueba-velocidad-lectura/', 'Prueba de velocidad'), ('/es/que-es-rsvp/', '¿Qué es RSVP?'), 'Contacto'],
  script='<script src="/calculadora.js"></script>'),
 dict(lang='en', en='/what-is-rsvp-reading/', es='/es/que-es-rsvp/', archivo='what-is-rsvp-reading',
  title='What Is RSVP Reading? How It Works and What It Can Do',
  desc='RSVP shows one word at a time in a fixed spot. Learn how it works, what research says about speed and comprehension, and when it is worth using.',
  h1='What is RSVP reading?', alt='Lince feature graphic', camp='rsvp-en',
  ld={'@type': 'Article', 'author': {'@type': 'Organization', 'name': 'Lince'}, 'publisher': {'@type': 'Organization', 'name': 'Lince'}, 'datePublished': HOY, 'dateModified': HOY},
  cuerpo=lambda: f'''
  <article class="articulo">
    <h1>What is RSVP reading?</h1>
    <p class="fecha">By the Lince team · November 2, 2026 · We make Lince, an RSVP reading app.</p>
    <p class="bajada">RSVP stands for rapid serial visual presentation: words appear one at a time, always in the same spot, so your eyes don't have to travel along the line.</p>
    <h2>How RSVP works</h2>
    <p>In a normal page, your eyes jump from one group of letters to the next and sometimes go back. With RSVP, the text comes to you instead: you look at one point and each word appears there at a speed you choose.</p>
    <p>Many RSVP readers color one letter in each word. It marks where to rest your eyes, so you don't have to search for the start of each word. You can <a href="/#try">try it in your browser</a> in 30 seconds.</p>
    <h2>Does RSVP make you read faster?</h2>
    <p>It lets you set a pace and hold it, but it isn't a shortcut to understanding more. A major <a href="{ESTUDIO}" rel="noopener">2016 scientific review of reading and speed reading</a> found a trade-off between speed and accuracy. It judged it unlikely that readers can double or triple their speed, from about 250 to 500-750 words per minute, and understand a text as well as at normal speed.</p>
    <p>The same review says that reading faster with good comprehension depends on practice and language skills, such as a larger vocabulary. So be wary of any app that promises to triple your speed.</p>
    <h2>When RSVP is useful</h2>
    <ul>
      <li>Articles, newsletters and light fiction, where you want to move along.</li>
      <li>Reading on a small phone screen, without scrolling.</li>
      <li>Keeping a steady pace when you tend to drift off the page.</li>
    </ul>
    <h2>When a normal page is better</h2>
    <ul>
      <li>Study material, contracts or anything you need to remember in detail.</li>
      <li>Tables, formulas and images.</li>
      <li>Texts where you often need to look back. In RSVP you have to pause to do that.</li>
    </ul>
    <h2>How to start</h2>
    <ol>
      <li><a href="/reading-speed-test/">Measure your normal speed</a>.</li>
      <li>Start close to that speed, not at the highest one.</li>
      <li>Raise it a little at a time, and slow down as soon as you stop following.</li>
      <li>Try a text you enjoy for a few minutes: the first moments feel strange.</li>
    </ol>
    <h2>Is RSVP good for ADHD or dyslexia?</h2>
    <p>We don't know of solid evidence that it helps, and RSVP is not a treatment. If you want to try it, go at a comfortable pace and keep what works for you.</p>
  </article>''',
  cta='Try RSVP on your own books', ctap='Lince is an RSVP speed reader for Android: EPUB, PDF, articles and 50 classics, one word at a time.', boton='Get it on Google Play',
  pie=[('/', 'Lince'), ('/reading-speed-test/', 'Speed test'), ('/how-long-to-read/', 'Reading time'), 'Contact'],
  script='<script src="/idioma.js" defer></script>'),
 dict(lang='es', en='/what-is-rsvp-reading/', es='/es/que-es-rsvp/', archivo='es/que-es-rsvp',
  title='¿Qué es la lectura RSVP? Cómo funciona y qué puede lograr',
  desc='RSVP muestra una palabra a la vez en un punto fijo. Aprende cómo funciona, qué dice la investigación sobre velocidad y comprensión, y cuándo conviene usarla.',
  h1='¿Qué es la lectura RSVP?', alt='Gráfico de presentación de Lince', camp='rsvp-es',
  ld={'@type': 'Article', 'author': {'@type': 'Organization', 'name': 'Lince'}, 'publisher': {'@type': 'Organization', 'name': 'Lince'}, 'datePublished': HOY, 'dateModified': HOY},
  cuerpo=lambda: f'''
  <article class="articulo">
    <h1>¿Qué es la lectura RSVP?</h1>
    <p class="fecha">Por el equipo de Lince · 2 de noviembre de 2026 · Hacemos Lince, una app de lectura RSVP.</p>
    <p class="bajada">RSVP significa presentación visual serial rápida: las palabras aparecen de a una, siempre en el mismo lugar, así tus ojos no tienen que recorrer la línea.</p>
    <h2>Cómo funciona RSVP</h2>
    <p>En una página normal, los ojos saltan de un grupo de letras al siguiente y a veces vuelven atrás. Con RSVP, el texto llega a ti: miras un punto y cada palabra aparece ahí a la velocidad que elijas.</p>
    <p>Muchos lectores RSVP colorean una letra de cada palabra. Marca dónde descansar la vista, para que no tengas que buscar el inicio de cada palabra. Puedes <a href="/es/#prueba">probarlo en tu navegador</a> en 30 segundos.</p>
    <h2>¿RSVP te hace leer más rápido?</h2>
    <p>Te deja fijar un ritmo y mantenerlo, pero no es un atajo para entender más. Una importante <a href="{ESTUDIO}" rel="noopener">revisión científica de 2016 sobre lectura y lectura rápida</a> encontró una compensación entre velocidad y precisión. Consideró poco probable duplicar o triplicar la velocidad, de unas 250 a 500-750 palabras por minuto, y entender un texto tan bien como a velocidad normal.</p>
    <p>La misma revisión dice que leer más rápido con buena comprensión depende de la práctica y del dominio del idioma, como tener más vocabulario. Por eso conviene desconfiar de cualquier app que prometa triplicar tu velocidad.</p>
    <h2>Cuándo sirve RSVP</h2>
    <ul>
      <li>Artículos, boletines y ficción ligera, cuando quieres avanzar.</li>
      <li>Leer en la pantalla pequeña del teléfono, sin desplazarte.</li>
      <li>Mantener un ritmo parejo si tiendes a distraerte de la página.</li>
    </ul>
    <h2>Cuándo es mejor una página normal</h2>
    <ul>
      <li>Material de estudio, contratos o lo que debas recordar con detalle.</li>
      <li>Tablas, fórmulas e imágenes.</li>
      <li>Textos en los que necesitas volver atrás seguido. En RSVP tienes que pausar para hacerlo.</li>
    </ul>
    <h2>Cómo empezar</h2>
    <ol>
      <li><a href="/es/prueba-velocidad-lectura/">Mide tu velocidad normal</a>.</li>
      <li>Empieza cerca de esa velocidad, no en la más alta.</li>
      <li>Súbela de a poco y baja apenas dejes de seguir el hilo.</li>
      <li>Prueba unos minutos con un texto que te guste: al principio se siente raro.</li>
    </ol>
    <h2>¿RSVP sirve para el TDAH o la dislexia?</h2>
    <p>No conocemos evidencia sólida de que ayude, y RSVP no es un tratamiento. Si quieres probarlo, ve a un ritmo cómodo y quédate con lo que te sirva.</p>
  </article>''',
  cta='Prueba RSVP con tus propios libros', ctap='Lince es un lector RSVP para Android: EPUB, PDF, artículos y 50 clásicos, una palabra a la vez.', boton='Descárgala en Google Play',
  pie=[('/es/', 'Lince'), ('/es/prueba-velocidad-lectura/', 'Prueba de velocidad'), ('/es/cuanto-tarda-leer/', 'Tiempo de lectura'), 'Contacto']),
]

for g in GUIAS:
    g['cuerpo'] = g['cuerpo']()
    destino = Path(g['archivo']) / 'index.html'
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(pagina(g))
