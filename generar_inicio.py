#!/usr/bin/env python3
"""Portada en portugués, francés, alemán e italiano (/pt/, /fr/, /de/, /it/), con la misma estructura que la
portada en inglés (index.html). Inglés y español se mantienen a mano: si cambia su estructura, cambiar también aquí.

Capturas: /img/<idioma>-<nombre>.webp (sacadas del emulador con la app en ese idioma). Video: /img/demo-<idioma>.*
"""
import html
import json
from pathlib import Path

from idiomas import B, LANGS, OG_LOCALE, RUTAS, alternos, menu_idiomas

PLAY = 'https://play.google.com/store/apps/details?id=co.com.monsalve.lince&referrer=utm_source%3Dsitio%26utm_medium%3Dweb%26utm_campaign%3D'
PLAY_ICONO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 2.6v18.8c0 .5.5.8 1 .6l15.6-9.4c.4-.3.4-.9 0-1.2L5 2c-.5-.2-1 .1-1 .6z"/></svg>'

T = {
 'pt': dict(
  title='Lince: App de Leitura Dinâmica para Android, Uma Palavra por Vez',
  desc='O Lince é um app de leitura dinâmica para Android: uma palavra por vez. Meça sua velocidade e leia clássicos, seus EPUB e PDF ou artigos. Sem anúncios.',
  og_title='Lince: leitura dinâmica e foco', og_desc='Uma palavra por vez, sempre no mesmo lugar. Leia mais e se distraia menos. Sem anúncios.',
  og_alt='Lince, app de leitura dinâmica', app_name='Lince: Leitura dinâmica e foco',
  ld_desc='App de leitura RSVP: mostra uma palavra por vez para ler com foco. Inclui teste de velocidade, 150 clássicos em 6 idiomas, importação de EPUB, PDF e TXT, metas e sequência.',
  nav=('Como funciona', 'Planos', 'Perguntas'),
  h1='Leia mais. <em>Distraia-se menos.</em>',
  bajada='O Lince é um app de leitura dinâmica que mostra uma palavra por vez, sempre no mesmo lugar. Seus olhos não pulam pela página e sua mente fica na história.',
  play='Baixar no Google Play', probar='Experimente aqui',
  marcas=('Grátis', 'Sem anúncios', 'Nunca vemos o que você lê', 'Funciona offline'),
  video_alt='O Lince lendo um texto uma palavra por vez',
  try_h='Experimente agora, aqui mesmo',
  try_p='Toque em "Ler" e olhe só para a letra marcada. Não mexa os olhos: as palavras vêm até você. É assim que se lê no Lince.',
  demo='Ler assim parece estranho nos primeiros segundos. Depois, quase sem perceber, você para de mexer os olhos e as palavras começam a chegar sozinhas. A letra marcada fica sempre no mesmo lugar, então seus olhos nunca precisam procurar onde começa cada palavra. Repare também nas pausas: o Lince espera um pouco mais nas vírgulas, mais nos pontos e mais ainda no fim de um parágrafo, para que cada ideia tenha tempo de assentar. Se algo escapar, toque na tela, veja o parágrafo inteiro e continue de onde quiser. Experimente subir a velocidade com a barra. Até onde você vai sem perder o fio?',
  leer='▶ Ler', pausa='❚❚ Pausar', otra='↺ De novo', velocidad='Velocidade', ppm_aria='Palavras por minuto', ppm='ppm',
  pista='No app você vai de 150 a 1.000 palavras por minuto e escolhe a duração das pausas.',
  medir='Medir minha velocidade',
  how_h='Como funciona',
  how_p='Quando você lê do jeito de sempre, seus olhos dão pequenos saltos pela linha, voltam sem querer e se perdem na página. O Lince faz esse trabalho por você: entrega cada palavra exatamente onde você já está olhando.',
  pasos=(('Meça sua velocidade', 'Leia um texto curto durante 1 minuto e responda 3 perguntas. O Lince diz quantas palavras por minuto você lê e sugere uma velocidade para começar.'),
         ('Escolha o que ler', 'Um clássico grátis, um dos seus livros, um artigo que você encontrou ou qualquer texto que copiou.'),
         ('Leia e suba de nível', 'Toque para ler, toque para pausar. Ao terminar, uma pergunta rápida confere se você entendeu: o Lince só sugere ir mais rápido quando você realmente acompanha.')),
  b1_h='Uma palavra por vez, sem perder nada',
  b1_p='A letra guia marcada fica sempre no mesmo lugar. O Lince faz pausas naturais nas vírgulas, nos pontos e no fim dos parágrafos. Enquanto você lê, a velocidade fica logo abaixo da palavra: aumente ou diminua sem parar.',
  b1_li=('<strong>Pause para ver o parágrafo inteiro</strong> e toque em qualquer palavra para continuar dali.',
         '<strong>Ir para…</strong> capítulos, páginas reais do PDF ou uma frase de que você se lembra.',
         '<strong>Continue sempre de onde parou</strong>, em cada livro.'),
  alt_leyendo='O Lince lendo: uma só palavra com a letra guia marcada', alt_pausa='O Lince em pausa: a palavra, o parágrafo inteiro e os controles',
  todo_h='Leia o que quiser', todo_p='Você não fica preso a uma loja. O Lince lê o que você já tem e o que você encontra.',
  tarjetas=(('📚', '150 clássicos incluídos', '25 em português e 125 em outros 5 idiomas: Dom Casmurro, Os Maias, O Cortiço, Iracema e muito mais.'),
            ('📄', 'Seus livros', 'Importe arquivos .epub, .pdf e .txt. Os capítulos vêm do índice do livro e os PDFs mantêm suas páginas.'),
            ('🌐', 'Artigos da web', 'No navegador, toque em Compartilhar → Lince e o artigo fica pronto para ler, sem menus nem anúncios.'),
            ('📋', 'Qualquer texto', 'Copie uma anotação, um e-mail longo ou um relatório e toque em "Colar" na tela inicial.'),
            ('🗂️', 'Sua biblioteca online', 'Conecte catálogos OPDS (Calibre-Web, Kavita e outros) para buscar e baixar seus livros direto no app.'),
            ('🌎', 'Pratique um idioma', 'O app está em português, espanhol, inglês, francês, alemão e italiano, e você pode ler os clássicos em qualquer um deles.')),
  b2_h='Um hábito que fica', b2_p='Ler um pouco todo dia muda mais do que ler muito de vez em quando. O Lince ajuda você a manter o ritmo sem pressão.',
  b2_li=('Uma meta diária em minutos e uma sequência de dias seguidos.', 'Um escudo por semana: um dia ruim não apaga sua sequência.',
         'Pontos, níveis e mais de 40 conquistas.', 'Um resumo semanal para compartilhar.', 'Um lembrete que fica em silêncio se você já cumpriu a meta.'),
  alt_inicio='Tela inicial do Lince: sequência, nível, meta diária e sua semana', alt_biblioteca='Biblioteca clássica do Lince',
  b3_h='Feito para mentes que se distraem',
  b3_p='Se você tem dificuldade de se concentrar, se lê uma página e não lembra de nada, ou se ler na tela cansa, o Lince se adapta a você.',
  b3_li=('Fontes pensadas para facilitar a leitura: <strong>Lexend</strong>, <strong>Atkinson Hyperlegible</strong> e <strong>OpenDyslexic</strong>.',
         '6 temas: Foco (creme), Claro, Sépia, Cinza escuro, Noite (preto puro) e Alto contraste.',
         'Texto maior quando você precisar, e a letra guia na cor que preferir.', 'Se o seu celular usa o modo escuro, o Lince também.'),
  alt_grande='O Lince com texto grande', alt_capitulos='Ir para: capítulos, página ou frase',
  horiz_h='Na horizontal e em tablets também', horiz_p='Vire o celular para ver a palavra maior, ou use o Lince no tablet com tudo à vista.',
  alt_acostado='O Lince num celular na horizontal, em pausa, com o parágrafo e os controles lado a lado',
  alt_tablet='O Lince num tablet, em pausa, com o parágrafo e os controles lado a lado',
  b4_h='Rápido, mas entendendo', b4_p='Ler rápido não serve de nada se você não entende. Por isso o Lince não te empurra a ir mais rápido: ele mede.',
  b4_li=('O teste de velocidade combina palavras por minuto com perguntas de compreensão, em 5 textos diferentes.',
         'Se você é rápido mas entende pouco, o Lince diz com sinceridade e sugere ir mais devagar.',
         'Depois de cada sessão, "Quanto você entendeu?" ajusta sua velocidade recomendada.'),
  alt_prueba='Resultado do teste de velocidade com uma velocidade recomendada', alt_prueba_baja='Resultado do teste sugerindo ir mais devagar para entender melhor',
  ciencia_h='O que dizem os estudos (sem exagero)', ciencia_p='Este método se chama RSVP (apresentação visual serial rápida) e é estudado há décadas.',
  ciencia=(('Ajuda a focar', 'Com uma só palavra na tela não há mais nada para olhar: sem saltos de linha, sem releituras sem querer, e fica mais difícil a mente se dispersar.'),
           ('Tem limites', 'As pesquisas mostram que em velocidades muito altas a compreensão cai. Não existe atalho mágico; por isso o Lince mede quanto você entende e nunca promete "ler 3× mais rápido".'),
           ('Funciona melhor assim', 'Sessões curtas, textos de que você gosta e uma velocidade confortável que você vai subindo aos poucos.')),
  ciencia_nota='Uma revisão completa: Rayner, Schotter, Masson, Potter &amp; Treiman (2016), "So Much to Read, So Little Time", <em>Psychological Science in the Public Interest</em>.',
  porque_h='Por que o Lince existe',
  porque_p='Lemos mais do que nunca, mas entre notificações, abas e telas lotadas é difícil terminar um capítulo. O Lince dá à leitura um espaço limpo: uma palavra, o seu ritmo, nada mais. Sem anúncios interrompendo, sem vender seus dados, e com clássicos grátis para você começar hoje.',
  planes_h='Planos', planes_p='Você pode ler de graça pelo tempo que quiser. O Lince Plus tira os limites.',
  gratis='Grátis', gratis_li=('O leitor completo, todos os temas e fontes', 'Teste de velocidade, metas, sequência e conquistas',
       '3 clássicos de cada vez (termine um e escolha outro)', '2 livros importados (arquivos ou bibliotecas OPDS)', 'Até 10 páginas por dia de texto colado ou artigos'),
  precio_plus='<strong>US$2,99</strong> por mês · US$19,99 por ano · US$34,99 uma vez',
  plus_li=('Tudo do plano grátis', 'A Biblioteca clássica inteira, sem esperar', 'Importações sem limite', 'Sem limite diário de texto colado e artigos', 'Início em negrito (destaca o começo de cada palavra)'),
  precio_nota='Os preços podem variar por país; o Google Play mostra o preço final na sua moeda.',
  priv_h='Sua privacidade',
  priv=(('🔒', 'O que você lê é seu', 'Seus textos e seu progresso ficam no seu celular. Não os enviamos.'),
        ('🚫', 'Sem anúncios', 'Só contamos dados de uso anônimos, nunca o que você lê, e você pode desativá-los em Configurações.'),
        ('👤', 'Sem conta para ler', 'Nem para comprar o Plus ou para o seu primeiro livro. Só pedimos a partir da segunda importação.')),
  priv_nota='Detalhes na <a href="{priv}">política de privacidade</a>.',
  galeria_h='Veja em ação',
  galeria=('Lendo', 'Em pausa', 'Ir a um capítulo', 'Tema escuro', 'Seu dia e sua sequência', 'Boas-vindas', 'Escolha 3 livros grátis', 'Texto grande'),
  faq_h='Perguntas frequentes',
  faq=(('O Lince é grátis?', 'Sim. Você pode ler sem pagar e sem limite de tempo. O Lince Plus é opcional e tira os limites de clássicos, importações e texto colado.'),
       ('Vou entender o que leio?', 'Essa é a ideia. Você começa numa velocidade confortável e o Lince confere sua compreensão com perguntas curtas. Ele só sugere ir mais rápido quando você está entendendo bem.'),
       ('Cansa ler assim?', 'No começo parece diferente. As pausas na pontuação ajudam, e você pode deixá-las mais longas em Configurações. Recomendamos sessões curtas, de 10 a 20 minutos.'),
       ('Ajuda com TDAH ou dislexia?', 'Muitas pessoas que se distraem com facilidade acham mais fácil se concentrar com uma palavra por vez, e o Lince inclui fontes como a OpenDyslexic. Mas não é um tratamento médico: experimente e fique com o que funcionar para você.'),
       ('Funciona offline?', 'Sim. Os 150 clássicos vêm dentro do app e seus livros importados ficam no seu celular. Você só precisa de internet para buscar um artigo, usar uma biblioteca online, entrar na conta ou comprar o Plus.'),
       ('Que formatos posso ler?', 'EPUB, PDF (com texto de verdade, não escaneado) e TXT, além de texto colado, artigos da web e catálogos OPDS.'),
       ('Tem versão para iPhone?', 'Por enquanto o Lince é só para Android.'),
       ('Como cancelo o Lince Plus?', 'No Google Play → seu perfil → Pagamentos e assinaturas → Assinaturas. A compra única não se renova.')),
  herr_h='Ferramentas de leitura grátis',
  herr=(('prueba', 'Teste de velocidade de leitura', 'Descubra quantas palavras por minuto você lê em 1 minuto.'),
        ('tiempo', 'Tempo de leitura de livros', 'Quanto tempo levam 25 clássicos na sua velocidade.'),
        ('rsvp', 'O que é a leitura RSVP?', 'Como funciona e o que dizem os estudos.')),
  cierre_h='Sua próxima página está esperando', cierre_p='Meça sua velocidade em 1 minuto e escolha seus 3 clássicos grátis.',
  pie=('Teste de velocidade', 'Tempo de leitura', 'O que é RSVP?', 'Privacidade', 'Excluir minha conta', 'Contato')),

 'fr': dict(
  title='Lince : appli de lecture rapide pour Android, un mot à la fois',
  desc="Lince est une appli de lecture rapide pour Android : un mot à la fois. Mesurez votre vitesse et lisez des classiques, vos EPUB et PDF ou des articles. Sans pub.",
  og_title='Lince : lecture rapide et concentration', og_desc='Un mot à la fois, toujours au même endroit. Lisez plus, dispersez-vous moins. Sans publicité.',
  og_alt='Lince, appli de lecture rapide', app_name='Lince : Lecture rapide et concentration',
  ld_desc='Appli de lecture RSVP : affiche un mot à la fois pour lire avec concentration. Test de vitesse, 150 classiques en 6 langues, import EPUB, PDF et TXT, objectifs et séries.',
  nav=('Comment ça marche', 'Offres', 'FAQ'),
  h1='Lisez plus. <em>Dispersez-vous moins.</em>',
  bajada="Lince est une appli de lecture rapide qui vous montre un mot à la fois, toujours au même endroit. Vos yeux ne sautent pas sur la page et votre esprit reste dans l'histoire.",
  play='Disponible sur Google Play', probar='Essayer ici',
  marcas=('Gratuit', 'Sans publicité', 'Nous ne voyons jamais ce que vous lisez', 'Fonctionne hors ligne'),
  video_alt='Lince affichant un texte mot à mot',
  try_h='Essayez tout de suite, ici même',
  try_p='Touchez « Lire » et regardez seulement la lettre marquée. Ne bougez pas les yeux : les mots viennent à vous. Voilà ce que donne la lecture avec Lince.',
  demo="Lire ainsi paraît étrange pendant les premières secondes. Puis, presque sans s'en rendre compte, on arrête de bouger les yeux et les mots arrivent tout seuls. La lettre marquée reste toujours au même endroit, alors vos yeux n'ont jamais à chercher où commence chaque mot. Remarquez aussi les pauses : Lince attend un peu plus aux virgules, davantage aux points et plus encore à la fin d'un paragraphe, pour que chaque idée ait le temps de s'installer. Si quelque chose vous échappe, touchez l'écran, voyez tout le paragraphe et reprenez où vous voulez. Essayez d'augmenter la vitesse avec le curseur. Jusqu'où pouvez-vous aller sans perdre le fil ?",
  leer='▶ Lire', pausa='❚❚ Pause', otra='↺ Encore', velocidad='Vitesse', ppm_aria='Mots par minute', ppm='mots/min',
  pista="Dans l'appli, vous allez de 150 à 1 000 mots par minute et choisissez la durée des pauses.",
  medir='Mesurer ma vitesse',
  how_h='Comment ça marche',
  how_p="Quand vous lisez de façon classique, vos yeux font de petits sauts le long de la ligne, reviennent en arrière et se perdent dans la page. Lince fait ce travail pour vous : il place chaque mot exactement là où vous regardez déjà.",
  pasos=(('Mesurez votre vitesse', "Lisez un texte court pendant 1 minute et répondez à 3 questions. Lince vous dit combien de mots par minute vous lisez et vous propose une vitesse de départ."),
         ('Choisissez quoi lire', "Un classique gratuit, l'un de vos livres, un article trouvé en ligne ou n'importe quel texte copié."),
         ('Lisez et progressez', "Touchez pour lire, touchez pour mettre en pause. À la fin, une petite question vérifie que vous avez compris : Lince ne propose d'accélérer que si vous suivez vraiment.")),
  b1_h='Un mot à la fois, sans rien manquer',
  b1_p="La lettre guide marquée reste toujours au même endroit. Lince fait des pauses naturelles aux virgules, aux points et en fin de paragraphe. Pendant la lecture, la vitesse reste sous le mot : accélérez ou ralentissez sans vous arrêter.",
  b1_li=("<strong>Mettez en pause pour voir tout le paragraphe</strong> et touchez n'importe quel mot pour reprendre à partir de là.",
         '<strong>Aller à…</strong> un chapitre, une vraie page du PDF ou une phrase dont vous vous souvenez.',
         '<strong>Reprenez toujours là où vous vous êtes arrêté</strong>, dans chaque livre.'),
  alt_leyendo='Lince en lecture : un seul mot avec la lettre guide marquée', alt_pausa='Lince en pause : le mot, tout le paragraphe et les commandes',
  todo_h='Lisez tout ce que vous voulez', todo_p="Vous n'êtes lié à aucune librairie. Lince lit ce que vous avez déjà et ce que vous trouvez.",
  tarjetas=(('📚', '150 classiques inclus', '25 en français et 125 dans 5 autres langues : Madame Bovary, Les Trois Mousquetaires, Germinal, Notre-Dame de Paris et bien d’autres.'),
            ('📄', 'Vos livres', 'Importez des fichiers .epub, .pdf et .txt. Les chapitres viennent de la table des matières et les PDF gardent leurs pages.'),
            ('🌐', 'Articles du web', 'Dans votre navigateur, touchez Partager → Lince et l’article est prêt à lire, sans menus ni publicité.'),
            ('📋', "N'importe quel texte", 'Copiez une note, un long e-mail ou un rapport et touchez « Coller » sur l’écran d’accueil.'),
            ('🗂️', 'Votre bibliothèque en ligne', 'Connectez des catalogues OPDS (Calibre-Web, Kavita et d’autres) pour chercher et télécharger vos livres dans l’appli.'),
            ('🌎', 'Pratiquez une langue', 'L’appli existe en français, anglais, espagnol, portugais, allemand et italien, et vous pouvez lire les classiques dans chacune.')),
  b2_h='Une habitude qui tient', b2_p='Lire un peu chaque jour change plus que lire beaucoup une fois. Lince vous aide à tenir sans pression.',
  b2_li=("Un objectif quotidien en minutes et une série de jours d'affilée.", "Un bouclier par semaine : une mauvaise journée n'efface pas votre série.",
         'Des points, des niveaux et plus de 40 badges.', 'Un résumé de la semaine à partager.', "Un rappel qui se tait si l'objectif est déjà atteint."),
  alt_inicio="Accueil de Lince : série, niveau, objectif du jour et votre semaine", alt_biblioteca='Bibliothèque classique de Lince',
  b3_h="Pensé pour les esprits qui s'égarent",
  b3_p="Si vous avez du mal à vous concentrer, si vous lisez une page sans rien en retenir, ou si lire sur écran vous fatigue, Lince s'adapte à vous.",
  b3_li=('Des polices conçues pour faciliter la lecture : <strong>Lexend</strong>, <strong>Atkinson Hyperlegible</strong> et <strong>OpenDyslexic</strong>.',
         '6 thèmes : Concentration (crème), Clair, Sépia, Gris foncé, Nuit (noir pur) et Contraste élevé.',
         'Un texte plus grand quand il le faut, et la lettre guide dans la couleur de votre choix.', 'Si votre téléphone est en mode sombre, Lince aussi.'),
  alt_grande='Lince avec un grand texte', alt_capitulos='Aller à : chapitres, page ou phrase',
  horiz_h="À l'horizontale et sur tablette aussi", horiz_p="Tournez votre téléphone pour un mot plus grand, ou utilisez Lince sur tablette avec tout sous les yeux.",
  alt_acostado="Lince sur un téléphone à l'horizontale, en pause, avec le paragraphe et les commandes côte à côte",
  alt_tablet='Lince sur une tablette, en pause, avec le paragraphe et les commandes côte à côte',
  b4_h='Vite, mais en comprenant', b4_p="Lire vite ne sert à rien si on ne comprend pas. C'est pourquoi Lince ne vous pousse pas à accélérer : il mesure.",
  b4_li=('Le test de vitesse combine mots par minute et questions de compréhension, sur 5 textes différents.',
         'Si vous lisez vite mais comprenez peu, Lince vous le dit franchement et vous propose de ralentir.',
         'Après chaque session, « Combien as-tu compris ? » ajuste votre vitesse conseillée.'),
  alt_prueba='Résultat du test de vitesse avec une vitesse conseillée', alt_prueba_baja='Résultat du test qui conseille de ralentir pour mieux comprendre',
  ciencia_h='Ce que dit la recherche (sans exagérer)', ciencia_p='Cette méthode s’appelle RSVP (présentation visuelle sérielle rapide) et elle est étudiée depuis des décennies.',
  ciencia=(('Elle aide à se concentrer', "Avec un seul mot à l'écran, il n'y a rien d'autre à regarder : pas de saut de ligne, pas de relecture involontaire, et l'esprit s'évade moins facilement."),
           ('Elle a des limites', "Les études montrent qu'à très grande vitesse la compréhension baisse. Il n'y a pas de raccourci magique, c'est pourquoi Lince mesure ce que vous comprenez et ne promet jamais de « lire 3× plus vite »."),
           ('Elle marche mieux ainsi', 'Des sessions courtes, des textes qui vous plaisent et une vitesse confortable que vous augmentez petit à petit.')),
  ciencia_nota='Une synthèse complète : Rayner, Schotter, Masson, Potter &amp; Treiman (2016), « So Much to Read, So Little Time », <em>Psychological Science in the Public Interest</em>.',
  porque_h='Pourquoi Lince existe',
  porque_p="Nous lisons plus que jamais, mais entre les notifications, les onglets et les écrans encombrés, il est difficile de finir un chapitre. Lince offre à la lecture un espace épuré : un mot, votre rythme, rien d'autre. Pas de publicité qui interrompt, pas de vente de vos données, et des classiques gratuits pour commencer dès aujourd'hui.",
  planes_h='Offres', planes_p='Vous pouvez lire gratuitement aussi longtemps que vous voulez. Lince Plus supprime les limites.',
  gratis='Gratuit', gratis_li=('Le lecteur complet, tous les thèmes et polices', 'Test de vitesse, objectifs, séries et badges',
       '3 classiques à la fois (terminez-en un, choisissez-en un autre)', '2 livres importés (fichiers ou bibliothèques OPDS)', "Jusqu'à 10 pages par jour de texte collé ou d'articles"),
  precio_plus='<strong>2,99 US$</strong> par mois · 19,99 US$ par an · 34,99 US$ une fois',
  plus_li=('Tout ce qui est dans la version gratuite', 'Toute la Bibliothèque classique, sans attendre', 'Imports illimités', "Pas de limite quotidienne de texte collé et d'articles", 'Début en gras (met en avant le début de chaque mot)'),
  precio_nota='Les prix peuvent varier selon le pays ; Google Play affiche le prix final dans votre devise.',
  priv_h='Votre vie privée',
  priv=(('🔒', 'Ce que vous lisez vous appartient', 'Vos textes et votre progression restent sur votre téléphone. Nous ne les envoyons pas.'),
        ('🚫', 'Sans publicité', 'Nous comptons seulement des données d’utilisation anonymes, jamais ce que vous lisez, et vous pouvez les désactiver dans les Réglages.'),
        ('👤', 'Pas de compte pour lire', "Ni pour acheter Plus, ni pour votre premier livre. Nous ne le demandons qu'à partir du deuxième import.")),
  priv_nota='Détails dans la <a href="{priv}">politique de confidentialité</a>.',
  galeria_h='Voir Lince en action',
  galeria=('Lecture', 'En pause', 'Aller à un chapitre', 'Thème sombre', 'Votre journée et votre série', 'Accueil', 'Choisissez 3 livres gratuits', 'Grand texte'),
  faq_h='Questions fréquentes',
  faq=(('Lince est-il gratuit ?', "Oui. Vous pouvez lire sans payer et sans limite de temps. Lince Plus est facultatif et supprime les limites de classiques, d'imports et de texte collé."),
       ('Vais-je comprendre ce que je lis ?', "C'est tout l'intérêt. Vous commencez à une vitesse confortable et Lince vérifie votre compréhension par de courtes questions. Il ne propose d'accélérer que si vous comprenez bien."),
       ('Est-ce fatigant de lire ainsi ?', "Au début, c'est différent. Les pauses à la ponctuation aident, et vous pouvez les allonger dans les Réglages. Nous conseillons des sessions courtes, de 10 à 20 minutes."),
       ('Est-ce que ça aide avec le TDAH ou la dyslexie ?', "Beaucoup de personnes facilement distraites se concentrent mieux avec un mot à la fois, et Lince inclut des polices comme OpenDyslexic. Mais ce n'est pas un traitement médical : essayez et gardez ce qui vous convient."),
       ('Fonctionne-t-il hors ligne ?', "Oui. Les 150 classiques sont inclus dans l'appli et vos livres importés restent sur votre téléphone. Internet n'est nécessaire que pour récupérer un article, utiliser une bibliothèque en ligne, vous connecter ou acheter Plus."),
       ('Quels formats puis-je lire ?', 'EPUB, PDF (avec du vrai texte, pas des scans) et TXT, ainsi que du texte collé, des articles web et des catalogues OPDS.'),
       ('Existe-t-il une version iPhone ?', "Pour l'instant, Lince est disponible uniquement sur Android."),
       ('Comment résilier Lince Plus ?', "Dans Google Play → votre profil → Paiements et abonnements → Abonnements. L'achat unique ne se renouvelle pas.")),
  herr_h='Outils de lecture gratuits',
  herr=(('prueba', 'Test de vitesse de lecture', 'Découvrez vos mots par minute en 1 minute.'),
        ('tiempo', 'Temps de lecture des livres', 'Combien de temps prennent 25 classiques à votre vitesse.'),
        ('rsvp', 'Qu’est-ce que la lecture RSVP ?', 'Comment ça marche et ce que dit la recherche.')),
  cierre_h='Votre prochaine page vous attend', cierre_p='Mesurez votre vitesse en 1 minute et choisissez vos 3 classiques gratuits.',
  pie=('Test de vitesse', 'Temps de lecture', 'Lecture RSVP', 'Confidentialité', 'Supprimer mon compte', 'Contact')),

 'de': dict(
  title='Lince: Schnelllese-App für Android, ein Wort nach dem anderen',
  desc='Lince ist eine Schnelllese-App für Android: ein Wort nach dem anderen. Miss dein Lesetempo und lies Klassiker, deine EPUBs und PDFs oder Artikel. Ohne Werbung.',
  og_title='Lince: Schnelllesen und Fokus', og_desc='Ein Wort nach dem anderen, immer an derselben Stelle. Mehr lesen, weniger abschweifen. Ohne Werbung.',
  og_alt='Lince, Schnelllese-App', app_name='Lince: Schnelllesen und Fokus',
  ld_desc='RSVP-Lese-App: zeigt ein Wort nach dem anderen, damit du konzentriert liest. Mit Tempotest, 150 Klassikern in 6 Sprachen, Import von EPUB, PDF und TXT, Zielen und Serien.',
  nav=('So funktioniert’s', 'Preise', 'FAQ'),
  h1='Mehr lesen. <em>Weniger abschweifen.</em>',
  bajada='Lince ist eine Schnelllese-App, die dir ein Wort nach dem anderen zeigt, immer an derselben Stelle. Deine Augen springen nicht über die Seite, und dein Kopf bleibt bei der Geschichte.',
  play='Jetzt bei Google Play', probar='Hier ausprobieren',
  marcas=('Kostenlos', 'Ohne Werbung', 'Wir sehen nie, was du liest', 'Funktioniert offline'),
  video_alt='Lince zeigt einen Text Wort für Wort',
  try_h='Probier es gleich hier aus',
  try_p='Tippe auf „Lesen“ und schau nur auf den markierten Buchstaben. Bewege die Augen nicht: Die Wörter kommen zu dir. So fühlt sich Lesen mit Lince an.',
  demo='So zu lesen fühlt sich in den ersten Sekunden seltsam an. Dann hörst du fast unbemerkt auf, die Augen zu bewegen, und die Wörter kommen von selbst. Der markierte Buchstabe bleibt immer an derselben Stelle, deshalb müssen deine Augen nie suchen, wo ein Wort anfängt. Achte auch auf die Pausen: Lince wartet bei Kommas etwas länger, bei Punkten noch länger und am Ende eines Absatzes am längsten, damit jeder Gedanke Zeit hat anzukommen. Wenn dir etwas entgeht, tippe auf den Bildschirm, sieh dir den ganzen Absatz an und lies weiter, wo du willst. Erhöhe das Tempo mit dem Regler. Wie schnell kannst du lesen, ohne den Faden zu verlieren?',
  leer='▶ Lesen', pausa='❚❚ Pause', otra='↺ Nochmal', velocidad='Tempo', ppm_aria='Wörter pro Minute', ppm='WpM',
  pista='In der App gehst du von 150 bis 1.000 Wörtern pro Minute und wählst, wie lang die Pausen sind.',
  medir='Mein Tempo messen',
  how_h='So funktioniert’s',
  how_p='Wenn du wie gewohnt liest, machen deine Augen kleine Sprünge entlang der Zeile, rutschen zurück und verlieren sich auf der Seite. Lince nimmt dir diese Arbeit ab: Jedes Wort erscheint genau dort, wo du schon hinschaust.',
  pasos=(('Miss dein Tempo', 'Lies 1 Minute lang einen kurzen Text und beantworte 3 Fragen. Lince sagt dir, wie viele Wörter pro Minute du liest, und schlägt ein Starttempo vor.'),
         ('Wähle, was du liest', 'Einen kostenlosen Klassiker, eines deiner Bücher, einen Artikel, den du gefunden hast, oder jeden kopierten Text.'),
         ('Lies und steig auf', 'Tippen zum Lesen, tippen zum Pausieren. Danach prüft eine kurze Frage, ob du verstanden hast: Lince schlägt nur dann mehr Tempo vor, wenn du wirklich folgst.')),
  b1_h='Ein Wort nach dem anderen, ohne etwas zu verpassen',
  b1_p='Der markierte Leitbuchstabe bleibt immer an derselben Stelle. Lince macht natürliche Pausen bei Kommas, Punkten und am Absatzende. Beim Lesen bleibt das Tempo unter dem Wort: schneller oder langsamer, ohne anzuhalten.',
  b1_li=('<strong>Pausiere, um den ganzen Absatz zu sehen</strong>, und tippe auf ein Wort, um dort weiterzulesen.',
         '<strong>Gehe zu…</strong> Kapiteln, echten PDF-Seiten oder einem Satz, an den du dich erinnerst.',
         '<strong>Lies immer dort weiter, wo du aufgehört hast</strong>, in jedem Buch.'),
  alt_leyendo='Lince beim Lesen: ein einzelnes Wort mit dem markierten Leitbuchstaben', alt_pausa='Lince in der Pause: das Wort, der ganze Absatz und die Steuerung',
  todo_h='Lies, was du willst', todo_p='Du bist an keinen Shop gebunden. Lince liest, was du schon hast und was du findest.',
  tarjetas=(('📚', '150 Klassiker inklusive', '25 auf Deutsch und 125 in 5 weiteren Sprachen: Die Verwandlung, Effi Briest, Der Schimmelreiter, Werther und mehr.'),
            ('📄', 'Deine Bücher', 'Importiere .epub-, .pdf- und .txt-Dateien. Kapitel kommen aus dem Inhaltsverzeichnis, PDFs behalten ihre Seiten.'),
            ('🌐', 'Artikel aus dem Netz', 'Tippe im Browser auf Teilen → Lince, und der Artikel ist bereit zum Lesen, ohne Menüs und Werbung.'),
            ('📋', 'Jeder Text', 'Kopiere eine Notiz, eine lange E-Mail oder einen Bericht und tippe auf dem Startbildschirm auf „Einfügen“.'),
            ('🗂️', 'Deine Online-Bibliothek', 'Verbinde OPDS-Kataloge (Calibre-Web, Kavita und andere), um deine Bücher direkt in der App zu suchen und zu laden.'),
            ('🌎', 'Übe eine Sprache', 'Die App gibt es auf Deutsch, Englisch, Spanisch, Portugiesisch, Französisch und Italienisch, und du kannst die Klassiker in jeder davon lesen.')),
  b2_h='Eine Gewohnheit, die bleibt', b2_p='Jeden Tag ein bisschen zu lesen verändert mehr als einmal viel. Lince hilft dir, dranzubleiben, ohne Druck.',
  b2_li=('Ein Tagesziel in Minuten und eine Serie von Tagen in Folge.', 'Ein Serienschutz pro Woche: Ein schlechter Tag löscht deine Serie nicht.',
         'Punkte, Level und mehr als 40 Abzeichen.', 'Eine Wochenübersicht zum Teilen.', 'Eine Erinnerung, die still bleibt, wenn du dein Ziel schon erreicht hast.'),
  alt_inicio='Startbildschirm von Lince: Serie, Level, Tagesziel und deine Woche', alt_biblioteca='Klassiker-Bibliothek von Lince',
  b3_h='Gemacht für Köpfe, die abschweifen',
  b3_p='Wenn dir Konzentration schwerfällt, wenn du eine Seite liest und nichts behältst oder wenn dich Lesen am Bildschirm ermüdet, passt sich Lince dir an.',
  b3_li=('Schriften, die das Lesen erleichtern: <strong>Lexend</strong>, <strong>Atkinson Hyperlegible</strong> und <strong>OpenDyslexic</strong>.',
         '6 Designs: Fokus (Creme), Hell, Sepia, Dunkelgrau, Nacht (reines Schwarz) und Hoher Kontrast.',
         'Größerer Text, wenn du ihn brauchst, und der Leitbuchstabe in deiner Lieblingsfarbe.', 'Wenn dein Handy den Dunkelmodus nutzt, tut Lince das auch.'),
  alt_grande='Lince mit großer Schrift', alt_capitulos='Gehe zu: Kapitel, Seite oder Satz',
  horiz_h='Auch im Querformat und auf Tablets', horiz_p='Dreh dein Handy für ein größeres Wort, oder nutze Lince auf dem Tablet mit allem im Blick.',
  alt_acostado='Lince auf einem Handy im Querformat, pausiert, mit Absatz und Steuerung nebeneinander',
  alt_tablet='Lince auf einem Tablet, pausiert, mit Absatz und Steuerung nebeneinander',
  b4_h='Schnell, aber mit Verständnis', b4_p='Schnell lesen bringt nichts, wenn du nichts verstehst. Deshalb treibt Lince dich nicht an: Lince misst.',
  b4_li=('Der Tempotest verbindet Wörter pro Minute mit Verständnisfragen, über 5 verschiedene Texte.',
         'Wenn du schnell bist, aber wenig verstehst, sagt Lince es dir ehrlich und schlägt vor, langsamer zu werden.',
         'Nach jeder Sitzung passt „Wie viel hast du verstanden?“ dein empfohlenes Tempo an.'),
  alt_prueba='Ergebnis des Tempotests mit empfohlenem Tempo', alt_prueba_baja='Ergebnis des Tempotests mit dem Vorschlag, für besseres Verständnis langsamer zu lesen',
  ciencia_h='Was die Forschung sagt (ohne Übertreibung)', ciencia_p='Diese Methode heißt RSVP (Rapid Serial Visual Presentation) und wird seit Jahrzehnten erforscht.',
  ciencia=(('Sie hilft bei der Konzentration', 'Mit nur einem Wort auf dem Bildschirm gibt es nichts anderes zu sehen: keine Zeilensprünge, kein versehentliches Zurücklesen, und die Gedanken schweifen seltener ab.'),
           ('Sie hat Grenzen', 'Studien zeigen, dass das Verständnis bei sehr hohem Tempo sinkt. Es gibt keine Zauberabkürzung; deshalb misst Lince, wie viel du verstehst, und verspricht nie „3× schneller lesen“.'),
           ('So funktioniert sie am besten', 'Kurze Sitzungen, Texte, die dich interessieren, und ein angenehmes Tempo, das du Schritt für Schritt erhöhst.')),
  ciencia_nota='Ein gründlicher Überblick: Rayner, Schotter, Masson, Potter &amp; Treiman (2016), „So Much to Read, So Little Time“, <em>Psychological Science in the Public Interest</em>.',
  porque_h='Warum es Lince gibt',
  porque_p='Wir lesen mehr denn je, aber zwischen Benachrichtigungen, Tabs und überladenen Bildschirmen ist es schwer, ein Kapitel zu Ende zu lesen. Lince gibt dem Lesen einen ruhigen Raum: ein Wort, dein Tempo, sonst nichts. Keine Werbung, die stört, kein Verkauf deiner Daten, und kostenlose Klassiker, damit du heute anfangen kannst.',
  planes_h='Preise', planes_p='Du kannst kostenlos lesen, so lange du willst. Lince Plus hebt die Grenzen auf.',
  gratis='Gratis', gratis_li=('Der komplette Leser, alle Designs und Schriften', 'Tempotest, Ziele, Serien und Abzeichen',
       '3 Klassiker gleichzeitig (eins beenden, ein anderes wählen)', '2 importierte Bücher (Dateien oder OPDS-Bibliotheken)', 'Bis zu 10 Seiten pro Tag eingefügter Text oder Artikel'),
  precio_plus='<strong>2,99 US$</strong> pro Monat · 19,99 US$ pro Jahr · 34,99 US$ einmalig',
  plus_li=('Alles aus der Gratisversion', 'Die ganze Klassiker-Bibliothek, ohne Warten', 'Unbegrenzte Importe', 'Kein Tageslimit für eingefügten Text und Artikel', 'Fetter Wortanfang (hebt den Anfang jedes Wortes hervor)'),
  precio_nota='Die Preise können je nach Land variieren; Google Play zeigt dir den Endpreis in deiner Währung.',
  priv_h='Deine Privatsphäre',
  priv=(('🔒', 'Was du liest, gehört dir', 'Deine Texte und dein Fortschritt bleiben auf deinem Handy. Wir laden sie nicht hoch.'),
        ('🚫', 'Ohne Werbung', 'Wir zählen nur anonyme Nutzungsdaten, nie, was du liest, und du kannst sie in den Einstellungen ausschalten.'),
        ('👤', 'Kein Konto zum Lesen', 'Auch nicht, um Plus zu kaufen, oder für dein erstes Buch. Wir fragen erst ab dem zweiten Import.')),
  priv_nota='Details in der <a href="{priv}">Datenschutzerklärung</a>.',
  galeria_h='Lince in Aktion',
  galeria=('Lesen', 'Pause', 'Zu einem Kapitel', 'Dunkles Design', 'Dein Tag und deine Serie', 'Willkommen', '3 Gratisbücher wählen', 'Große Schrift'),
  faq_h='Häufige Fragen',
  faq=(('Ist Lince kostenlos?', 'Ja. Du kannst ohne zu zahlen und ohne Zeitlimit lesen. Lince Plus ist optional und hebt die Grenzen bei Klassikern, Importen und eingefügtem Text auf.'),
       ('Verstehe ich, was ich lese?', 'Genau darum geht es. Du beginnst mit einem angenehmen Tempo, und Lince prüft dein Verständnis mit kurzen Fragen. Mehr Tempo schlägt Lince nur vor, wenn du gut verstehst.'),
       ('Ist es anstrengend, so zu lesen?', 'Am Anfang fühlt es sich anders an. Die Pausen bei Satzzeichen helfen, und du kannst sie in den Einstellungen verlängern. Wir empfehlen kurze Sitzungen von 10 bis 20 Minuten.'),
       ('Hilft es bei ADHS oder Legasthenie?', 'Viele Menschen, die sich leicht ablenken lassen, können sich mit einem Wort nach dem anderen besser konzentrieren, und Lince enthält Schriften wie OpenDyslexic. Es ist aber keine medizinische Behandlung: Probier es aus und behalte, was dir hilft.'),
       ('Funktioniert es offline?', 'Ja. Die 150 Klassiker sind in der App enthalten, und deine importierten Bücher liegen auf deinem Handy. Internet brauchst du nur, um einen Artikel zu laden, eine Online-Bibliothek zu nutzen, dich anzumelden oder Plus zu kaufen.'),
       ('Welche Formate kann ich lesen?', 'EPUB, PDF (mit echtem Text, keine Scans) und TXT, dazu eingefügten Text, Webartikel und OPDS-Kataloge.'),
       ('Gibt es eine iPhone-Version?', 'Im Moment gibt es Lince nur für Android.'),
       ('Wie kündige ich Lince Plus?', 'In Google Play → dein Profil → Zahlungen und Abos → Abos. Der Einmalkauf verlängert sich nicht.')),
  herr_h='Kostenlose Lese-Tools',
  herr=(('prueba', 'Lesegeschwindigkeit testen', 'Finde in 1 Minute heraus, wie viele Wörter pro Minute du liest.'),
        ('tiempo', 'Lesezeit von Büchern', 'Wie lange 25 Klassiker bei deinem Tempo dauern.'),
        ('rsvp', 'Was ist RSVP-Lesen?', 'Wie es funktioniert und was die Forschung sagt.')),
  cierre_h='Deine nächste Seite wartet', cierre_p='Miss dein Tempo in 1 Minute und wähle deine 3 kostenlosen Klassiker.',
  pie=('Tempotest', 'Lesezeit', 'Was ist RSVP?', 'Datenschutz', 'Mein Konto löschen', 'Kontakt')),

 'it': dict(
  title="Lince: app di lettura veloce per Android, una parola alla volta",
  desc="Lince è un'app di lettura veloce per Android: una parola alla volta. Misura la tua velocità e leggi classici, i tuoi EPUB e PDF o articoli. Senza pubblicità.",
  og_title='Lince: lettura veloce e concentrazione', og_desc='Una parola alla volta, sempre nello stesso punto. Leggi di più, distraiti di meno. Senza pubblicità.',
  og_alt="Lince, app di lettura veloce", app_name='Lince: Lettura veloce e concentrazione',
  ld_desc='App di lettura RSVP: mostra una parola alla volta per leggere con concentrazione. Test di velocità, 150 classici in 6 lingue, importazione di EPUB, PDF e TXT, obiettivi e serie.',
  nav=('Come funziona', 'Piani', 'Domande'),
  h1='Leggi di più. <em>Distraiti di meno.</em>',
  bajada="Lince è un'app di lettura veloce che ti mostra una parola alla volta, sempre nello stesso punto. I tuoi occhi non saltano per la pagina e la tua mente resta nella storia.",
  play='Disponibile su Google Play', probar='Provalo qui',
  marcas=('Gratis', 'Senza pubblicità', 'Non vediamo mai cosa leggi', 'Funziona offline'),
  video_alt='Lince che mostra un testo una parola alla volta',
  try_h='Provalo subito, qui',
  try_p='Tocca "Leggi" e guarda solo la lettera evidenziata. Non muovere gli occhi: le parole vengono da te. Ecco come si legge con Lince.',
  demo="Leggere così sembra strano nei primi secondi. Poi, quasi senza accorgertene, smetti di muovere gli occhi e le parole iniziano ad arrivare da sole. La lettera evidenziata resta sempre nello stesso punto, quindi i tuoi occhi non devono mai cercare dove inizia ogni parola. Fai caso anche alle pause: Lince aspetta un po' di più alle virgole, di più ai punti e ancora di più alla fine di un paragrafo, perché ogni idea abbia il tempo di sedimentare. Se qualcosa ti sfugge, tocca lo schermo, guarda tutto il paragrafo e continua da dove vuoi. Prova ad alzare la velocità con il cursore. Fin dove arrivi senza perdere il filo?",
  leer='▶ Leggi', pausa='❚❚ Pausa', otra='↺ Ancora', velocidad='Velocità', ppm_aria='Parole al minuto', ppm='ppm',
  pista="Nell'app vai da 150 a 1.000 parole al minuto e scegli quanto durano le pause.",
  medir='Misura la mia velocità',
  how_h='Come funziona',
  how_p='Quando leggi nel modo solito, gli occhi fanno piccoli salti lungo la riga, tornano indietro e si perdono nella pagina. Lince fa questo lavoro per te: porta ogni parola esattamente dove stai già guardando.',
  pasos=(('Misura la tua velocità', 'Leggi un testo breve per 1 minuto e rispondi a 3 domande. Lince ti dice quante parole al minuto leggi e ti propone una velocità di partenza.'),
         ('Scegli cosa leggere', 'Un classico gratuito, uno dei tuoi libri, un articolo trovato in rete o qualsiasi testo copiato.'),
         ('Leggi e sali di livello', 'Tocca per leggere, tocca per mettere in pausa. Alla fine, una breve domanda verifica che tu abbia capito: Lince propone di andare più veloce solo quando segui davvero.')),
  b1_h='Una parola alla volta, senza perdere niente',
  b1_p="La lettera guida evidenziata resta sempre nello stesso punto. Lince fa pause naturali alle virgole, ai punti e alla fine dei paragrafi. Mentre leggi, la velocità resta sotto la parola: aumentala o diminuiscila senza fermarti.",
  b1_li=('<strong>Metti in pausa per vedere tutto il paragrafo</strong> e tocca una parola qualsiasi per riprendere da lì.',
         '<strong>Vai a…</strong> capitoli, pagine reali del PDF o una frase che ricordi.',
         '<strong>Riprendi sempre da dove eri rimasto</strong>, in ogni libro.'),
  alt_leyendo='Lince in lettura: una sola parola con la lettera guida evidenziata', alt_pausa='Lince in pausa: la parola, tutto il paragrafo e i comandi',
  todo_h='Leggi quello che vuoi', todo_p='Non sei legato a nessuno store. Lince legge quello che hai già e quello che trovi.',
  tarjetas=(('📚', '150 classici inclusi', '25 in italiano e 125 in altre 5 lingue: I promessi sposi, Il fu Mattia Pascal, I Malavoglia, Pinocchio e molti altri.'),
            ('📄', 'I tuoi libri', 'Importa file .epub, .pdf e .txt. I capitoli arrivano dall’indice del libro e i PDF mantengono le loro pagine.'),
            ('🌐', 'Articoli dal web', 'Nel browser tocca Condividi → Lince e l’articolo è pronto da leggere, senza menu né pubblicità.'),
            ('📋', 'Qualsiasi testo', 'Copia una nota, un’email lunga o un documento e tocca "Incolla" nella schermata iniziale.'),
            ('🗂️', 'La tua biblioteca online', 'Collega cataloghi OPDS (Calibre-Web, Kavita e altri) per cercare e scaricare i tuoi libri direttamente nell’app.'),
            ('🌎', 'Esercita una lingua', 'L’app è in italiano, inglese, spagnolo, portoghese, francese e tedesco, e puoi leggere i classici in ognuna di queste lingue.')),
  b2_h="Un'abitudine che resta", b2_p='Leggere un po’ ogni giorno cambia più che leggere tanto una volta. Lince ti aiuta a continuare senza pressione.',
  b2_li=('Un obiettivo giornaliero in minuti e una serie di giorni di fila.', 'Uno scudo a settimana: una giornata storta non cancella la tua serie.',
         'Punti, livelli e più di 40 badge.', 'Un riepilogo settimanale da condividere.', "Un promemoria che tace se hai già raggiunto l'obiettivo."),
  alt_inicio='Home di Lince: serie, livello, obiettivo del giorno e la tua settimana', alt_biblioteca='Biblioteca classica di Lince',
  b3_h='Pensata per le menti che si distraggono',
  b3_p='Se fai fatica a concentrarti, se leggi una pagina e non ricordi niente, o se leggere sullo schermo ti stanca, Lince si adatta a te.',
  b3_li=('Caratteri pensati per leggere meglio: <strong>Lexend</strong>, <strong>Atkinson Hyperlegible</strong> e <strong>OpenDyslexic</strong>.',
         '6 temi: Focus (crema), Chiaro, Seppia, Grigio scuro, Notte (nero puro) e Alto contrasto.',
         'Testo più grande quando ti serve, e la lettera guida del colore che preferisci.', 'Se il tuo telefono usa la modalità scura, anche Lince.'),
  alt_grande='Lince con testo grande', alt_capitulos='Vai a: capitoli, pagina o frase',
  horiz_h='Anche in orizzontale e sui tablet', horiz_p='Gira il telefono per una parola più grande, oppure usa Lince sul tablet con tutto a portata di vista.',
  alt_acostado='Lince su un telefono in orizzontale, in pausa, con il paragrafo e i comandi affiancati',
  alt_tablet='Lince su un tablet, in pausa, con il paragrafo e i comandi affiancati',
  b4_h='Veloce, ma capendo', b4_p='Leggere veloce non serve a niente se non capisci. Per questo Lince non ti spinge ad andare più veloce: misura.',
  b4_li=('Il test di velocità unisce parole al minuto e domande di comprensione, su 5 testi diversi.',
         'Se sei veloce ma capisci poco, Lince te lo dice sinceramente e ti propone di rallentare.',
         'Dopo ogni sessione, "Quanto hai capito?" regola la tua velocità consigliata.'),
  alt_prueba='Risultato del test di velocità con una velocità consigliata', alt_prueba_baja='Risultato del test che consiglia di rallentare per capire meglio',
  ciencia_h='Cosa dice la ricerca (senza esagerare)', ciencia_p='Questo metodo si chiama RSVP (presentazione visiva seriale rapida) ed è studiato da decenni.',
  ciencia=(('Aiuta la concentrazione', "Con una sola parola sullo schermo non c'è nient'altro da guardare: niente salti di riga, niente riletture involontarie, ed è più difficile che la mente si distragga."),
           ('Ha dei limiti', 'Le ricerche mostrano che a velocità molto alte la comprensione cala. Non esiste una scorciatoia magica: per questo Lince misura quanto capisci e non promette mai di "leggere 3 volte più veloce".'),
           ('Funziona meglio così', 'Sessioni brevi, testi che ti interessano e una velocità comoda che aumenti poco a poco.')),
  ciencia_nota='Una rassegna completa: Rayner, Schotter, Masson, Potter &amp; Treiman (2016), "So Much to Read, So Little Time", <em>Psychological Science in the Public Interest</em>.',
  porque_h='Perché esiste Lince',
  porque_p="Leggiamo più che mai, ma tra notifiche, schede e schermi affollati è difficile finire un capitolo. Lince dà alla lettura uno spazio pulito: una parola, il tuo ritmo, nient'altro. Nessuna pubblicità che interrompe, nessuna vendita dei tuoi dati, e classici gratuiti per iniziare oggi stesso.",
  planes_h='Piani', planes_p='Puoi leggere gratis per tutto il tempo che vuoi. Lince Plus toglie i limiti.',
  gratis='Gratis', gratis_li=('Il lettore completo, tutti i temi e i caratteri', 'Test di velocità, obiettivi, serie e badge',
       '3 classici alla volta (finiscine uno e scegline un altro)', '2 libri importati (file o biblioteche OPDS)', 'Fino a 10 pagine al giorno di testo incollato o articoli'),
  precio_plus='<strong>2,99 US$</strong> al mese · 19,99 US$ all’anno · 34,99 US$ una volta',
  plus_li=('Tutto il piano gratuito', 'Tutta la Biblioteca classica, senza aspettare', 'Importazioni illimitate', 'Nessun limite giornaliero di testo incollato e articoli', "Inizio in grassetto (evidenzia l'inizio di ogni parola)"),
  precio_nota='I prezzi possono variare in base al paese; Google Play ti mostra il prezzo finale nella tua valuta.',
  priv_h='La tua privacy',
  priv=(('🔒', 'Quello che leggi è tuo', 'I tuoi testi e i tuoi progressi restano sul telefono. Non li carichiamo.'),
        ('🚫', 'Senza pubblicità', 'Contiamo solo dati di utilizzo anonimi, mai quello che leggi, e puoi disattivarli nelle Impostazioni.'),
        ('👤', 'Nessun account per leggere', 'Né per comprare Plus né per il primo libro. Lo chiediamo solo dalla seconda importazione.')),
  priv_nota="Dettagli nell'<a href=\"{priv}\">informativa sulla privacy</a>.",
  galeria_h='Guardalo in azione',
  galeria=('In lettura', 'In pausa', 'Vai a un capitolo', 'Tema scuro', 'La tua giornata e la tua serie', 'Benvenuto', 'Scegli 3 libri gratis', 'Testo grande'),
  faq_h='Domande frequenti',
  faq=(('Lince è gratis?', 'Sì. Puoi leggere senza pagare e senza limiti di tempo. Lince Plus è facoltativo e toglie i limiti su classici, importazioni e testo incollato.'),
       ('Capirò quello che leggo?', "È proprio questo il punto. Inizi a una velocità comoda e Lince verifica la comprensione con brevi domande. Propone di andare più veloce solo quando capisci bene."),
       ('È faticoso leggere così?', "All'inizio è diverso. Le pause alla punteggiatura aiutano e puoi allungarle nelle Impostazioni. Consigliamo sessioni brevi, da 10 a 20 minuti."),
       ('Aiuta con ADHD o dislessia?', 'Molte persone che si distraggono facilmente trovano più facile concentrarsi con una parola alla volta, e Lince include caratteri come OpenDyslexic. Ma non è una terapia medica: provalo e tieni quello che funziona per te.'),
       ('Funziona offline?', "Sì. I 150 classici sono inclusi nell'app e i libri importati restano sul telefono. Internet serve solo per recuperare un articolo, usare una biblioteca online, accedere o comprare Plus."),
       ('Quali formati posso leggere?', 'EPUB, PDF (con testo vero, non scansioni) e TXT, più testo incollato, articoli web e cataloghi OPDS.'),
       ("C'è una versione per iPhone?", 'Per ora Lince è solo per Android.'),
       ('Come annullo Lince Plus?', "In Google Play → il tuo profilo → Pagamenti e abbonamenti → Abbonamenti. L'acquisto unico non si rinnova.")),
  herr_h='Strumenti di lettura gratuiti',
  herr=(('prueba', 'Test di velocità di lettura', 'Scopri quante parole al minuto leggi in 1 minuto.'),
        ('tiempo', 'Tempo di lettura dei libri', 'Quanto ci vuole per 25 classici alla tua velocità.'),
        ('rsvp', "Cos'è la lettura RSVP?", 'Come funziona e cosa dice la ricerca.')),
  cierre_h='La tua prossima pagina ti aspetta', cierre_p='Misura la tua velocità in 1 minuto e scegli i tuoi 3 classici gratuiti.',
  pie=('Test di velocità', 'Tempo di lettura', "Cos'è RSVP?", 'Privacy', 'Elimina il mio account', 'Contatti')),
}

