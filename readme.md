<h1 align="center"> scrolly-telling sur les ilots de chaleur en belgique</h1>
<h3 align="center">  Explication de la méthodologie employée pour réaliser <a href="">l'article</a> (lien actif lorsque le projet sera publié) sur les ilots de chaleur en Belgique </h3>

<p align="center"> 
  <img src="/assets/map_second.png" alt="image représentative du projet (graphique montrant les ilot de chaleur dans les principales villes de belgiques)" width="25%">
</p>

<h2 id="table-of-contents"> :book: Contenu</h2>

<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li><a href="#Description"> ➤ Description</a></li>
    <li><a href="#themes"> ➤ thèmes techniques abordés</a></li>
    <li><a href="#etapes"> ➤Etapes du projet</a></li>
    <ul>
        <li><a href="#recolte"> Récolte de données</a></li>
        <li><a href="#transformation">Transformation des données(jongler avec les formats cryptiques)</a></li>
        <li><a href="#web">Web dev</a></li>
      </ul>
    <li><a href="#structure"> ➤ Structure du projet</a></li>
    <li><a href="#installation"> ➤ Installation</a></li>
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
<h2 id="etapes"> :dart: Etapes du projet</h2>
   <p align="center"> 
  <img src="assets\diagramme_transfo.png" alt="diagramme des étapes de transformation de données du projet" width="75%">
</p>
    <h3 id="recolte"> Récoltes des données</h3>
        <p align="justify">  
        Lien des sites où on a trouvé les infos (statbel, geoportail, gee) <br>
        :radio_button: <a href="\récolte-data\Landsat-NASA.md">Données satelitaires LST</a><br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-7">Geojson secteurs statistiques</a><br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-7">Données de densité par secteur stat</a><br>
        :radio_button: <a href="https://statbel.fgov.be/fr/open-data/statistique-fiscale-des-revenus-par-secteur-statistique">Données de revenus par secteur stat</a><br>
        :radio_button: <a href="https://geoportail.wallonie.be/catalogue/47b348f1-6e7a-4baa-963c-0232a43c0cff.html">Donnée d'occupation du sol</a>(il faut demander l'accès)<br>
        </p>
    <h3 id="transformation"> Transformation des données </h3>
        <p align="justify"> 
        Utilisation du script nasa pour récolter les geotif utiles pour nos zones de recherches -> <a href="récolte-data\1-Landsat-NASA.md"> ce md file</a> <br>
        Transformation des fichiers geotif en centroid -> <a href="récolte-data\2-centroid-temperature.ipynb.ipynb"> ce notebook</a> <br>
        Extraire les centroid de température qui ne sont pas dans les secteurs statistisques -> <a href="récolte-data\2-centroid-temperature.ipynb.ipynb"> ce notebook</a>  <br>
        Sélection des polygones des villes qui nous interessent -> <a href="récolte-data\3-commune_secteur.ipynb"> ce notebook</a> <br>
        Rassembler les données de densité de population avec les données de revenus dans un geojson des secteurs statistiques -> <a href="récolte-data\4-Densite_revenu_added.ipynb"> ce notebook</a> <br>
        </p>
    <h3 id="web"> Web dev</h3>
        <p align="justify"> 
        </p>


<h2 id="structure"> :file_folder: Structure du projet</h2>
    <p align="justify"> 
    1. <b>/récolte-data</b> -> fichier contenant les différentes étapes de transformation et assemblage de data</br>
    </p>

<h2 id="inspirations"> :repeat: Inspirations</h2>
    <p align="justify"> 
    :radio_button: <a href="https://ici.radio-canada.ca/info/2022/07/ilots-chaleur-villes-inegalites-injustice-changements-climatiques/en"> grand format ilot de chaleur radio canada </a><br>
    :radio_button: <a href="https://www.theguardian.com/environment/ng-interactive/2021/oct/14/climate-change-happening-now-stats-graphs-maps-cop26"> climat the guardian</a><br>
    :radio_button: <a href="https://www.srf.ch/news/schweiz/ungleichheit-in-den-staedten-hitzeinseln-treffen-aermere-staerke"> srf </a><br>
    </p>

<h2 id="Results-and-discussion"> :pushpin: Resultats et discussions</h2>
   
<h2 id="installation"> :repeat: Installation</h2>
    <p align="justify"> 
    </p>

<h2 id="Timeline"> :calendar: Timeline</h2>
    <p align="justify"> 
    récolte des données: du 17/07/23 au 21/07/23
    </p>

<h2 id="Contributors"> :raising_hand: Contributors</h2>
    <p>Héloïse feldmann <a href="https://github.com/Yheloww">  Github account</a></p>