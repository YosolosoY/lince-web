#!/usr/bin/env python3
"""Prueba de velocidad de lectura en portugués, francés, alemán e italiano.

Los textos y preguntas son los de la app (datos/pruebas.json, sacado de src/speedtest/tests-*.ts del repo lince).
Inglés y español (reading-speed-test, es/prueba-velocidad-lectura) se mantienen a mano.
"""
import html
import json
from pathlib import Path

from idiomas import B, OG_LOCALE, RUTAS, alternos, menu_idiomas, otros_idiomas

PLAY = 'https://play.google.com/store/apps/details?id=co.com.monsalve.lince&referrer=utm_source%3Dsitio%26utm_medium%3Dweb%26utm_campaign%3Dprueba-'
PRUEBAS = json.loads(Path('datos/pruebas.json').read_text())
BRYSBAERT = 'https://doi.org/10.1016/j.jml.2019.104047'

T = {
 'pt': dict(
  title='Teste de velocidade de leitura grátis em 1 minuto | Lince',
  desc='Descubra quantas palavras por minuto você lê: um texto curto e 3 perguntas para medir velocidade e compreensão. Grátis e sem cadastro.',
  og_title='Teste de velocidade de leitura em 1 minuto', og_desc='Quantas palavras por minuto você lê? Descubra em 1 minuto, com 3 perguntas de compreensão.',
  nombre='Teste de velocidade de leitura',
  h1='Teste de velocidade de leitura',
  bajada='Descubra quantas palavras por minuto você lê. Leva uns 2 minutos, é grátis e não precisa se cadastrar nem instalar nada.',
  instr='Leia no seu ritmo de sempre, sem pressa. O relógio começa quando você toca em "Começar" e para quando toca em "Pronto". Depois responda 3 perguntas simples.',
  empezar='Começar', nojs='Este teste precisa de JavaScript.',
  cuerpo=f'''
    <h2>Como o resultado é calculado?</h2>
    <p>Dividimos as palavras do texto pelo tempo que você levou para ler. As perguntas não mudam esse número: elas conferem
    que você leu de verdade, porque ir rápido sem entender não é ler. Nada sai desta página: tudo acontece no seu navegador.</p>
    <h2>O que é uma boa velocidade de leitura?</h2>
    <p>Uma <a href="{BRYSBAERT}" rel="noopener">revisão de 190 estudos com mais de 18 mil pessoas</a> estimou que adultos leem em
    silêncio, em inglês, cerca de 238 palavras por minuto em não ficção e 260 em ficção. Em português as palavras costumam ser
    mais longas, então o número tende a ser um pouco menor. Use como referência, não como nota: sua velocidade muda com o
    idioma, o assunto e o cansaço.</p>
    <h2>Como ler mais rápido sem perder o fio</h2>
    <ul>
      <li>Leia todos os dias, nem que sejam 10 minutos. A prática é o que mais ajuda.</li>
      <li>Deixe o celular e as notificações de lado enquanto lê.</li>
      <li>Suba a velocidade aos poucos e diminua assim que deixar de entender.</li>
      <li>Refaça o teste com outro texto de vez em quando para ver seu progresso.</li>
    </ul>
    <h2>O que é ler uma palavra por vez?</h2>
    <p>Chama-se RSVP: as palavras aparecem uma a uma, sempre no mesmo lugar, para que seus olhos não precisem percorrer a linha.
    É o que faz o Lince, um app de leitura dinâmica para Android. <a href="{{inicio}}#try">Experimente aqui mesmo</a> ou use nos
    seus próprios livros EPUB e PDF.</p>
    <p>Veja agora <a href="{{tiempo}}">quanto tempo os livros clássicos levam na sua velocidade</a>, ou descubra
    <a href="{{rsvp}}">o que é a leitura RSVP</a>.</p>''',
  cierre_h='Leve sua leitura para o Lince', cierre_p='O teste também está no app, junto com 150 clássicos incluídos e seus próprios livros.',
  play='Baixar no Google Play', pie=('Privacidade', 'Contato'),
  textos={'termine': 'Pronto', 'pregunta': 'Pergunta {n} de {t}', 'otra': 'Refazer com outro texto', 'muyRapido': 'Rápido demais',
          'muyRapidoTexto': 'Deu {ppm} palavras por minuto. Parece que você não chegou a ler o texto inteiro. Tente de novo no seu ritmo normal.',
          'unidad': 'palavras por minuto · {c} de {t} respostas certas',
          'bajaComprension': 'Sua compreensão foi baixa desta vez, então esse número pode ser maior que sua velocidade real. Tente de novo com mais calma.',
          'sugerencia': 'Para ler uma palavra por vez, sugerimos começar a {ppm} palavras por minuto.', 'descargar': 'Experimente no Lince',
          'compartir': 'Compartilhar meu resultado', 'copiado': 'Link copiado', 'textoCompartir': 'Eu leio {ppm} palavras por minuto. E você, quanto lê?'}),
 'fr': dict(
  title='Test de vitesse de lecture gratuit en 1 minute | Lince',
  desc='Combien de mots par minute lisez-vous ? Un texte court et 3 questions pour mesurer vitesse et compréhension. Gratuit, sans inscription.',
  og_title='Test de vitesse de lecture en 1 minute', og_desc='Combien de mots par minute lisez-vous ? Découvrez-le en 1 minute, avec 3 questions de compréhension.',
  nombre='Test de vitesse de lecture',
  h1='Test de vitesse de lecture',
  bajada="Découvrez combien de mots par minute vous lisez. Ça prend environ 2 minutes, c'est gratuit, sans inscription ni installation.",
  instr="Lisez à votre rythme habituel, sans vous presser. Le chrono démarre quand vous touchez « Commencer » et s'arrête quand vous touchez « Terminé ». Répondez ensuite à 3 questions simples.",
  empezar='Commencer', nojs='Ce test nécessite JavaScript.',
  cuerpo=f'''
    <h2>Comment le résultat est-il calculé ?</h2>
    <p>Nous divisons le nombre de mots du texte par le temps que vous avez mis à le lire. Les questions ne changent pas ce
    chiffre : elles vérifient que vous l'avez vraiment lu, car aller vite sans comprendre, ce n'est pas lire. Rien ne quitte
    cette page : tout se passe dans votre navigateur.</p>
    <h2>Qu'est-ce qu'une bonne vitesse de lecture ?</h2>
    <p>Une <a href="{BRYSBAERT}" rel="noopener">synthèse de 190 études portant sur plus de 18 000 personnes</a> estime que les
    adultes lisent en silence, en anglais, environ 238 mots par minute pour les textes documentaires et 260 pour la fiction.
    En français, les mots sont en moyenne plus longs, donc le chiffre est souvent un peu plus bas. Prenez-le comme repère, pas
    comme une note : votre vitesse change selon la langue, le sujet et la fatigue.</p>
    <h2>Comment lire plus vite sans perdre le fil</h2>
    <ul>
      <li>Lisez chaque jour, même 10 minutes. C'est la pratique qui aide le plus.</li>
      <li>Éloignez le téléphone et les notifications pendant la lecture.</li>
      <li>Augmentez la vitesse peu à peu et ralentissez dès que vous ne comprenez plus.</li>
      <li>Refaites le test avec un autre texte de temps en temps pour voir vos progrès.</li>
    </ul>
    <h2>Qu'est-ce que lire un mot à la fois ?</h2>
    <p>Cela s'appelle RSVP : les mots apparaissent un par un, toujours au même endroit, et vos yeux n'ont pas à parcourir la
    ligne. C'est ce que fait Lince, une appli de lecture rapide pour Android. <a href="{{inicio}}#try">Essayez-la ici</a> ou
    utilisez-la avec vos propres livres EPUB et PDF.</p>
    <p>Voyez maintenant <a href="{{tiempo}}">combien de temps prennent les grands classiques à votre vitesse</a>, ou découvrez
    <a href="{{rsvp}}">ce qu'est la lecture RSVP</a>.</p>''',
  cierre_h='Emportez votre lecture dans Lince', cierre_p="Le test est aussi dans l'appli, avec 150 classiques inclus et vos propres livres.",
  play='Disponible sur Google Play', pie=('Confidentialité', 'Contact'),
  textos={'termine': 'Terminé', 'pregunta': 'Question {n} sur {t}', 'otra': 'Recommencer avec un autre texte', 'muyRapido': 'Trop rapide',
          'muyRapidoTexto': "Cela donne {ppm} mots par minute. On dirait que vous n'avez pas lu tout le texte. Réessayez à votre rythme normal.",
          'unidad': 'mots par minute · {c} bonnes réponses sur {t}',
          'bajaComprension': 'Votre compréhension était faible cette fois, ce chiffre peut donc dépasser votre vitesse réelle. Réessayez plus calmement.',
          'sugerencia': 'Pour lire un mot à la fois, nous vous conseillons de commencer à {ppm} mots par minute.', 'descargar': 'Essayer dans Lince',
          'compartir': 'Partager mon résultat', 'copiado': 'Lien copié', 'textoCompartir': 'Je lis {ppm} mots par minute. Et vous ?'}),
 'de': dict(
  title='Lesegeschwindigkeit testen: kostenlos in 1 Minute | Lince',
  desc='Wie viele Wörter pro Minute liest du? Ein kurzer Text und 3 Fragen messen Tempo und Verständnis. Kostenlos und ohne Anmeldung.',
  og_title='Lesegeschwindigkeit testen in 1 Minute', og_desc='Wie viele Wörter pro Minute liest du? Finde es in 1 Minute heraus, mit 3 Verständnisfragen.',
  nombre='Lesegeschwindigkeitstest',
  h1='Lesegeschwindigkeit testen',
  bajada='Finde heraus, wie viele Wörter pro Minute du liest. Es dauert etwa 2 Minuten, ist kostenlos und du musst dich weder anmelden noch etwas installieren.',
  instr='Lies in deinem gewohnten Tempo, ohne dich zu beeilen. Die Uhr startet, wenn du auf „Starten“ tippst, und stoppt bei „Fertig“. Danach beantwortest du 3 einfache Fragen.',
  empezar='Starten', nojs='Dieser Test braucht JavaScript.',
  cuerpo=f'''
    <h2>Wie wird das Ergebnis berechnet?</h2>
    <p>Wir teilen die Wörter des Textes durch die Zeit, die du zum Lesen gebraucht hast. Die Fragen ändern diese Zahl nicht:
    Sie prüfen, ob du wirklich gelesen hast, denn schnell sein ohne zu verstehen ist kein Lesen. Nichts verlässt diese Seite:
    Alles passiert in deinem Browser.</p>
    <h2>Was ist eine gute Lesegeschwindigkeit?</h2>
    <p>Eine <a href="{BRYSBAERT}" rel="noopener">Übersicht über 190 Studien mit mehr als 18.000 Personen</a> schätzt, dass
    Erwachsene auf Englisch still etwa 238 Wörter pro Minute bei Sachtexten und 260 bei Belletristik lesen. Deutsche Wörter sind
    im Schnitt länger, deshalb liegt die Zahl meist etwas niedriger. Nimm sie als Anhaltspunkt, nicht als Note: Dein Tempo
    hängt von Sprache, Thema und Müdigkeit ab.</p>
    <h2>Schneller lesen, ohne den Faden zu verlieren</h2>
    <ul>
      <li>Lies jeden Tag, auch wenn es nur 10 Minuten sind. Übung hilft am meisten.</li>
      <li>Leg Handy und Benachrichtigungen beim Lesen weg.</li>
      <li>Steigere das Tempo nach und nach und werde langsamer, sobald du nicht mehr verstehst.</li>
      <li>Mach den Test ab und zu mit einem anderen Text, um deinen Fortschritt zu sehen.</li>
    </ul>
    <h2>Was heißt, ein Wort nach dem anderen zu lesen?</h2>
    <p>Das nennt man RSVP: Die Wörter erscheinen nacheinander, immer an derselben Stelle, sodass deine Augen nicht die Zeile
    entlangwandern müssen. Genau das macht Lince, eine Schnelllese-App für Android. <a href="{{inicio}}#try">Probier es hier
    aus</a> oder nutze sie mit deinen eigenen EPUB- und PDF-Büchern.</p>
    <p>Sieh dir jetzt an, <a href="{{tiempo}}">wie lange Klassiker bei deinem Tempo dauern</a>, oder erfahre,
    <a href="{{rsvp}}">was RSVP-Lesen ist</a>.</p>''',
  cierre_h='Nimm dein Lesen mit zu Lince', cierre_p='Den Test gibt es auch in der App, dazu 150 enthaltene Klassiker und deine eigenen Bücher.',
  play='Jetzt bei Google Play', pie=('Datenschutz', 'Kontakt'),
  textos={'termine': 'Fertig', 'pregunta': 'Frage {n} von {t}', 'otra': 'Mit anderem Text wiederholen', 'muyRapido': 'Zu schnell',
          'muyRapidoTexto': 'Das ergibt {ppm} Wörter pro Minute. Es sieht so aus, als hättest du nicht den ganzen Text gelesen. Versuch es noch einmal in deinem normalen Tempo.',
          'unidad': 'Wörter pro Minute · {c} von {t} Antworten richtig',
          'bajaComprension': 'Dein Verständnis war diesmal niedrig, die Zahl kann also über deinem echten Tempo liegen. Versuch es noch einmal in Ruhe.',
          'sugerencia': 'Zum Lesen Wort für Wort empfehlen wir dir, mit {ppm} Wörtern pro Minute anzufangen.', 'descargar': 'In Lince ausprobieren',
          'compartir': 'Mein Ergebnis teilen', 'copiado': 'Link kopiert', 'textoCompartir': 'Ich lese {ppm} Wörter pro Minute. Wie schnell liest du?'}),
 'it': dict(
  title='Test di velocità di lettura gratis in 1 minuto | Lince',
  desc='Quante parole al minuto leggi? Un testo breve e 3 domande per misurare velocità e comprensione. Gratis e senza registrazione.',
  og_title='Test di velocità di lettura in 1 minuto', og_desc='Quante parole al minuto leggi? Scoprilo in 1 minuto, con 3 domande di comprensione.',
  nombre='Test di velocità di lettura',
  h1='Test di velocità di lettura',
  bajada='Scopri quante parole al minuto leggi. Ci vogliono circa 2 minuti, è gratis e non devi registrarti né installare nulla.',
  instr='Leggi al tuo ritmo abituale, senza fretta. Il cronometro parte quando tocchi "Inizia" e si ferma quando tocchi "Fatto". Poi rispondi a 3 domande semplici.',
  empezar='Inizia', nojs='Questo test richiede JavaScript.',
  cuerpo=f'''
    <h2>Come si calcola il risultato?</h2>
    <p>Dividiamo le parole del testo per il tempo che hai impiegato a leggerlo. Le domande non cambiano quel numero: verificano
    che tu abbia letto davvero, perché andare veloce senza capire non è leggere. Niente esce da questa pagina: succede tutto
    nel tuo browser.</p>
    <h2>Qual è una buona velocità di lettura?</h2>
    <p>Una <a href="{BRYSBAERT}" rel="noopener">rassegna di 190 studi con più di 18.000 persone</a> ha stimato che gli adulti
    leggono in silenzio, in inglese, circa 238 parole al minuto nei testi di saggistica e 260 nella narrativa. In italiano le
    parole sono in media più lunghe, quindi il numero tende a essere un po' più basso. Usalo come riferimento, non come voto:
    la tua velocità cambia con la lingua, l'argomento e la stanchezza.</p>
    <h2>Come leggere più veloce senza perdere il filo</h2>
    <ul>
      <li>Leggi ogni giorno, anche solo 10 minuti. È la pratica che aiuta di più.</li>
      <li>Metti da parte il telefono e le notifiche mentre leggi.</li>
      <li>Aumenta la velocità poco a poco e rallenta appena smetti di capire.</li>
      <li>Ripeti il test con un altro testo ogni tanto per vedere i progressi.</li>
    </ul>
    <h2>Cosa vuol dire leggere una parola alla volta?</h2>
    <p>Si chiama RSVP: le parole compaiono una alla volta, sempre nello stesso punto, così gli occhi non devono percorrere la
    riga. È quello che fa Lince, un'app di lettura veloce per Android. <a href="{{inicio}}#try">Provala qui</a> o usala con i
    tuoi libri EPUB e PDF.</p>
    <p>Ora guarda <a href="{{tiempo}}">quanto tempo richiedono i grandi classici alla tua velocità</a>, oppure scopri
    <a href="{{rsvp}}">cos'è la lettura RSVP</a>.</p>''',
  cierre_h='Porta la tua lettura su Lince', cierre_p="Il test c'è anche nell'app, insieme a 150 classici inclusi e ai tuoi libri.",
  play='Disponibile su Google Play', pie=('Privacy', 'Contatti'),
  textos={'termine': 'Fatto', 'pregunta': 'Domanda {n} di {t}', 'otra': 'Ripeti con un altro testo', 'muyRapido': 'Troppo veloce',
          'muyRapidoTexto': 'Risultano {ppm} parole al minuto. Sembra che tu non abbia letto tutto il testo. Riprova al tuo ritmo normale.',
          'unidad': 'parole al minuto · {c} risposte giuste su {t}',
          'bajaComprension': 'Questa volta la comprensione è stata bassa, quindi il numero può essere più alto della tua velocità reale. Riprova con più calma.',
          'sugerencia': 'Per leggere una parola alla volta, ti consigliamo di iniziare a {ppm} parole al minuto.', 'descargar': 'Provalo in Lince',
          'compartir': 'Condividi il mio risultato', 'copiado': 'Link copiato', 'textoCompartir': 'Leggo {ppm} parole al minuto. E tu?'}),
}

