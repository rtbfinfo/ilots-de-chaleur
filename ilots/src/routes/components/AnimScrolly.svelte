<script>
    import * as d3 from "d3"
    import { tweened } from "svelte/motion";    
    import { feature, point } from "turf";
    import Scrolly from "./scrolly.svelte";


    export let point_data
    export let selected
    export let secteurs_geo
    export let width
    export let belgium_geo


    let height = 700;

    $: console.log(point_data)
    $: console.log(secteurs_geo)

//    if (selected == "Liège") {
//         selected == "liege"
//     }
//     // console.log(secteurs_geo.features)
//     // let real_point = {...point_d}
//     // $: point_data = 0
//     // point_data = real_point.features.map(d => d.properties).filter(d => d.city == (selected == "Liège" ? "liege" : selected.toLowerCase())).filter(d => d.REVENU_MOYEN !== null)
//     let test = {...secteurs_geo}
//     $: test.features = test.features.filter(d => d.properties.city == (selected == "Liège" ? "liege" : selected.toLowerCase()))
    // $: console.log(test.features)
    // $: console.log(selected)
    let other_point = JSON.parse(JSON.stringify(point_data));


    // let value = "NOMBRE_HAB";
    let isMap=true;

    // // point_data = point_data.

    let margin = {
        top: 20,
        bottom: 150,
        left : 60,
        right: 50,
    }

    // base scale for color
    let color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.median(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range(["#144265","whitesmoke","#DA4D1A"])

    // base scale for point plot
    $: XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.value)),d3.max(point_data.map(d => d.value))])
        .range([0 + margin.left ,height - margin.right])

    $: yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range([height- margin.bottom , 0 + margin.top])

    $: radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

    // projection for the map

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);

    projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);
    

    $: geoGenerator = d3.geoPath(projection)

    let currentStep =0;

    const steps = [`<p>Prenons la température de surface pour ${selected} par exemple</p>`,
                    "<p>Voici les zones extremes</p>",
                    "<p>Les températures</p>",
                    "<p>Ici les points sont classés en fonction de la temperature</p>",
				    "<p>Ici la température de surface est mise en relation avec les revenus median de chaque secteur</p>",
                    "<p>Ici la verdure</p>",
				   ];

    $: tweenedX = tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]),
        {
            duration: 1000,
            delay: 0,

        }) 
    $: tweenedY =tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[1]))
    $: tweendRad = tweened(other_point.map(d => 2))
    $: tweenedColor = tweened(point_data.map(d => color_scale(d.raster_value_x)))

    const step1 = function() {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);

        geoGenerator = d3.geoPath(projection)


        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 2))


    }
    const step2 = function() {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);

        geoGenerator = d3.geoPath(projection)


        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 2))

    }
    const step3 = function() {
        
        radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

        isMap = false;
        tweenedX.set(point_data.map(d => width/2))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }
    const step4 = function() {
        XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.REVENU_MOYEN)),d3.max(point_data.map(d => d.REVENU_MOYEN))])
        .range([0 + margin.left ,width - margin.right])

        radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

        tweenedX.set(point_data.map(d => XScale(d.REVENU_MOYEN)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }
    const step5 = function() {
        XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.perc_ver)),d3.max(point_data.map(d => d.perc_ver))])
        .range([0 + margin.left ,width - margin.right])

        tweenedX.set(point_data.map(d => XScale(d.perc_ver)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }   
    const step6 = function() {

    }
    $: console.log(currentStep)

    $: if (currentStep == 0) {
        isMap = true
        step1()
    } else if (currentStep == 1) {
        isMap = true
        step2()
    } else if (currentStep == 2) {
        isMap = true
        step3()
    } else if (currentStep== 3) {
        isMap = false
        step5()
    } else if (currentStep==4) {
        isMap = false
        step5()
    } else if (currentStep==5) {
        isMap = false
        step6()
    }

    </script>
<div class="chart">
    <svg width={width} height="100vh">
        {#if isMap}
        <g>
        {#each belgium_geo.features as province}
            <path d={geoGenerator(province)} 
            style="stroke:whitesmoke;fill:none;stroke-width:0.5;stroke-opacity:1"
            />
        {/each}
        </g>
        <g>
            {#each secteurs_geo.features as secteur}
                <path d={geoGenerator(secteur)} 
                style="stroke:white;fill:#1D2E3C;stroke-width:0.5;stroke-opacity:1;fill-opacity:0.5;z-index:-100"
                />
            {/each}
        </g>
        {/if}
        <g>
            {#each point_data as temp, index}
            <circle r={$tweendRad[index]}
            cx={$tweenedX[index]} 
            cy={$tweenedY[index]}
            fill={color_scale(temp.raster_value_y)} 
            stroke={isMap ? "none" : "black"}
            style="stroke-width:0.5;"/>
            {/each}
        </g>
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
            <line x1={0 + margin.left}
            y1={height - margin.bottom} 
            x2={width - margin.right} 
            y2={height - margin.bottom} 
            stroke="white"
            stroke-width="2"
            marker-end="url(#triangle)"
            marker-start="url(#triangle)"
            stroke-linecap="round"/>
            <line 
            x1={0 + margin.left -30} 
            y1={height- margin.bottom - 50} 
            x2={0 + margin.left -30} 
            y2={0 + margin.top + 100} 
            stroke="white"
            stroke-width="2"
            marker-end="url(#triangle)"
            marker-start="url(#triangle)"
            stroke-linecap="round"
            />
        </g>
        {/if}
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
    /* background: whitesmoke; */
    width: 100%;
    height: 80%;
    /* box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2); */
    position: sticky;
    top: 0.1%;
    margin: auto;
    z-index: -10;
    margin-bottom: 10rem;
    border-radius: 10rem;
  }
    .step {
        
        height: 90vh;
        display: flex;
        place-items: center;
        justify-content: right;
        margin-right: 2vw;

    }

    .step-content {
        color: #ccc;
        padding: .5rem 1rem;
        transition: background 500ms ease, color 500ms ease;
        box-shadow: 1px 1px 10px rgba(0, 0, 0, .2);
        max-width: 25vw;
        /* backdrop-filter: blur(3rem); */

    }

	.step.active .step-content {
        background: rgba(234, 71, 12, 0.603);
        /* backdrop-filter: blur(3rem); */
		color: whitesmoke;
        border-radius: 0.5rem;
        font-size: var(--font-size-base);
	}

</style>