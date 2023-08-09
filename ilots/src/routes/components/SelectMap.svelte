<script>
    import * as d3 from "d3"
    import { draw } from  "svelte/transition";
    import { tweened } from "svelte/motion";    
    import { onMount } from "svelte";
    import { feature } from "turf";


    export let Belgium_geo 
    export let secteurs_geo
    export let width

    // export let width 
    // export let height 
    let height = 700;

    $: projection = d3.geoMercator()
    .fitExtent([[0, 0], [width, height]], Belgium_geo);

    $: geoGenerator = d3.geoPath(projection)

    const listCity = ["Liège","Charleroi","Namur","Mons"]

    let hover;
    $: console.log(hover)

</script>


<g>
     {#each Belgium_geo.features as province}
                  <path d={geoGenerator(province)} 
                  style="stroke:whitesmoke;fill:grey;stroke-width:0.5;fill-opacity:0.2;stroke-opacity:0.5"
                  />
     {/each}
</g>
{#each listCity as city}  
    <g class={city}>
        {#each secteurs_geo.features.filter(d => d.properties.tx_munty_descr_fr == city) as secteur}

                <path d={geoGenerator(secteur)} 
                class={city}
                stroke={hover == city ? "var(--dark-orange)" : "var(--light-blue)"}
                fill={hover == city ? "var(--dark-orange)" : "var(--light-blue)"}
                on:mouseover={() => {
                    hover = city
                }}
            />
        {/each}
    </g>
{/each}
<p>{hover}</p>

