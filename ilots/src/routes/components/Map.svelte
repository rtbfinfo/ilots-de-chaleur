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
        .domain([20,35,50])
        .range(["blue","white","red"])
    
</script>


<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div id="content">
   <svg width={width} height={width/2}>
      <g>
        {#each point_data as temp}
          <circle r="1.5"
          cx={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[0]} 
          cy={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[1]}
          fill={color_scale(temp.properties.raster_value)} 
          />

        {/each}
    </g>
    <g>
        {#each geometry_data as data}
          <path d={geoGenerator(data)} 
          style="stroke:black;fill:none;stroke-width:0.4;"
          transition:draw={{duration:2000, delay:0.1}}/>
        {/each}
    </g>
 
  </svg>
  </div>