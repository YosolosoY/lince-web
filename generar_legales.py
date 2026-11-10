#!/usr/bin/env python3
"""Política de privacidad y "Borrar mi cuenta" en portugués, francés, alemán e italiano.

Las versiones en inglés y español se mantienen a mano (en/privacy, privacidad, en/delete-account, borrar-cuenta):
si cambian, cambiar también estos textos y la fecha.
"""
from pathlib import Path

from idiomas import B, RUTAS, alternos, otros_idiomas

MAIL = 'lince.revision@gmail.com'


def pagina(lang, clave, title, desc, cuerpo, pie):
    url = RUTAS[clave][lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Lince</title>
<link rel="canonical" href="{B + url}">
{alternos(clave)}
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="stylesheet" href="/estilo.css">
</head>
<body>
<main>
  <header><a href="{RUTAS['inicio'][lang]}" class="logo">L<span>i</span>nce</a></header>
{cuerpo}
  <footer>
    <a href="{RUTAS['inicio'][lang]}">{pie[0]}</a> · <a href="{RUTAS[pie[1]][lang]}">{pie[2]}</a><br>
    {otros_idiomas(clave, lang)}
  </footer>
</main>
</body>
</html>
'''


PRIVACIDAD = {
 'pt': dict(title='Política de privacidade', desc='A política de privacidade do Lince: que dados são guardados, para que servem e como pedir que sejam apagados a qualquer momento.',
  pie=('Início', 'borrar', 'Excluir minha conta'), cuerpo=f'''
  <h1>Política de privacidade</h1>
  <p class="fecha">Última atualização: 3 de novembro de 2026</p>

  <div class="caja">
    <strong>Em resumo:</strong> o que você lê no Lince fica no seu celular. Não mostramos anúncios nem vendemos dados.
    Contamos dados de uso anônimos, nunca o que você lê, e você pode desativá-los em Configurações. Se você decidir
    entrar com o Google, guardamos apenas seu e-mail, seu nome e quantos arquivos você importou, para que os limites do
    plano grátis funcionem com a sua conta.
  </div>

  <h2>Quem é o responsável</h2>
  <p>O Lince é um app feito no Chile por um desenvolvedor independente. Para qualquer dúvida sobre privacidade, escreva
  para <a href="mailto:{MAIL}">{MAIL}</a>.</p>

  <h2>O que fica guardado só no seu celular</h2>
  <p>Tudo isto fica no seu aparelho e nunca é enviado a nenhum servidor:</p>
  <ul>
    <li>Os textos e livros que você cola ou importa (.txt, .epub, .pdf) e os livros da Biblioteca clássica que você escolhe.</li>
    <li>Seu progresso em cada texto, suas sessões de leitura, sequência, pontos (XP), conquistas e recordes.</li>
    <li>Suas respostas a "Quanto você entendeu?" e os resultados do teste de velocidade.</li>
    <li>Suas configurações: idioma, tema, cores, fonte, velocidade, meta diária e horário do lembrete.</li>
    <li>Os endereços e, se você os informar, o usuário e a senha das bibliotecas OPDS que você adicionar.</li>
  </ul>
  <p>Se você desinstalar o app, tudo isso é apagado do seu celular.</p>

  <h2>Quando o app se conecta à internet</h2>
  <p>Você não precisa de internet para ler. O app se conecta nestes casos:</p>
  <ul>
    <li><strong>Você compartilha um link com o Lince:</strong> seu celular baixa essa página diretamente do site para
    extrair o texto do artigo. O site vê isso como qualquer visita de um navegador. O link e o texto não passam pelos
    nossos servidores.</li>
    <li><strong>Você usa uma biblioteca online (OPDS):</strong> seu celular se conecta diretamente ao endereço que você
    informou, com o usuário e a senha que você adicionou, se houver. Se o endereço começar com <code>http://</code> (e não
    <code>https://</code>), a conexão não é criptografada e alguém na mesma rede poderia ver o que é enviado; use
    <code>https://</code> sempre que sua biblioteca permitir.</li>
    <li><strong>Você entra na sua conta ou compra o Lince Plus:</strong> explicado abaixo.</li>
    <li><strong>Você abre o app:</strong> ele verifica se há atualização, consulta a RevenueCat sobre o seu Lince Plus e,
    se você não desativou, envia dados de uso anônimos.</li>
  </ul>

  <h2>Área de transferência</h2>
  <p>O Lince lê o que você copiou só quando você toca em "Colar". Ele não olha sua área de transferência em segundo plano
  nem guarda o que há nela, exceto o texto que você escolhe adicionar à sua biblioteca.</p>

  <h2>Se você entrar com o Google (opcional)</h2>
  <p>Você pode usar o Lince sem conta. Só pedimos que você entre com o Google a partir da sua segunda importação de
  arquivo. Você também pode entrar depois de comprar o Lince Plus, para que ele te acompanhe se trocar de celular. Se
  você entrar, guardamos:</p>
  <ul>
    <li>Seu e-mail, seu nome e o identificador da sua conta Google.</li>
    <li>Um registro das suas importações: a data e o número de palavras de cada arquivo importado (não o conteúdo nem o
    nome do arquivo), para aplicar o limite de importações grátis.</li>
  </ul>
  <p>Esses dados ficam na <a href="https://supabase.com/privacy">Supabase</a>, nosso provedor de contas, em servidores
  em São Paulo, Brasil. Eles servem apenas para o funcionamento do app; nunca são vendidos nem compartilhados para
  publicidade.</p>

  <h2>Compras</h2>
  <p>As compras do Lince Plus são processadas pelo Google Play. Nunca vemos nem guardamos os dados do seu cartão. Para
  saber se você tem o Plus usamos a <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, que recebe do Google Play
  as informações da compra (produto, data e estado da assinatura) ligadas a um identificador anônimo da sua conta do
  Lince.</p>

  <h2>Dados de uso anônimos</h2>
  <p>Para saber o que funciona e o que falha, o app envia à <a href="https://posthog.com/privacy">PostHog</a>, em servidores
  nos Estados Unidos, alguns eventos com um identificador aleatório não ligado à sua conta: abrir e fechar o app,
  terminar as boas-vindas, terminar o teste de velocidade, abrir um livro, ler 5 minutos, voltar no dia seguinte,
  chegar a um limite do plano grátis, ver ou comprar o Lince Plus, compartilhar seu resumo semanal e erros do app. Nunca
  incluem títulos, textos, seu nome ou seu e-mail. Você pode desativá-los em Configurações → Compartilhar dados de uso
  anônimos.</p>

  <h2>Este site</h2>
  <p>Este site conta visitas com a <a href="https://posthog.com/privacy">PostHog</a>, em servidores nos Estados Unidos, sem
  cookies. Ele envia a página que você vê, o site de onde você veio, o idioma do navegador, seu país aproximado, um
  identificador aleatório que termina com a sessão do navegador e ações como começar o teste de velocidade ou usar a
  calculadora. Não envia o resultado do teste, suas respostas nem o que você digita, e não guarda seu endereço IP.
  Respeita o "Do Not Track" e não funciona nesta página nem na de exclusão de conta.</p>

  <h2>O que não fazemos</h2>
  <ul>
    <li>Não mostramos anúncios.</li>
    <li>Não usamos o ID de publicidade nem seguimos você por outros apps ou sites.</li>
    <li>Não acessamos sua localização, contatos, fotos, microfone ou câmera.</li>
    <li>Não enviamos os textos que você lê.</li>
  </ul>

  <h2>Notificações</h2>
  <p>Se você ativar o lembrete diário, quem o agenda é o seu próprio celular. Ele não passa por nenhum servidor.</p>

  <h2>Como apagar seus dados</h2>
  <ul>
    <li><strong>Dados no seu celular:</strong> apague um texto mantendo-o pressionado na sua biblioteca, ou desinstale o
    app para apagar tudo.</li>
    <li><strong>Sua conta:</strong> no app, vá em Configurações → Conta → Apagar minha conta. Sua conta e seu registro de
    importações são apagados na hora. Você também pode pedir por e-mail; veja
    <a href="{RUTAS['borrar']['pt']}">como excluir sua conta</a>.</li>
  </ul>

  <h2>Crianças</h2>
  <p>O Lince não é voltado para menores de 13 anos e não coletamos conscientemente dados de crianças dessa idade. Se você
  acredita que uma criança criou uma conta, escreva para nós e a apagaremos.</p>

  <h2>Mudanças nesta política</h2>
  <p>Se mudarmos esta política, atualizaremos a data acima. Se a mudança for importante, também avisaremos no app.</p>
'''),
 'fr': dict(title='Politique de confidentialité', desc='La politique de confidentialité de Lince : quelles données sont conservées, à quoi elles servent et comment demander leur suppression à tout moment.',
  pie=('Accueil', 'borrar', 'Supprimer mon compte'), cuerpo=f'''
  <h1>Politique de confidentialité</h1>
  <p class="fecha">Dernière mise à jour : 3 novembre 2026</p>

  <div class="caja">
    <strong>En bref :</strong> ce que vous lisez dans Lince reste sur votre téléphone. Nous n'affichons pas de publicité
    et ne vendons aucune donnée. Nous comptons des données d'utilisation anonymes, jamais ce que vous lisez, et vous pouvez
    les désactiver dans les Réglages. Si vous choisissez de vous connecter avec Google, nous conservons seulement votre
    e-mail, votre nom et le nombre de fichiers importés, pour que les limites de la version gratuite suivent votre compte.
  </div>

  <h2>Responsable</h2>
  <p>Lince est une appli créée au Chili par un développeur indépendant. Pour toute question sur la confidentialité,
  écrivez à <a href="mailto:{MAIL}">{MAIL}</a>.</p>

  <h2>Ce qui reste uniquement sur votre téléphone</h2>
  <p>Tout ceci reste sur votre appareil et n'est jamais envoyé à un serveur :</p>
  <ul>
    <li>Les textes et livres que vous collez ou importez (.txt, .epub, .pdf) et les livres de la Bibliothèque classique que vous choisissez.</li>
    <li>Votre progression dans chaque texte, vos sessions de lecture, votre série, vos points (XP), badges et records.</li>
    <li>Vos réponses à « Combien as-tu compris ? » et les résultats du test de vitesse.</li>
    <li>Vos réglages : langue, thème, couleurs, police, vitesse, objectif quotidien et heure du rappel.</li>
    <li>Les adresses et, si vous les saisissez, l'identifiant et le mot de passe des bibliothèques OPDS que vous ajoutez.</li>
  </ul>
  <p>Si vous désinstallez l'appli, tout cela est supprimé de votre téléphone.</p>

  <h2>Quand l'appli se connecte à internet</h2>
  <p>Vous n'avez pas besoin d'internet pour lire. L'appli se connecte dans ces cas :</p>
  <ul>
    <li><strong>Vous partagez un lien avec Lince :</strong> votre téléphone télécharge cette page directement depuis le
    site pour en extraire le texte de l'article. Le site le voit comme n'importe quelle visite depuis un navigateur. Le
    lien et le texte ne passent pas par nos serveurs.</li>
    <li><strong>Vous utilisez une bibliothèque en ligne (OPDS) :</strong> votre téléphone se connecte directement à
    l'adresse saisie, avec l'identifiant et le mot de passe ajoutés, le cas échéant. Si l'adresse commence par
    <code>http://</code> (et non <code>https://</code>), la connexion n'est pas chiffrée et quelqu'un sur le même réseau
    pourrait voir ce qui est envoyé ; utilisez <code>https://</code> dès que votre bibliothèque le permet.</li>
    <li><strong>Vous vous connectez ou achetez Lince Plus :</strong> expliqué plus bas.</li>
    <li><strong>Vous ouvrez l'appli :</strong> elle vérifie s'il y a une mise à jour, demande à RevenueCat l'état de votre
    Lince Plus et, sauf si vous l'avez désactivé, envoie des données d'utilisation anonymes.</li>
  </ul>

  <h2>Presse-papiers</h2>
  <p>Lince lit ce que vous avez copié uniquement quand vous touchez « Coller ». Il ne consulte pas votre presse-papiers en
  arrière-plan et n'en garde rien, sauf le texte que vous choisissez d'ajouter à votre bibliothèque.</p>

  <h2>Si vous vous connectez avec Google (facultatif)</h2>
  <p>Vous pouvez utiliser Lince sans compte. Nous vous demandons de vous connecter avec Google seulement à partir de votre
  deuxième import de fichier. Vous pouvez aussi vous connecter après avoir acheté Lince Plus, pour le retrouver si vous
  changez de téléphone. Si vous vous connectez, nous conservons :</p>
  <ul>
    <li>Votre adresse e-mail, votre nom et l'identifiant de votre compte Google.</li>
    <li>Un registre de vos imports : la date et le nombre de mots de chaque fichier importé (ni son contenu ni son nom),
    pour appliquer la limite d'imports gratuits.</li>
  </ul>
  <p>Ces données sont hébergées chez <a href="https://supabase.com/privacy">Supabase</a>, notre fournisseur de comptes, sur
  des serveurs situés à São Paulo, au Brésil. Elles servent uniquement au fonctionnement de l'appli ; elles ne sont jamais
  vendues ni partagées à des fins publicitaires.</p>

  <h2>Achats</h2>
  <p>Les achats de Lince Plus sont traités par Google Play. Nous ne voyons ni ne conservons jamais les données de votre
  carte. Pour savoir si vous avez Plus, nous utilisons <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, qui
  reçoit de Google Play les informations d'achat (produit, date et état de l'abonnement) liées à un identifiant anonyme de
  votre compte Lince.</p>

  <h2>Données d'utilisation anonymes</h2>
  <p>Pour savoir ce qui marche et ce qui casse, l'appli envoie à <a href="https://posthog.com/privacy">PostHog</a>, sur des
  serveurs aux États-Unis, quelques événements avec un identifiant aléatoire non lié à votre compte : ouverture et
  fermeture de l'appli, fin de l'accueil, fin du test de vitesse, ouverture d'un livre, 5 minutes de lecture, retour le
  lendemain, atteinte d'une limite de la version gratuite, consultation ou achat de Lince Plus, partage du résumé
  hebdomadaire et erreurs de l'appli. Ils ne contiennent jamais de titres, de textes, votre nom ou votre e-mail. Vous
  pouvez les désactiver dans Réglages → Partager des données d'utilisation anonymes.</p>

  <h2>Ce site</h2>
  <p>Ce site compte les visites avec <a href="https://posthog.com/privacy">PostHog</a>, sur des serveurs aux États-Unis,
  sans cookies. Il envoie la page consultée, le site d'où vous venez, la langue du navigateur, votre pays approximatif, un
  identifiant aléatoire qui expire avec la session du navigateur et des actions comme commencer le test de vitesse ou
  utiliser le calculateur. Il n'envoie ni le résultat du test, ni vos réponses, ni ce que vous tapez, et ne conserve pas
  votre adresse IP. Il respecte « Do Not Track » et ne fonctionne pas sur cette page ni sur celle de suppression du
  compte.</p>

  <h2>Ce que nous ne faisons pas</h2>
  <ul>
    <li>Nous n'affichons pas de publicité.</li>
    <li>Nous n'utilisons pas l'identifiant publicitaire et ne vous suivons pas dans d'autres applis ou sites.</li>
    <li>Nous n'accédons pas à votre position, vos contacts, vos photos, votre micro ou votre appareil photo.</li>
    <li>Nous n'envoyons pas les textes que vous lisez.</li>
  </ul>

  <h2>Notifications</h2>
  <p>Si vous activez le rappel quotidien, c'est votre téléphone qui le programme. Il ne passe par aucun serveur.</p>

  <h2>Comment supprimer vos données</h2>
  <ul>
    <li><strong>Données sur votre téléphone :</strong> supprimez un texte par un appui long dans votre bibliothèque, ou
    désinstallez l'appli pour tout supprimer.</li>
    <li><strong>Votre compte :</strong> dans l'appli, allez dans Réglages → Compte → Supprimer mon compte. Votre compte et
    votre registre d'imports sont supprimés immédiatement. Vous pouvez aussi le demander par e-mail ; voir
    <a href="{RUTAS['borrar']['fr']}">comment supprimer votre compte</a>.</li>
  </ul>
  <p>Selon le RGPD, vous pouvez aussi demander l'accès à vos données ou leur rectification en écrivant à l'adresse
  ci-dessus, et introduire une réclamation auprès de l'autorité de protection des données de votre pays.</p>

  <h2>Enfants</h2>
  <p>Lince ne s'adresse pas aux enfants de moins de 13 ans et nous ne collectons pas sciemment de données d'enfants de cet
  âge. Si vous pensez qu'un enfant a créé un compte, écrivez-nous et nous le supprimerons.</p>

  <h2>Modifications de cette politique</h2>
  <p>Si nous modifions cette politique, nous mettrons à jour la date ci-dessus. Si le changement est important, nous
  l'annoncerons aussi dans l'appli.</p>
