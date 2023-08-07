<script>
  import * as d3 from "d3";
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";

  import Map from "./components/Map.svelte";
  import PointPlot from "./components/PointPlot.svelte";
  import MapPoint from "./components/MapPoint.svelte";
  import Grid from "./components/Grid.svelte";
  import BigMap from "./components/BigMap.svelte";
  import Text from "./components/Text.svelte";
  import Title from "./components/Title.svelte";
  import Lenis from '@studio-freight/lenis';
  import Img from "./components/Img.svelte";

  export let data;

  const secteur = data.secteur.features;
  const total = data.secteur;
  const datas = data.temp.features
    .map((d) => d.properties)
    .filter((d) => d.city == "liege");
  

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

  //const mar = data.mar
</script>

<div class="wrapper">
  <Title
  content={"Title"}/>
  <Text
    content={"Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus."}
    type={"bloc"}
  />
  <Text
  content={"Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus."}
  type={"bloc"}
  />

  <Img
    type={"multiple"}
    img={["https://static.vecteezy.com/ti/photos-gratuite/p2/719584-canetons-et-cinq-canetons-photo.jpg",
          "https://www.southernliving.com/thmb/kbA2khXaJQqn9mo5R9ZRAYL8zCw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x665:1001x667)/gettyimages-837898820-2000-667fc4cc028a43369037e229c9bd52fb.jpg"]}
    />

  <Title
  content={"Title"}
  />
  <Text
  content={"Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus."}
  type={"bloc"}
  />
  <Title
  content={"Title"}
  />
  <Text
  content={"Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus.Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga et repellendus a, perspiciatis porro quasi tempore qui quia veniam ullam, omnis, tenetur repellat molestias deleniti consequuntur at aspernatur ad ipsum Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius optio quidem aliquam exercitationem perferendis itaque voluptates. Exercitationem recusandae assumenda magni, animi necessitatibus, quam numquam harum libero dicta minus soluta doloribus."}
  type={"bloc"}
  />

  
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

  
  <section>      
    <BigMap
      geometry_data={secteur}
      complete_geo={total}
      point_data={datas}
      />
  </section>
  
  <section>
    <MapPoint
    complete_geo={total}
    point_data={datas} 
    />
  </section>
</div>

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
}
  /* :global(div) {
    border: 2px solid red;
  } */
</style>
