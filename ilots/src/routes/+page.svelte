<script>
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import {gsap} from "gsap";
  import {ScrollTrigger} from "gsap/dist/ScrollTrigger";

  import Hero from "./components/Hero.svelte";
  import Title from "./components/Title.svelte";
  import Lenis from '@studio-freight/lenis';
  import Img from "./components/Img.svelte";
  import Quote from "./components/Quote.svelte";
  import LinePlot from "./components/LinePlot.svelte";
  import Select from "./components/Select.svelte";
  import GameCalc from "./components/GameCalc.svelte";
  import Video from "./components/Video.svelte";
  export let data;

  const annot = data.annot.features
  const Lst = data.temp;
  const province = data.provinces
  const mar = data.mar
  const secteur_all = data.secteur_all;

  let width;
  gsap.registerPlugin(ScrollTrigger);

  let colours = ["#1D2E3B", "#E48E50","#1D2E3B", "#3F4460", "#5D627E", "#BCBBD2"]

  onMount(() => {
    //smooth scroll 
    const lenis = new Lenis()

    lenis.on('scroll', (e) => {
    })

    function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    gsap.utils.toArray('.chapitre').forEach((section, i) => {
  
  if(section.getAttribute('data-color') !== null) {
    
    var colorAttr = section.getAttribute('data-color')
    
    gsap.to("body", {
      backgroundColor: colorAttr,
      immediateRender: false,
      scrollTrigger: {
        trigger: section,
        scrub: true,
        start:'top bottom',
        end: '+=150%',
        markers :true,
      }
    });
  }

  })
})
</script>

<svelte:window bind:innerWidth={width}></svelte:window>


  <Hero
  title={"Réchauffement climatique en Belgique :"}
  subtitle={"Comment les températures de nos villes mettent en évidence les inégalités entre les Belges "}
  />