'''),
 'de': dict(title='Datenschutzerklärung', desc='Die Datenschutzerklärung von Lince: welche Daten gespeichert werden, wofür sie dienen und wie du jederzeit ihre Löschung verlangen kannst.',
  pie=('Startseite', 'borrar', 'Mein Konto löschen'), cuerpo=f'''
  <h1>Datenschutzerklärung</h1>
  <p class="fecha">Zuletzt aktualisiert: 3. November 2026</p>

  <div class="caja">
    <strong>Kurz gesagt:</strong> Was du in Lince liest, bleibt auf deinem Handy. Wir zeigen keine Werbung und verkaufen
    keine Daten. Wir zählen anonyme Nutzungsdaten, nie, was du liest, und du kannst sie in den Einstellungen ausschalten.
    Wenn du dich mit Google anmeldest, speichern wir nur deine E-Mail-Adresse, deinen Namen und wie viele Dateien du
    importiert hast, damit die Grenzen der Gratisversion mit deinem Konto funktionieren.
  </div>

  <h2>Verantwortlicher</h2>
  <p>Lince ist eine App, die in Chile von einem unabhängigen Entwickler gemacht wird. Für Fragen zum Datenschutz schreib an
  <a href="mailto:{MAIL}">{MAIL}</a>.</p>

  <h2>Was nur auf deinem Handy gespeichert wird</h2>
  <p>All das bleibt auf deinem Gerät und wird nie an einen Server geschickt:</p>
  <ul>
    <li>Die Texte und Bücher, die du einfügst oder importierst (.txt, .epub, .pdf), und die Bücher, die du aus der Klassiker-Bibliothek auswählst.</li>
    <li>Dein Fortschritt in jedem Text, deine Lesesitzungen, deine Serie, Punkte (XP), Abzeichen und Rekorde.</li>
    <li>Deine Antworten auf „Wie viel hast du verstanden?“ und die Ergebnisse des Tempotests.</li>
    <li>Deine Einstellungen: Sprache, Design, Farben, Schrift, Tempo, Tagesziel und Uhrzeit der Erinnerung.</li>
    <li>Die Adressen und, falls du sie eingibst, Benutzername und Passwort der OPDS-Bibliotheken, die du hinzufügst.</li>
  </ul>
  <p>Wenn du die App deinstallierst, wird all das von deinem Handy gelöscht.</p>

  <h2>Wann die App sich mit dem Internet verbindet</h2>
  <p>Zum Lesen brauchst du kein Internet. Die App verbindet sich in diesen Fällen:</p>
  <ul>
    <li><strong>Du teilst einen Link mit Lince:</strong> Dein Handy lädt diese Seite direkt von der Website, um den Text des
    Artikels herauszuholen. Die Website sieht das wie jeden Besuch mit einem Browser. Link und Text laufen nicht über unsere
    Server.</li>
    <li><strong>Du nutzt eine Online-Bibliothek (OPDS):</strong> Dein Handy verbindet sich direkt mit der eingegebenen
    Adresse, mit Benutzername und Passwort, falls du welche angegeben hast. Beginnt die Adresse mit <code>http://</code>
    (statt <code>https://</code>), ist die Verbindung nicht verschlüsselt und jemand im selben Netz könnte mitlesen; nutze
    <code>https://</code>, wann immer deine Bibliothek das unterstützt.</li>
    <li><strong>Du meldest dich an oder kaufst Lince Plus:</strong> siehe unten.</li>
    <li><strong>Du öffnest die App:</strong> Sie prüft, ob es ein Update gibt, fragt bei RevenueCat den Stand deines Lince
    Plus ab und schickt, wenn du es nicht ausgeschaltet hast, anonyme Nutzungsdaten.</li>
  </ul>

  <h2>Zwischenablage</h2>
  <p>Lince liest, was du kopiert hast, nur wenn du auf „Einfügen“ tippst. Die App schaut nicht im Hintergrund in deine
  Zwischenablage und speichert nichts daraus, außer dem Text, den du deiner Bibliothek hinzufügst.</p>

  <h2>Wenn du dich mit Google anmeldest (optional)</h2>
  <p>Du kannst Lince ohne Konto nutzen. Erst ab deinem zweiten Dateiimport bitten wir dich, dich mit Google anzumelden. Du
  kannst dich auch nach dem Kauf von Lince Plus anmelden, damit es dich beim Handywechsel begleitet. Wenn du dich anmeldest,
  speichern wir:</p>
  <ul>
    <li>Deine E-Mail-Adresse, deinen Namen und die Kennung deines Google-Kontos.</li>
    <li>Ein Protokoll deiner Importe: Datum und Wortzahl jeder importierten Datei (nicht ihr Inhalt oder Dateiname), um
    die Grenze der kostenlosen Importe anzuwenden.</li>
  </ul>
  <p>Diese Daten liegen bei <a href="https://supabase.com/privacy">Supabase</a>, unserem Kontoanbieter, auf Servern in São
  Paulo, Brasilien. Sie dienen nur dem Betrieb der App und werden nie verkauft oder für Werbung weitergegeben.</p>

  <h2>Käufe</h2>
  <p>Käufe von Lince Plus werden von Google Play abgewickelt. Wir sehen und speichern nie deine Kartendaten. Um zu wissen,
  ob du Plus hast, nutzen wir <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, das von Google Play die
  Kaufinformationen (Produkt, Datum und Abo-Status) erhält, verknüpft mit einer anonymen Kennung deines Lince-Kontos.</p>

  <h2>Anonyme Nutzungsdaten</h2>
  <p>Um zu sehen, was funktioniert und was nicht, schickt die App an <a href="https://posthog.com/privacy">PostHog</a>, auf
  Servern in den USA, einige Ereignisse mit einer zufälligen Kennung, die nicht mit deinem Konto verknüpft ist: App öffnen
  und schließen, Einführung beenden, Tempotest beenden, ein Buch öffnen, 5 Minuten lesen, am nächsten Tag wiederkommen, eine
  Grenze der Gratisversion erreichen, Lince Plus ansehen oder kaufen, die Wochenübersicht teilen und App-Fehler. Sie
  enthalten nie Titel, Texte, deinen Namen oder deine E-Mail-Adresse. Du kannst sie unter Einstellungen → Anonyme
  Nutzungsdaten teilen ausschalten.</p>

  <h2>Diese Website</h2>
  <p>Diese Website zählt Besuche mit <a href="https://posthog.com/privacy">PostHog</a>, auf Servern in den USA, ohne
  Cookies. Sie sendet die angesehene Seite, die Seite, von der du kommst, die Sprache des Browsers, dein ungefähres Land,
  eine zufällige Kennung, die mit der Browsersitzung endet, und Aktionen wie das Starten des Tempotests oder die Nutzung des
  Rechners. Sie sendet weder dein Testergebnis noch deine Antworten oder Eingaben und speichert deine IP-Adresse nicht. Sie
  respektiert „Do Not Track“ und läuft weder auf dieser Seite noch auf der Seite zum Löschen des Kontos.</p>

  <h2>Was wir nicht tun</h2>
  <ul>
    <li>Wir zeigen keine Werbung.</li>
    <li>Wir nutzen nicht die Werbe-ID und verfolgen dich nicht in anderen Apps oder auf anderen Websites.</li>
    <li>Wir greifen nicht auf deinen Standort, deine Kontakte, Fotos, dein Mikrofon oder deine Kamera zu.</li>
    <li>Wir laden die Texte, die du liest, nicht hoch.</li>
  </ul>

  <h2>Benachrichtigungen</h2>
  <p>Wenn du die tägliche Erinnerung einschaltest, plant dein Handy sie selbst. Sie läuft über keinen Server.</p>

  <h2>So löschst du deine Daten</h2>
  <ul>
    <li><strong>Daten auf deinem Handy:</strong> Lösche einen Text, indem du ihn in deiner Bibliothek gedrückt hältst, oder
    deinstalliere die App, um alles zu löschen.</li>
    <li><strong>Dein Konto:</strong> In der App unter Einstellungen → Konto → Mein Konto löschen. Dein Konto und dein
    Import-Protokoll werden sofort gelöscht. Du kannst es auch per E-Mail verlangen; siehe
    <a href="{RUTAS['borrar']['de']}">wie du dein Konto löschst</a>.</li>
  </ul>
  <p>Nach der DSGVO kannst du außerdem Auskunft über deine Daten oder ihre Berichtigung verlangen, indem du an die obige
  Adresse schreibst, und dich bei der Datenschutzaufsichtsbehörde deines Landes beschweren.</p>

  <h2>Kinder</h2>
  <p>Lince richtet sich nicht an Kinder unter 13 Jahren, und wir erheben nicht wissentlich Daten von Kindern in diesem
  Alter. Wenn du glaubst, dass ein Kind ein Konto angelegt hat, schreib uns, und wir löschen es.</p>

  <h2>Änderungen dieser Erklärung</h2>
  <p>Wenn wir diese Erklärung ändern, aktualisieren wir das Datum oben. Bei wichtigen Änderungen kündigen wir sie auch in
  der App an.</p>
'''),
 'it': dict(title='Informativa sulla privacy', desc="L'informativa sulla privacy di Lince: quali dati vengono conservati, a cosa servono e come chiederne la cancellazione in qualsiasi momento.",
  pie=('Home', 'borrar', 'Elimina il mio account'), cuerpo=f'''
  <h1>Informativa sulla privacy</h1>
  <p class="fecha">Ultimo aggiornamento: 3 novembre 2026</p>

  <div class="caja">
    <strong>In breve:</strong> quello che leggi in Lince resta sul tuo telefono. Non mostriamo pubblicità e non vendiamo
    dati. Contiamo dati di utilizzo anonimi, mai quello che leggi, e puoi disattivarli nelle Impostazioni. Se scegli di
    accedere con Google, conserviamo solo la tua email, il tuo nome e quanti file hai importato, perché i limiti del piano
    gratuito funzionino con il tuo account.
  </div>

  <h2>Titolare</h2>
  <p>Lince è un'app creata in Cile da uno sviluppatore indipendente. Per qualsiasi domanda sulla privacy scrivi a
  <a href="mailto:{MAIL}">{MAIL}</a>.</p>

  <h2>Cosa resta solo sul tuo telefono</h2>
  <p>Tutto questo resta sul tuo dispositivo e non viene mai inviato a nessun server:</p>
  <ul>
    <li>I testi e i libri che incolli o importi (.txt, .epub, .pdf) e i libri della Biblioteca classica che scegli.</li>
    <li>I tuoi progressi in ogni testo, le sessioni di lettura, la serie, i punti (XP), i badge e i record.</li>
    <li>Le tue risposte a "Quanto hai capito?" e i risultati del test di velocità.</li>
    <li>Le tue impostazioni: lingua, tema, colori, carattere, velocità, obiettivo giornaliero e orario del promemoria.</li>
    <li>Gli indirizzi e, se li inserisci, nome utente e password delle biblioteche OPDS che aggiungi.</li>
  </ul>
  <p>Se disinstalli l'app, tutto questo viene cancellato dal telefono.</p>

  <h2>Quando l'app si collega a internet</h2>
  <p>Non serve internet per leggere. L'app si collega in questi casi:</p>
  <ul>
    <li><strong>Condividi un link con Lince:</strong> il telefono scarica quella pagina direttamente dal sito per estrarre
    il testo dell'articolo. Il sito lo vede come una qualsiasi visita da un browser. Il link e il testo non passano dai
    nostri server.</li>
    <li><strong>Usi una biblioteca online (OPDS):</strong> il telefono si collega direttamente all'indirizzo inserito, con
    nome utente e password se li hai aggiunti. Se l'indirizzo inizia con <code>http://</code> (e non
    <code>https://</code>), la connessione non è cifrata e qualcuno sulla stessa rete potrebbe vedere cosa viene inviato;
    usa <code>https://</code> ogni volta che la tua biblioteca lo consente.</li>
    <li><strong>Accedi o acquisti Lince Plus:</strong> spiegato qui sotto.</li>
    <li><strong>Apri l'app:</strong> controlla se c'è un aggiornamento, chiede a RevenueCat lo stato del tuo Lince Plus e,
    se non l'hai disattivato, invia dati di utilizzo anonimi.</li>
  </ul>

  <h2>Appunti</h2>
  <p>Lince legge ciò che hai copiato solo quando tocchi "Incolla". Non controlla gli appunti in background e non ne
  conserva nulla, tranne il testo che scegli di aggiungere alla tua biblioteca.</p>

  <h2>Se accedi con Google (facoltativo)</h2>
  <p>Puoi usare Lince senza account. Ti chiediamo di accedere con Google solo dalla seconda importazione di un file in poi.
  Puoi anche accedere dopo aver acquistato Lince Plus, perché ti segua se cambi telefono. Se accedi, conserviamo:</p>
  <ul>
    <li>Il tuo indirizzo email, il tuo nome e l'identificativo del tuo account Google.</li>
    <li>Un registro delle importazioni: la data e il numero di parole di ogni file importato (non il contenuto né il nome
    del file), per applicare il limite di importazioni gratuite.</li>
  </ul>
  <p>Questi dati sono conservati presso <a href="https://supabase.com/privacy">Supabase</a>, il nostro fornitore di account,
  su server a San Paolo, in Brasile. Servono solo al funzionamento dell'app; non vengono mai venduti né condivisi per
  pubblicità.</p>

  <h2>Acquisti</h2>
  <p>Gli acquisti di Lince Plus sono gestiti da Google Play. Non vediamo né conserviamo mai i dati della tua carta. Per sapere
  se hai Plus usiamo <a href="https://www.revenuecat.com/privacy">RevenueCat</a>, che riceve da Google Play le informazioni
  sull'acquisto (prodotto, data e stato dell'abbonamento) collegate a un identificativo anonimo del tuo account Lince.</p>

  <h2>Dati di utilizzo anonimi</h2>
  <p>Per capire cosa funziona e cosa si rompe, l'app invia a <a href="https://posthog.com/privacy">PostHog</a>, su server
  negli Stati Uniti, alcuni eventi con un identificativo casuale non collegato al tuo account: apertura e chiusura
  dell'app, fine del benvenuto, fine del test di velocità, apertura di un libro, 5 minuti di lettura, ritorno il giorno
  dopo, raggiungimento di un limite del piano gratuito, visualizzazione o acquisto di Lince Plus, condivisione del
  riepilogo settimanale ed errori dell'app. Non includono mai titoli, testi, il tuo nome o la tua email. Puoi disattivarli
  in Impostazioni → Condividi dati di utilizzo anonimi.</p>

  <h2>Questo sito</h2>
  <p>Questo sito conta le visite con <a href="https://posthog.com/privacy">PostHog</a>, su server negli Stati Uniti, senza
  cookie. Invia la pagina che visiti, il sito da cui arrivi, la lingua del browser, il tuo paese approssimativo, un
  identificativo casuale che scade con la sessione del browser e azioni come iniziare il test di velocità o usare il
  calcolatore. Non invia il risultato del test, le tue risposte o ciò che scrivi, e non conserva il tuo indirizzo IP.
  Rispetta "Do Not Track" e non funziona in questa pagina né in quella di eliminazione dell'account.</p>

  <h2>Cosa non facciamo</h2>
  <ul>
    <li>Non mostriamo pubblicità.</li>
    <li>Non usiamo l'ID pubblicitario e non ti seguiamo su altre app o siti.</li>
    <li>Non accediamo alla tua posizione, ai contatti, alle foto, al microfono o alla fotocamera.</li>
    <li>Non carichiamo i testi che leggi.</li>
  </ul>

  <h2>Notifiche</h2>
  <p>Se attivi il promemoria giornaliero, è il tuo telefono a programmarlo. Non passa da nessun server.</p>

  <h2>Come cancellare i tuoi dati</h2>
  <ul>
    <li><strong>Dati sul telefono:</strong> elimina un testo tenendolo premuto nella tua biblioteca, oppure disinstalla
    l'app per cancellare tutto.</li>
    <li><strong>Il tuo account:</strong> nell'app vai in Impostazioni → Account → Elimina il mio account. L'account e il
    registro delle importazioni vengono cancellati subito. Puoi chiederlo anche via email; vedi
    <a href="{RUTAS['borrar']['it']}">come eliminare il tuo account</a>.</li>
  </ul>
  <p>In base al GDPR puoi anche chiedere l'accesso ai tuoi dati o la loro rettifica scrivendo all'indirizzo sopra, e
  presentare un reclamo all'autorità per la protezione dei dati del tuo paese.</p>

  <h2>Minori</h2>
  <p>Lince non è rivolta a minori di 13 anni e non raccogliamo consapevolmente dati di bambini sotto quell'età. Se pensi che
  un bambino abbia creato un account, scrivici e lo cancelleremo.</p>

  <h2>Modifiche a questa informativa</h2>
  <p>Se modifichiamo questa informativa, aggiorneremo la data qui sopra. Se il cambiamento è importante, lo annunceremo
  anche nell'app.</p>
