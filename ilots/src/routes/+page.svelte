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
  import Select from "./components/Select.svelte";
  import GameCalc from "./components/GameCalc.svelte";
  import Video from "./components/Video.svelte";
  import Navbar from "./components/navbar.svelte";
  export let data;

  const annot = data.annot.features
  const Lst = data.temp;
  const province = data.provinces
  const mar = data.mar
  const secteur_all = data.secteur_all;

  let width;
  let height;
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

    gsap.to("body", {
      backgroundColor: "#D66819",
      immediateRender: false,
      scrollTrigger: {
        trigger: "#quartiers",
        scrub: true,
        start:'top bottom',
        end: '+=100%',
      }
    })
    gsap.fromTo("body", {
      backgroundColor: "#D66819",
      immediateRender: false,
      scrollTrigger: {
        trigger: "#nuit",
        scrub: true,
        start:'top center',
        end: '+=100%',
      }},
      {
      backgroundColor: "#1D2E3C",
      immediateRender: false,
      scrollTrigger: {
        trigger: "#nuit",
        scrub: true,
        start:'top bottom',
        end: '+=100%',
      }
    })
})

</script>

<svelte:window bind:innerHeight={height} bind:innerWidth={width}></svelte:window>

<Navbar/>

<Hero
title={"Réchauffement climatique en Belgique :"}
subtitle={"Comment les températures de nos villes mettent en évidence les inégalités entre les Belges "}
/>

