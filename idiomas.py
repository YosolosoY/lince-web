"""Rutas de cada página en cada idioma (las usan generar_legales.py, generar_inicio.py y generar_guias.py).

Inglés en la raíz, español en /es/. Las páginas legales en inglés y español conservan sus URL antiguas
(la app 1.2.2 y Google Play enlazan a /privacidad/ y /borrar-cuenta/).
"""

B = 'https://lincereader.com'
LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it']
NOMBRES = {'en': 'English', 'es': 'Español', 'pt': 'Português', 'fr': 'Français', 'de': 'Deutsch', 'it': 'Italiano'}
OG_LOCALE = {'en': 'en_US', 'es': 'es_LA', 'pt': 'pt_BR', 'fr': 'fr_FR', 'de': 'de_DE', 'it': 'it_IT'}

RUTAS = {
    'inicio': {'en': '/', 'es': '/es/', 'pt': '/pt/', 'fr': '/fr/', 'de': '/de/', 'it': '/it/'},
    'privacidad': {'en': '/en/privacy/', 'es': '/privacidad/', 'pt': '/pt/privacidade/', 'fr': '/fr/confidentialite/',
                   'de': '/de/datenschutz/', 'it': '/it/privacy/'},
    'borrar': {'en': '/en/delete-account/', 'es': '/borrar-cuenta/', 'pt': '/pt/excluir-conta/',
               'fr': '/fr/supprimer-compte/', 'de': '/de/konto-loeschen/', 'it': '/it/elimina-account/'},
    'prueba': {'en': '/reading-speed-test/', 'es': '/es/prueba-velocidad-lectura/', 'pt': '/pt/teste-velocidade-leitura/',
               'fr': '/fr/test-vitesse-lecture/', 'de': '/de/lesegeschwindigkeit-test/', 'it': '/it/test-velocita-lettura/'},
    'tiempo': {'en': '/how-long-to-read/', 'es': '/es/cuanto-tarda-leer/', 'pt': '/pt/quanto-tempo-ler-livro/',
               'fr': '/fr/temps-lecture-livre/', 'de': '/de/lesezeit-buch/', 'it': '/it/quanto-tempo-leggere-libro/'},
    'rsvp': {'en': '/what-is-rsvp-reading/', 'es': '/es/que-es-rsvp/', 'pt': '/pt/o-que-e-rsvp/', 'fr': '/fr/lecture-rsvp/',
             'de': '/de/was-ist-rsvp/', 'it': '/it/lettura-rsvp/'},
}


def alternos(pagina, sangria=''):
    """Etiquetas hreflang de una página en todos los idiomas (x-default: inglés)."""
    r = RUTAS[pagina]
    lineas = [f'<link rel="alternate" hreflang="{l}" href="{B + r[l]}">' for l in LANGS]
    lineas.append(f'<link rel="alternate" hreflang="x-default" href="{B + r["en"]}">')
    return '\n'.join(sangria + l for l in lineas)


def otros_idiomas(pagina, actual, sep=' · '):
    """Enlaces a la misma página en los demás idiomas, para pies de página."""
    r = RUTAS[pagina]
    return sep.join(f'<a href="{r[l]}" hreflang="{l}" lang="{l}">{NOMBRES[l]}</a>' for l in LANGS if l != actual)


def menu_idiomas(pagina, actual):
    """Selector de idioma de la barra superior (sin JavaScript)."""
    r = RUTAS[pagina]
    enlaces = ''.join(f'<a href="{r[l]}" hreflang="{l}" lang="{l}">{NOMBRES[l]}</a>' for l in LANGS if l != actual)
    return (f'<details class="idiomas"><summary aria-label="Language">🌐 {NOMBRES[actual]}</summary>'
            f'<div>{enlaces}</div></details>')