'''),
}

BORRAR = {
 'pt': dict(title='Excluir minha conta', desc='Como excluir sua conta do Lince e seus dados, pelo app ou por e-mail, e o que acontece com uma assinatura ativa.',
  pie=('Início', 'privacidad', 'Política de privacidade'), asunto='Excluir minha conta do Lince', cuerpo='''
  <h1>Excluir minha conta do Lince</h1>
  <p class="fecha">Lince (app para Android)</p>

  <h2>Pelo app (na hora)</h2>
  <ol>
    <li>Abra o Lince e toque na engrenagem de <strong>Configurações</strong>.</li>
    <li>Na seção <strong>Conta</strong>, toque em <strong>Apagar minha conta</strong>.</li>
    <li>Confirme. Sua conta é apagada na hora.</li>
  </ol>

  <h2>Por e-mail</h2>
  <p>Se você não tem mais o app, escreva para {mail} com o assunto "Excluir minha conta do Lince", a partir do mesmo
  e-mail do Google com que você entrou. Apagamos em até 7 dias e confirmamos por e-mail.</p>

  <h2>O que é apagado</h2>
  <ul>
    <li>Sua conta: e-mail, nome e identificador do Google.</li>
    <li>Seu registro de importações (datas e número de palavras).</li>
  </ul>
  <p>Não guardamos nenhum outro dado seu nos nossos servidores. O que está no seu celular (textos, progresso, sequência,
  configurações) é apagado quando você desinstala o app.</p>

  <h2>O que é mantido</h2>
  <p>Se você comprou o Lince Plus, o Google Play guarda o registro da compra segundo as próprias políticas, e a RevenueCat
  mantém o histórico de transações pelo tempo exigido por lei (por exemplo, para reembolsos ou impostos). Para cancelar uma
  assinatura, faça isso em Google Play → Pagamentos e assinaturas.</p>