GALERIA = ('leyendo', 'pausa', 'capitulos', 'oscuro-leyendo', 'inicio', 'bienvenida', 'regalo', 'letra-grande')


def esc(s):
    return html.escape(s, quote=True)


def lista(items, sangria='        '):
    return '\n'.join(f'{sangria}<li>{i}</li>' for i in items)


def captura(lang, nombre, alt, w=540, h=870):
    return f'<img src="/img/{lang}-{nombre}.webp" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy">'


def portada(lang):
    t = T[lang]
    url = RUTAS['inicio'][lang]
    play = lambda camp: PLAY + f'{camp}-{lang}'
    ld_app = {'@context': 'https://schema.org', '@type': 'MobileApplication', 'name': t['app_name'], 'operatingSystem': 'Android',
              'applicationCategory': 'BookApplication', 'inLanguage': [lang] + [l for l in LANGS if l != lang], 'description': t['ld_desc'],
              'url': B + url, 'downloadUrl': 'https://play.google.com/store/apps/details?id=co.com.monsalve.lince',
              'image': 'https://lincereader.com/prensa/img/icono-512.png', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}
    ld_web = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Lince', 'url': B + url, 'inLanguage': lang}
    tarjetas = '\n'.join(f'      <div class="tarjeta"><span class="icono">{i}</span><h3>{h}</h3>\n        <p>{p}</p></div>' for i, h, p in t['tarjetas'])
    pasos = '\n'.join(f'      <div class="paso">\n        <h3>{h}</h3>\n        <p>{p}</p>\n      </div>' for h, p in t['pasos'])
    ciencia = '\n'.join(f'      <div class="tarjeta"><h3>{h}</h3>\n        <p>{p}</p></div>' for h, p in t['ciencia'])
    priv = '\n'.join(f'      <div class="tarjeta"><span class="icono">{i}</span><h3>{h}</h3>\n        <p>{p}</p></div>' for i, h, p in t['priv'])
    galeria = '\n'.join(f'      <figure>{captura(lang, n, "")}<figcaption>{c}</figcaption></figure>' for n, c in zip(GALERIA, t['galeria']))
    faq = '\n'.join(f'    <details><summary>{q}</summary>\n      <p>{a}</p></details>' for q, a in t['faq'])
    herr = '\n'.join(f'      <div class="tarjeta"><h3><a href="{RUTAS[k][lang]}">{h}</a></h3><p>{p}</p></div>' for k, h, p in t['herr'])
    pie = t['pie']
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t['title'])}</title>
<meta name="description" content="{esc(t['desc'])}">
<link rel="canonical" href="{B + url}">
{alternos('inicio')}
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/icono-180.png">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0B0B" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lince">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:title" content="{esc(t['og_title'])}">
<meta property="og:description" content="{esc(t['og_desc'])}">
<meta property="og:url" content="{B + url}">
<meta property="og:image" content="https://lincereader.com/prensa/img/grafico-{lang}.png">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta property="og:image:alt" content="{esc(t['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/estilo.css">
<script type="application/ld+json">
{json.dumps(ld_app, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(ld_web, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
<main class="sitio">
  <header class="barra">
    <a href="{url}" class="logo">L<span>i</span>nce</a>
    <nav>
      <a href="#how" class="secundario">{t['nav'][0]}</a>
      <a href="#plans" class="secundario">{t['nav'][1]}</a>
      <a href="#faq" class="secundario">{t['nav'][2]}</a>
      {menu_idiomas('inicio', lang)}
    </nav>
  </header>

  <div class="portada">
    <div>
      <h1>{t['h1']}</h1>
      <p class="bajada">{t['bajada']}</p>
      <div class="botones">
        <a class="boton" href="{play('inicio')}">
          {PLAY_ICONO}
          {t['play']}
        </a>
        <a class="boton secundario" href="#try">{t['probar']}</a>
      </div>
      <ul class="marcas">
        {''.join(f'<li>{m}</li>' for m in t['marcas'])}
      </ul>
    </div>
    <div class="telefono">
      <video autoplay muted loop playsinline poster="/img/demo-{lang}-poster.jpg" aria-label="{esc(t['video_alt'])}">
        <source src="/img/demo-{lang}.webm" type="video/webm">
        <source src="/img/demo-{lang}.mp4" type="video/mp4">
      </video>
    </div>
  </div>

  <section id="try">
    <h2>{t['try_h']}</h2>
    <p class="intro">{t['try_p']}</p>
    <div class="demo" data-demo data-texto="{esc(t['demo'])}">
      <div class="demo-zona" aria-live="off"><span class="demo-texto"><span class="pre"></span><span class="piv"></span><span class="suf"></span></span></div>
      <div class="demo-controles">
        <button type="button" data-leer="{t['leer']}" data-pausa="{t['pausa']}" data-otra="{t['otra']}">{t['leer']}</button>
        <label>{t['velocidad']} <input type="range" min="150" max="600" step="10" value="300" aria-label="{t['ppm_aria']}"> <span><span class="demo-ppm">300</span> {t['ppm']}</span></label>
      </div>
      <p class="demo-pista">{t['pista']}</p>
    </div>
    <div class="botones" style="margin-top: 20px; justify-content: center;">
      <a class="boton" href="{play('demo')}">{t['play']}</a>
      <a class="boton secundario" href="{RUTAS['prueba'][lang]}">{t['medir']}</a>
    </div>
  </section>

  <section id="how">
    <h2>{t['how_h']}</h2>
    <p class="intro">{t['how_p']}</p>
    <div class="pasos">
{pasos}
    </div>
  </section>

  <section class="bloque">
    <div class="texto">
      <h2>{t['b1_h']}</h2>
      <p>{t['b1_p']}</p>
      <ul>
{lista(t['b1_li'])}
      </ul>
    </div>
    <div class="capturas">
      {captura(lang, 'leyendo', t['alt_leyendo'])}
      {captura(lang, 'pausa', t['alt_pausa'])}
    </div>
  </section>

  <section>
    <h2>{t['todo_h']}</h2>
    <p class="intro">{t['todo_p']}</p>
    <div class="tarjetas">
{tarjetas}
    </div>
  </section>

  <section class="bloque inverso">
    <div class="texto">
      <h2>{t['b2_h']}</h2>
      <p>{t['b2_p']}</p>
      <ul>
{lista(t['b2_li'])}
      </ul>
    </div>
    <div class="capturas">
      {captura(lang, 'inicio', t['alt_inicio'])}
      {captura(lang, 'biblioteca', t['alt_biblioteca'])}
    </div>
  </section>

  <section class="bloque">
    <div class="texto">
      <h2>{t['b3_h']}</h2>
      <p>{t['b3_p']}</p>
      <ul>
{lista(t['b3_li'])}
      </ul>
    </div>
    <div class="capturas">
      {captura(lang, 'letra-grande', t['alt_grande'])}
      {captura(lang, 'capitulos', t['alt_capitulos'])}
    </div>
  </section>

  <section>
    <h2>{t['horiz_h']}</h2>
    <p class="intro">{t['horiz_p']}</p>
    <div class="ancha">{captura(lang, 'acostado-pausa', t['alt_acostado'], 1200, 619)}</div>
  </section>

  <section class="bloque inverso">
    <div class="texto">
      <h2>{t['b4_h']}</h2>
      <p>{t['b4_p']}</p>
      <ul>
{lista(t['b4_li'])}
      </ul>
    </div>
    <div class="capturas">
      {captura(lang, 'prueba', t['alt_prueba'])}
      {captura(lang, 'prueba-baja', t['alt_prueba_baja'])}
    </div>
  </section>

  <section>
    <h2>{t['ciencia_h']}</h2>
    <p class="intro">{t['ciencia_p']}</p>
    <div class="tarjetas">
{ciencia}
    </div>
    <p class="nota">{t['ciencia_nota']}</p>
  </section>

  <section>
    <h2>{t['porque_h']}</h2>
    <p class="intro">{t['porque_p']}</p>
  </section>

  <section id="plans">
    <h2>{t['planes_h']}</h2>
    <p class="intro">{t['planes_p']}</p>
    <div class="planes">
      <div class="plan">
        <h3>{t['gratis']}</h3>
        <p class="precio"><strong>US$0</strong></p>
        <ul>
{lista(t['gratis_li'], '          ')}
        </ul>
      </div>
      <div class="plan destacado">
        <h3>Lince Plus</h3>
        <p class="precio">{t['precio_plus']}</p>
        <ul>
{lista(t['plus_li'], '          ')}
        </ul>
      </div>
    </div>
    <p class="nota">{t['precio_nota']}</p>
  </section>

  <section>
    <h2>{t['priv_h']}</h2>
    <div class="tarjetas">
{priv}
    </div>
    <p class="nota">{t['priv_nota'].replace('{priv}', RUTAS['privacidad'][lang])}</p>
  </section>

  <section>
    <h2>{t['galeria_h']}</h2>
    <div class="galeria-inicio">
{galeria}
    </div>
  </section>

  <section id="faq">
    <h2>{t['faq_h']}</h2>
{faq}
  </section>

  <section id="herramientas">
    <h2>{t['herr_h']}</h2>
    <div class="tarjetas">
{herr}
    </div>
  </section>

  <section class="cierre">
    <h2>{t['cierre_h']}</h2>
    <p class="intro" style="margin: 0 auto 24px;">{t['cierre_p']}</p>
    <div class="botones">
      <a class="boton" href="{play('cierre')}">
        {PLAY_ICONO}
        {t['play']}
      </a>
    </div>
  </section>

  <footer class="pie">
    <span>© 2026 Lince</span>
    <nav>
      <a href="{RUTAS['prueba'][lang]}">{pie[0]}</a>
      <a href="{RUTAS['tiempo'][lang]}">{pie[1]}</a>
      <a href="{RUTAS['rsvp'][lang]}">{pie[2]}</a>
      <a href="{RUTAS['privacidad'][lang]}">{pie[3]}</a>
      <a href="{RUTAS['borrar'][lang]}">{pie[4]}</a>
      <a href="mailto:lince.revision@gmail.com">{pie[5]}</a>
    </nav>
  </footer>
</main>
<script src="/demo.js"></script>
<script src="/idioma.js" defer></script>
<script src="/analitica.js" defer></script>
</body>
</html>
'''


def main():
    for lang in T:
        out = Path(RUTAS['inicio'][lang].strip('/')) / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(portada(lang))
        print('ok', out)


if __name__ == '__main__':
    main()
