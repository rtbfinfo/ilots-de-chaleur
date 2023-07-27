<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import { onMount } from "svelte";
    import { draw, fade } from  "svelte/transition";
    
    $: width = 700;
    $: height = 700;

    export let geometry_data;
    export let complete_geo;
    export let legend;

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], complete_geo);
    
    $: geoGenerator = d3.geoPath(projection)
  

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(geometry_data.map(d => d.properties[legend])),d3.max(geometry_data.map(d => d.properties[legend]))])
        .range(["white","#DA4D1A"])

    
</script>


<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div id="content">
   <svg width={width} height={width/2}>
    <g>
        {#each geometry_data as data}
          <path d={geoGenerator(data)} 
          style="stroke:grey;stroke-width:0.2;"
          transition:fade={{duration:5000}}
          fill={data.properties[legend] == null ? "grey" : color_scale(data.properties[legend])}/>
        {/each}
    </g>
 
  </svg>
  </div>