'''),
 'fr': dict(title='Supprimer mon compte', desc="Comment supprimer votre compte Lince et ses données, depuis l'appli ou par e-mail, et ce qui arrive à un abonnement actif.",
  pie=('Accueil', 'privacidad', 'Politique de confidentialité'), asunto='Supprimer mon compte Lince', cuerpo='''
  <h1>Supprimer mon compte Lince</h1>
  <p class="fecha">Lince (appli Android)</p>

  <h2>Depuis l'appli (immédiat)</h2>
  <ol>
    <li>Ouvrez Lince et touchez la roue dentée des <strong>Réglages</strong>.</li>
    <li>Dans la section <strong>Compte</strong>, touchez <strong>Supprimer mon compte</strong>.</li>
    <li>Confirmez. Votre compte est supprimé tout de suite.</li>
  </ol>

  <h2>Par e-mail</h2>
  <p>Si vous n'avez plus l'appli, écrivez à {mail} avec l'objet « Supprimer mon compte Lince », depuis l'adresse Google
  utilisée pour vous connecter. Nous le supprimons sous 7 jours et confirmons par e-mail.</p>

  <h2>Ce qui est supprimé</h2>
  <ul>
    <li>Votre compte : e-mail, nom et identifiant Google.</li>
    <li>Votre registre d'imports (dates et nombre de mots).</li>
  </ul>
  <p>Nous ne conservons aucune autre donnée vous concernant sur nos serveurs. Ce qui est sur votre téléphone (textes,
  progression, série, réglages) est supprimé quand vous désinstallez l'appli.</p>

  <h2>Ce qui est conservé</h2>
  <p>Si vous avez acheté Lince Plus, Google Play conserve la trace de l'achat selon ses propres règles, et RevenueCat garde
  l'historique des transactions aussi longtemps que la loi l'exige (par exemple pour les remboursements ou la fiscalité).
  Pour annuler un abonnement, faites-le dans Google Play → Paiements et abonnements.</p>
