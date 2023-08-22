<script>
    import * as d3 from "d3"
    import AnimScrolly from "./AnimScrolly.svelte";
    import { fade } from 'svelte/transition';
    import {gsap} from "gsap";
    import {ScrollTrigger} from "gsap/dist/ScrollTrigger";

    gsap.registerPlugin(ScrollTrigger);

    export let point_data
    export let Belgium_geo
    export let secteurs_geo
    export let annot

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

    const listCity = ["Liège","Charleroi","Namur","Mons","bxl"]

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
    <div class="chart" id="choix"  bind:clientWidth={width}>
        <div id="content">
        {#if selected}
              <div class='wrapper-text'>
                <a 
                style="text-align:center"
                transition:fade 
                on:click={() => {
                    selected = undefined;
                }} href="#choix">Revenez à la carte principale</a>
              </div>  
        {/if}
        {#if !selected}
            <svg width={width} height={height}  transition:fade >
                <!-- Fond de carte Belqigue -->
                <g>
                    {#each Belgium_geo.features as province}
                                 <path d={geoGenerator(province)} 
                                 style="stroke:whitesmoke;fill:none;stroke-width:0.5;fill-opacity:0.2;stroke-opacity:0.5"
                                 />
                    {/each}
               </g>
               <!-- Agglomération qui renvoi le hover -->
               {#each listCity as city}  
                   <g class="city"
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
                        ScrollTrigger.refresh()
                       }}
                    on:touchstart={(event) => {
                        hover = city;
                       }}
                    on:touchend={() => {
                        selected = city;
                        hover=undefined;
                        ScrollTrigger.refresh()
                    }
                    }
                    on:focus={() => {
                        hover=city
                    }}
                    tabIndex="0">
                       {#each secteurs_geo.features.filter(d => d.properties.city == (city == "Liège" ? "liege" : city.toLowerCase())) as secteur}
                               <path d={geoGenerator(secteur)} 
                               class=city
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
        <div class="hover" style="position:absolute;top:{100}px;left:{width/5}px;">
            <p>Je veux explorer {hover == undefined ? "..." : hover == "bxl" ? "Bruxelles" : hover} </p>
        </div>
        {/if}

        </div>
        {#if selected}
        <div transition:fade >
            <AnimScrolly
            selected={selected}
            point_data={data_map}
            secteurs_geo={geo}
            belgium_geo={Belgium_geo}
            annot={annot}
            />
        </div>
         
        {/if}
    </div>
</section>
{#if selected}
<div class="wrapper-text">
    <p><a 
        on:click={() => {
            selected = undefined;
        }}
        href="#choix">Revenez au choix de ville</a> ou <span class='orange'>scrollez vers le bas </span> pour continuer votre lecture. Dans la suite de cet article nous allons analyser les causes de ces différences de températures… Et voir quelles solutions peuvent être mises en place. </p>
</div>
{/if}

<style> 

  .city {
    transition: all 500ms ease;
    cursor: pointer;
  }
  .wrapper-text {
        max-width: 90rch;
        margin-inline: auto;
        margin-block: 2rem;
        line-height: 2.5rem;
        font-size: var(--font-size-md);
        color: whitesmoke;
        font-weight: 500;
        padding-inline: 1rem;
    }
    .hover {
        color: whitesmoke;
        background-color: rgba(234, 71, 12, 0.703);
        border-radius: 0.5rem;
        padding-inline: 1rem;
        font-size: var(--font-size-md);
        transition: all 300ms ease;
   }
    .orange {
        color: rgba(234, 71, 12);
    }
    a {
        text-decoration: none;
        color: whitesmoke;
        background-color: rgba(234, 71, 12, 0.603);
        border-radius: 0.5rem;
        padding: 0.5rem;
        transition: all 750ms;

    }
    a:hover {
        color:rgba(234, 71, 12, 0.603);;
        background-color: whitesmoke;
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