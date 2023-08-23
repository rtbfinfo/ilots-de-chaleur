<script>
    import * as d3 from "d3"
    import { tweened } from "svelte/motion";    
    import Scrolly from "./scrolly.svelte";
    import Axes from "./Axes.svelte";
    import { fade } from 'svelte/transition';



    export let point_data
    export let selected
    export let secteurs_geo
    export let annot
    export let belgium_geo

    let hab = {
        Namur : "113.286",
        Liège : "195.346",
        Charleroi : " 203.785",
        bxl : "1.235.192",
        Mons: "96.465"
    }

    $: width = 500;
    let height = 500;
    let raster = "raster_value_y"

    let other_point = JSON.parse(JSON.stringify(point_data));

    let isMap=true;
    let emptyMap = true;
    let class_name="map";
    let annot_state=false;

    $: if (width < 400) {
    margin = {
        top: height/4,
        bottom: height/5,
        left: 30,
        right: 30    }
}

    let margin = {
        top: height/3,
        bottom: height/3,
        left: 400,
        right: 400
    }

    // base scale for color
    $: color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.median(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range(["#144265","whitesmoke","#dc351f"])

    // base scale for point plot
    $: XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range([0 + margin.left ,height - margin.right])

    $: yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_x)),d3.max(point_data.map(d => d.raster_value_x))])
        .range([height- margin.bottom , 0 + margin.top])

    $: radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

    // projection for the map
    $: projection = d3.geoMercator()
        .fitExtent([[0, 50], [width, height/1.1]], secteurs_geo);

    projection = d3.geoMercator()
        .fitExtent([[0, 50], [width, height/1.1]], secteurs_geo);
    
    $: geoGenerator = d3.geoPath(projection)

    let currentStep;
    let value="revenu";
    const steps = [`<p>Voici ${selected == "bxl" ? "la Région de Bruxelles-Capitale" : selected}, ${hab[selected]} habitants ... qui ne vivent pas tous dans les mêmes conditions.</p>`,
                    "<p>Ajoutons sur cette carte les températures moyennes du sol en juillet et août de 2013 à 2022. Les zones plus froides sont en <span style='background-color:blue;border-radius:5px;padding: 0 5px 0 5px'>bleu</span> et les zones plus chaudes sont en <span style='background-color:red;border-radius:5px;padding: 0 5px 0 5px'>rouge</span></p>",
                    "<p>Les zones les plus fraîches sont souvent des parcs, des forêts ou des cours d’eau.</p>",
                    "<p>Faisons maintenant la moyenne de ces températures pour chaque secteur statistiques. Cela nous sera utile dans l’étape suivante…</p>",
                    "<p>Prenons chaque quartier et mettons-les sur un graphique. Plus un cercle est grand, plus il y a d’habitants dans ce quartier. Nous remarquons que les cercles rouges foncés sont les plus grands: les zones les plus chaudes sont aussi les plus peuplées.</p>",
				    "<p> Si on met en parallèle les revenus médians et les températures, une tendance se dégage. Les points rouges se concentrent en haut à gauche du graphique : les zones qui subissent les plus hautes températures abritent des habitants aux revenus plus faibles. En revanche, dans la partie droite du graphique (là où les gens gagnent le plus), il y a surtout des points bleus (températures basses) et quasi pas de points rouges</p>",
                    "<p> Enfin, les zones où la végétation est la plus abondante sont aussi les plus fraîches.</p>"
				   ];

    $: tweenedX = tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]),
        {
            duration: 1000,
            delay: 0,

        }) 
    $: tweenedY =tweened(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[1]),  {
            duration: 500,
            delay: 0,

        })
    $: tweendRad = tweened(other_point.map(d => 2),  {
            duration: 500,
            delay: 0,

        })
    $: tweenedColor = tweened(point_data.map(d => color_scale(d.raster_value_y)))

    const step1 = function() {
        projection = d3.geoMercator()
        .fitExtent([[0, 50], [width, height/1.1]], secteurs_geo);

        geoGenerator = d3.geoPath(projection)


        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lat,d.centroid_lat])[1]))

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 3))


    }
    const step2 = function() {
        projection = d3.geoMercator()
        .fitExtent([[0, 50], [width, height/1.1]], secteurs_geo);

        geoGenerator = d3.geoPath(projection)


        tweenedX.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[0]))
        tweenedY.set(point_data.map(d => projection([d.centroid_lon,d.centroid_lat])[1]))

        tweendRad.set(other_point.map(d => d.NOMBRE_HAB = 3))

    }
    const step3 = function() {
        
        tweenedX.set(other_point.map(d => d.centroid_lon = width/2))

        radiusScale = d3.scaleSqrt()
        .domain([d3.min(point_data.map(d => d.NOMBRE_HAB)),d3.max(point_data.map(d => d.NOMBRE_HAB))])
        .range([5,20])

        yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.raster_value_y)),d3.max(point_data.map(d => d.raster_value_y))])
        .range([height - margin.bottom , 0 + margin.top])

        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))
        // tweenedColor.set(point_data.map(d => color_scale(d.raster_value_y)))

    }
    const step4 = function() {
        XScale = d3.scaleLinear()
        .domain([d3.min(point_data.filter(d => d.REVENU_MOYEN != 0).map(d => d.REVENU_MOYEN)),d3.max(point_data.map(d => d.REVENU_MOYEN))])
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
        .range([0 + margin.left,width - margin.right])
        console.log(point_data)

        tweenedX.set(point_data.map(d => XScale(d.perc_ver)))
        tweenedY.set(point_data.map(d => yScale(d.raster_value_y)))

        tweendRad.set(point_data.map(d => radiusScale(d.NOMBRE_HAB)))

    }   
    const step6 = function() {

    }
    $: console.log(currentStep)

    $: if (currentStep==0) {
        isMap = true
        emptyMap=true
        class_name="map"
        step1()
    } else if (currentStep == 1) {
        isMap = true
        emptyMap=false
        class_name="map"
        annot_state = false
        raster = "raster_value_x"
        step1()
    } else if (currentStep == 2) {
        isMap = true
        class_name= "map"
        annot_state = true
        raster = "raster_value_x"
        step2()
    }  else if (currentStep == 3) {
        isMap = true
        class_name= "map"
        annot_state = false
        raster = "raster_value_y"
        step2()
    } 
    else if (currentStep == 4) {
        isMap = false
        class_name="chart"
        value = "temp"
        step3()
        raster = "raster_value_y"
        annot_state = false
    } else if (currentStep== 5) {
        isMap = false
        class_name="chart"
        value = "revenu"
        annot_state=false 
        step4()
    } else if (currentStep==6) {
        isMap = false
        class_name="chart"
        value = "verdure"
        step5()
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
        {/if}
        {#if !emptyMap}
        <g transition:fade>
            {#each point_data as temp, index}
            <circle r={$tweendRad[index]}
            cx={$tweenedX[index]} 
            cy={$tweenedY[index]}
            fill={currentStep == 5 && temp.REVENU_MOYEN == 0 ? "none" : color_scale(temp[raster])} 
            stroke={isMap || (currentStep == 5 && temp.REVENU_MOYEN == 0) ? "none" : "var(--dark-blue)"}
            style="stroke-width:0.5;"/>
            {/each}
        </g> 
        {/if}
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
          value={value}
          margin={margin}/>
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
    max-width:100%; 
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
        justify-content: center;
        margin-right: 2vw;
    }

    .step-content {
        color: #ccc;
        padding: .5rem 1rem;
        transition: background 500ms ease, color 500ms ease;
        box-shadow: 1px 1px 10px rgba(0, 0, 0, .2);
        max-width: 25vw;

    }

	.step.active .step-content {
        background: rgba(234, 71, 12, 0.803);
		color: whitesmoke;
        border-radius: 0.5rem;
        font-size: var(--font-size-base);
	}

    @media screen and (max-width: 550px) {
        .chart {
            max-width: 100%;
        }
        .step-content {
            max-width: 75%;
        }
    }
</style>