'''),
 'de': dict(title='Mein Konto löschen', desc='So löschst du dein Lince-Konto und seine Daten, in der App oder per E-Mail, und was mit einem laufenden Abo passiert.',
  pie=('Startseite', 'privacidad', 'Datenschutzerklärung'), asunto='Mein Lince-Konto löschen', cuerpo='''
  <h1>Mein Lince-Konto löschen</h1>
  <p class="fecha">Lince (Android-App)</p>

  <h2>In der App (sofort)</h2>
  <ol>
    <li>Öffne Lince und tippe auf das Zahnrad <strong>Einstellungen</strong>.</li>
    <li>Tippe im Bereich <strong>Konto</strong> auf <strong>Mein Konto löschen</strong>.</li>
    <li>Bestätige. Dein Konto wird sofort gelöscht.</li>
  </ol>

  <h2>Per E-Mail</h2>
  <p>Wenn du die App nicht mehr hast, schreib an {mail} mit dem Betreff „Mein Lince-Konto löschen“, von derselben
  Google-Adresse, mit der du dich angemeldet hast. Wir löschen es innerhalb von 7 Tagen und bestätigen per E-Mail.</p>

  <h2>Was gelöscht wird</h2>
  <ul>
    <li>Dein Konto: E-Mail-Adresse, Name und Google-Kennung.</li>
    <li>Dein Import-Protokoll (Daten und Wortzahlen).</li>
  </ul>
  <p>Wir speichern keine anderen Daten über dich auf unseren Servern. Was auf deinem Handy ist (Texte, Fortschritt, Serie,
  Einstellungen), wird gelöscht, wenn du die App deinstallierst.</p>

  <h2>Was bleibt</h2>
  <p>Wenn du Lince Plus gekauft hast, behält Google Play den Kaufnachweis nach seinen eigenen Regeln, und RevenueCat bewahrt
  den Transaktionsverlauf so lange auf, wie es das Gesetz verlangt (zum Beispiel für Erstattungen oder Steuern). Ein Abo
  kündigst du in Google Play → Zahlungen und Abos.</p>
