<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import { onMount } from "svelte";
    import { draw } from  "svelte/transition";
    import Scrolly from "./scrolly.svelte";
    import { fade } from "svelte/transition";
    
    $: width = 700;
    $: height = 800;

    export let geometry_data;
    export let point_data;
    export let complete_geo;
    export let provinces

    $: value = "NOMBRE_HAB"

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 800]], complete_geo)
        // .translate([(width/2)/10, 10700])
        // .scale(10000); 
              
    
    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d[value])),d3.median(point_data.map(d => d[value])),d3.max(point_data.map(d => d[value]))])
        .range(["#144265","whitesmoke","#DA4D1A"])

    let currentStep;
    const steps = ["<p>Densité de population</p>", 
                "<p>Revenus moyen</p>", 
                "<p>Land surface temperature</p>",
              "<p>Percentage de verdure</p>"];
      
    $: if (currentStep == 0) {
      value = "NOMBRE_HAB"
    } else if (currentStep == 1) {
      value = "REVENU_MOYEN"
    } else if (currentStep == 2) {
      value="raster_value_x"
    } else if (currentStep == 3) {
      value="perc_ver"
    }
    
</script>


<div bind:clientHeight={height}></div>

<div class="chart" bind:clientWidth={width}>
   <svg width={width} height={800}>
      <g>
        {#each point_data as temp}
          <circle r="3"
          cx={projection([temp.centroid_lon, temp.centroid_lat])[0]} 
          cy={projection([temp.centroid_lon, temp.centroid_lat])[1]}
          fill={temp[value] == null ? "grey" : color_scale(temp[value])} 
          style="opacity:2;"/>
        {/each}
    </g>
    <g>
        {#each geometry_data as data}
          <path d={geoGenerator(data)} 
          style="stroke:black;fill:none;stroke-width:0.5;stroke-opacity:1"
          />
        {/each}
    </g>
    <g>
      {#each provinces as province}
        <path d={geoGenerator(province)} 
        style="stroke:black;fill:none;stroke-width:0.5;stroke-opacity:1"
        />
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
    /* background-color: black; */
      width: 80%;
      height: 80%;
      /* box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2); */
      position: sticky;
      top: 2%;
      margin: auto;
      z-index: -100;
      border-radius: 10rem;
      display: flex;
      align-items: center;
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
    svg {
      border: 3px solid blue;
    }
  </style>