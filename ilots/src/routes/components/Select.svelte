<script>
    import * as d3 from "d3"
    import AnimScrolly from "./AnimScrolly.svelte";
    import { point } from "turf";


    export let point_data
    export let Belgium_geo
    export let secteurs_geo
    export let annot
    // export let selected

    let width = 700;
    let height = 700;

    let height_map = -500;
    let width_change = 0;
    let rechange= 0;

    $: if (width < 400) {
        height_map = -750;
        width_change = -200;
        rechange = 100;
    }
    $: projection = d3.geoMercator()
    .fitExtent([[width_change, height_map], [width + rechange, height*2]], Belgium_geo);

    $: geoGenerator = d3.geoPath(projection)

    const listCity = ["Liège","Charleroi","Namur","Mons"]

    let hover;
    let mouseX;
    let selected;
    let mouseY;
    $: other = {...point_data}
    let geo =   {...secteurs_geo}
    let data_map;


    $: console.log(selected)

    $: if (selected) {
        if (selected == "Liège") {
        selected == "liege"
    }
    data_map = other.features.map(d => d.properties).filter(d => d.city == (selected == "Liège" ? "liege" : selected.toLowerCase()))
    //.filter(d => d.REVENU_MOYEN !== null)
    geo.features = secteurs_geo.features.filter(d => d.properties.city == (selected == "Liège" ? "liege" : selected.toLowerCase()))
       
    }
</script>

<svelte:window bind:innerHeight={height}></svelte:window>

<section>
    <div class="chart"   bind:clientWidth={width}>
        <div id="content">

        {#if !selected}
            <svg width={width} height={height}>
                <!-- Fond de carte Belqigue -->
                <g id="choix">
                    {#each Belgium_geo.features as province}
                                 <path d={geoGenerator(province)} 
                                 style="stroke:whitesmoke;fill:none;stroke-width:0.5;fill-opacity:0.2;stroke-opacity:0.5"
                                 />
                    {/each}
               </g>
               <!-- Agglomération qui renvoi le hover -->
               {#each listCity as city}  
                   <g class={city}
                   on:mouseover={(event) => {
                    hover = city
                    }}
                    on:mouseenter= {(event) => {
                        mouseX = event.clientX;
                        mouseY = event.clientY;
                    }}
                    on:mousedown={(event) => {
                        selected = city
                        hover = undefined;
                       }}
                    on:touchstart={(event) => {
                        selected = city
                        hover = undefined;
                       }}>
                       {#each secteurs_geo.features.filter(d => d.properties.tx_munty_descr_fr == city) as secteur}
                               <path d={geoGenerator(secteur)} 
                               class={city}
                               stroke={hover == city ? "var(--dark-orange)" : "var(--light-blue)"}
                               fill={hover == city ? "var(--dark-orange)" : "var(--light-blue)"}
                               on:mouseleave={() => {
                                    hover = undefined;
                               }}
                           />
                       {/each}
                   </g>
               {/each}
            </svg>
        {/if}
        
        {#if hover}
        <div class="hover" style="position:absolute;top:{mouseY}px;left:{mouseX}px;">
            <p>{hover}</p>
        </div>
        {/if}

        </div>
        {#if selected}
            <AnimScrolly
            selected={selected}
            point_data={data_map}
            secteurs_geo={geo}
            belgium_geo={Belgium_geo}
            annot={annot}
            />
        {/if}
    </div>
</section>
{#if selected}
<div class="wrapper">
    <button 
    on:click={() => {
        selected = undefined;
        console.log("click")
    }}><a href="#choix">Retour au choix de ville</a></button>
</div>
{/if}

<style> 
    .hover {
        color: whitesmoke;
        background-color: rgba(234, 71, 12, 0.603);
        border-radius: 1rem;
        padding: 2rem;

    }
    .wrapper {
    display: flex;
    justify-content: center;
    padding: 5rem;
    }
    button {
        font-size: var(--font-size-lg);
        padding: 0.5rem;
        text-decoration: none;
        color: var(--light-orange);
        background-color: var(--light-orange);
        border-radius: 1rem;
        border:none;
        transition: all 500ms;
    }
    button:hover {
        background-color: whitesmoke;
    }
    a {
        text-decoration: none;
        color: whitesmoke;
        transition: all 500ms;
    }
    a:hover {
        color: var(--light-orange)
    }
    .map {
    width: 100%;
    height: 80%;
    position: sticky;
    top: 5%;
    margin: auto;
    z-index: 10;
    border-radius: 10rem;
  }
  .chart {
   max-width: 100%;
    height: 80%;
    position: sticky;
    top: 5%;
    margin: auto;
    z-index: 10;
    border-radius: 10rem;
  }

  @media (max-width: 400px) {
    .chart {
        max-width: 150%;
    }
  }
</style>