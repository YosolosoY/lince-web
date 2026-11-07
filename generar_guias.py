#!/usr/bin/env python3
"""Páginas de guía en inglés y español. datos/clasicos.json sale del catálogo de la app."""
import html, json
from pathlib import Path

from idiomas import OG_LOCALE, RUTAS, alternos, menu_idiomas, otros_idiomas

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
    url = p.get('url') or RUTAS[p['clave']][p['lang']]
    home = RUTAS['inicio'][p['lang']]
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
{p['alternos'] if 'alternos' in p else alternos(p['clave'])}
<link rel="icon" href="/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/icono-180.png">
<meta name="theme-color" content="#FDF6E3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#151515" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Lince">
<meta property="og:locale" content="{OG_LOCALE[p['lang']]}">
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
      {p['menu'] if 'menu' in p else menu_idiomas(p['clave'], p['lang'])}
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
    <nav class="pie-idiomas">{p['otros'] if 'otros' in p else otros_idiomas(p['clave'], p['lang'], ' ')}</nav>
  </footer>
</main>
{p.get('script', '')}
<script src="/analitica.js" defer></script>
</body>
</html>
'''


MILES = {'en': ',', 'es': '.', 'pt': '.', 'fr': '\u202f', 'de': '.', 'it': '.'}


def enlace_libro(b):
    import re, unicodedata
    s = re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', b['t']).encode('ascii', 'ignore').decode().lower()).strip('-')
    return f"<a href=\"{RUTAS['tiempo'][b['l']]}{s}/\">{html.escape(b['t'])}</a>"


def tabla(lang, t):
    filas = sorted((b for b in LIBROS if b['l'] == lang), key=lambda b: b['w'])
    cuerpo = '\n'.join(
        f'''        <tr data-palabras="{b['w']}"><td>{enlace_libro(b)}<br><small>{html.escape(b['a'])}</small></td><td>{f"{b['w']:,}".replace(',', MILES[lang])}</td><td class="tiempo">{tiempo(b['w'], 238)}</td></tr>'''
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


SCRIPTS_CALC = '<script src="/calculadora.js"></script>\n<script src="/idioma.js" defer></script>'

GUIAS = [
 dict(lang='en', en='/how-long-to-read/', es='/es/cuanto-tarda-leer/', clave='tiempo', archivo='how-long-to-read',
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
 dict(lang='es', en='/how-long-to-read/', es='/es/cuanto-tarda-leer/', clave='tiempo', archivo='es/cuanto-tarda-leer',
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
  script=SCRIPTS_CALC),
 dict(lang='en', en='/what-is-rsvp-reading/', es='/es/que-es-rsvp/', clave='rsvp', archivo='what-is-rsvp-reading',
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
  cta='Try RSVP on your own books', ctap='Lince is an RSVP speed reader for Android: EPUB, PDF, articles and 150 classics in 6 languages, one word at a time.', boton='Get it on Google Play',
  pie=[('/', 'Lince'), ('/reading-speed-test/', 'Speed test'), ('/how-long-to-read/', 'Reading time'), 'Contact'],
  script='<script src="/idioma.js" defer></script>'),
 dict(lang='es', en='/what-is-rsvp-reading/', es='/es/que-es-rsvp/', clave='rsvp', archivo='es/que-es-rsvp',
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
  cta='Prueba RSVP con tus propios libros', ctap='Lince es un lector RSVP para Android: EPUB, PDF, artículos y 150 clásicos en 6 idiomas, una palabra a la vez.', boton='Descárgala en Google Play',
  pie=[('/es/', 'Lince'), ('/es/prueba-velocidad-lectura/', 'Prueba de velocidad'), ('/es/cuanto-tarda-leer/', 'Tiempo de lectura'), 'Contacto'],
  script='<script src="/idioma.js" defer></script>'),
]


# ---------- Portugués, francés, alemán e italiano ----------

CALC.update({
 'pt': dict(ppm='Sua velocidade (palavras por minuto)', pag='Qualquer outro livro: número de páginas', res='Cerca de {t} a {p} ppm, contando 300 palavras por página.',
   col=('Livro', 'Palavras', 'Tempo'), ph='320'),
 'fr': dict(ppm='Votre vitesse (mots par minute)', pag="N'importe quel autre livre : nombre de pages", res='Environ {t} à {p} mots/min, en comptant 300 mots par page.',
   col=('Livre', 'Mots', 'Temps'), ph='320'),
 'de': dict(ppm='Dein Tempo (Wörter pro Minute)', pag='Jedes andere Buch: Anzahl der Seiten', res='Etwa {t} bei {p} WpM, gerechnet mit 300 Wörtern pro Seite.',
   col=('Buch', 'Wörter', 'Zeit'), ph='320'),
 'it': dict(ppm='La tua velocità (parole al minuto)', pag='Qualsiasi altro libro: numero di pagine', res='Circa {t} a {p} ppm, contando 300 parole per pagina.',
   col=('Libro', 'Parole', 'Tempo'), ph='320'),
})

LD_CALC = lambda nombre: {'@type': 'WebApplication', 'name': nombre, 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Any', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}
LD_ART = {'@type': 'Article', 'author': {'@type': 'Organization', 'name': 'Lince'}, 'publisher': {'@type': 'Organization', 'name': 'Lince'}, 'datePublished': '2026-11-03', 'dateModified': '2026-11-03'}

TIEMPO = {
 'pt': dict(title='Quanto tempo leva para ler um livro? Calculadora de clássicos',
   desc='Veja quanto tempo 25 clássicos levam na sua velocidade, com a contagem real de palavras, ou calcule qualquer livro pelas páginas.',
   h1='Quanto tempo leva para ler um livro?', alt='Gráfico do Lince', nombre='Calculadora de tempo de leitura',
   bajada='Um adulto médio lê um livro de 300 páginas em cerca de 6 horas. Nos clássicos abaixo contamos as palavras reais, para você ver o tempo na sua própria velocidade.',
   nosabes='Não sabe sua velocidade? <a href="{prueba}">Faça o teste de velocidade de leitura de 1 minuto</a> e ela aparecerá aqui.',
   h2a='Tempo de leitura de 25 clássicos', pa='As palavras foram contadas nas edições de domínio público incluídas no Lince. Os tempos são de leitura pura, sem pausas.',
   h2b='Como calculamos', pb='O tempo é o número de palavras dividido pelas suas palavras por minuto. Partimos de 238 palavras por minuto, a estimativa de leitura silenciosa de não ficção em inglês de uma <a href="{brys}" rel="noopener">revisão de 190 estudos</a>. Em português as palavras costumam ser mais longas, e sua velocidade real muda com o livro e o cansaço.',
   h2c='Por que as páginas são só uma estimativa', pc='Uma página pode ter de 200 a 400 palavras, dependendo da edição, então contamos 300. Se você souber quantas palavras um livro tem, o resultado é melhor.',
   cta='Leia seu próximo livro com o Lince', ctap='Um app de leitura dinâmica que mostra quanto tempo cada clássico leva na sua velocidade, uma palavra por vez.', boton='Baixar no Google Play',
   pie=('Teste de velocidade', 'O que é RSVP?', 'Contato')),
 'fr': dict(title='Combien de temps pour lire un livre ? Calculateur de classiques',
   desc='Combien de temps pour lire 25 classiques à votre vitesse, d’après le vrai nombre de mots ? Ou calculez n’importe quel livre par ses pages.',
   h1='Combien de temps faut-il pour lire un livre ?', alt='Visuel de Lince', nombre='Calculateur de temps de lecture',
   bajada='Un adulte moyen lit un livre de 300 pages en environ 6 heures. Pour les classiques ci-dessous, nous avons compté les vrais mots, pour que vous voyiez le temps à votre propre vitesse.',
   nosabes='Vous ne connaissez pas votre vitesse ? <a href="{prueba}">Faites le test de vitesse de lecture en 1 minute</a> et elle s’affichera ici.',
   h2a='Temps de lecture de 25 classiques', pa='Les mots ont été comptés dans les éditions du domaine public incluses dans Lince. Les temps sont de la lecture pure, sans pauses.',
   h2b='Notre calcul', pb='Le temps correspond au nombre de mots divisé par vos mots par minute. Nous partons de 238 mots par minute, l’estimation de la lecture silencieuse de textes documentaires en anglais issue d’une <a href="{brys}" rel="noopener">synthèse de 190 études</a>. En français les mots sont en moyenne plus longs, et votre vitesse réelle varie selon le livre et la fatigue.',
   h2c='Pourquoi les pages ne sont qu’une estimation', pc='Une page peut contenir de 200 à 400 mots selon l’édition, nous en comptons donc 300. Si vous connaissez le nombre de mots d’un livre, le résultat est plus juste.',
   cta='Lisez votre prochain livre avec Lince', ctap='Une appli de lecture rapide qui montre combien de temps prend chaque classique à votre vitesse, un mot à la fois.', boton='Disponible sur Google Play',
   pie=('Test de vitesse', 'Lecture RSVP', 'Contact')),
 'de': dict(title='Wie lange dauert es, ein Buch zu lesen? Klassiker-Rechner',
   desc='Sieh, wie lange 25 Klassiker bei deinem Lesetempo dauern, mit echter Wortzahl. Ändere deine Wörter pro Minute oder gib die Seitenzahl eines beliebigen Buchs ein.',
   h1='Wie lange dauert es, ein Buch zu lesen?', alt='Grafik von Lince', nombre='Lesezeit-Rechner',
   bajada='Ein durchschnittlicher Erwachsener liest ein Buch mit 300 Seiten in etwa 6 Stunden. Bei den Klassikern unten haben wir die echten Wörter gezählt, damit du die Zeit bei deinem eigenen Tempo siehst.',
   nosabes='Du kennst dein Tempo nicht? <a href="{prueba}">Mach den 1-Minuten-Lesetest</a>, dann erscheint es hier.',
   h2a='Lesezeit von 25 Klassikern', pa='Die Wörter wurden in den gemeinfreien Ausgaben gezählt, die in Lince enthalten sind. Die Zeiten sind reine Lesezeit, ohne Pausen.',
   h2b='So rechnen wir', pb='Die Zeit ist die Zahl der Wörter geteilt durch deine Wörter pro Minute. Wir starten mit 238 Wörtern pro Minute, der Schätzung für stilles Lesen von Sachtexten auf Englisch aus einer <a href="{brys}" rel="noopener">Übersicht über 190 Studien</a>. Deutsche Wörter sind im Schnitt länger, und dein echtes Tempo hängt vom Buch und von deiner Müdigkeit ab.',
   h2c='Warum Seiten nur eine Schätzung sind', pc='Eine Seite kann je nach Ausgabe 200 bis 400 Wörter haben, deshalb rechnen wir mit 300. Wenn du die Wortzahl eines Buchs kennst, wird das Ergebnis genauer.',
   cta='Lies dein nächstes Buch mit Lince', ctap='Eine Schnelllese-App, die zeigt, wie lange jeder Klassiker bei deinem Tempo dauert, ein Wort nach dem anderen.', boton='Jetzt bei Google Play',
   pie=('Tempotest', 'Was ist RSVP?', 'Kontakt')),
 'it': dict(title='Quanto tempo ci vuole per leggere un libro? Calcolatore dei classici',
   desc='Quanto tempo richiedono 25 classici alla tua velocità, con il conteggio reale delle parole? Oppure calcola qualsiasi libro dalle pagine.',
   h1='Quanto tempo ci vuole per leggere un libro?', alt='Grafica di Lince', nombre='Calcolatore del tempo di lettura',
   bajada='Un adulto medio legge un libro di 300 pagine in circa 6 ore. Per i classici qui sotto abbiamo contato le parole reali, così vedi il tempo alla tua velocità.',
   nosabes='Non conosci la tua velocità? <a href="{prueba}">Fai il test di velocità di lettura di 1 minuto</a> e comparirà qui.',
   h2a='Tempo di lettura di 25 classici', pa='Le parole sono state contate nelle edizioni di pubblico dominio incluse in Lince. I tempi sono di sola lettura, senza pause.',
   h2b='Come lo calcoliamo', pb='Il tempo è il numero di parole diviso per le tue parole al minuto. Partiamo da 238 parole al minuto, la stima della lettura silenziosa di saggistica in inglese di una <a href="{brys}" rel="noopener">rassegna di 190 studi</a>. In italiano le parole sono in media più lunghe, e la tua velocità reale cambia con il libro e la stanchezza.',
   h2c='Perché le pagine sono solo una stima', pc='Una pagina può avere da 200 a 400 parole a seconda dell’edizione, quindi ne contiamo 300. Se conosci il numero di parole di un libro, il risultato è più preciso.',
   cta='Leggi il tuo prossimo libro con Lince', ctap="Un'app di lettura veloce che ti mostra quanto tempo richiede ogni classico alla tua velocità, una parola alla volta.", boton='Disponibile su Google Play',
   pie=('Test di velocità', "Cos'è RSVP?", 'Contatti')),
}

RSVP = {
 'pt': dict(title='O que é a leitura RSVP? Como funciona e o que ela pode fazer',
   desc='O RSVP mostra uma palavra por vez num ponto fixo. Entenda como funciona, o que dizem as pesquisas sobre velocidade e compreensão, e quando vale a pena usar.',
   h1='O que é a leitura RSVP?', alt='Gráfico do Lince', fecha='Pela equipe do Lince · 3 de novembro de 2026 · Fazemos o Lince, um app de leitura RSVP.',
   cuerpo=r"""<p class="bajada">RSVP significa apresentação visual serial rápida: as palavras aparecem uma a uma, sempre no mesmo lugar, e seus olhos não precisam percorrer a linha.</p>
    <h2>Como o RSVP funciona</h2>
    <p>Numa página normal, os olhos saltam de um grupo de letras para o próximo e às vezes voltam. Com o RSVP é o texto que vem até você: você olha para um ponto e cada palavra aparece ali, na velocidade que escolher.</p>
    <p>Muitos leitores RSVP colorem uma letra de cada palavra. Ela marca onde apoiar a vista, para você não ter que procurar o início de cada palavra. Você pode <a href="{inicio}#try">experimentar no navegador</a> em 30 segundos.</p>
    <h2>O RSVP faz você ler mais rápido?</h2>
    <p>Ele permite fixar um ritmo e mantê-lo, mas não é um atalho para entender mais. Uma importante <a href="{estudio}" rel="noopener">revisão científica de 2016 sobre leitura e leitura dinâmica</a> encontrou uma troca entre velocidade e precisão. Considerou improvável dobrar ou triplicar a velocidade, de cerca de 250 para 500-750 palavras por minuto, e entender um texto tão bem quanto na velocidade normal.</p>
    <p>A mesma revisão diz que ler mais rápido com boa compreensão depende da prática e do domínio do idioma, como ter mais vocabulário. Por isso, desconfie de qualquer app que prometa triplicar sua velocidade.</p>
    <h2>Quando o RSVP é útil</h2>
    <ul>
      <li>Artigos, newsletters e ficção leve, quando você quer avançar.</li>
      <li>Ler na tela pequena do celular, sem rolar.</li>
      <li>Manter um ritmo constante se você costuma se distrair da página.</li>
    </ul>
    <h2>Quando uma página normal é melhor</h2>
    <ul>
      <li>Material de estudo, contratos ou o que você precisa lembrar em detalhe.</li>
      <li>Tabelas, fórmulas e imagens.</li>
      <li>Textos em que você precisa voltar com frequência. No RSVP é preciso pausar para isso.</li>
    </ul>
    <h2>Como começar</h2>
    <ol>
      <li><a href="{prueba}">Meça sua velocidade normal</a>.</li>
      <li>Comece perto dessa velocidade, não na mais alta.</li>
      <li>Suba aos poucos e diminua assim que deixar de acompanhar.</li>
      <li>Experimente por alguns minutos com um texto de que você goste: no começo parece estranho.</li>
    </ol>
    <h2>O RSVP serve para TDAH ou dislexia?</h2>
    <p>Não conhecemos evidências sólidas de que ajude, e o RSVP não é um tratamento. Se quiser experimentar, vá num ritmo confortável e fique com o que funcionar para você.</p>""",
   cta='Experimente o RSVP com seus próprios livros', ctap='O Lince é um leitor RSVP para Android: EPUB, PDF, artigos e 150 clássicos em 6 idiomas, uma palavra por vez.', boton='Baixar no Google Play',
   pie=('Teste de velocidade', 'Tempo de leitura', 'Contato')),
 'fr': dict(title="Qu'est-ce que la lecture RSVP ? Fonctionnement et limites",
   desc='La lecture RSVP affiche un mot à la fois à un endroit fixe. Fonctionnement, ce que dit la recherche sur vitesse et compréhension, et quand l’utiliser.',
   h1="Qu'est-ce que la lecture RSVP ?", alt='Visuel de Lince', fecha="Par l'équipe de Lince · 3 novembre 2026 · Nous développons Lince, une appli de lecture RSVP.",
   cuerpo=r"""<p class="bajada">RSVP signifie présentation visuelle sérielle rapide : les mots apparaissent un par un, toujours au même endroit, et vos yeux n'ont pas à parcourir la ligne.</p>
    <h2>Comment fonctionne la lecture RSVP</h2>
    <p>Sur une page normale, les yeux sautent d'un groupe de lettres au suivant et reviennent parfois en arrière. Avec la RSVP, c'est le texte qui vient à vous : vous regardez un point et chaque mot y apparaît, à la vitesse que vous choisissez.</p>
    <p>Beaucoup de lecteurs RSVP colorent une lettre de chaque mot. Elle indique où poser le regard, pour ne pas chercher le début de chaque mot. Vous pouvez <a href="{inicio}#try">l'essayer dans votre navigateur</a> en 30 secondes.</p>
    <h2>La RSVP fait-elle lire plus vite ?</h2>
    <p>Elle permet de fixer un rythme et de le tenir, mais ce n'est pas un raccourci pour comprendre davantage. Une importante <a href="{estudio}" rel="noopener">synthèse scientifique de 2016 sur la lecture et la lecture rapide</a> a constaté un compromis entre vitesse et précision. Elle juge peu probable de doubler ou tripler sa vitesse, d'environ 250 à 500-750 mots par minute, tout en comprenant un texte aussi bien qu'à vitesse normale.</p>
    <p>La même synthèse explique que lire plus vite en comprenant bien dépend de la pratique et de la maîtrise de la langue, comme un vocabulaire plus riche. Méfiez-vous donc des applis qui promettent de tripler votre vitesse.</p>
    <h2>Quand la RSVP est utile</h2>
    <ul>
      <li>Articles, newsletters et romans légers, quand vous voulez avancer.</li>
      <li>Lire sur le petit écran du téléphone, sans faire défiler.</li>
      <li>Garder un rythme régulier si vous avez tendance à décrocher.</li>
    </ul>
    <h2>Quand une page normale vaut mieux</h2>
    <ul>
      <li>Cours, contrats ou tout ce que vous devez retenir en détail.</li>
      <li>Tableaux, formules et images.</li>
      <li>Les textes où vous devez souvent revenir en arrière. En RSVP, il faut faire une pause pour cela.</li>
    </ul>
    <h2>Comment commencer</h2>
    <ol>
      <li><a href="{prueba}">Mesurez votre vitesse normale</a>.</li>
      <li>Commencez près de cette vitesse, pas à la plus élevée.</li>
      <li>Augmentez-la peu à peu et ralentissez dès que vous ne suivez plus.</li>
      <li>Essayez quelques minutes avec un texte qui vous plaît : au début, c'est étrange.</li>
    </ol>
    <h2>La RSVP aide-t-elle en cas de TDAH ou de dyslexie ?</h2>
    <p>Nous ne connaissons pas de preuves solides qu'elle aide, et la RSVP n'est pas un traitement. Si vous voulez l'essayer, allez à un rythme confortable et gardez ce qui vous convient.</p>""",
   cta='Essayez la RSVP avec vos propres livres', ctap='Lince est un lecteur RSVP pour Android : EPUB, PDF, articles et 150 classiques en 6 langues, un mot à la fois.', boton='Disponible sur Google Play',
   pie=('Test de vitesse', 'Temps de lecture', 'Contact')),
 'de': dict(title='Was ist RSVP-Lesen? Wie es funktioniert und was es kann',
   desc='RSVP zeigt ein Wort nach dem anderen an einer festen Stelle. Erfahre, wie es funktioniert, was die Forschung über Tempo und Verständnis sagt und wann es sich lohnt.',
   h1='Was ist RSVP-Lesen?', alt='Grafik von Lince', fecha='Vom Lince-Team · 3. November 2026 · Wir entwickeln Lince, eine RSVP-Lese-App.',
   cuerpo=r"""<p class="bajada">RSVP steht für Rapid Serial Visual Presentation: Die Wörter erscheinen nacheinander, immer an derselben Stelle, sodass deine Augen nicht die Zeile entlangwandern müssen.</p>
    <h2>Wie RSVP funktioniert</h2>
    <p>Auf einer normalen Seite springen die Augen von einer Buchstabengruppe zur nächsten und manchmal zurück. Bei RSVP kommt der Text zu dir: Du schaust auf einen Punkt, und jedes Wort erscheint dort in dem Tempo, das du wählst.</p>
    <p>Viele RSVP-Leser färben einen Buchstaben jedes Wortes ein. Er zeigt, wo dein Blick ruhen soll, damit du nicht den Anfang jedes Wortes suchen musst. Du kannst es <a href="{inicio}#try">im Browser ausprobieren</a>, in 30 Sekunden.</p>
    <h2>Liest man mit RSVP schneller?</h2>
    <p>Du kannst ein Tempo festlegen und halten, aber es ist keine Abkürzung zu mehr Verständnis. Eine wichtige <a href="{estudio}" rel="noopener">wissenschaftliche Übersicht von 2016 über Lesen und Schnelllesen</a> fand einen Zielkonflikt zwischen Tempo und Genauigkeit. Sie hielt es für unwahrscheinlich, die Geschwindigkeit zu verdoppeln oder zu verdreifachen, von etwa 250 auf 500 bis 750 Wörter pro Minute, und einen Text trotzdem so gut zu verstehen wie bei normalem Tempo.</p>
    <p>Dieselbe Übersicht sagt, dass schnelleres Lesen mit gutem Verständnis von Übung und Sprachkenntnissen abhängt, etwa einem größeren Wortschatz. Sei also misstrauisch bei jeder App, die dir dreifaches Tempo verspricht.</p>
    <h2>Wann RSVP nützlich ist</h2>
    <ul>
      <li>Artikel, Newsletter und leichte Romane, wenn du vorankommen willst.</li>
      <li>Lesen auf dem kleinen Handybildschirm, ohne zu scrollen.</li>
      <li>Ein gleichmäßiges Tempo halten, wenn du sonst leicht abschweifst.</li>
    </ul>
    <h2>Wann eine normale Seite besser ist</h2>
    <ul>
      <li>Lernstoff, Verträge oder alles, was du dir genau merken musst.</li>
      <li>Tabellen, Formeln und Bilder.</li>
      <li>Texte, bei denen du oft zurückblättern musst. Bei RSVP musst du dafür pausieren.</li>
    </ul>
    <h2>So fängst du an</h2>
    <ol>
      <li><a href="{prueba}">Miss dein normales Tempo</a>.</li>
      <li>Beginne nahe an diesem Tempo, nicht beim höchsten.</li>
      <li>Steigere es nach und nach und werde langsamer, sobald du nicht mehr folgst.</li>
      <li>Probier es ein paar Minuten mit einem Text, der dir gefällt: Am Anfang fühlt es sich seltsam an.</li>
    </ol>
    <h2>Hilft RSVP bei ADHS oder Legasthenie?</h2>
    <p>Wir kennen keine soliden Belege dafür, und RSVP ist keine Behandlung. Wenn du es ausprobieren willst, lies in einem angenehmen Tempo und behalte, was dir hilft.</p>""",
   cta='Probier RSVP mit deinen eigenen Büchern', ctap='Lince ist ein RSVP-Leser für Android: EPUB, PDF, Artikel und 150 Klassiker in 6 Sprachen, ein Wort nach dem anderen.', boton='Jetzt bei Google Play',
   pie=('Tempotest', 'Lesezeit', 'Kontakt')),
 'it': dict(title="Cos'è la lettura RSVP? Come funziona e cosa può fare",
   desc='La lettura RSVP mostra una parola alla volta in un punto fisso. Scopri come funziona, cosa dice la ricerca su velocità e comprensione, e quando conviene usarla.',
   h1="Cos'è la lettura RSVP?", alt='Grafica di Lince', fecha="Dal team di Lince · 3 novembre 2026 · Sviluppiamo Lince, un'app di lettura RSVP.",
   cuerpo=r"""<p class="bajada">RSVP significa presentazione visiva seriale rapida: le parole compaiono una alla volta, sempre nello stesso punto, così gli occhi non devono percorrere la riga.</p>
    <h2>Come funziona la lettura RSVP</h2>
    <p>In una pagina normale gli occhi saltano da un gruppo di lettere al successivo e a volte tornano indietro. Con la RSVP è il testo a venire da te: guardi un punto e ogni parola compare lì, alla velocità che scegli.</p>
    <p>Molti lettori RSVP colorano una lettera di ogni parola. Indica dove appoggiare lo sguardo, così non devi cercare l'inizio di ogni parola. Puoi <a href="{inicio}#try">provarla nel browser</a> in 30 secondi.</p>
    <h2>La RSVP fa leggere più veloce?</h2>
    <p>Ti permette di fissare un ritmo e mantenerlo, ma non è una scorciatoia per capire di più. Un'importante <a href="{estudio}" rel="noopener">rassegna scientifica del 2016 sulla lettura e la lettura veloce</a> ha trovato un compromesso tra velocità e precisione. Ha giudicato improbabile raddoppiare o triplicare la velocità, da circa 250 a 500-750 parole al minuto, e capire un testo bene come a velocità normale.</p>
    <p>La stessa rassegna dice che leggere più veloce capendo bene dipende dalla pratica e dalla padronanza della lingua, come un vocabolario più ampio. Quindi diffida di qualsiasi app che prometta di triplicare la tua velocità.</p>
    <h2>Quando la RSVP è utile</h2>
    <ul>
      <li>Articoli, newsletter e narrativa leggera, quando vuoi andare avanti.</li>
      <li>Leggere sul piccolo schermo del telefono, senza scorrere.</li>
      <li>Mantenere un ritmo costante se tendi a distrarti dalla pagina.</li>
    </ul>
    <h2>Quando è meglio una pagina normale</h2>
    <ul>
      <li>Materiale di studio, contratti o ciò che devi ricordare nei dettagli.</li>
      <li>Tabelle, formule e immagini.</li>
      <li>Testi in cui devi tornare indietro spesso. Con la RSVP devi mettere in pausa per farlo.</li>
    </ul>
    <h2>Come iniziare</h2>
    <ol>
      <li><a href="{prueba}">Misura la tua velocità normale</a>.</li>
      <li>Inizia vicino a quella velocità, non alla più alta.</li>
      <li>Aumentala poco a poco e rallenta appena smetti di seguire.</li>
      <li>Prova per qualche minuto con un testo che ti piace: all'inizio sembra strano.</li>
    </ol>
    <h2>La RSVP aiuta con ADHD o dislessia?</h2>
    <p>Non conosciamo prove solide che aiuti, e la RSVP non è una terapia. Se vuoi provarla, vai a un ritmo comodo e tieni ciò che funziona per te.</p>""",
   cta='Prova la RSVP con i tuoi libri', ctap='Lince è un lettore RSVP per Android: EPUB, PDF, articoli e 150 classici in 6 lingue, una parola alla volta.', boton='Disponibile su Google Play',
   pie=('Test di velocità', 'Tempo di lettura', 'Contatti')),
}

for _l, _t in TIEMPO.items():
    _r = lambda k: RUTAS[k][_l]
    GUIAS.append(dict(lang=_l, clave='tiempo', archivo=_r('tiempo').strip('/'), title=_t['title'], desc=_t['desc'], h1=_t['h1'], alt=_t['alt'],
      camp=f'calculadora-{_l}', ld=LD_CALC(_t['nombre']),
      cuerpo=(lambda l=_l, t=_t: f"""
  <div class="articulo">
    <h1>{t['h1']}</h1>
    <p class="bajada">{t['bajada']}</p>
  </div>
  {calculadora(l)}
  <div class="articulo">
    <p>{t['nosabes'].replace('{prueba}', RUTAS['prueba'][l])}</p>
    <h2>{t['h2a']}</h2>
    <p>{t['pa']}</p>
    {tabla(l, CALC[l]['col'])}
    <h2>{t['h2b']}</h2>
    <p>{t['pb'].replace('{brys}', BRYSBAERT)}</p>
    <h2>{t['h2c']}</h2>
    <p>{t['pc']}</p>
  </div>"""),
      cta=_t['cta'], ctap=_t['ctap'], boton=_t['boton'],
      pie=[(RUTAS['inicio'][_l], 'Lince'), (RUTAS['prueba'][_l], _t['pie'][0]), (RUTAS['rsvp'][_l], _t['pie'][1]), _t['pie'][2]],
      script=SCRIPTS_CALC))

for _l, _t in RSVP.items():
    GUIAS.append(dict(lang=_l, clave='rsvp', archivo=RUTAS['rsvp'][_l].strip('/'), title=_t['title'], desc=_t['desc'], h1=_t['h1'], alt=_t['alt'],
      camp=f'rsvp-{_l}', ld=LD_ART,
      cuerpo=(lambda l=_l, t=_t: f"""
  <article class="articulo">
    <h1>{t['h1']}</h1>
    <p class="fecha">{t['fecha']}</p>
    {t['cuerpo'].replace('{inicio}', RUTAS['inicio'][l]).replace('{estudio}', ESTUDIO).replace('{prueba}', RUTAS['prueba'][l])}
  </article>"""),
      cta=_t['cta'], ctap=_t['ctap'], boton=_t['boton'],
      pie=[(RUTAS['inicio'][_l], 'Lince'), (RUTAS['prueba'][_l], _t['pie'][0]), (RUTAS['tiempo'][_l], _t['pie'][1]), _t['pie'][2]],
      script='<script src="/idioma.js" defer></script>'))

for g in GUIAS:
    g['cuerpo'] = g['cuerpo']()
    destino = Path(g['archivo']) / 'index.html'
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(pagina(g))