<div class="test">
  <section class="chapeau">
    <div class="wrapper-text test">
      <p><span class="lettrine">L</span>a canicule ? Quelle canicule ? L’été 2023 en Belgique a jusqu’ici été marqué par un temps gris et maussade.
         Avec 21 jours de pluie, ce mois de juillet 2023 a même battu des records historiques bien au-dessus des normales saisonnières. </p>
        <p>Pourtant, même s’il n’en a pas l’air, le réchauffement climatique touche bel et bien notre pays.
        Cette météo qui nous propose “tout ou rien” en est un des indicateurs. Certes, en juillet,
        les pluies et la grisaille ont battu des records historiques. Mais souvenez-vous du mois de juin.
        À ce moment-là, un autre record a été battu : nous n'avions jamais eu aussi chaud à cette période de l’année 
        depuis le relevé des températures dans notre pays en 1833. </p>
        <p>Et que dire de l’été 2022 ? Le mois d’août était alors le plus chaud jamais enregistré dans l’histoire de notre pays.
        Dans ce contexte, une question se pose : notre pays est-il adapté à ces fortes chaleurs
        qui deviendront à l’avenir plus longues, plus fréquentes et plus intenses ? </p>
        <p>Pour le savoir, nous avons croisé des données venues de différentes sources : </p>
        <ul>
          <li>les températures du sol captées par satellite pendant l’été, </li>
          <li>les revenus des Belges</li>
          <li>et la couverture de végétation dans nos régions.</li>
        </ul>
        <p>Verdict: si vous vivez en ville, les plus riches sont les mieux protégés contre les effets des vagues de chaleur. Suivez-nous, on vous explique pourquoi.</p>
      </div>
      <!-- <Quote
      content={"Lorem ipsum dolor sit, amet consectetur adipisicing elit."}
      />
  
      <div class="wrapper-text test">
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.</p>
      </div> -->
  </section>
  
  
  <section class="chapitre" data-color="#E48E50">
    <Title
    content={"Quartiers chauds"}
    index=0
    />
    <div class="wrapper-text">
      <p>Grand-Place de Bruxelles, une chaude journée de juillet. Les températures atteignent des sommets.
        A quelques kilomètres de là, au sud de la capitale, il fait chaud aussi. Mais beaucoup moins que dans le centre-ville. </p>
    <p>En fait, plus on s’écarte du cœur de la cité, plus il fait frais. Une étude publiée en 2018 a montré que “les températures de l’air sont plus élevées de 3°C en moyenne au centre de la Région de Bruxelles-Capitale 
      qu'à ses alentours ruraux en été (sur la période 1987-2016). Les températures les plus élevées s'observent dans de grandes zones au centre-ville urbanisé. Les températures sont légèrement plus basses au-dessus des eaux 
      et dans les grands parcs.” </p>
      <p>Dans le milieu des climatologues et des urbanistes, c’est ce qu’on appelle un phénomène “d’îlot de chaleur urbain” (ICU). “Dans les zones urbaines,
         la chaleur solaire est absorbée par les matériaux de construction, et les bâtiments hauts et denses retiennent cette chaleur et limitent le refroidissement par la circulation du vent. 
         En outre, les zones urbaines sont généralement densément peuplées et produisent de la chaleur, due aux transports et à la climatisation, par exemple”, explique l’institut Royal Météorologique (IRM) sur son site internet. </p>
    </div>
    <Img
    type={"middle"}
    img={["./image/ilots_infographie.png"]}
    />
  </section>
  
  <section class="chapitre" data-color="#1D2E3B">
    <Title
    content={"Un phénomène qui se manifeste la nuit"}
    index=1
    />
    <div class="wrapper-text">
      <p>Mais c'est surtout la nuit que les ICU entrent en action. “C'est un phénomène nocturne et intermittent, explique Yves Richard, professeur de géographie à l'université de Bourgogne, 
        qui étudie la question pour le compte de la ville de Dijon, en France. Il se produit les nuits qui suivent les journées de beau temps et de vent calme. 
        C'est à cause de la propriété des matériaux qui absorbent l'énergie pendant la journée et qui relâchent cette énergie la nuit que ce phénomène peut se déployer.” </p>
    <p>En pratique, à Bruxelles, “à 23h (heure à laquelle l'îlot thermique urbain est normalement le plus prononcé), les différences de température entre le 
      centre de la ville et la campagne environnante avoisinent en moyenne 4,5°C sur la même période", 
      observe l’IRM qui ajoute qu'il y a “en moyenne 3 fois plus de périodes de fortes chaleurs dans le centre de Bruxelles que dans les zones rurales avoisinantes”. </p>
    <p>Rafiq Hamdi, scientifique à l’IRM et spécialiste du sujet relève que “la température entre la ville et la campagne peut monter jusqu’à 8°C de différence la nuit avec un ciel clair et une absence de vent”. </p>
    </div>
    <Img
    type={"inline"}
    img={["./image/GettyImages-1241386865 (1).jpg","./image/GettyImages-1241386865 (1).jpg"]}
    />
  </section>
  
  
  <section class="chapitre" data-color="#3F4460">
    <Title
    content={"Les satellites à la rescousse"}
    index=2
    />
  
    <div class="wrapper-text test">
      <p>Il est difficile de suivre avec précision l’évolution des températures à différents endroits d’une ville au jour le jour.
         Cela nécessiterait de placer des stations météo à des endroits stratégiques. Et plus on a de stations, mieux c’est.  </p>
      <p>Dijon, la capitale de la Bourgogne, dans l’Est de la France, a tenté l’expérience. Aujourd’hui 90 stations mesurent la température de l’air à différents endroits de l’agglomération dijonnaise.
         Objectif de ce projet nommé MUSTARDijon (pour Measuring Urban Systems Temperature Around Dijon) : 
        aider les communes à identifier les zones vulnérables pour agir en conséquence. </p>
      <p>D’autres ressources existent, à commencer par les données satellites. Ce sont celles que nous allons utiliser pour vous emmener au cœur de nos villes.
         De son petit nom “Landsat 8”, ce satellite cartographie la température du sol sur l’ensemble du globe. Certes, la température de l’air serait plus représentative.
          Mais cela donne un aperçu assez fidèle des zones plus chaudes et moins chaudes. Vous allez le voir,
         si on croise ces données avec les revenus fiscaux des Belges et la végétation, les résultats sont pour le moins évocateurs. </p>
    </div>
  
    <div class="wrapper-text test"  data-color="blue">
      <p>Choisissez la ville que vous voulez explorer sur cette carte interactive
      </p>
    </div>
  
    <Select 
      Belgium_geo={province}
      secteurs_geo={secteur_all}
      point_data={Lst}
      annot={annot}
      />
  </section>
  <section class="chapitre" data-color="5D627E">
    <Title
    content={"Analyse Sociologique"}
    index=3
    />
    <div class="wrapper-text test" data-color="light-blue">
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Rerum voluptatem laborum placeat enim adipisci voluptatum! 
        Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
        ratione nobis minima, velit esse ut unde. Lorem ipsum dolor,
        sit amet consctetur adipisicing elit. Ducimus quasi illum 
        omnis maiores sequi fugit soluta, mollitia ipsum esse. 
        Deleniti nesciunt, saepe tempora adipisci possimus commodi 
        inventore provident reprehenderit soluta.</p>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.</p>
    </div>
  
    
    <Quote
    content={"Lorem ipsum dolor sit, amet consectetur adipisicing elit."}/>
  
    <div class="wrapper-text">
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.</p>
    </div>
      <div class="wrapper-text">
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde. Lorem ipsum dolor,
          sit amet consctetur adipisicing elit. Ducimus quasi illum 
          omnis maiores sequi fugit soluta, mollitia ipsum esse. 
          Deleniti nesciunt, saepe tempora adipisci possimus commodi 
          inventore provident reprehenderit soluta.</p>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Rerum voluptatem laborum placeat enim adipisci voluptatum! 
        Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
        ratione nobis minima, velit esse ut unde.</p>
      </div>
  </section>

  
  <section class="chapitre" data-color="#5D627E">
    <Title
    content={"Chaleur et taux de mortalité en hausse"}
    index=4
    />
    <div class="wrapper-text">
      <p>
        Retour à l’été 2022. Cette année-là, Sciensano voit que la courbe de surmortalité grimpe en flèche.
         En clair, on constate davantage de décès qu’en temps normal à cette période. Durant cette période estivale (16 mai au 9 octobre),
         la surmortalité a été importante avec 2312 décès supplémentaires (5,8 % d’excès de mortalité)”, rapporte l’ex-institut de Santé publique. 
      </p>
      <p>
        Sciensano s’était déjà penché sur la question en 2020 avec une analyse des périodes chaudes à Bruxelles et Anvers entre 2002 et 2011.
         Résultat : la mortalité augmente dès que la température dépasse 25,2°C à Anvers ou 22,8°C à Bruxelles. 
      </p>
      <p>
        Cette tendance ne devrait pas aller en s’améliorant. Le réchauffement climatique est tout à fait perceptible en Belgique,
         comme nous l’expliquions déjà dans un grand format publié fin 2020.  
      </p>
    </div>
    
    <Quote
    content={"Pour le moment, on est dix en en avance sur le pire des scénarios"}/>

    <div class="wrapper-text">
      <p>
        “Le scénario le plus probable, c’est une hausse de 3,2°C d’ici à la fin du siècle”, rapporte Xavier Fettweis, climatologue à l’Université de Liège.
         “Ce scénario-là, c’est le minium qu’on va obtenir, le reprend aussitôt son collègue Sébastien Doutreloup. 
         Tout dépend en effet des promesses et des décisions prises au niveau politique. 
      </p>
      <p>
        Xavier Fettweis enchaîne : “Pour le moment, on est dix en en avance [sur le pire des scénarios].
         Rien que sur la dernière décennie 2011-2020, on a gagné un degré en été en Belgique par rapport à la période 1981-2010.
         Et pour ce qui est des inondations de juillet 2021, les modèles suggéraient plutôt que ça arrive en 2030.” 
      </p>
      <p>
        Dans un rapport de 2020 écrit pour le gouvernement fédéral, des chercheurs rappellent que “si le monde continue sur cette tendance de business as usual’,
         près de 30% des jours d’été (donc de juin à août), 
        seront des jours de fortes chaleurs [où la température maximale moyenne sur trois jours dépasse 30°C, ndlr].
         À Liège, la population pourrait être confrontée à 6 à 8 jours de fortes chaleurs sur l’été, contre un1 ou deux2 actuellement.”  
      </p>
      <p>
        Ce même document insiste sur le fait que “les groupes de la société qui sont déjà précaires 
        (les gens en mauvaise santé, avec un revenu faible ou un logement inadapté) 
        sont souvent aussi les plus vulnérables au changement climatique”
      </p>
    </div>
    <div class="flourish-embed flourish-chart" data-src="visualisation/14758903"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
  <!-- <LinePlot
    MAR={mar}/> -->
  </section>
  
   <section class="chapitre" data-color="#BCBBD2">
    <Title
    content={"Savez-vous planter des arbres ?"}
    index=5
    />
    <div class="wrapper-text test" data-color="green">
      <p>Que faire alors ? Changer la ville, répond Yves Richard de l’université de Bourgogne. “Pour déployer des solutions vertes, il faut identifier des espaces. Et dans les espaces publics, 
        ce sont les zones qui sont pour l'instant dédiées à la voirie qui doivent être mobilisées.
         Il faut désimperméabiliser les sols et végétaliser la ville”, expose ce professeur de géographie. 
      </p>
      <p> A l’IRM, on invite aussi à regarder du côté de l’albédo des bâtiments, c’est-à-dire la part des rayonnements solaires qui sont renvoyés vers l'atmosphère.
      "L’albédo des bâtiments pourrait être modifié (en utilisant différents matériaux, des peintures de couleur blanche...) afin que plus de rayonnement solaire soit réfléchi. Une étude récente de 
      l’IRM a montré que cela pourrait réduire l’îlot de chaleur urbain de 0,45°C et rendre la température moins stressante pour les habitants des villes. Quant à la verdure supplémentaire, 
      l’IRM estime qu’elle “pourrait éviter 33% des vagues de chaleur. Et de conclure : “Afin de minimiser l’effet de la ville pendant les vagues de chaleur, une combinaison des deux mesures ci-dessus est recommandée.” 
      </p>
    </div>
    <Video
    type={"big"}
    img={["./image/drone bxl immeubles.mp4",
    "./image/drone bxl immeubles.mp4"
    ]}
      />
    <div class="wrapper-text">
      <p>“Les arbres sont vraiment un paramètre primordial pour rafraichir l’espace. Ils puisent l’eau dans le sol. Et quand il fait chaud ils font comme nous, ils transpirent. C’est l’évaporation de l’eau qui va rafraîichir l’air”, 
        résumait Mirjana Velickovic, project manager chez mkengineering.be, dans un reportage du journal télévisé diffusé en août 2022. </p>
    </div>

    {#if width < 400}
    <Img
    type="big"
    img={["./image/arbres9-16.png"]}
    />
    {:else}
    <Img
    type="big"
    img={["./image/arbres16-9.png"]}
    />
    {/if}

    <div class="wrapper-text">
      <p>Cela ne se fera pas sans quelques changements d’habitudes. Yves Richard invite ainsi à "repenser nos modes de déplacements à l'intérieur de la ville pour consommer moins d'espaces.
         Cela peut passer par le déploiement des transports en commun, la mobilité douce. Il faut aussi donner moins de place à l'automobile. Celle-ci, qu'elle soit électrique ou pas, prend trop de place.”  
      </p>
    </div>
  
    {#if width > 400}
    <GameCalc
    images={["./image/solutions/Horizontal/01-REVETEMENT.png","./image/solutions/Horizontal/02-ISOLATION.png","./image/solutions/Horizontal/03-PELOUSE.png",
    "./image/solutions/Horizontal/04-POINT D EAU.png","./image/solutions/Horizontal/05-TRAFFIC.png","./image/solutions/Horizontal/06-FONTAINES.png","./image/solutions/Horizontal/07-OMBRE.png",
    "./image/solutions/Horizontal/08-ARROSAGE.png","./image/solutions/Horizontal/09-TOITURES.png","./image/solutions/Horizontal/10-TOITURES+FACADES.png",
    "./image/solutions/Horizontal/11-BRUMIFICATEURS.png","./image/solutions/Horizontal/12-ARBRES.png","./image/solutions/Horizontal/00-BASE VILLE.png"]}/> 
   {:else}
   <GameCalc
    images={["./image/solutions/Vertical/01-REVETEMENT.png","./image/solutions/Vertical/02-ISOLATION.png","./image/solutions/Vertical/03-PELOUSE.png",
    "./image/solutions/Vertical/04-POINT D EAU.png","./image/solutions/Vertical/05-TRAFFIC.png","./image/solutions/Vertical/06-FONTAINES.png","./image/solutions/Vertical/07-OMBRE.png",
    "./image/solutions/Vertical/08-ARROSAGE.png","./image/solutions/Vertical/09-TOITURES.png","./image/solutions/Vertical/10-TOITURES+FACADES.png",
    "./image/solutions/Vertical/11-BRUMIFICATEURS.png","./image/solutions/Vertical/12-ARBRES.png","./image/solutions/Vertical/00-BASE VILLE.png"]}/> 
    {/if}


  </section>
</div>
<div class="wrapper">
<p>
  Pour régler les défis de demain, mieux vaut agir dès aujourd’hui. En Belgique, certaines villes s’organisent.
   C’est le cas à Liège avec le plan Canopée. “À Liège, nous constatons que la superficie totale de canopée d’arbres s’élève à 2.156 hectares (répartis à 60% en espace public et à 40% en espace privé),
    soit 31,4%, du territoire communal”,
   écrit la ville sur son site internet.  
</p>
</div>


<style>
@import url('https://fonts.googleapis.com/css2?family=Baskervville&family=Montserrat:wght@200;400;500&display=swap');
/* .wrapper {
        max-width: 100rem;
        margin-inline: auto;
    } */

  :root {
    --dark-color:#1D2E3C;
    --dark-blue:#144265;
    --middle-blue:#6391B4;
    --light-blue:#BCE1FE;
    --redish:#DC351F;
    --light-orange:#D66819;
    --dark-orange:#DA4D1A;
    --green-color:#728A63;

    --font-size-sm: clamp(0.7rem, 0.35vw + 0.61rem, 0.89rem);
    --font-size-base: clamp(0.88rem, 0.57vw + 0.73rem, 1.19rem);
    --font-size-md: clamp(1.09rem, 0.89vw + 0.87rem, 1.58rem);
    --font-size-lg: clamp(1.37rem, 1.35vw + 1.03rem, 2.11rem);
    --font-size-xl: clamp(1.71rem, 2.01vw + 1.21rem, 2.81rem);
    --font-size-xxl: clamp(2.14rem, 2.93vw + 1.4rem, 3.75rem);
    --font-size-xxxl: clamp(2.67rem, 4.23vw + 1.61rem, 5rem);

    --font-title:'Baskervville', serif;
  }

  :global(body) {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    background-color: var(--dark-color);
}
  /* :global(div) {
    border: 2px solid red;
  } */

  :global(h1) {
    margin-block:0;
  }

  .chapeau{
    backdrop-filter: blur(3rem);
  }

  .wrapper-text {
        max-width: 90rch;
        margin-inline: auto;
        margin-block: 2rem;
        line-height: 1.7rem;
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 500;
        padding-inline: 1rem;
    }
   .lettrine{
      float: left;
      font-size: var(--font-size-xxxl);
      padding-right: 0.5rem;
      line-height: 80%; 
      margin:-.1em 0px;
   }


    section {
      margin-block: 0;
      padding-block: 2rem;
    }
</style>
