<script>
    import * as d3 from "d3"
    import { onMount } from "svelte";
    import { fade } from "svelte/transition";
  
    import Scrolly from "./components/scrolly.svelte";
    import Map from "./components/Map.svelte";
    import MapDensity from "./components/Map_density.svelte";
    import PointPlot from "./components/PointPlot.svelte";
    import MapPoint from "./components/MapPoint.svelte";


    export let data 

    const secteur = data.secteur
    const temp = data.temp

</script>

<div class="wrapper">
  <section>      
    <Map
      geometry_data={secteur.features}
      complete_geo={secteur}
      point_data={temp.features}
      />
  </section>
  
  <section>
    <MapPoint
    complete_geo={secteur}
    point_data={temp.features} 
    />
  </section>
</div>



<style>
    /* .wrapper {
        max-width: 100rem;
        margin-inline: auto;
    } */
    :root {
    --dark-blue : #144265;
    --light-blue: #0D738A;
    --redish : #DC351F;
    --light-orange: #D66819;
    --dark-orange: #DA4D1A;
  }

  :global(body) {
    background-color: rgb(174, 195, 207);
  }

</style>
