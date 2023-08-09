<script>
  import * as d3 from "d3";
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";

  import Map from "./components/Map.svelte";
  import PointPlot from "./components/PointPlot.svelte";
  import MapPoint from "./components/MapPoint.svelte";
  import Grid from "./components/Grid.svelte";
  import BigMap from "./components/BigMap.svelte";
  import Hero from "./components/Hero.svelte";
  import Title from "./components/Title.svelte";
  import Lenis from '@studio-freight/lenis';
  import Img from "./components/Img.svelte";
  import Quote from "./components/Quote.svelte";
  import LinePlot from "./components/LinePlot.svelte";

  export let data;

  const secteur = data.secteur.features;
  const total = data.secteur;
  const datas = data.temp.features.map((d) => d.properties)
    .filter((d) => d.city == "liege");
  const province = data.provinces
  const mar = data.mar

  onMount(() => {
    //smooth scroll 
    const lenis = new Lenis()

    lenis.on('scroll', (e) => {
    console.log(e)
    })

    function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)
  })

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
  <div class="wrapper-text">
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
    content={"Lorem ipsum dolor sit, amet consectetur adipisicing elit."}/>

    <div class="wrapper-text">
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Rerum voluptatem laborum placeat enim adipisci voluptatum! 
        Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
        ratione nobis minima, velit esse ut unde.</p>
    </div>

  <Title
  content={"Les îlots de chaleur à Liège"}
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

  <!-- <section>      
    <BigMap
      geometry_data={secteur}
      complete_geo={total}
      point_data={datas}
      provinces={province.features}
      />
    </section> -->

  <!-- inline / middle / big -->

    <section>
      <MapPoint
      complete_geo={total}
      point_data={datas} 
      provinces={province}
      />
    </section>

    <Title
  content={"Dans le futur"}
  />

  <div class="wrapper-text">
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
      ratione nobis minima, velit esse ut unde.</p>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
      Rerum voluptatem laborum placeat enim adipisci voluptatum! 
      Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
      ratione nobis minima, velit esse ut unde.</p>
  </div>

  <LinePlot
  MAR={mar}/>

  <Img
    type={"middle"}
    img={["https://static.vecteezy.com/ti/photos-gratuite/p2/719584-canetons-et-cinq-canetons-photo.jpg",
        "https://static.vecteezy.com/ti/photos-gratuite/p2/719584-canetons-et-cinq-canetons-photo.jpg"]}
    />


<!-- 
    <section>
    <Grid/>
    </section>

    <section>      
    <Map
      geometry_data={secteur}
      complete_geo={total}
      point_data={datas}
      />
    </section>


    </div> -->

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
    --light-orange: #d66819;
    --dark-orange: #da4d1a;
    --backgound-color: #312e3d;

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
        font-weight: 400;
        padding-inline: 1rem;
    }
</style>
