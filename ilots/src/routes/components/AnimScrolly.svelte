<script>
    import * as d3 from "d3"
    import { tweened } from "svelte/motion";    
    import { feature, point } from "turf";
    import Scrolly from "./scrolly.svelte";
    import Axes from "./Axes.svelte";


    export let point_data
    export let selected
    export let secteurs_geo
    export let annot
    export let belgium_geo

    $: width = 500;
    let height = 500;

    let other_point = JSON.parse(JSON.stringify(point_data));

    let isMap=true;
    let class_name="map";
    let annot_state=false;

    $: margin = {
        top: height/4,
        bottom: height/4,
        left: 100,
        right: 50
    }

    // base scale for color
    let color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.median(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range(["#144265","whitesmoke","#dc351f"])

    // base scale for point plot
    $: XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range([0 + margin.left + 50 ,height - margin.right -50])

    $: yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range([height- margin.bottom , 0])

    $: radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

    // projection for the map
    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);

    projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);
    
    $: geoGenerator = d3.geoPath(projection)

    let currentStep;
    let value="revenu";
    const steps = [`<p>Prenons la température de surface pour ${selected} par exemple</p>`,
                    "<p>Voici les zones les plus fraiches</p>",
                    "<p>Les températures</p>",
                    "<p>Ici les points sont classés en fonction de la temperature</p>",
				    "<p>Ici la température de surface est mise en relation avec les revenus median de chaque secteur</p>",
                    `<p>nothing here</p>`
				   ];

    $: tweenedX = tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]),
        {
            duration: 500,
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

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 3))


    }
    const step2 = function() {
        projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, 700]], secteurs_geo);

        geoGenerator = d3.geoPath(projection)


        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 3))

    }
    const step3 = function() {
        
        radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

        yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range([height- margin.bottom , 0])

        width=width 

        isMap = false;
        tweenedX.set(other_point.map(d => d.centroid_lon = width/2))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }
    const step4 = function() {
        XScale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN != 0).map(d => d.REVENU_MOYEN)),d3.max(point_data.map(d => d.REVENU_MOYEN))])
        .range([0 + margin.left  + 50,width - margin.right - 50])

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
        .range([0 + margin.left + 50,width - margin.right -50])

        tweenedX.set(point_data.map(d => XScale(d.perc_ver)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }   
    const step6 = function() {

    }
    $: console.log(currentStep)

    $: if (currentStep == 0) {
        isMap = true
        class_name="map"
        annot_state = false
        step1()
    } else if (currentStep == 1) {
        isMap = true
        class_name= "map"
        annot_state = true
        step2()
    } else if (currentStep == 2) {
        isMap = true
        class_name="chart"
        value = "temp"
        annot_state = false
        step3()
    } else if (currentStep== 3) {
        isMap = false
        class_name="chart"
        value = "revenu"
        annot_state=false 
        step4()
    } else if (currentStep==4) {
        isMap = false
        class_name="chart"
        value = "verdure"
        step5()
    } else if (currentStep==5) {
        isMap = false
        class_name="chart"
        step6()
    }

    </script>

<svelte:window bind:innerHeight={height}></svelte:window>

<div class={class_name} bind:clientWidth={width}>
    <svg width={width} height={height}>
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
                style="stroke:white;fill:grey;stroke-width:0.5;stroke-opacity:1;fill-opacity:0.5;z-index:-100"
                />
            {/each}
        </g>
        <g>
            {#each secteurs_geo.features as secteur}
                <path d={geoGenerator(secteur)} 
                style="stroke:white;fill:grey;stroke-width:0.5;stroke-opacity:1;fill-opacity:0.5;z-index:-100"
                />
            {/each}
        </g>
        {/if}
        <g>
            {#each point_data as temp, index}
            <circle r={$tweendRad[index]}
            cx={$tweenedX[index]} 
            cy={$tweenedY[index]}
            fill={color_scale(temp.raster_value_x)} 
            stroke={isMap ? "none" : "black"}
            style="stroke-width:0.5;"/>
            {/each}
        </g> 
        {#if annot_state}
        <g>
            {#each annot as secteur}
                <path d={geoGenerator(secteur )} 
                fill="none"
                style="stroke:black; stroke-width:3;z-index:-10; stroke-opacity: 0.7"
                />
            {/each}
        </g>
        {/if}
          {#if !isMap}          
          <Axes
          width={width}
          height={height}
          value={value}/>
        {/if}
    </svg>
</div>

<Scrolly bind:value={currentStep}>
    {#each steps as text, i}
        {#if i == 5}
        <div class="step">
            <div class="step-content">
                <button on:click={() => { selected = undefined; console.log("click") }}><a href="#test">Click</a></button>
            </div>
        </div>
        {:else}
        <div class="step" class:active={currentStep === i}>
            <div class="step-content">
                {@html text}
            </div>
        </div>
        {/if}
    {/each}
</Scrolly>

<style>
    .chart {
    width: 60%;
    height: 100%;
    position: sticky;
    top: 0.1%;
    margin: auto;
    z-index: -10;
    }
    .map {
        width: 100%;
        height: 100%;
        position: sticky;
        top: 0.1%;
        margin: auto;
        z-index: -10;
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
        backdrop-filter: blur(3rem);

    }

	.step.active .step-content {
        background: rgba(234, 71, 12, 0.603);
        backdrop-filter: blur(3rem);
		color: whitesmoke;
        border-radius: 0.5rem;
        font-size: var(--font-size-base);
	}

</style>