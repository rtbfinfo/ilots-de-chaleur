<script>
    import Scrolly from "./scrolly.svelte";
    import * as d3 from "d3"
    import { draw } from  "svelte/transition";

    $: width = 700;
    $: height = 700;

    export let point_data;
    export let complete_geo;
    export let value_yscale;

    $: isMap = true;

    // scale for map
    let projection = d3.geoMercator()
        // .fitExtent([[0, 0], [width, width/2.5]], complete_geo);

    let projectionX = isMap  
        ?  d3.geoMercator()
            .fitExtent([[0, 0], [width, width/2.5]], complete_geo) 
        :  d3.scaleLinear()
            .domain([d3.min(point_data.map(d => d.properties.NOMBRE_HAB)),d3.median(point_data.map(d => d.properties.NOMBRE_HAB)),d3.max(point_data.map(d => d.properties.NOMBRE_HAB))])
            .range([0,350,700])
    let projectionY = isMap  
        ?  d3.geoMercator()
            .fitExtent([[0, 0], [width, width/2.5]], complete_geo) 
        :  d3.scaleLinear()
            .domain([d3.min(point_data.map(d => d.properties.raster_value)),d3.median(point_data.map(d => d.properties.raster_value)),d3.max(point_data.map(d => d.properties.raster_value))])
            .range([0,350,700])
           
    
    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.raster_value)),d3.median(point_data.map(d => d.properties.raster_value)),d3.max(point_data.map(d => d.properties.raster_value))])
        .range(["blue","white","red"])

    // scale for point plot
    let XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.NOMBRE_HAB)),d3.median(point_data.map(d => d.properties.NOMBRE_HAB)),d3.max(point_data.map(d => d.properties.NOMBRE_HAB))])
        .range([0,350,700])

    let yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.raster_value)),d3.median(point_data.map(d => d.properties.raster_value)),d3.max(point_data.map(d => d.properties.raster_value))])
        .range([700,350,0])
    

    // step scrolly (à mettre dans la page principale)
    let currentStep;

    $: value = "NOMBRE_HAB"
    const steps = ["<p>Step 0!</p>", 
				   "<p>Step 1?</p>", 
				   "<p>Step 2.</p>"];

    import { tweened } from "svelte/motion";
    import { point } from "turf";

    test = 
    

    const tweenedX = tweened([point_data.map(d => d.properties.centroid_lon), point_data.map(d => d.properties.centroid_lat)]) 
    const tweenedY =tweened([point_data.map(d => d.properties.centroid_lon), point_data.map(d => d.properties.centroid_lat)])

    const setMap = function () {
        tweenedX.set([point_data.map(d => d.properties.centroid_lon), point_data.map(d => d.properties.centroid_lat)]) 
        tweenedY.set([point_data.map(d => d.properties.centroid_lon), point_data.map(d => d.properties.centroid_lat)])

    }

    const setPoint = function () {
        tweenedX.set(point_data.map(d => d.properties.NOMBRE_HAB))
        tweenedY.set(point_data.map(d => d.properties.raster_value))
    }
  
    $: if (currentStep == 0) {
        isMap = true
        setMap()
    } else if (currentStep == 1) {
        isMap = false
        setPoint()
    } else if (currentStep == 2) {
        isMap = true
        setMap()
    }


</script>

<div bind:clientWidth={width} bind:clientHeight={height}></div>

<section>
    <div id="chart">
        <svg width={width} height={width/2}>
           <g>
             {#each point_data as temp, index}
               <circle r="2.5"
               cx={projectionX($tweenedX[index])} 
               cy={projectionY($tweenedY[index])}
               fill={color_scale(temp.properties.raster_value)} 
               style="opacity:2;"/>
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
</section>

<style>
    .chart {
    background: whitesmoke;
    width: 90%;
    height: 100%;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
    position: sticky;
    top: 10%;
    margin: auto;
    z-index: -100;
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

