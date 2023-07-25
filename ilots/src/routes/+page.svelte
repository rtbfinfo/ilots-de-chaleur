<script>
    import * as d3 from "d3"
    import Map from "./components/Map.svelte";
    import { onMount } from "svelte";
    import { updated } from "$app/stores";

    onMount(async () => {

   d3.json("https://gist.githubusercontent.com/Yheloww/b871de29011161706a3ae896690f65f7/raw/90e0574e594379bee3907f062048726526ff88b6/liege_sel_centroid.json")
   .then(function(data) {
    console.log(data)
    update(data);
   })

    

    function update(data) {

        let projection = d3.geoEquirectangular;

        let geoGenerator = d3.geoPath()
                       .projection(projection)

        const svg = d3.select("#map")
        .append("svg")
        .attr("width", 500)
        .attr("height", 500);

        svg.append('g').selectAll('path')
        .data(data.features)
        .enter().append('path')
        .attr('d', d3.geoPath().projection(d3.geoEquirectangular))
            }

    })

 
</script>


<div id="content">
    <svg width="800px" height="400px">
      <g id="map"></g>
    </svg>
  </div>