'''),
 'it': dict(title='Elimina il mio account', desc="Come eliminare il tuo account Lince e i suoi dati, dall'app o via email, e cosa succede a un abbonamento attivo.",
  pie=('Home', 'privacidad', 'Informativa sulla privacy'), asunto='Elimina il mio account Lince', cuerpo='''
  <h1>Elimina il mio account Lince</h1>
  <p class="fecha">Lince (app Android)</p>

  <h2>Dall'app (subito)</h2>
  <ol>
    <li>Apri Lince e tocca l'ingranaggio delle <strong>Impostazioni</strong>.</li>
    <li>Nella sezione <strong>Account</strong>, tocca <strong>Elimina il mio account</strong>.</li>
    <li>Conferma. L'account viene eliminato subito.</li>
  </ol>

  <h2>Via email</h2>
  <p>Se non hai più l'app, scrivi a {mail} con oggetto "Elimina il mio account Lince", dallo stesso indirizzo Google con
  cui hai effettuato l'accesso. Lo eliminiamo entro 7 giorni e te lo confermiamo via email.</p>

  <h2>Cosa viene eliminato</h2>
  <ul>
    <li>Il tuo account: email, nome e identificativo Google.</li>
    <li>Il registro delle importazioni (date e numero di parole).</li>
  </ul>
  <p>Non conserviamo nessun altro dato su di te nei nostri server. Ciò che è sul telefono (testi, progressi, serie,
  impostazioni) viene cancellato quando disinstalli l'app.</p>

  <h2>Cosa viene conservato</h2>
  <p>Se hai acquistato Lince Plus, Google Play conserva la registrazione dell'acquisto secondo le proprie regole, e
  RevenueCat conserva lo storico delle transazioni per il tempo richiesto dalla legge (per esempio per rimborsi o fini
  fiscali). Per annullare un abbonamento, fallo in Google Play → Pagamenti e abbonamenti.</p>
'''),
}


def main():
    from urllib.parse import quote
    for lang, p in PRIVACIDAD.items():
        out = Path(RUTAS['privacidad'][lang].strip('/')) / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pagina(lang, 'privacidad', p['title'], p['desc'], p['cuerpo'], p['pie']))
        print('ok', out)
    for lang, p in BORRAR.items():
        mail = f'<a href="mailto:{MAIL}?subject={quote(p["asunto"])}">{MAIL}</a>'
        out = Path(RUTAS['borrar'][lang].strip('/')) / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pagina(lang, 'borrar', p['title'], p['desc'], p['cuerpo'].replace('{mail}', mail), p['pie']))
        print('ok', out)


if __name__ == '__main__':
    main()
