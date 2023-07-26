<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import { onMount } from "svelte";
    import { draw } from  "svelte/transition";
    
    $: width = 700;
    $: height = 700;

    export let geometry_data;
    export let point_data;
    export let complete_geo;

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], complete_geo);
    
    $: geoGenerator = d3.geoPath(projection)

    let color_scale = d3.scaleLinear()
        .domain([25,35,48])
        .range(["#144265","White","#DA4D1A"])
    
</script>


<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div id="content">
   <svg width={width} height={width/2}>

      <g>
        {#each point_data as temp}
          <circle r="3.5"
          cx={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[0]} 
          cy={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[1]}
          fill={color_scale(temp.properties.raster_value)} 
          style="opacity:2;"/>

        {/each}
    </g>

    <g>
        {#each geometry_data as data}
          <path d={geoGenerator(data)} 
          style="stroke:grey;fill:none;stroke-width:0.1;stroke-opacity:0.2"
          transition:draw={{duration:2000, delay:0.1}}/>
        {/each}
    </g>

 
  </svg>
  </div>

  

  <style>

  </style>