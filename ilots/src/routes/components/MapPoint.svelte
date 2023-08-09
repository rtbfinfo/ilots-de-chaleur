<script>
    import Scrolly from "./scrolly.svelte";
    import * as d3 from "d3"
    import { draw } from  "svelte/transition";
    import SelectMap from "./SelectMap.svelte";

    $: width = 700;
    $: height = 700;
    $: big = true

    export let point_data;
    export let complete_geo;
    export let provinces;
    export let every_sector;

    let margin = {
        top: 20,
        bottom: 50,
        left : 200,
        right: 20,
    }

    console.log(provinces)
    point_data = point_data.filter(d => d.REVENU_MOYEN !== null)

    $: isMap = true;

    // scale for map
    let projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width5]], complete_geo);

    $: geoGenerator = d3.geoPath(projection)

    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.median(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range(["#144265","whitesmoke","#DA4D1A"])

    // scale for point plot
    $: XScale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([0 + margin.left ,width - margin.right])

    $: revscale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.REVENU_MOYEN)),d3.max(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.REVENU_MOYEN))])
        .range([0 + margin.left ,width - margin.right])

    $: ver_scale= d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.perc_ver !== null).map(d => d.perc_ver)),d3.max(point_data.filter(d => d.perc_ver !== null).map(d => d.perc_ver))])
        .range([0 + margin.left ,width - margin.right])

    $: yScale =d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range([800 - margin.bottom , 0 + margin.top])

    let radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN !== null).map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

    // step scrolly (à mettre dans la page principale)
    let currentStep;

    $: value = "NOMBRE_HAB"
    const steps = ["<p>Sélectionnez sur la carte la ville qui vous intéresse</p>",
                    "<p>Prenons la température de surface pour liège par exemple</p>","<p>Voici les zones extremes</p>",
                    "<p>Ici les points sont classés en fonction de la temperature</p>",
				   "<p>Ici la température de surface est mise en relation avec les revenus median de chaque secteur</p>",
                   "<p>Ici la verdure</p>" 
				   ];

    import { tweened } from "svelte/motion";    
    import { onMount } from "svelte";
    const tweenedX = tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0])) 
    const tweenedY =tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[1]))
    const tweendRad = tweened(point_data.map(d => 2))
    
    const setMap = function () {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 800]], complete_geo);

        geoGenerator = d3.geoPath(projection)

        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

        tweendRad.set(point_data.map(d => d.NOMBRE_HAB = 3))

    }

    const setProv = function () {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 800]], provinces);

        geoGenerator = d3.geoPath(projection)
        big = true

    }

    const setPoint = function () {

        tweenedX.set(point_data.map(d => XScale(d.NOMBRE_HAB)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))
    }

    const setTemp = function () {

        tweenedX.set(point_data.map(d => width/2))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

        }

    const setRev = function () {

        tweenedX.set(point_data.map(d => revscale(d.REVENU_MOYEN)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }

    const setVer = function () {

        tweenedX.set(point_data.map(d => ver_scale(d.perc_ver)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))
    }
  
    $: if (currentStep == 0) {
        isMap = true
        setProv()
    } else if (currentStep == 1) {
        isMap = true
        setMap()
    } else if (currentStep == 2) {
        isMap = true
        setMap()
    } else if (currentStep== 3) {
        isMap = false
        setTemp()
    } else if (currentStep==4) {
        isMap = false
        setRev()
    } else if (currentStep==5) {
        isMap = false
        setVer()
    }

    onMount( () => {
        setProv()
    })

</script>

<div bind:clientHeight={height}></div>

<section>
    <div class="chart"   bind:clientWidth={width}>
        <div id="content">
            <svg width={width} height=800>
                
              <SelectMap
              Belgium_geo={provinces}
              secteurs_geo={every_sector}
              width={width}
              />
              
              
              
              
              
                <!-- <g>
                  {#each point_data as temp, index}
                    <circle r={$tweendRad[index]}
                    cx={$tweenedX[index]} 
                    cy={$tweenedY[index]}
                    fill={color_scale(temp.raster_value_y)} 
                    style="stroke:black;stroke-width:0.5"/>
                  {/each}
              </g>
              {#if isMap}
              <g>
                {#each provinces.features as province}
                  <path d={geoGenerator(province)} 
                  style="stroke:whitesmoke;fill:none;stroke-width:0.5;stroke-opacity:1"
                  />
                {/each}
            </g>
            <g>
                {#each complete_geo.features as secteur}
                  <path d={geoGenerator(secteur)} 
                  style="stroke:white;fill:none;stroke-width:0.5;stroke-opacity:1"
                  />
                {/each}
            </g>
            {/if}
            <defs>
                <marker
                  id="triangle"
                  viewBox="0 0 10 10"
                  refX="1"
                  refY="5"
                  markerUnits="strokeWidth"
                  markerWidth="10"
                  markerHeight="10"
                  orient="auto-start-reverse">
                  <path d="M 0 0 L 10 5 L 0 10 " stroke="white" fill="none" stroke-linecap="round" />
                </marker>
              </defs>  
              {#if !isMap}          
            <g>
                <text 
                x={margin.left - 35}
                y={200}
                fill="white"
                stroke="none"
                text-anchor="end"> Chaud</text>
                <text 
                x={margin.left - 35}
                y={650}
                fill="white"
                stroke="none"
                text-anchor="end"> moins Chaud </text>
                <line x1={0 + margin.left + 100} 
                y1={800 - margin.bottom + 30} 
                x2={width - margin.right - 100} 
                y2={800 - margin.bottom + 30} 
                stroke="white"
                stroke-width="2"
                marker-end="url(#triangle)"
                marker-start="url(#triangle)"
                stroke-linecap="round"/>
                <line 
                x1={0 + margin.left -30} 
                y1={800 - margin.bottom - 50} 
                x2={0 + margin.left -30} 
                y2={0 + margin.top + 100} 
                stroke="white"
                stroke-width="2"
                marker-end="url(#triangle)"
                marker-start="url(#triangle)"
                stroke-linecap="round"
                />

            </g>
            {/if} -->
          </svg>
          </div>
        </div>
   
<!--   
     
     <Scrolly bind:value={currentStep}>
         {#each steps as text, i}
             <div class="step" class:active={currentStep === i}>
                 <div class="step-content">
                     {@html text}
                 </div>
             </div>
         {/each}
     </Scrolly> -->
</section>

<style>
    /* .wrapper {
        max-width: 50rem;
        margin-inline: auto;
    } */

    .chart {
    /* background: whitesmoke; */
    width: 90%;
    height: 80%;
    /* box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2); */
    position: sticky;
    top: 5%;
    margin: auto;
    z-index: 10;
    margin-bottom: 10rem;
    border-radius: 10rem;
  }

  .step {
    
    height: 90vh;
    display: flex;
    place-items: center;
    justify-content: right;
    margin-right: 5vw;
  }

  .step-content {
    color: #ccc;
    padding: .5rem 1rem;
    transition: background 500ms ease, color 500ms ease;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, .2);
    max-width: 25vw;
  }

	.step.active .step-content {
        background: rgba(234, 71, 12, 0.603);
		color: whitesmoke;
        border-radius: 0.5rem;
        font-size: var(--font-size-base);
	}

    /* :global(svg) {
        border : 2px solid red;
    } */
</style>