ICONO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 2.6v18.8c0 .5.5.8 1 .6l15.6-9.4c.4-.3.4-.9 0-1.2L5 2c-.5-.2-1 .1-1 .6z"/></svg>'


def pagina(lang):
    t = T[lang]
    url = RUTAS['prueba'][lang]
    e = lambda s: html.escape(s, quote=True)
    ld = {'@context': 'https://schema.org', '@type': 'WebApplication', 'name': t['nombre'], 'url': B + url,
          'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Any', 'inLanguage': lang, 'description': t['desc'],
          'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}
    datos = {'textos': t['textos'], 'pruebas': PRUEBAS[lang], 'play': PLAY + f'{lang}-resultado'}
    cuerpo = t['cuerpo'].replace('{inicio}', RUTAS['inicio'][lang]).replace('{tiempo}', RUTAS['tiempo'][lang]).replace('{rsvp}', RUTAS['rsvp'][lang])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{B + url}">
{alternos('prueba')}
<link rel="icon" href="/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/icono-180.png">
<meta name="theme-color" content="#FDF6E3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#151515" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lince">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:title" content="{e(t['og_title'])}">
<meta property="og:description" content="{e(t['og_desc'])}">
<meta property="og:url" content="{B + url}">
<meta property="og:image" content="https://lincereader.com/prensa/img/grafico-{lang}.png">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta property="og:image:alt" content="Lince">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/estilo.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
<main class="sitio">
  <header class="barra">
    <a href="{RUTAS['inicio'][lang]}" class="logo">L<span>i</span>nce</a>
    <nav>
      <a href="{RUTAS['inicio'][lang]}" class="secundario">Lince</a>
      {menu_idiomas('prueba', lang)}
    </nav>
  </header>

  <div class="articulo">
    <h1>{t['h1']}</h1>
    <p class="bajada">{t['bajada']}</p>
  </div>

  <div class="prueba articulo" data-prueba>
    <p>{t['instr']}</p>
    <button type="button" class="boton">{t['empezar']}</button>
    <noscript><p class="nota">{t['nojs']}</p></noscript>
  </div>

  <div class="articulo">{cuerpo}
  </div>

  <section class="cierre">
    <h2>{t['cierre_h']}</h2>
    <p class="intro" style="margin: 0 auto 24px;">{t['cierre_p']}</p>
    <div class="botones">
      <a class="boton" href="{PLAY + lang}">
        {ICONO}
        {t['play']}
      </a>
    </div>
  </section>

  <footer class="pie">
    <span>© 2026 Lince</span>
    <nav>
      <a href="{RUTAS['inicio'][lang]}">Lince</a>
      <a href="{RUTAS['privacidad'][lang]}">{t['pie'][0]}</a>
      <a href="mailto:lince.revision@gmail.com">{t['pie'][1]}</a>
    </nav>
    <nav class="pie-idiomas">{otros_idiomas('prueba', lang, ' ')}</nav>
  </footer>
</main>
<script type="application/json" id="prueba-datos">{json.dumps(datos, ensure_ascii=False).replace('</', '<\\/')}</script>
<script src="/velocidad.js"></script>
<script src="/idioma.js" defer></script>
<script src="/analitica.js" defer></script>
</body>
</html>
'''


def main():
    for lang in T:
        out = Path(RUTAS['prueba'][lang].strip('/')) / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pagina(lang))
        print('ok', out)


if __name__ == '__main__':
    main()
