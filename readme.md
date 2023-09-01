<h1 align="center"> scrolly-telling sur les ilots de chaleur en belgique</h1>
<h3 align="center">  Explication de la méthodologie employée pour réaliser <a href="https://www.rtbf.be/article/rechauffement-climatique-en-belgique-les-pauvres-au-chaud-les-riches-au-frais-grand-format-11243914">l'article</a> sur les ilots de chaleur en Belgique </h3>

<p align="center"> 
  <img src="assets\map_second.png" alt="image représentative du projet (graphique montrant les ilot de chaleur dans les principales villes de belgiques)" width="25%">
</p>

<h2 id="table-of-contents"> :book: Contenu</h2>

<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li><a href="#Description"> ➤ Description</a></li>
    <li><a href="#themes"> ➤ thèmes techniques abordés</a></li>
    <li><a href="#installation"> ➤ Installation</a></li>
    <li><a href="#etapes"> ➤Etapes du projet</a></li>
    <ul>
        <li><a href="#recolte"> Récolte de données</a></li>
        <li><a href="#transformation">Transformation des données(jongler avec les formats cryptiques)</a></li>
        <li><a href="#web">Web dev</a></li>
      </ul>
    <li><a href="#structure"> ➤ Structure du projet</a></li>
    <!-- <li><a href="#usage"> ➤ Usage</a></li> -->
    <li><a href="#Results-and-discussion"> ➤ Résultats et discussion(réusabilité)</a></li>
    <!-- <li><a href="#Visuals"> ➤ Visuals</a></li> -->
    <!--<li><a href="#experiments">Experiments</a></li>-->
    <li><a href="#inspirations"> ➤ Inspirations</a></li>
    <li><a href="#Timeline"> ➤ Timeline</a></li>
    <li><a href="#contributors"> ➤ Contributors</a></li>
  </ol>
</details>

<h2 id="Description"> :memo: Description</h2>
    <p align="justify"> 
    Ce repo est un repo de recherches et de documentation de méthodologie de data journalisme, il est le premier d'une série de projets réalisés à la RTBF par Decrypte. Il a pour but de poser des bases pour une méthodologie plus complète à l'avenir. Ici le thème c'est les ilots de chaleur dans les grandes villes wallonne, comment ces différences de température se traduisent-elles dans les revenus de la population et sa densité ? Comment les espaces verts influencent-ils les ilots dans ces villes belges ? Qu'est-ce qu'un ilot de chaleur ?+ offre de solutions et reportage sur place pour impliquer le lecteur.</p>

<h2 id="themes"> :dart: Thèmes techniques abordés</h2>
    <p align="justify">  
     :radio_button: Récolte de données satellitaire en utilisant <a href="https://earthengine.google.com/">Google Earth Engine</a></br>
     :radio_button: Gestion de formats geospatiaux dans python (geotif, geojson)</br>
     :radio_button: Creation de cartes en utilisant D3</br>
     :radio_button: plus</br>
    </p>

<h2 id="installation"> :repeat: Installation</h2>
    <p align="justify"> Les étapes d'installations se trouvent dans le <a href="setup.md">setup.md</a> </p>

<h2 id="etapes"> :dart: Etapes du projet</h2>
   <p align="center"> 
  <img src="assets\diagramme_transfo.png" alt="diagramme des étapes de transformation de données du projet" width="75%">
</p>
    <h3 id="recolte"> Récoltes des données</h3>
        <p align="justify">  
        Lien des sites où on a trouvé les infos (statbel, geoportail, gee) <br>
        :radio_button: <a href="\récolte-data\Landsat-NASA.md">Données satelitaires LST</a> les geotiffs des villes sont dans le folder /assets<br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-7">Geojson secteurs statistiques</a><br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-7">Données de densité par secteur stat</a><br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/statistique-fiscale-des-revenus-par-secteur-statistique">Données de revenus par secteur stat</a><br>
        :radio_button: <a href="https://geoportail.wallonie.be/catalogue/47b348f1-6e7a-4baa-963c-0232a43c0cff.html">Donnée d'occupation du sol</a> (il faut demander l'accès, je les ai inclues dans le /assets folder pour plus de facilités)<br>
        </p>
    <h3 id="transformation"> Transformation des données </h3>
        <p align="justify"> Pour effectuer la transformation des données il vous suffit de run <a href="./python_scripts/main.py">main.py </a>(! il vous faut 3 fichiers de datas qui sont spécifiés dans les commentaires du script!)</p>
        <p align="justify"> Si le process complet vous intéresse il y a quelques explications aux niveau des notebooks ( ! ils n'ont pas encore été nettoyés ! )
    <h3 id="web"> Web dev</h3>
        <p align="justify"> Le developpement de la page interactive à été réalisé en svelte via <a href="">sveltekit</a> et ensuite déployée sur <a href="">Vercel</a>. Si vous avez de suggestions pour améliorer les performances du code sur le web n'hésitez pas ! 
        </p>
        <p align="justify">Attention les données sont fetch dans <a href="./ilots/src/routes/+page.js">page.js</a> à partir de github gists de mon profils, si vous voulez fetch vos propres liens changez les</p>


<h2 id="structure"> :file_folder: Structure du projet</h2>
    <p align="justify"> 
    1. <b>/récolte-data</b> -> dossier contenant les notebooks des expérimentations et plus d'explications du process</br>
    1. <b>/assets</b> -> dossier contenant les différents assets dont certaines sources de data tels que les géotifs et les geojson avec le pourcentage de verdure</br>
    1. <b>/python_scripts</b> -> dossier contenant les scripts pour nettoyer et merger les différentes sources de data</br>
    1. <b>/ilots</b> -> dossier content le code sveltekit de la partie web development</br>
    </p>

<h2 id="inspirations"> :repeat: Inspirations</h2>
    <p align="justify"> 
    :radio_button: <a href="https://ici.radio-canada.ca/info/2022/07/ilots-chaleur-villes-inegalites-injustice-changements-climatiques/en"> grand format ilot de chaleur radio canada </a><br>
    :radio_button: <a href="https://www.theguardian.com/environment/ng-interactive/2021/oct/14/climate-change-happening-now-stats-graphs-maps-cop26"> climat the guardian</a><br>
    :radio_button: <a href="https://www.srf.ch/news/schweiz/ungleichheit-in-den-staedten-hitzeinseln-treffen-aermere-staerke"> srf </a><br>
    </p>

<h2 id="Results-and-discussion"> :pushpin: Résultats</h2>
<p align="justify">Quelques images du projet</p>
<p align="center"> 
  <img src="assets\hero.png" alt="hero du projet" width="50%">
</p>
<p align="center"> 
  <img src="assets\carte_interactive.png" alt="carte intéractive" width="50%">
</p>
<p align="center"> 
  <img src="assets\carte_lst.pgn.png" alt="carte ville" width="50%">
</p>
<p align="center"> 
  <img src="assets\graphe.png" alt="graphique température vs revenu" width="50%">
</p>
   

<h2 id="Timeline"> :calendar: Timeline</h2>
    <p align="justify"> 
    récolte des données: du 17/07/23 au 28/07/23
    dev web: du 28/07/23 au 23/08/23
    </p>

<h2 id="Contributors"> :raising_hand: Contributors</h2>
    <p>Héloïse feldmann <a href="https://github.com/Yheloww">Github account</a></p>
    <p>Ambroise Carton <a href="https://github.com/amcaw">Github account</a></p>
    <p>Sébastien Barbieri <a href="https://github.com/scips">Github account</a></p>