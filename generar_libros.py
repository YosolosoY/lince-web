#!/usr/bin/env python3
"""Una página por clásico ("¿cuánto tarda leer X?") en el idioma del libro. 150 páginas desde datos/clasicos.json.

Responde a las búsquedas reales de Search Console ("how long to read 1984", "tiempo de lectura"). Cada página vive bajo la
guía de su idioma (RUTAS['tiempo']) y no tiene hreflang: el libro existe solo en ese idioma. Correr tras generar_guias.py:
    python3 generar_libros.py && python3 generar_sitemap.py
"""
import html
import json
import math
import re
import unicodedata
from pathlib import Path

from generar_guias import LIBROS, MILES, PLAY, SCRIPTS_CALC, pagina, tiempo  # noqa: F401  (importar regenera las guías, sin cambios)
from idiomas import B, RUTAS

LD_LIBRO = lambda t, a, url: {'@type': 'Article', 'author': {'@type': 'Organization', 'name': 'Lince'}, 'publisher': {'@type': 'Organization', 'name': 'Lince'},
                              'datePublished': '2026-11-07', 'dateModified': '2026-11-07', 'about': {'@type': 'Book', 'name': t, 'author': {'@type': 'Person', 'name': a}}}
VEL = (150, 238, 300, 400)

T = {
 'en': dict(title='How Long Does It Take to Read {t}? ({a})', desc='{t} by {a} has about {w} words. At an average speed it takes {tm}. See the time at 150, 238, 300 and 400 words per minute.',
   h1='How long does it take to read {t}?', bajada='{t} by {a} has about {w} words in the edition included in Lince. At the average adult reading speed of 238 words per minute, that is about <strong>{tm}</strong>.',
   h2v='Reading time at different speeds', cab=('Speed', 'Time'), nom=('Slow reader', 'Average', 'Fast', 'Very fast'), ppm='{v} wpm',
   nota='Times are pure reading, without breaks. At 300 words per page, this edition would be about {pg} pages.',
   h2p='Common questions', q1='How many words are in {t}?', a1='About {w} words in the edition included in Lince. Other editions vary a little.',
   q2='How many days to finish {t}?', a2='Reading 30 minutes a day at an average speed, about {d} days.',
   prueba='Don\'t know your speed? <a href="{u}">Take the 1-minute reading speed test</a>.', todos='See the reading time of all the classics',
   cta='Read {t} with Lince', ctap='Lince is a speed-reading app for Android: one word at a time, with {t} and 149 other classics included.', boton='Get it on Google Play',
   pie=('Reading speed test', 'Reading time', 'Contact')),
 'es': dict(title='¿Cuánto se tarda en leer {t}? ({a})', desc='{t} de {a} tiene unas {w} palabras. A velocidad media se lee en {tm}. Mira el tiempo a 150, 238, 300 y 400 palabras por minuto.',
   h1='¿Cuánto se tarda en leer {t}?', bajada='{t} de {a} tiene unas {w} palabras en la edición incluida en Lince. A la velocidad media de un adulto, 238 palabras por minuto, son unas <strong>{tm}</strong>.',
   h2v='Tiempo de lectura a distintas velocidades', cab=('Velocidad', 'Tiempo'), nom=('Lector lento', 'Promedio', 'Rápido', 'Muy rápido'), ppm='{v} ppm',
   nota='Los tiempos son de lectura pura, sin pausas. Con 300 palabras por página, esta edición tendría unas {pg} páginas.',
   h2p='Preguntas frecuentes', q1='¿Cuántas palabras tiene {t}?', a1='Unas {w} palabras en la edición incluida en Lince. Otras ediciones varían un poco.',
   q2='¿En cuántos días se termina {t}?', a2='Leyendo 30 minutos al día a velocidad media, en unos {d} días.',
   prueba='¿No sabes tu velocidad? <a href="{u}">Haz la prueba de velocidad de lectura de 1 minuto</a>.', todos='Mira el tiempo de lectura de todos los clásicos',
   cta='Lee {t} con Lince', ctap='Lince es una app de lectura rápida para Android: una palabra a la vez, con {t} y otros 149 clásicos incluidos.', boton='Descargar en Google Play',
   pie=('Prueba de velocidad', 'Tiempo de lectura', 'Contacto')),
 'pt': dict(title='Quanto tempo leva para ler {t}? ({a})', desc='{t}, de {a}, tem cerca de {w} palavras. Em velocidade média leva {tm}. Veja o tempo a 150, 238, 300 e 400 palavras por minuto.',
   h1='Quanto tempo leva para ler {t}?', bajada='{t}, de {a}, tem cerca de {w} palavras na edição incluída no Lince. Na velocidade média de um adulto, 238 palavras por minuto, são cerca de <strong>{tm}</strong>.',
   h2v='Tempo de leitura em diferentes velocidades', cab=('Velocidade', 'Tempo'), nom=('Leitor lento', 'Médio', 'Rápido', 'Muito rápido'), ppm='{v} ppm',
   nota='Os tempos são de leitura pura, sem pausas. Com 300 palavras por página, esta edição teria cerca de {pg} páginas.',
   h2p='Perguntas frequentes', q1='Quantas palavras tem {t}?', a1='Cerca de {w} palavras na edição incluída no Lince. Outras edições variam um pouco.',
   q2='Em quantos dias se termina {t}?', a2='Lendo 30 minutos por dia em velocidade média, em cerca de {d} dias.',
   prueba='Não sabe sua velocidade? <a href="{u}">Faça o teste de velocidade de leitura de 1 minuto</a>.', todos='Veja o tempo de leitura de todos os clássicos',
   cta='Leia {t} com o Lince', ctap='O Lince é um app de leitura dinâmica para Android: uma palavra por vez, com {t} e outros 149 clássicos incluídos.', boton='Baixar no Google Play',
   pie=('Teste de velocidade', 'Tempo de leitura', 'Contato')),
 'fr': dict(title='Combien de temps pour lire {t} ? ({a})', desc='{t}, de {a}, compte environ {w} mots. À vitesse moyenne, il se lit en {tm}. Voyez la durée à 150, 238, 300 et 400 mots par minute.',
   h1='Combien de temps pour lire {t} ?', bajada='{t}, de {a}, compte environ {w} mots dans l\'édition incluse dans Lince. À la vitesse moyenne d\'un adulte, 238 mots par minute, cela fait environ <strong>{tm}</strong>.',
   h2v='Durée de lecture selon la vitesse', cab=('Vitesse', 'Durée'), nom=('Lecteur lent', 'Moyen', 'Rapide', 'Très rapide'), ppm='{v} mots/min',
   nota='Les durées sont de la lecture pure, sans pauses. À 300 mots par page, cette édition ferait environ {pg} pages.',
   h2p='Questions fréquentes', q1='Combien de mots compte {t} ?', a1='Environ {w} mots dans l\'édition incluse dans Lince. Les autres éditions varient un peu.',
   q2='En combien de jours finit-on {t} ?', a2='En lisant 30 minutes par jour à vitesse moyenne, en environ {d} jours.',
   prueba='Vous ne connaissez pas votre vitesse ? <a href="{u}">Faites le test de vitesse de lecture d\'une minute</a>.', todos='Voir la durée de lecture de tous les classiques',
   cta='Lisez {t} avec Lince', ctap='Lince est une appli de lecture rapide pour Android : un mot à la fois, avec {t} et 149 autres classiques inclus.', boton='Disponible sur Google Play',
   pie=('Test de vitesse', 'Temps de lecture', 'Contact')),
 'de': dict(title='Wie lange dauert es, {t} zu lesen? ({a})', desc='{t} von {a} hat etwa {w} Wörter. Bei durchschnittlichem Tempo dauert es {tm}. Sieh die Zeit bei 150, 238, 300 und 400 Wörtern pro Minute.',
   h1='Wie lange dauert es, {t} zu lesen?', bajada='{t} von {a} hat etwa {w} Wörter in der Ausgabe, die in Lince enthalten ist. Beim durchschnittlichen Lesetempo eines Erwachsenen, 238 Wörter pro Minute, sind das etwa <strong>{tm}</strong>.',
   h2v='Lesezeit bei verschiedenem Tempo', cab=('Tempo', 'Zeit'), nom=('Langsamer Leser', 'Durchschnitt', 'Schnell', 'Sehr schnell'), ppm='{v} WpM',
   nota='Die Zeiten sind reine Lesezeit, ohne Pausen. Bei 300 Wörtern pro Seite hätte diese Ausgabe etwa {pg} Seiten.',
   h2p='Häufige Fragen', q1='Wie viele Wörter hat {t}?', a1='Etwa {w} Wörter in der Ausgabe, die in Lince enthalten ist. Andere Ausgaben weichen etwas ab.',
   q2='In wie vielen Tagen schafft man {t}?', a2='Bei 30 Minuten Lesen am Tag und durchschnittlichem Tempo in etwa {d} Tagen.',
   prueba='Du kennst dein Tempo nicht? <a href="{u}">Mach den Lesegeschwindigkeitstest in einer Minute</a>.', todos='Lesezeit aller Klassiker ansehen',
   cta='Lies {t} mit Lince', ctap='Lince ist eine Schnelllese-App für Android: ein Wort nach dem anderen, mit {t} und 149 weiteren Klassikern.', boton='Jetzt bei Google Play',
   pie=('Tempotest', 'Lesezeit', 'Kontakt')),
 'it': dict(title='Quanto tempo ci vuole per leggere {t}? ({a})', desc='{t} di {a} ha circa {w} parole. A velocità media si legge in {tm}. Guarda il tempo a 150, 238, 300 e 400 parole al minuto.',
   h1='Quanto tempo ci vuole per leggere {t}?', bajada='{t} di {a} ha circa {w} parole nell\'edizione inclusa in Lince. Alla velocità media di un adulto, 238 parole al minuto, sono circa <strong>{tm}</strong>.',
   h2v='Tempo di lettura a diverse velocità', cab=('Velocità', 'Tempo'), nom=('Lettore lento', 'Medio', 'Veloce', 'Molto veloce'), ppm='{v} ppm',
   nota='I tempi sono di lettura pura, senza pause. Con 300 parole per pagina, questa edizione avrebbe circa {pg} pagine.',
   h2p='Domande frequenti', q1='Quante parole ha {t}?', a1='Circa {w} parole nell\'edizione inclusa in Lince. Le altre edizioni variano un poco.',
   q2='In quanti giorni si finisce {t}?', a2='Leggendo 30 minuti al giorno a velocità media, in circa {d} giorni.',
   prueba='Non conosci la tua velocità? <a href="{u}">Fai il test di velocità di lettura di 1 minuto</a>.', todos='Guarda il tempo di lettura di tutti i classici',
   cta='Leggi {t} con Lince', ctap='Lince è un\'app di lettura veloce per Android: una parola alla volta, con {t} e altri 149 classici inclusi.', boton='Disponibile su Google Play',
   pie=('Test di velocità', 'Tempo di lettura', 'Contatti')),
}