<div class="test">
  <section class="chapeau">
    <div class="wrapper-text test">
      <p><span class="lettrine">N</span>ous sommes en train de vivre le septième été le plus chaud de l'histoire de la Belgique depuis l’enregistrement des températures en 1833.
         Avec un record : <a href='https://www.rtbf.be/article/climat-en-belgique-les-records-du-mois-de-juin-2023-tres-chaud-et-ensoleille-11221832' target='_blank' rel=noreferrer>celui du mois de juin</a>, le plus ardent de tous. Et que dire de l’été 2022&nbsp;?
         <a href='https://www.rtbf.be/article/climat-en-belgique-les-records-de-lete-meteorologique-2022-11058042' target='_blank' rel=noreferrer>Le mois d’août de cette année-là</a> dépassait également tous les relevés. De record en record, 
          une question se pose : notre pays est-il adapté à ces fortes chaleurs qui deviendront à l’avenir plus longues, plus fréquentes et plus intenses&nbsp;?
           Qui paye le prix de ce changement climatique indiscutable&nbsp;? </p>

        <p>Pour le savoir, nous avons croisé des données venues de différentes sources : </p>
        <ul>
          <li>les températures du sol captées par satellite pendant l’été&nbsp;; </li>
          <li>les revenus des Belges&nbsp;;</li>
          <li>et la couverture en végétation dans nos régions.</li>
        </ul>
        <p>Verdict&nbsp;: en ville, les plus riches ont tendance à être mieux protégés contre les effets des vagues de chaleur. 
          <b>Suivez-nous, on vous explique pourquoi</b>.</p>
      </div>
  </section>
  
  
  <section class="chapitre" data-color="#E48E50" id="quartiers">
    <Title
    content={"Quartiers chauds"}
    index=0
    />
    <div class="wrapper-text">
      <p>Laeken, au nord de Bruxelles, une chaude journée de juin 2023. 
        Il est midi et il fait 31°C. À quelques kilomètres de là, à Zaventem, il fait chaud aussi. Mais un peu moins que dans la ville&nbsp;: 29°C «&nbsp;seulement&nbsp;». </p>
    <p>En fait, plus on s’écarte du cœur de la capitale, plus il fait frais. <a style="color:#1D2E3C;" href='https://environnement.brussels/citoyen/outils-et-donnees/etat-des-lieux-de-lenvironnement/climat-etat-des-lieux#cartographie-des-ilots-de-fraicheur-bruxelles' target='_blank' rel=noreferrer>Une étude publiée en 2018</a> a montré que «&nbsp;<i>les températures de l’air sont plus élevées de 3°C 
      en moyenne au centre de la Région de Bruxelles-Capitale qu'à ses alentours ruraux en été (sur la période 1987-2016). Les températures les plus élevées 
      s'observent dans de grandes zones au centre-ville urbanisé.
       Les températures sont légèrement plus basses au-dessus des eaux et dans les grands parcs.</i>&nbsp;» </p>
    </div>
    <Img
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/1.webp","https://rtbfmedia.be/rtbfinfo/ICU_pics/2.webp"]}
    legend={["Rafraîchissement dans l’eau d’une fontaine sur la place Flagey, à Bruxelles, le 24 juillet 2019. Crédit: Thierry Monasse, Getty images","À Namur, un côté de la Sambre est plus chaud que l’autre. Ceux qui vivent sur les coteaux verts de la Citadelle sont bien plus au frais que ceux qui vivent dans le centre-ville. Crédit: Santiago Urquijo – Getty images"]}
    alt={["Rafraîchissement dans l’eau d’une fontaine sur la place Flagey, à Bruxelles, le 24 juillet 2019. Crédit: Thierry Monasse, Getty images","À Namur, un côté de la Sambre est plus chaud que l’autre. Ceux qui vivent sur les coteaux verts de la Citadelle sont bien plus au frais que ceux qui vivent dans le centre-ville. Crédit: Santiago Urquijo – Getty images"]}
    />
    <div class="wrapper-text">
      <p>Dans le milieu des climatologues et des urbanistes, c’est ce qu’on appelle un phénomène d’îlot de chaleur urbain (ICU).
         «&nbsp;<i>Dans les zones urbaines, la chaleur solaire est absorbée par les matériaux de construction, et les bâtiments hauts et denses retiennent cette chaleur 
         et limitent le refroidissement par la circulation du vent. En outre, les zones urbaines sont généralement densément peuplées et produisent de la chaleur,
         due aux transports et à la climatisation, par exemple</i>&nbsp;», <a style="color:#1D2E3C;" href='https://www.meteo.be/fr/infos/actualite/les-toits-blancs-et-les-arbres-aident-les-citadins-durant-les-periodes-de-chaleur' target='_blank' rel=noreferrer>explique l’Institut Royal Météorologique (IRM) sur son site internet.</a></p>
    </div>
    <Img
    type={"middle-transparent"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/ilots_expliques.webp"]}
    legend={["Quentin Vanhoof d’après Earth Resources Observation and Science (EROS) Center"]}
    alt={["Quentin Vanhoof d’après Earth Resources Observation and Science (EROS) Center"]}
    />
  </section>
  
  <section class="chapitre" data-color="#1D2E3B">
    <Title
    content={"Un phénomène qui se manifeste la nuit"}
    index=1
    />
    <div class="wrapper-text" id="nuit">
      <p>Mais c'est surtout la nuit que les ICU entrent en action. «&nbsp;<i>C'est un phénomène nocturne et intermittent.
         Il se produit les nuits qui suivent les journées de beau temps et de vent calme</i>&nbsp;», détaille Yves Richard, professeur de géographie à l'université de Bourgogne.</p>
    <p>Celui qui étudie la question pour le compte de la ville de Dijon, en France, précise&nbsp;:
      «&nbsp;<i>C'est à cause de la propriété des matériaux qui absorbent l'énergie pendant la journée et qui relâchent cette énergie la nuit que ce phénomène peut se déployer.</i>&nbsp;» </p>
    </div>
    <Img
    type={"inline"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/3.webp"]}
    legend={["Une fois la nuit tombée, le phénomène d’îlot de chaleur se fait d’autant plus ressentir. Crédit: Marie-Laure Mathot, RTBF"]}
    alt={["Une fois la nuit tombée, le phénomène d’îlot de chaleur se fait d’autant plus ressentir. Crédit: Marie-Laure Mathot, RTBF"]}
    />
    <div class="wrapper-text">
      <p>En pratique, à Bruxelles, «&nbsp;<i>à 23h (heure à laquelle l'îlot thermique urbain est normalement le plus prononcé), 
        les différences de température entre le centre de la ville et la campagne environnante avoisinent en moyenne 4,5°C [sur la période 1987-2016]</i>&nbsp;»,
         observe l’IRM. L'Institut belge de météorologie ajoute qu'il y a «&nbsp;<i>en moyenne trois fois plus de périodes de fortes chaleurs dans 
         le centre de Bruxelles que dans les zones rurales avoisinantes</i>&nbsp;». </p>
    <p>Rafiq Hamdi, scientifique à l’IRM et spécialiste du sujet, relève que «&nbsp;<i>la température entre la ville et 
      la campagne peut monter jusqu’à 8°C de différence la nuit avec un ciel clair et une absence de vent</i>&nbsp;». Cette différence, les Bruxellois ont par exemple pu la constater lors des fortes chaleurs à la fin du mois de juin dernier, comme le montre le graphique ci-dessous. </p>
    </div>
    <div class="wrapper-plot">
      <iframe src='https://flo.uri.sh/story/2009134/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/story/2009134/?utm_source=embed&utm_campaign=story/2009134' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    </div>
  </section>
  
  
  <section class="chapitre">
    <Title
    content={"Les satellites à la rescousse"}
    index=2
    />
  
    <div class="wrapper-text test">
      <p>Il est difficile de suivre avec précision l’évolution des températures à différents endroits d’une ville au jour le jour.
         Cela nécessiterait de placer des stations météo à des endroits stratégiques. Et plus on a de stations, mieux c’est.  </p>
      <p>Dijon, la capitale de la Bourgogne, a tenté l’expérience. Aujourd’hui 90 stations mesurent la température de l’air à différents endroits de l’agglomération dijonnaise.
         Objectif de ce projet <a href='https://popsu-dijon.u-bourgogne.fr/wp-content/uploads/2019/12/MustarDijon.pdf' target='_blank' rel=noreferrer>bien nommé MUSTARDijon</a> (pour Measuring Urban Systems Temperature Around Dijon)&nbsp;: 
        aider les communes à identifier les zones vulnérables pour agir en conséquence. </p>
      </div>
        <Img
        type={"middle"}
        img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/4.webp"]}
        legend={["Le palais des ducs et des états de Bourgogne à Dijon, une ville où les îlots de chaleur sont étudiés de près. Crédit: Getty images "]}
        alt={["Le palais des ducs et des états de Bourgogne à Dijon, une ville où les îlots de chaleur sont étudiés de près. Crédit: Getty images "]}
        />
      <div class="wrapper-text">
        <p>D’autres ressources, venues de l'espace celles-là, se révèlent bien utiles. C'est le cas des données récoltées par Landsat 8, un outil d'observation de la Terre lancé par la NASA en 2013. Grâce à ce satellite dont nous avons récupéré des milliers de données, nous allons vous emmener au cœur de nos villes.</p>
        <p>Certes, la température de l’air serait plus représentative. Mais Landsat nous donne quand même un aperçu assez fidèle des zones plus chaudes et moins chaudes (voir notre méthodologie à la fin de l’article).
          Vous allez le voir, si on croise ces données avec les revenus fiscaux des Belges et la végétation, les résultats mettent en lumière des inégalités. </p>
          <p><b>Cliquez sur une ville en bleu clair sur la carte ci-dessous puis scrollez directement vers le bas pour découvrir ses particularités en détails.</b></p>
      </div>
      

    <Select 
      Belgium_geo={province}
      secteurs_geo={secteur_all}
      point_data={Lst}
      annot={annot}
      />
  </section>

  <section class="chapitre">
    <Title
    content={"Inégaux face au réchauffement climatique"}
    index=3
    />
    <div class="wrapper-text test" data-color="light-blue">
      <p>Nous ne sommes donc pas tous égaux face au changement climatique. C'est aussi l'analyse que fait Yves Richard à Dijon. «&nbsp;<i>Il existe des inégalités de vulnérabilité,
         surtout quand on regarde l’air intérieur des habitations. Si j’habite un pavillon avec jardin et que je peux ouvrir mes fenêtres la nuit quand je dors, je bénéficie de la fraîcheur de l’air extérieur, surtout si mon appartement est traversant [c'est-à-dire qu'il dispose d'ouvertures vitrées sur au moins deux façades d'orientation différente, ndlr]. Si, au contraire, j’habite dans un immeuble qui n'est pas 
          traversant, qui est dans une zone bruyante, où il y a de l'insécurité, alors, je vais avoir du mal à rafraîchir mon appartement la nuit.
         Et c'est là où il y a une grande inégalité.</i>&nbsp;» </p>
    <p>Chloé Salembier, ethnologue et professeur à la faculté d’architecture à l’UCLouvain, parle d’injustice spatiale.
       «&nbsp;<i>C’est le fait que les rapports sociaux soient inscrits dans le territoire</i>&nbsp;», définit-elle. «&nbsp;<i>Les êtres humains organisent leur territoire et le territoire 
       produit des pratiques en retour.</i>&nbsp;»
      C’est donc la façon dont nous avons construit nos villes qui a contribué, plus d’un siècle plus tard, à ces vulnérabilités face au changement climatique.</p>
      <p>Des habitants touchés différemment par un phénomène climatique extrême, ça ne vous rappelle rien ? 2021,
         les inondations dans la vallée de la Vesdre bien sûr. «&nbsp;<i>Verviers, par son histoire autour de l’industrie textile, avait une population ouvrière 
         dans le bas de la ville, le long de la Vesdre, proche des usines</i>, contextualise Alain Malherbe, historien de l’art et urbaniste, chargé de cours à l’UCLouvain. <i>Cela s’est construit en grande partie au moment de l’industrialisation, dès le milieu du XIX<sup style="line-height: 1;">e</sup> siècle... même si la Belgique a connu, par son fonctionnement et sa mobilité, une classe ouvrière qui s’est répartie de manière plus diffuse</i>&nbsp;», nuance-t-il.  
      </p>
    </div>

    <Img
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/5.webp","https://rtbfmedia.be/rtbfinfo/ICU_pics/6.webp"]}
    legend={["Le quartier de Prés-Javais, à Verviers est particulièrement vulnérable aux phénomènes climatiques extrêmes. Crédit: Marie-Laure Mathot, RTBF","Au contraire, dans un quartier plus riche et vert comme ceux situés sur les coteaux de la Citadelle à Liège, les températures au sol sont beaucoup moins élevées lors des canicules. Crédit: Getty images"]}
    alt={["Le quartier de Prés-Javais, à Verviers est particulièrement vulnérable aux phénomènes climatiques extrêmes. Crédit: Marie-Laure Mathot, RTBF","Au contraire, dans un quartier plus riche et vert comme ceux situés sur les coteaux de la Citadelle à Liège, les températures au sol sont beaucoup moins élevées lors des canicules. Crédit: Getty images"]}
    />

    <div class="wrapper-text">
    <p>Néanmoins, «&nbsp;<i>la vallée de la Vesdre s’est construite avec une population très précaire dès l’industrialisation.
       La bourgeoisie, elle, occupe les coteaux, du côté de Heusy avec de grandes villas ou des maisons avec jardin.
       Il existe des écarts de revenus importants entre ces deux types de population. Les conditions socio-économiques sont aussi très différentes.</i>&nbsp;» </p>
    </div>
      <div class="wrapper-text">
        <p>Des extrêmes encore visibles à Verviers. Dans un quartier en bord de Vesdre comme Hodimont, le revenu médian était de 16.193 &nbsp;€ par an en 2020.
           C’est beaucoup moins que le revenu médian wallon (24.808 &nbsp;€ par an) et quasiment la moitié de celui du quartier d’Heusy, situé sur les hauteurs, 
           avec 31.234 &nbsp;€ par an. Les quartiers les moins nantis sont donc ceux qui subissent le plus les effets du changement climatique&nbsp;: fortes chaleurs et inondations,
            souligne Hélène Ancion, chargée de mission en aménagement du territoire et urbanisme pour Canopea,
           la fédération des associations environnementales belges qui défend l'environnement en Wallonie et en Belgique. </p>
      <p>Ces constats sont valables pour d’autres villes&nbsp;: les sols ont été imperméabilisés là où les industries se sont implantées au XIXe siècle.
         Et c’est là que l’on retrouve les logements, autrefois d’ouvriers, aujourd’hui, des plus précarisés. À Liège, en zone inondable, la part de la population
          qui présente un niveau socio-économique très faible s’élève à 37% contre 29 % en moyenne dans la population wallonne,
         soit près de 30% en plus de personnes socio-économiquement défavorisées en zone inondable, selon l’ISSEP, l’Institut scientifique de service public. </p>
        <p>Ce sont des inégalités environnementales pour Hélène Ancion. «&nbsp;<i>Les personnes se retrouvent face à de mauvaises conditions de vie. Elles subissent
           les conséquences d’un aménagement 
          du territoire où l’on retrouve des quartiers riches et des quartiers pauvres. Et ce niveau socio-économique empêche de changer la donne.</i>&nbsp;»  </p>
        <p>Car depuis lors, l’industrie n’est plus aussi présente dans les cœurs de ville et ils sont confrontés à un processus de gentrification : la classe moyenne s’y installe. «&nbsp;<i>Les effets de la spéculation immobilière, les effets de l'augmentation des loyers, de la crise du logement... 
          impactent ces phénomènes d'injustice sociale</i>, ajoute Chloé Salembier. <i>Les loyers sont plus chers dans les quartiers les moins denses et les plus verts. C’est impayable pour des familles qui ont des revenus bas ou moyens. Cela renforce l’obligation d’aller dans les quartiers les plus denses lorsqu’on n’a pas les moyens.</i>&nbsp;»</p>
        <p>
          «&nbsp;<i>Les personnes à Bruxelles qui sont isolées - ce qui représente quand même  <a href='https://ibsa.brussels/chiffres/chiffres-cles-par-commune/ville-de-bruxelles' target='_blank' rel=noreferrer>près de 50% de la population</a> - 
          rencontrent des difficultés à se loger de manière décente</i>&nbsp;», continue l’ethnologue.  La part de budget des ménages qui est utilisée pour
            se loger est ainsi passée de 26,1% en 1999,
            soit un peu plus d’un quart du budget, à 31,8% en 2020, soit presque un tiers du budget des ménages.</p>
      </div>

      <Quote
      content={" Ces personnes vont donc diminuer leurs critères de confort en étant dans des quartiers moins bien desservis en termes de transport en commun, moins verts, plus denses... pour avoir suffisamment de chambres pour les enfants par exemple."}/>

  <div class="wrapper-text">
    <p>
      Parmi les personnes victimes de mal-logement, il y a trois types de profils, énumère Chloé Salembier. «&nbsp;<i>En Région bruxelloise,
       ce sont les familles monoparentales, les personnes isolées et les aînés. Dans chacune de ces catégories, les femmes sont surreprésentées.
        Par contre, on n'a pas les chiffres sur les facteurs de discrimination liées à l'origine des personnes. Mais on sait que dans le croissant pauvre 
        (la zone au nord du canal, ndlr), 
      ce sont des quartiers qui accueillent des personnes qui cumulent les facteurs de discrimination en termes d'accès à l'emploi, d'accès au logement, etc.</i>&nbsp;»  
    </p>
    <p>
      Les personnes que l’on retrouve dans les îlots de chaleur ont non seulement de plus petits revenus en général, mais sont donc aussi à l’intersection 
      d’autres inégalités basées sur le genre ou la couleur de peau, par exemple. 
    </p>
  </div>
  </section>
  
  <section class="chapitre">
    <Title
    content={"Chaleur mortalité en hausse, quid à l'avenir ?"}
    index=4
    />
    <div class="wrapper-text">
      <p>
        Retour à l’été 2022. Cette année-là, Sciensano constate que la courbe de surmortalité grimpe en flèche en Belgique.
         En clair, on comptabilise davantage de décès qu’en temps normal à cette période. Durant cette période estivale (16 mai au 9 octobre),
         la surmortalité a été importante avec 2312 décès supplémentaires (5,8 % d’excès de mortalité), rapporte l’Institut de Santé publique. 
      </p>
      <p>
        Sciensano s’était <a href='https://www.sciensano.be/en/biblio/heat-related-mortality-two-largest-belgian-urban-areas-a-time-series-analysis' target='_blank' rel=noreferrer>déjà penché sur la question en 2020</a> avec une analyse des périodes chaudes à Bruxelles et Anvers entre 2002 et 2011.
         Résultat&nbsp;: la mortalité augmente dès que la température dépasse 25,2°C à Anvers ou 22,8°C à Bruxelles. 
      </p>
      <p>
        Cette tendance ne devrait pas aller en s’améliorant. Le réchauffement climatique est tout à fait perceptible en Belgique,
         comme nous l’expliquions déjà <a href='https://www.rtbf.be/article/a-quel-point-fait-il-plus-chaud-dans-votre-commune-depuis-votre-naissance-et-quelles-consequences-pour-le-futur-10893043' target='_blank' rel=noreferrer>dans un grand format publié fin 2020</a>.  
      </p>
   
    </div>

    <Quote
    content={"Pour le moment, on est dix ans en avance sur le pire des scénarios"}/>

    <div class="wrapper-text">
      <p>
        «&nbsp;<i>Le scénario le plus probable, c’est une hausse de 3,2°C d’ici à la fin du siècle</i>&nbsp;», rapporte Xavier Fettweis, climatologue à l’Université de Liège.
         «&nbsp;<i>Ce scénario-là, c’est le minium qu’on va obtenir</i>&nbsp;», le reprend aussitôt son collègue Sébastien Doutreloup. 
         Tout dépend en effet des promesses et des décisions prises au niveau politique. 
      </p>
    </div>

    <Img
    type={"middle"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/7.webp"]}
    legend={["À Mons comme ailleurs, les températures augmentent selon le pire des scénarios proposés par le GIEC, Groupe d'experts intergouvernemental sur l'évolution du climat. Crédit: Samere Fahim Photography, Getty images"]}
    alt={["À Mons comme ailleurs, les températures augmentent selon le pire des scénarios proposés par le GIEC, Groupe d'experts intergouvernemental sur l'évolution du climat. Crédit: Samere Fahim Photography, Getty images"]}
    />

    <div class="wrapper-text">
      <p>
        Xavier Fettweis enchaîne : «&nbsp;<i>Pour le moment, on est dix ans en avance [sur le pire des scénarios].
         Rien que sur la dernière décennie 2011-2020, on a gagné un degré en été en Belgique par rapport à la période 1981-2010.
         Et pour ce qui est des inondations de juillet 2021, les modèles suggéraient plutôt que ça arrive en 2030.</i>&nbsp;» 
      </p>
      <p>
        <a href='https://climat.be/doc/seclim-be-2020-finalreport.pdf' target='_blank' rel=noreferrer>Dans un rapport de 2020</a> écrit pour le gouvernement fédéral, des chercheurs rappellent que «&nbsp;<i>si le monde continue sur cette tendance de 'business as usual',
         près de 30% des jours d’été (donc de juin à août), 
        seront des jours de fortes chaleurs [où la température maximale moyenne sur trois jours dépasse 30°C, ndlr].
         À Liège, la population pourrait être confrontée à 6 à 8 jours de fortes chaleurs sur l’été, contre un ou deux actuellement.</i>&nbsp;»  
      </p>
      <p>
        Ce même document insiste sur le fait que «&nbsp;<i>les groupes de la société qui sont déjà précaires 
        (les gens en mauvaise santé, avec un revenu faible ou un logement inadapté) 
        sont souvent aussi les plus vulnérables au changement climatique</i>&nbsp;».
      </p>
    </div>
    <div class="wrapper-plot">
      <iframe src='https://flo.uri.sh/visualisation/14758903/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/14758903/?utm_source=embed&utm_campaign=visualisation/14758903' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>
    </div>

  </section>
  
   <section class="chapitre" data-color="#BCBBD2">
    <Title
    content={"Savez-vous planter des arbres ?"}
    index=5
    />
    <div class="wrapper-text test" data-color="green">
      <p>Que faire alors&nbsp;? Changer la ville, répond Yves Richard de l’université de Bourgogne. «&nbsp;<i>Pour déployer des solutions vertes, 
        il faut identifier des espaces. Et dans les espaces publics, ce sont les zones qui sont pour l'instant dédiées à la voirie qui doivent être mobilisées.
         Il faut désimperméabiliser les sols et végétaliser la ville</i>&nbsp;», expose le professeur de géographie.  
      </p>
      <p><a href='https://www.meteo.be/resources/misc/climate_report/RapportClimatique-2020.pdf' target='_blank' rel=noreferrer>À l’IRM</a>, on invite aussi à regarder du côté de l’albédo des bâtiments, c’est-à-dire la part des rayonnements solaires qui sont renvoyés vers l'atmosphère.
         «&nbsp;<i>L’albédo des bâtiments pourrait être modifié (en utilisant différents matériaux, des peintures de couleur blanche...) afin que plus de rayonnement solaire 
         soit réfléchi. Une étude récente
         de l’IRM a montré que cela pourrait réduire l’îlot de chaleur urbain de 0,45°C et rendre la température moins stressante pour les habitants des villes.</i>&nbsp;» 
      </p>
    <p>Quant à la verdure supplémentaire, l’Institut estime qu’elle «&nbsp;<i>pourrait éviter 33% des vagues de chaleur.</i>&nbsp;»
       Et de conclure&nbsp;: «&nbsp;<i>Afin de minimiser l’effet de la ville pendant les vagues de chaleur, une combinaison des deux mesures ci-dessus est recommandée.</i>&nbsp;» </p>
    </div>
    <Video
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/drone_bxl_1.mp4",
    "https://rtbfmedia.be/rtbfinfo/ICU_pics/drone_bxl_2.mp4"
    ]}
    legend={["À Bruxelles, le toit du Palais du Midi a été peint en blanc pour absorber moins de chaleur.","De hauts immeubles, peu de verdure: la recette parfaite pour un îlot de chaleur."]}
      />
    <div class="wrapper-text">
      <p>«&nbsp;<i>Les arbres sont vraiment un paramètre primordial pour rafraîchir l’espace. Ils puisent l’eau dans le sol. Et,
         quand il fait chaud, ils font comme nous : ils transpirent. C’est l’évaporation de l’eau qui va rafraîchir l’air</i>&nbsp;», 
         résumait Mirjana Velickovic, project manager chez mkengineering.be,
         dans un reportage du journal télévisé diffusé en août 2022. </p>
    </div>
    {#if width < 550}
    <Img
    type="big"
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/arbre_9_16.webp"]}
    alt={["Quentin Vanhoof d’après Ateliers parisiens de l’urbanisme"]}
    legend={["Quentin Vanhoof d’après Ateliers parisiens de l’urbanisme"]}/>
    {:else}
    <Img
    type="middle"
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/arbre_16_9.webp"]}
    alt={["Quentin Vanhoof d’après Ateliers parisiens de l’urbanisme"]}
    legend={["Quentin Vanhoof d’après Ateliers parisiens de l’urbanisme"]}
    />
    {/if}

    <div class="wrapper-text">
      <p>Cela ne se fera pas sans quelques changements d’habitudes. Yves Richard invite ainsi à «&nbsp;<i>repenser nos modes de déplacements à l'intérieur de 
        la ville pour consommer moins d'espace. Cela peut passer par le déploiement des transports en commun, la mobilité douce. 
        Il faut aussi donner moins de place à l'automobile. Celle-ci, qu'elle soit électrique ou pas, prend trop de place.</i>&nbsp;»  
      </p>
      <p>À votre tour de remodeler la ville. En cliquant sur les boutons, découvrez l'influence concrète de chaque aménagement urbain sur la température.</p>
    </div>

    {#if width > 550}
    <GameCalc
    base={"http://rtbfmedia.be/rtbfinfo/ICU_pics/Gamecalc_desktop_webp/"}
    images={["01-REVETEMENT.webp","02-ISOLATION.webp","03-PELOUSE.webp","04-POINT D EAU.webp","05-TRAFFIC.webp","06-FONTAINES.webp","07-OMBRE.webp","08-ARROSAGE.webp","09-TOITURES.webp","10-TOITURES+FACADES.webp","11-BRUMIFICATEURS.webp","12-ARBRES.webp","VILLE-BASE.webp"]
  }/> 
   {:else}
   <GameCalc
    base={"http://rtbfmedia.be/rtbfinfo/ICU_pics/Gamecalc_mobile_webp/"}
    images={["01-REVETEMENT.webp","02-ISOLATION.webp","03-PELOUSE.webp","04-POINT D EAU.webp","05-TRAFFIC.webp","06-FONTAINES.webp","07-OMBRE.webp","08-ARROSAGE.webp","09-TOITURES.webp","10-TOITURES+FACADES.webp","11-BRUMIFICATEURS.webp","12-ARBRES.webp","VILLE-BASE.webp"]
  }/> 
    {/if}

  </section>
</div>
    <Title
    content={"Agir aujourd'hui pour régler les défis de demain"}
    index=5
    />
<div class="wrapper-text">
<p>
  Encore une condition pour Chloé Salembier&nbsp;: lier les questions d’espace public avec celles du logement. 
  «&nbsp;<i>Elles sont complètement imbriquées. Si l’on verdurise un quartier, il faut mettre en place des mesures compensatoires, par exemple un plafonnement des loyers ou une rétrocession de la plus-value faite grâce à l’augmentation du loyer.</i>&nbsp;»
   Dans le cas contraire, ce quartier attirerait simplement des personnes qui ont les moyens de se le payer... et les inégalités perdureraient.   
</p>
<p>
  Pour relever les défis de demain, mieux vaut agir dès aujourd’hui. En Belgique, certaines villes s’organisent.
   C’est le cas à Liège avec <a href='https://www.rtbf.be/article/plan-canopee-a-liege-24000-arbres-pour-faire-respirer-la-ville-dici-2030-10880961' target='_blank' rel=noreferrer>le plan Canopée</a> qui vise à augmenter la quantité d'arbres dans l’espace public et l’espace privé d’ici à 2030. 
  À Bruxelles aussi, certaines actions sont mises en place&nbsp;: la commune d’Ixelles compte par exemple <a href='https://www.rtbf.be/article/ixelles-feu-vert-pour-la-verdurisation-des-places-flagey-et-sainte-croix-11240594' target='_blank' rel=noreferrer>verduriser les places Flagey et Sainte-Croix</a>. 
</p>
<p>
  Hélène Ancion de l’association Canopea reste cependant circonspecte face à ces plans de verdurisation.
   «&nbsp;<i>Beaucoup d’arbres plantés sont des arbres à fruits car productifs, mais c’est très difficile pour eux de s’épanouir en ville.
   </i>&nbsp;» Bien choisir l’essence et lui laisser l’espace est donc primordial pour la chargée de mission.
   Mais surtout, «&nbsp;<i>garder ce qui est déjà existant et arrêter de couper les arbres déjà présents et bien implantés</i>&nbsp;». 
</p>
<p>
  Quoi qu’il en soit, il va falloir changer «&nbsp;<i>la skyline</i>&nbsp;» de nos villes dans les prochaines années si l’on ne veut pas subir 
  les pics de températures toujours plus nombreux et toujours plus intenses.  
</p>
</div>
<div class="center">
<div class="wrapper-text methodo"> 
  <p style="font-size:var(--font-size-md)">Comment avons-nous travaillé&nbsp;?</p>
  <p>Pour déterminer les températures de surface – seul moyen d’obtenir une image exhaustive des zones étudiées - nous avons extrait les données du <a href='https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1' target='_blank' rel=noreferrer>satellite de la NASA Landsat 8</a> pour les mois de juillet et août entre 2013 et 2022.</p>
  <p>Ces températures de surface diffèrent des températures de l’air ressenties par les humains à un endroit donné. 
    Il ne faut donc pas les considérer en valeurs absolues. Il s’agit avant tout d’une cartographie indicative – mais cohérente - pour déceler les zones plus chaudes et plus froides. 
    Des études scientifiques (lire notamment <a href='https://www.mdpi.com/2073-445X/10/4/410' target='_blank' rel=noreferrer>ici</a> et <a href='https://www.sciencedirect.com/science/article/abs/pii/S0034425796002167' target='_blank' rel=noreferrer>là</a>) ont montré que lorsque la température du sol est élevée, celle de l’air l’est aussi.  </p>
   <p><a href='https://statbel.fgov.be/fr/open-data/statistique-fiscale-des-revenus-par-secteur-statistique' target='_blank' rel=noreferrer>Les revenus des Belges</a> et <a href='https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-7' target='_blank' rel=noreferrer>la densité de population</a> par secteurs statistiques proviennent de Statbel.
     Les informations concernant la couverture de la végétation en Région wallonne proviennent de la couche de données WALOUS 2020 sur <a href='https://geoportail.wallonie.be/catalogue/47b348f1-6e7a-4baa-963c-0232a43c0cff.html' target='_blank' rel=noreferrer>le géoportail de Wallonie</a>. Pour la Région bruxelloise,
     les données de répartition de la végétation haute et basse datées de septembre 2021 ont été récupérées sur <a href='https://geodata.environnement.brussels/client/view/67bc5ff0-90f6-4b76-9f05-15c15a928980' target='_blank' rel=noreferrer>le portail environnement.brussels</a>. </p> 
     <p>Différents scripts en Python ainsi que le logiciel de cartographie QGIS ont été utilisés pour extraire les données et les compiler.
       L’ensemble du code est disponible <a href='https://github.com/rtbfinfo/ilots-de-chaleur' target='_blank' rel=noreferrer>sur Github</a>.</p>
</div>
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

    --font-title:'Montserrat', sans-serif;
  }

  
  a {
        /* text-decoration: none; */
        color:rgb(245, 78, 52);
        font-style: bold;
        
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
        max-width: 50rem;
        margin-inline: auto;
        margin-block: 2rem;
        line-height: 1.7rem;
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 500;
        padding-inline: 1rem;
    }

  .methodo {
    border: 5px solid var(--dark-orange);
    border-radius: 2rem;
    margin: 5rem 1rem;
  }
  .center {
    margin-inline: auto;
    max-width: 50rem;
  }

  .wrapper-plot {
    max-width: 80rem;
    margin-inline: auto;
    margin-block: 2rem;
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

    @media screen and (max-width: 550px) {
      .wrapper-text {
        font-size: var(--font-size-md);
        line-height: 1.5;
      }
    }
</style>
