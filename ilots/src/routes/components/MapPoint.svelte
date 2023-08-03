<script>
    import Scrolly from "./scrolly.svelte";
    import * as d3 from "d3"
    import { draw } from  "svelte/transition";

    $: width = 700;
    $: height = 700;

    export let point_data;
    export let complete_geo;

    point_data = point_data.filter(d => d.REVENU_MOYEN !== null)

    $: isMap = true;

    // scale for map
    let projection = d3.geoMercator()
        //fitExtent([[0, 0], [width, width/2.5]], complete_geo);

    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.median(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range(["#144265","whitesmoke","#DA4D1A"])

    // scale for point plot
    $: XScale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([0,width/2])

    let revscale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.REVENU_MOYEN)),d3.max(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.REVENU_MOYEN))])
        .range([300,1000])

    let ver_scale= d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.perc_ver !== null).map(d => d.perc_ver)),d3.max(point_data.filter(d => d.perc_ver !== null).map(d => d.perc_ver))])
        .range([300,1000])

    $: yScale =d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range([0,width])
    

    // step scrolly (à mettre dans la page principale)
    let currentStep;

    $: value = "NOMBRE_HAB"
    const steps = ["<p></p>", 
				   "<p></p>", 
				   "<p>Step 2.</p>"];

    import { tweened } from "svelte/motion";
    import { point } from "turf";
    
    const tweenedX = tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0])) 
    const tweenedY =tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[1]))
    const tweendRad = tweened(2.5)


    const BiggerPoint = function () {
        tweendRad.set(4)
    }
    const SmallPoint = function () {
        tweendRad.set(2.5)
    }
    
    const setMap = function () {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], complete_geo);

        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

    }

    const setPoint = function () {
        tweenedX.set(point_data.map(d => XScale(d.NOMBRE_HAB)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))
    }

    const setRev = function () {
        tweenedX.set(point_data.map(d => revscale(d.REVENU_MOYEN)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))
    }

    const setVer = function () {
        tweenedX.set(point_data.map(d => ver_scale(d.perc_ver)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))
    }
  
    $: if (currentStep == 0) {
        isMap = true
        setMap()
        SmallPoint()
    } else if (currentStep == 1) {
        isMap = false
        setRev()
        BiggerPoint()
    } else if (currentStep == 2) {
        isMap = true
        setVer()
    }


</script>

<div bind:clientHeight={height}></div>

<section>
    <div class="chart"   bind:clientWidth={width}>
        <div id="content">
            <svg width={width} height={width/2}>
                <g>
                  {#each point_data as temp, index}
                    <circle r={$tweendRad}
                    cx={$tweenedX[index]} 
                    cy={$tweenedY[index]}
                    fill={color_scale(temp.raster_value_y)} 
                    style="opacity:2;"/>
                  {/each}
              </g>
          </svg>
          </div>
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
    /* .wrapper {
        max-width: 50rem;
        margin-inline: auto;
    } */

    .chart {
    /* background: whitesmoke; */
    width: 80%;
    height: 80%;
    /* box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2); */
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

    :global(svg) {
        border : 2px solid red;
    }
</style>