def slug(t):
    s = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def titulo_seo(plantilla, f):
    t = plantilla.format(**f)
    return t if len(t) <= 65 else plantilla.replace(' ({a})', '').format(**f)


def desc_seo(d):
    return d if len(d) <= 160 else d.rsplit('. ', 1)[0] + '.'


MAS = dict(en='More reading times', es='Más tiempos de lectura', pt='Mais tempos de leitura', fr='Autres temps de lecture', de='Weitere Lesezeiten', it='Altri tempi di lettura')


def parecidos(b, n=5):
    # mismo idioma: primero otras obras del mismo autor, luego los siguientes de la lista (orden fijo, sin azar)
    mios = [c for c in LIBROS if c['l'] == b['l'] and c is not b]
    mismo = [c for c in mios if c['a'] == b['a']]
    sig = [c for c in LIBROS[LIBROS.index(b) + 1:] + LIBROS[:LIBROS.index(b)] if c['l'] == b['l'] and c not in mismo]
    return (mismo + sig)[:n]


total = 0
for b in LIBROS:
    l, w, titulo, autor = b['l'], b['w'], b['t'], b['a']
    x = T[l]
    ruta = f"{RUTAS['tiempo'][l]}{slug(titulo)}/"
    miles = lambda n: f'{n:,}'.replace(',', MILES[l])  # noqa: E731
    tm = tiempo(w, 238)
    f = dict(t=titulo, a=autor, w=miles(w), tm=tm, pg=miles(round(w / 300)), d=math.ceil(w / 238 / 30))
    e = lambda k: html.escape(x[k].format(**f))  # noqa: E731
    filas = ''.join(f'<tr><td>{n} ({x["ppm"].format(v=v)})</td><td class="tiempo">{tiempo(w, v)}</td></tr>' for n, v in zip(x['nom'], VEL))
    faq = {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': x[q].format(**f), 'acceptedAnswer': {'@type': 'Answer', 'text': x[a].format(**f)}} for q, a in (('q1', 'a1'), ('q2', 'a2'))]}
    cuerpo = f'''
  <article class="articulo">
    <h1>{e('h1')}</h1>
    <p class="bajada">{x['bajada'].format(**f)}</p>
    <h2>{x['h2v']}</h2>
    <table class="tabla-libros">
      <thead><tr><th scope="col">{x['cab'][0]}</th><th scope="col">{x['cab'][1]}</th></tr></thead>
      <tbody>{filas}</tbody>
    </table>
    <p>{html.escape(x['nota'].format(**f))}</p>
    <p>{x['prueba'].format(u=RUTAS['prueba'][l])}</p>
    <h2>{x['h2p']}</h2>
    <h3>{e('q1')}</h3><p>{e('a1')}</p>
    <h3>{e('q2')}</h3><p>{e('a2')}</p>
    <h2>{MAS[l]}</h2>
    <ul>{''.join(f'<li><a href="{RUTAS["tiempo"][l]}{slug(c["t"])}/">{html.escape(c["t"])}</a></li>' for c in parecidos(b))}</ul>
    <p><a href="{RUTAS['tiempo'][l]}">{x['todos']}</a></p>
  </article>'''
    ld = [LD_LIBRO(titulo, autor, ruta), faq]
    g = dict(lang=l, clave='tiempo', url=ruta, alternos='', menu='', otros='', title=titulo_seo(x['title'], f), desc=desc_seo(x['desc'].format(**f)), h1=x['h1'].format(**f),
             alt='Lince', camp=f'libro-{l}', ld=ld[0], cuerpo=cuerpo, cta=x['cta'].format(**f), ctap=x['ctap'].format(**f), boton=x['boton'],
             pie=[(RUTAS['inicio'][l], 'Lince'), (RUTAS['prueba'][l], x['pie'][0]), (RUTAS['tiempo'][l], x['pie'][1]), x['pie'][2]])
    # pagina() solo admite un objeto ld: se agrega la pregunta frecuente en una segunda etiqueta
    out = pagina(g).replace('</head>', f'<script type="application/ld+json">\n{json.dumps({"@context": "https://schema.org", **faq}, ensure_ascii=False)}\n</script>\n</head>', 1)
    d = Path(ruta.strip('/'))
    d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(out)
    total += 1
    b['ruta'] = ruta

Path('datos/rutas-libros.json').write_text(json.dumps([b['ruta'] for b in LIBROS], indent=0))
print(total, 'páginas de libros')
