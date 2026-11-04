#!/usr/bin/env python3
"""sitemap.xml con todas las páginas en los seis idiomas y sus alternativas (hreflang). Correr tras cambiar páginas."""
from idiomas import B, LANGS, RUTAS

HOY = '2026-11-03'
ORDEN = ['inicio', 'prueba', 'tiempo', 'rsvp', 'privacidad', 'borrar']

urls = []
for clave in ORDEN:
    r = RUTAS[clave]
    alt = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{B + r[l]}"/>' for l in LANGS)
    alt += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{B + r["en"]}"/>'
    for l in LANGS:
        urls.append(f'  <url><loc>{B + r[l]}</loc><lastmod>{HOY}</lastmod>{alt}</url>')
urls.append(f'  <url><loc>{B}/prensa/</loc><lastmod>2026-11-02</lastmod></url>')

open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + '\n'.join(urls) + '\n</urlset>\n')
print(len(urls), 'URL')
