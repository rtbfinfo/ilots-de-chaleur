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
    export let legend;

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], complete_geo);
    
    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties[legend])),d3.median(point_data.map(d => d.properties[legend])),d3.max(point_data.map(d => d.properties[legend]))])
        .range(["blue","white","red"])
    
</script>


<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div id="content">
   <svg width={width} height={width/2}>

      <g>
        {#each point_data as temp}
          <circle r="2.5"
          cx={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[0]} 
          cy={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[1]}
          fill={temp.properties[legend] == null ? "grey" : color_scale(temp.properties[legend])} 
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