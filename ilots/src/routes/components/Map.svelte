<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import { onMount } from "svelte";
    import { draw } from  "svelte/transition";
    import Scrolly from "./scrolly.svelte";
    import { fade } from "svelte/transition";
    
    $: width = 700;
    $: height = 700;

    export let geometry_data;
    export let point_data;
    export let complete_geo;

    $: value = "NOMBRE_HAB"

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], complete_geo);
    
    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties[value])),d3.median(point_data.map(d => d.properties[value])),d3.max(point_data.map(d => d.properties[value]))])
        .range(["blue","white","red"])

    let currentStep;
    const steps = ["<p>Densité de population</p>", 
                "<p>Revenus moyen</p>", 
                "<p>Land surface temperature</p>"];
      
    $: if (currentStep == 0) {
      value = "NOMBRE_HAB"
    } else if (currentStep == 1) {
      value = "REVENU_MOYEN"
    } else if (currentStep == 2) {
      value="raster_value"
    }
    
</script>


<div bind:clientHeight={height}></div>

<div class="chart" transition:fade={{duration:5000}}  bind:clientWidth={width}>
   <svg width={width} height={width/2}>
      <g>
        {#each point_data as temp}
          <circle r="2.5"
          cx={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[0]} 
          cy={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[1]}
          fill={temp.properties[value] == null ? "grey" : color_scale(temp.properties[value])} 
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

  <Scrolly bind:value={currentStep}>
    {#each steps as text, i}
      <div class="step" class:active={currentStep === i}>
        <div class="step-content">
          {@html text}
        </div>
      </div>
    {/each}
  </Scrolly>


  <style>
    .chart {
      background: whitesmoke;
      width: 80%;
      height: 80%;
      box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
      position: sticky;
      top: 10%;
      margin: auto;
      z-index: -100;
      margin-bottom: 10rem;
      border-radius: 10rem;
    }

    .step {
      height: 90vh;
      display: flex;
      place-items: center;
      justify-content: center;
    }

    .step-content {
      background: whitesmoke;
      color: #ccc;
      padding: .5rem 1rem;
      transition: background 500ms ease, color 500ms ease;
      box-shadow: 1px 1px 10px rgba(0, 0, 0, .2);
    }

    .step.active .step-content {
      background: white;
      color: black;
    }
  </style>