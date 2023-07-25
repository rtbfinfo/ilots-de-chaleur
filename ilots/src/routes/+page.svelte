<script>
    import * as d3 from "d3"
    import Map from "./components/Map.svelte";
    import { onMount } from "svelte";

    onMount(async () => {

        async function fetchLiege() {
        const response = await fetch('https://raw.githubusercontent.com/rtbfinfo/ilots-de-chaleur/main/assets/selection/liege_sel_centroid.csv?token=GHSAT0AAAAAACFAIAPDK2RU3IH2CFY2RBY2ZF7TU2A');
        console.log(response)
        return await response.json()
    }
      
    let geoJson = fetchLiege()

    let projection = d3.geoEquirectangular;

    let geoGenerator = d3.geoPath()
                       .projection(projection)

    let u = d3.select('#content g.map')
              .selectAll("path")
              .data(geoJson.features)
              .join('path')
              .attr('d', geoGenerator);

    })
 
</script>


<div id="content">
    <svg width="800px" height="400px">
      <g class="map"></g>
    </svg>
  </div>