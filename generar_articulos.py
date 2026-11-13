#!/usr/bin/env python3
"""Artículos de blog (inglés, una sola versión) a partir de datos/articulos/*.md. Markdown mínimo: ##, párrafos, listas, tabla, **negrita**, *cursiva*, enlaces."""
import html, json, re
from pathlib import Path

from generar_guias import pagina

B = 'https://lincereader.com'
ARTICULOS = [
    dict(archivo='skimming-vs-scanning', fecha='2026-11-13', camp='articulo-skimming',
         enlaces='<p>Related: <a href="/what-is-rsvp-reading/">What is RSVP reading?</a> · <a href="/reading-speed-test/">Test your reading speed</a> · <a href="/how-long-to-read/">How long does it take to read a book?</a></p>'),
]


def en_linea(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', t)


def cuerpo_md(md):
    out, lista, tabla = [], None, []

    def cierra():
        nonlocal lista, tabla
        if lista:
            out.append(f'</{lista}>')
            lista = None
        if tabla:
            filas = [[c.strip() for c in f.strip().strip('|').split('|')] for f in tabla if not re.match(r'^\|[\s|:-]+\|$', f.strip())]
            cab = ''.join(f'<th scope="col">{en_linea(c) or "Aspect"}</th>' for c in filas[0])
            cu = ''.join('<tr>' + ''.join(f'<td>{en_linea(c)}</td>' for c in f) + '</tr>' for f in filas[1:])
            out.append(f'<table class="tabla-libros"><thead><tr>{cab}</tr></thead><tbody>{cu}</tbody></table>')
            tabla = []

    for linea in md.split('\n'):
        s = linea.rstrip()
        if s.startswith('|'):
            tabla.append(s)
            continue
        m_ul, m_ol = re.match(r'^- (.*)', s), re.match(r'^\d+\. (.*)', s)
        if m_ul or m_ol:
            tag = 'ul' if m_ul else 'ol'
            if lista != tag:
                cierra()
                out.append(f'<{tag}>')
                lista = tag
            out.append(f'<li>{en_linea((m_ul or m_ol).group(1))}</li>')
            continue
        cierra()
        if s.startswith('## '):
            out.append(f'<h2>{en_linea(s[3:])}</h2>')
        elif s.strip():
            out.append(f'<p>{en_linea(s)}</p>')
    cierra()
    return '\n    '.join(out)


for a in ARTICULOS:
    texto = Path(f"datos/articulos/{a['archivo']}.md").read_text()
    meta = dict(re.findall(r'^(titulo|meta_descripcion): (.*)$', texto.split('---')[1], re.M))
    cuerpo = texto.split('---', 2)[2].split('\n---\n')[0]  # sin la nota al editor
    cuerpo = re.sub(r'^# .*\n', '', cuerpo.strip(), count=1).strip()
    primero, resto = cuerpo.split('\n\n', 1)
    ruta = f"/{a['archivo']}/"
    g = dict(lang='en', clave='rsvp', url=ruta, alternos='', menu='', otros='', title=meta['titulo'], desc=meta['meta_descripcion'], h1=meta['titulo'],
             alt='Lince', camp=a['camp'],
             ld={'@type': 'Article', 'author': {'@type': 'Person', 'name': 'YosolosoY'}, 'publisher': {'@type': 'Organization', 'name': 'Lince'},
                 'datePublished': a['fecha'], 'dateModified': a['fecha']},
             cuerpo=f'''  <article class="articulo">
    <h1>{html.escape(meta['titulo'])}</h1>
    <p class="fecha">By YosolosoY, developer of Lince · November 13, 2026</p>
    {cuerpo_md(primero + chr(10) + chr(10) + resto)}
    {a['enlaces']}
  </article>''',
             cta='Try RSVP reading with Lince', ctap='Lince is a speed-reading app for Android: one word at a time, with an EPUB library and 150 classics included.', boton='Get it on Google Play',
             pie=[('/', 'Lince'), ('/reading-speed-test/', 'Speed test'), ('/what-is-rsvp-reading/', 'What is RSVP?'), 'Contact'])
    d = Path(a['archivo'])
    d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(pagina(g))
    print('artículo', ruta)
