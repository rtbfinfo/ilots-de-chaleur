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

  gsap.registerPlugin(ScrollTrigger);


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

    gsap.utils.toArray(".test").forEach(function(elem) {


      gsap.to('body', {
        scrollTrigger: {
              trigger:".blue",
              start: "80% 80%",
              end: "bottom top",
              scrub: true,
              // pin: true,
              anticipatePin: 1,
              // markers: true
          },
          backgroundColor: "#e19186"
      })
    })
  })
    //   })
  // let participants = [
  //   {
  //     nom: "Héloïse",
  //     job: "Data"
  //   },
  //   {
  //     nom: "Ambroise",
  //     job: "journaliste"
  //   }
  // ]

  //const mar = data.mar



</script>
  <Hero
  title={"Les îlots de chaleur, ce problème qui menace les villes belges"}
  subtitle={"Comment ce phénomène climatique va creuser les écarts entre les riches et les pauvres"}
  />
  <div class="wrapper-text test" style="color:var(--dark-blue)" data-color="red">
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.</p>
    </div>

    <Quote
    content={"Lorem ipsum dolor sit, amet consectetur adipisicing elit."}
    />

    <div class="wrapper-text test">
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Rerum voluptatem laborum placeat enim adipisci voluptatum! 
        Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
        ratione nobis minima, velit esse ut unde.</p>
    </div>

  <Title
  content={"C'est quoi un ilot de chaleur ?"}
  />
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
  <Img
  type={"middle"}
  img={["./image/ilots_infographie.png"]}
  />

    <Title
  content={"Bloc de scroll"}
  />

  <div class="blue"></div>

  <div class="wrapper-text test"  data-color="blue">
    <p>Choisissez la ville que vous voulez explorer sur cette carte interactive
    </p>
  </div>

  <section>
    <Select 
    Belgium_geo={province}
    secteurs_geo={secteur_all}
    point_data={Lst}
    annot={annot}
    />
  </section>

  <Title
  content={"Analyse Sociologique"}
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
  <Video
  type={"big"}
  img={["./image/drone bxl immeubles.mp4",
  "./image/drone bxl immeubles.mp4"
]}
  />

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

  <Title
  content={"Le problème va s'accentuer à l'avenir"}
  />

  <LinePlot
  MAR={mar}/>


  <Title
  content={"Quelles solutions ?"}
  />
  <div class="wrapper-text test" data-color="green">
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

  <GameCalc
  images={["./image/solutions/Horizontal/01-REVETEMENT.png","./image/solutions/Horizontal/02-ISOLATION.png","./image/solutions/Horizontal/03-PELOUSE.png",
  "./image/solutions/Horizontal/04-POINT D EAU.png","./image/solutions/Horizontal/05-TRAFFIC.png","./image/solutions/Horizontal/06-FONTAINES.png","./image/solutions/Horizontal/07-OMBRE.png",
  "./image/solutions/Horizontal/08-ARROSAGE.png","./image/solutions/Horizontal/09-TOITURES.png","./image/solutions/Horizontal/10-TOITURES+FACADES.png",
  "./image/solutions/Horizontal/11-BRUMIFICATEURS.png","./image/solutions/Horizontal/12-ARBRES.png","./image/solutions/Horizontal/VILLE-BASE.png"]}/> 

  <!-- inline / middle / big -->

<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;500&display=swap');
  /* .wrapper {
        max-width: 100rem;
        margin-inline: auto;
    } */
  :root {
    --dark-blue: #144265;
    --light-blue: #0d738a;
    --redish: #dc351f;
    --redish-clear: #e19186;
    --light-orange: #d66819;
    --dark-orange: #da4d1a;
    --backgound-color: #e3afa0;

    --font-size-sm: clamp(0.7rem, 0.35vw + 0.61rem, 0.89rem);
    --font-size-base: clamp(0.88rem, 0.57vw + 0.73rem, 1.19rem);
    --font-size-md: clamp(1.09rem, 0.89vw + 0.87rem, 1.58rem);
    --font-size-lg: clamp(1.37rem, 1.35vw + 1.03rem, 2.11rem);
    --font-size-xl: clamp(1.71rem, 2.01vw + 1.21rem, 2.81rem);
    --font-size-xxl: clamp(2.14rem, 2.93vw + 1.4rem, 3.75rem);
    --font-size-xxxl: clamp(2.67rem, 4.23vw + 1.61rem, 5rem);
  }

  :global(body) {
    background-color: var(--backgound-color);
    font-family: 'Montserrat', sans-serif;
    margin: 0;
}
  /* :global(div) {
    border: 2px solid red;
  } */

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
</style>
