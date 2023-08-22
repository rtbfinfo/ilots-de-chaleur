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
      <p><span class="lettrine">N</span>ous venons de vivre le septième été le plus chaud de Belgique depuis l’enregistrement des températures en 1833.
         Avec un record : celui du mois juin, le plus ardent de tous. Et que dire de l’été 2022 ?
          Le mois d’août de cette année-là dépassait également tous les enregistrements. De record en record, 
          une question se pose : notre pays est-il adapté à ces fortes chaleurs qui deviendront à l’avenir plus longues, plus fréquentes et plus intenses ?
           Qui paye le prix de ce changement climatique indiscutable ? </p>

        <p>Pour le savoir, nous avons croisé des données venues de différentes sources : </p>
        <ul>
          <li>les températures du sol captées par satellite pendant l’été, </li>
          <li>les revenus des Belges</li>
          <li>et la couverture de végétation dans nos régions.</li>
        </ul>
        <p>Verdict: si vous vivez en ville, les plus riches sont les mieux protégés contre les effets des vagues de chaleur. 
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
        Il est midi et il fait 31°C. À quelques kilomètres de là, à Zaventem, il fait chaud aussi. Mais un peu moins que dans la ville : 29°C « seulement ». </p>
    <p>En fait, plus on s’écarte du cœur de la cité, plus il fait frais. Une étude publiée en 2018 a montré que « les températures de l’air sont plus élevées de 3°C 
      en moyenne au centre de la Région de Bruxelles-Capitale qu'à ses alentours ruraux en été (sur la période 1987-2016). Les températures les plus élevées 
      s'observent dans de grandes zones au centre-ville urbanisé.
       Les températures sont légèrement plus basses au-dessus des eaux et dans les grands parcs. » </p>
    </div>
    <Img
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/1.webp","https://rtbfmedia.be/rtbfinfo/ICU_pics/2.webp"]}
    legend={["Rafraîchissement dans l’eau d’une fontaine sur la place Flagey, à Bruxelles, le 24 juillet 2019. Crédit: Thierry Monasse, Getty images)","À Namur, un côté de la Sambre est plus chaud que l’autre. Ceux qui vivent sur les coteaux verts de la Citadelle sont bien plus au frais que ceux qui vivent dans le centre-ville. Crédit: Santiago Urquijo – Getty images"]}
    alt={["Rafraîchissement dans l’eau d’une fontaine sur la place Flagey, à Bruxelles, le 24 juillet 2019. Crédit: Thierry Monasse, Getty images)","À Namur, un côté de la Sambre est plus chaud que l’autre. Ceux qui vivent sur les coteaux verts de la Citadelle sont bien plus au frais que ceux qui vivent dans le centre-ville. Crédit: Santiago Urquijo – Getty images"]}
    />
    <div class="wrapper-text">
      <p>Dans le milieu des climatologues et des urbanistes, c’est ce qu’on appelle un phénomène « d’îlot de chaleur urbain » (ICU).
         « Dans les zones urbaines, la chaleur solaire est absorbée par les matériaux de construction, et les bâtiments hauts et denses retiennent cette chaleur 
         et limitent le refroidissement par la circulation du vent. En outre, les zones urbaines sont généralement densément peuplées et produisent de la chaleur,
         due aux transports et à la climatisation, par exemple », explique l’Institut Royal Météorologique (IRM) sur son site internet. </p>
    </div>
    <Img
    type={"middle"}
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
      <p>Mais c'est surtout la nuit que les ICU entrent en action. « C'est un phénomène nocturne et intermittent.
         Il se produit les nuits qui suivent les journées de beau temps et de vent calme », détaille Yves Richard, professeur de géographie à l'université de Bourgogne.</p>
    <p>Celui qui étudie la question pour le compte de la ville de Dijon, en France précise :
      « C'est à cause de la propriété des matériaux qui absorbent l'énergie pendant la journée et qui relâchent cette énergie la nuit que ce phénomène peut se déployer. » </p>
    </div>
    <Img
    type={"inline"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/3.webp"]}
    legend={["Une fois la nuit tombée, le phénomène d’îlot de chaleur se fait d’autant plus ressentir. Crédit: Marie-Laure Mathot, RTBF"]}
    alt={["Une fois la nuit tombée, le phénomène d’îlot de chaleur se fait d’autant plus ressentir. Crédit: Marie-Laure Mathot, RTBF"]}
    />
    <div class="wrapper-text">
      <p>En pratique, à Bruxelles, « à 23h (heure à laquelle l'îlot thermique urbain est normalement le plus prononcé), 
        les différences de température entre le centre de la ville et la campagne environnante avoisinent en moyenne 4,5°C [ sur la période 1987-2016] »,
         observe l’IRM qui ajoute qu'il y a « en moyenne trois fois plus de périodes de fortes chaleurs dans 
         le centre de Bruxelles que dans les zones rurales avoisinantes ». </p>
    <p>Rafiq Hamdi, scientifique à l’IRM et spécialiste du sujet, relève que « la température entre la ville et 
      la campagne peut monter jusqu’à 8°C de différence la nuit avec un ciel clair et une absence de vent ». Cette différence
      , les Bruxellois ont par exemple pu la constater lors des fortes chaleurs à la fin du mois de juin dernier, comme le montre le graphique ci-dessous. </p>
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
      <p>Dijon, la capitale de la Bourgogne, dans l’Est de la France, a tenté l’expérience. Aujourd’hui 90 stations mesurent la température de l’air à différents endroits de l’agglomération dijonnaise.
         Objectif de ce projet nommé MUSTARDijon (pour Measuring Urban Systems Temperature Around Dijon) : 
        aider les communes à identifier les zones vulnérables pour agir en conséquence. </p>
      </div>
        <Img
        type={"middle"}
        img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/4.webp"]}
        legend={["Observée depuis le ciel, Charleroi se révèle plus chaude en son centre. Crédit: Getty images "]}
        alt={["Observée depuis le ciel, Charleroi se révèle plus chaude en son centre. Crédit: Getty images "]}
        />
      <div class="wrapper-text">
        <p>D’autres ressources existent, à commencer par les données satellites. Ce sont celles que nous allons utiliser pour vous emmener au cœur de nos villes.
          De son petit nom Landsat 8, ce satellite cartographie la température du sol sur l’ensemble du globe. Certes, la température de l’air serait plus représentative.
          Mais Landsat nous donne quand même un aperçu assez fidèle des zones plus chaudes et moins chaudes (voir notre méthodologie à la fin de l’article).
          Vous allez le voir, si on croise ces données avec les revenus fiscaux des Belges et la végétation, les résultats mettent en lumière des inégalités. </p>
          <p>Cliquez sur une ville sur la carte ci-dessous pour découvrir ses particularités en détail.</p>
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
      <p>Conséquence : nous ne sommes pas tous égaux face au changement climatique, analyse Yves Richard à Dijon. « Il existe des inégalités de vulnérabilité,
         surtout quand on regarde l’air intérieur (des habitations, ndlr). Si j’habite un pavillon avec jardin et que je peux ouvrir mes fenêtres la nuit quand je dors,
          je bénéficie de la fraîcheur (de l’air extérieur, ndlr), surtout si mon appartement est traversant. Si, au contraire, j’habite dans un immeuble qui n'est pas 
          traversant, qui est dans une zone bruyante, où il y a de l'insécurité, alors, je vais avoir du mal à rafraîchir mon appartement la nuit.
         Et c'est là où il y a une grande inégalité. » </p>
    <p>Chloé Salembier, ethnologue et professeur à la faculté d’architecture à l’UCLouvain, parle d’injustice spatiale.
       « C’est le fait que les rapports sociaux soient inscrits dans le territoire », définit-elle. « Les êtres humains organisent leur territoire et le territoire 
       produit des pratiques en retour. »
      C’est donc la façon dont nous avons construit nos villes qui a contribué, plus d’un siècle plus tard, à ces vulnérabilités face au changement climatique.</p>
      <p>Des habitants touchés différemment par un phénomène climatique extrême, ça ne vous rappelle rien? 2021,
         les inondations dans la vallée de la Vesdre bien sûr. « Verviers, de par son histoire autour de l’industrie textile avait une population ouvrière 
         dans le bas de la ville, le long de la Vesdre, proche des usines, contextualise Alain Malherbe, historien de l’art et urbaniste, chargé de cours à l’UCLouvain.
          Cela s’est construit en grande partie au moment de l’industrialisation, dès le milieu du XIXe siècle… même si la Belgique a connu,
         de par son fonctionnement et sa mobilité, une classe ouvrière qui s’est répartie de manière plus diffuse », nuance-t-il.  
      </p>
    </div>

    <Img
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/5.webp","https://rtbfmedia.be/rtbfinfo/ICU_pics/6.webp"]}
    legend={["Le quartier de Prés-Javais, à Verviers est particulièrement vulnérable aux phénomènes climatiques extrêmes. Crédit: Marie-Laure Mathot, RTBF","Au contraire, dans un quartier plus riche et vert comme ceux situés sur les coteaux de la Citadelle à Liège, les températures au sol sont beaucoup moins élevées lors des canicules. Crédit: Getty images"]}
    alt={["Le quartier de Prés-Javais, à Verviers est particulièrement vulnérable aux phénomènes climatiques extrêmes. Crédit: Marie-Laure Mathot, RTBF","Au contraire, dans un quartier plus riche et vert comme ceux situés sur les coteaux de la Citadelle à Liège, les températures au sol sont beaucoup moins élevées lors des canicules. Crédit: Getty images"]}
    />

    <div class="wrapper-text">
    <p>Néanmoins, « la vallée de la Vesdre s’est construite avec une population très précaire dès l’industrialisation.
       La bourgeoisie, elle, occupe les coteaux, du côté de Heusy avec de grandes villas ou des maisons avec jardin.
       Il existe des écarts de revenus importants entre ces deux types de population. Les conditions socio-économiques sont aussi très différentes. » </p>
    </div>
      <div class="wrapper-text">
        <p>Des extrêmes encore visibles à Verviers. Dans un quartier en bord de Vesdre comme Hodimont, le revenu médian est de 16.193 € par an en 2020.
           C’est beaucoup moins que le revenu médian wallon (24.808 € par an) et quasiment la moitié de celui du quartier d’Heusy, situé sur les hauteurs, 
           avec 31.234 € par an. Les quartiers les moins riches sont donc ceux qui subissent les effets du changement climatique : fortes chaleurs et inondations,
            souligne Hélène Ancion, chargée de mission en aménagement du territoire et urbanisme pour Canopea,
           la fédération des associations environnementales belges qui défend l'environnement en Wallonie et en Belgique. </p>
      <p>Ces constats sont valables pour d’autres villes: les sols ont été imperméabilisés là où se sont les industries se sont implantées au XIXe siècle.
         Et c’est là que l’on retrouve les logements, autrefois d’ouvriers, aujourd’hui, des plus précarisés. À Liège, en zone inondable, la part de la population
          qui présente un niveau socio-économique très faible s’élève à 37% contre 29 % en moyenne dans la population wallonne,
         soit près de 30% en plus de personnes socio-économiquement défavorisées en zone inondable, selon l’ISSEP, l’Institut scientifique de service public. </p>
        <p>Ce sont des inégalités environnementales pour Hélène Ancion. « Les personnes se retrouvent face à de mauvaises conditions de vie. Elles sont
           les conséquences d’un aménagement 
          du territoire où l’on retrouve des quartiers riches et des quartiers pauvres. Et ce niveau socio-économique empêche de changer la donne. »  </p>
        <p>Car depuis lors, l’industrie n’est plus aussi présente dans les cœurs de ville et ils subissent un processus de gentrification 
          : la classe moyenne s’y installe. « Les effets de la spéculation immobilière, les effets de l'augmentation des loyers, de la crise du logement… 
          impactent ces phénomènes d'injustice sociale », ajoute Chloé Salembier. « Les loyers sont plus chers dans les quartiers qui sont les moins denses, qui sont 
          les plus verts. C’est impayable pour des familles qui ont des revenus bas ou moyens.»
            Cela renforce l’obligation d’aller dans les quartiers les plus denses lorsqu’on n’a pas les moyens. </p>
        <p>
          « Les personnes à Bruxelles qui sont isolées - ce qui représente quand même près de 50% de la population - 
          rencontrent des difficultés à se loger de manière décente », continue l’ethnologue.  La part de budget des ménages qui est utilisée pour
            se loger est ainsi passée de 26,1% en 1999,
            soit un peu plus d’un quart du budget, à 31,8% en 2020, soit presque un tiers du budget des ménages 
        </p>
      </div>

      <Quote
      content={" Ces personnes vont donc diminuer leurs critères de confort en étant dans des quartiers moins bien desservis en termes de transport en commun, moins verts, plus denses… pour avoir suffisamment de chambres pour les enfants par exemple."}/>
  </section>

  <div class="wrapper-text">
    <p>
      Parmi les personnes victimes de mal-logement, il y a trois types de profils, énumère Chloé Salembier. « En Région bruxelloise,
       ce sont les familles monoparentales, les personnes isolées et les aînés. Dans chacune de ces catégories, les femmes sont surreprésentées.
        Par contre, on n'a pas les chiffres sur les facteurs de discrimination liées à l'origine des personnes. Mais on sait que dans le croissant pauvre 
        (la zone au nord du canal, ndlr), 
      ce sont des quartiers qui accueillent des personnes qui cumulent les facteurs de discrimination en termes d'accès à l'emploi, en termes d'accès au logement etc. »  
    </p>
    <p>
      Les personnes que l’on retrouve dans les îlots de chaleur ont non seulement de plus petits revenus en général mais sont donc aussi à l’intersection 
      d’autres inégalités basées sur le genre ou la couleur de peau, par exemple. 
    </p>
  </div>
  
  <section class="chapitre">
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
    </div>

    <Img
    type={"middle"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/7.webp"]}
    legend={["À Mons comme ailleurs, les températures augmentent selon le pire des scénarios proposés par le GIEC, Groupe d'experts intergouvernemental sur l'évolution du climat. Crédit: Samere Fahim Photography, Getty images"]}
    alt={["À Mons comme ailleurs, les températures augmentent selon le pire des scénarios proposés par le GIEC, Groupe d'experts intergouvernemental sur l'évolution du climat. Crédit: Samere Fahim Photography, Getty images"]}
    />

    <div class="wrapper-text">
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
      <p>Que faire alors ? Changer la ville, répond Yves Richard de l’université de Bourgogne. « Pour déployer des solutions vertes, 
        il faut identifier des espaces. Et dans les espaces publics, ce sont les zones qui sont pour l'instant dédiées à la voirie qui doivent être mobilisées.
         Il faut désimperméabiliser les sols et végétaliser la ville », expose le professeur de géographie.  
      </p>
      <p>À l’IRM, on invite aussi à regarder du côté de l’albédo des bâtiments, c’est-à-dire la part des rayonnements solaires qui sont renvoyés vers l'atmosphère.
         « L’albédo des bâtiments pourrait être modifié (en utilisant différents matériaux, des peintures de couleur blanche...) afin que plus de rayonnement solaire 
         soit réfléchi. Une étude récente
         de l’IRM a montré que cela pourrait réduire l’îlot de chaleur urbain de 0,45°C et rendre la température moins stressante pour les habitants des villes. » 
      </p>
    <p>Quant à la verdure supplémentaire, l’Institut estime qu’elle « pourrait éviter 33% des vagues de chaleur.
       Et de conclure : « Afin de minimiser l’effet de la ville pendant les vagues de chaleur, une combinaison des deux mesures ci-dessus est recommandée. » </p>
    </div>
    <Video
    type={"big"}
    img={["https://rtbfmedia.be/rtbfinfo/ICU_pics/drone_bxl_1.mp4",
    "https://rtbfmedia.be/rtbfinfo/ICU_pics/drone_bxl_2.mp4"
    ]}
    legend={["À Bruxelles, le toit du Palais du Midi a été peint en blanc pour absorber moins de chaleur.","De hauts immeubles, peu de verdure : la recette parfaite pour un îlot de chaleur."]}
      />
    <div class="wrapper-text">
      <p>« Les arbres sont vraiment un paramètre primordial pour rafraîchir l’espace. Ils puisent l’eau dans le sol. Et,
         quand il fait chaud, ils font comme nous :i ls transpirent. C’est l’évaporation de l’eau qui va rafraîchir l’air », 
         résumait Mirjana Velickovic, project manager chez mkengineering.be,
         dans un reportage du journal télévisé diffusé en août 2022. </p>
    </div>
    {#if width < 400}
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
      <p>Cela ne se fera pas sans quelques changements d’habitudes. Yves Richard invite ainsi à « repenser nos modes de déplacements à l'intérieur de 
        la ville pour consommer moins d'espaces. Cela peut passer par le déploiement des transports en commun, la mobilité douce. 
        Il faut aussi donner moins de place à l'automobile. Celle-ci, qu'elle soit électrique ou pas, prend trop de place. »  
      </p>
      <p>À votre tour de remodeler la ville. En cliquant sur les boutons, découvrez l'influence concrète de chaque aménagement urbain sur la température.</p>
    </div>

    {#if width > 400}
    <GameCalc
    base={"http://rtbfmedia.be/rtbfinfo/ICU_pics/Gamecalc_desktop_webp/"}
    images={["01-REVETEMENT.webp","02-ISOLATION_.webp","03-PELOUSE.webp","04-POINT D EAU.webp","05-TRAFFIC.webp","06-FONTAINES.webp","07-OMBRE.webp","08-ARROSAGE.webp","09-TOITURES.webp","10-TOITURES+FACADES.webp","11-BRUMIFICATEURS.webp","12-ARBRES.webp","VILLE-BASE.webp"]
  }/> 
   {:else}
   <GameCalc
    base={"http://rtbfmedia.be/rtbfinfo/ICU_pics/Gamecalc_mobile_webp/"}
    images={["01-REVETEMENT.webp","02-ISOLATION_.webp","03-PELOUSE.webp","04-POINT D EAU.webp","05-TRAFFIC.webp","06-FONTAINES.webp","07-OMBRE.webp","08-ARROSAGE.webp","09-TOITURES.webp","10-TOITURES+FACADES.webp","11-BRUMIFICATEURS.webp","12-ARBRES.webp","VILLE-BASE.webp"]
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
  Encore une condition pour Chloé Salembier : lier les questions d’espace public avec celles du logement. 
  « Elles sont complètement imbriquées. Si l’on verdurise un quartier, il faut mettre en place des mesures compensatoires. 
  Par exemple un plafonnement des loyers ou une rétrocession de la plus-value faite grâce à l’augmentation du loyer. »
   Dans le cas contraire, ce quartier attirerait simplement des personnes qui ont les moyens de se le payer. Les inégalités resteraient.   
</p>
<p>
  Pour régler les défis de demain, mieux vaut agir dès aujourd’hui. En Belgique, certaines villes s’organisent.
   C’est le cas à Liège avec le plan Canopée qui vise à augmenter la quantité d'arbres dans l’espace public et l’espace privé d’ici à 2030. 
  À Bruxelles aussi, certaines actions sont mises en place : la commune d’Ixelles compte verduriser les places Flagey et Sainte-Croix. 
</p>
<p>
  Hélène Ancion de l’association Canopea reste circonspecte face à ces plans de verdurisation.
   « Beaucoup d’arbres plantés sont des arbres à fruits car productifs, mais c’est très difficile pour eux de s’épanouir en ville.
    » Bien choisir l’essence et lui laisser l’espace est donc primordial pour la chargée de mission.
   Mais surtout, « garder ce qui est déjà existant et arrêter de couper les arbres déjà présents et bien implantés ». 
</p>
<p>
  Quoi qu’il en soit, il va falloir changer « la skyline » de nos villes dans les prochaines années si l’on ne veut pas subir 
  les pics de températures toujours plus nombreux et toujours plus intenses.  
</p>
</div>

<div class="wrapper-text methodo"> 
  <p style="font-size:var(--font-size-md)">Comment avons-nous travaillé ? Python, QGIS, D3...</p>
  <p>Pour déterminer les températures de surface – seul moyen d’obtenir une image exhaustive des zones étudiées - nous avons extrait les données du satellite de la NASA Landsat 8 pour les mois de juillet et août entre 2013 et 2022.</p>
  <p>Ces températures de surface diffèrent des températures de l’air ressenties par les humains à un endroit donné. 
    Il ne faut donc pas les considérer en valeurs absolues. Il s’agit avant tout d’une cartographie indicative – mais cohérente - pour déceler les zones plus chaudes et plus froides. 
    Des études scientifiques (lire notamment ici et là) ont montré que lorsque la température du sol est élevée, celle de l’air l’est aussi.  </p>
   <p>Les revenus des Belges et la densité de population par secteurs statistiques proviennent de Statbel.
     Les informations concernant la couverture de la végétation en Région wallonne proviennent de la couche de données WALOUS 2020 sur le géoportail
      de Wallonie. Pour la Région bruxelloise,
     les données de répartition de la végétation haute et basse datées de septembre 2021 ont été récupérées sur le portail environnement.brussels. </p> 
     <p>Différents scripts en Python ainsi que le logiciel de cartographie QGIS ont été utilisés pour extraire les données et les compiler.
       L’ensemble du code est disponible sur Github.</p>
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
        max-width: 60ch;
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
    margin-top: 5rem;
  }
  .wrapper-plot {
    max-width: 150rch;
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
</style>
