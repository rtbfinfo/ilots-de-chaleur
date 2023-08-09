<script>
    import * as d3 from "d3"
    import AnimScrolly from "./AnimScrolly.svelte";


    export let point_data
    export let Belgium_geo
    export let secteurs_geo

    let width = 700;
    let height = 700;

    $: projection = d3.geoMercator()
    .fitExtent([[0, 0], [width, height]], Belgium_geo);

    $: geoGenerator = d3.geoPath(projection)

    const listCity = ["Liège","Charleroi","Namur","Mons"]

    let hover;
    let selected;
</script>


<section>
    <div class="chart"   bind:clientWidth={width}>
        <div id="content">
            <svg width={width} height=800>
                <!-- Fond de carte Belqigue -->
                <g>
                    {#each Belgium_geo.features as province}
                                 <path d={geoGenerator(province)} 
                                 style="stroke:whitesmoke;fill:grey;stroke-width:0.5;fill-opacity:0.2;stroke-opacity:0.5"
                                 />
                    {/each}
               </g>
               <!-- Agglomération qui renvoi le hover -->
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
                               on:mousedown={() => {
                                selected = city
                               }}
                           />
                       {/each}
                   </g>
               {/each}
            </svg>

        </div>
        {#if selected}
            <AnimScrolly
            selected={selected}
            point_data={point_data}
            secteurs_geo={secteurs_geo}
            width={width}
            belgium_geo={Belgium_geo}/>
        {/if}
    </div>
</section>


<style> 
    .chart {
    /* background: whitesmoke; */
    width: 50%;
    height: 80%;
    /* box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2); */
    position: sticky;
    top: 5%;
    margin: auto;
    z-index: 10;
    margin-bottom: 10rem;
    border-radius: 10rem;
  }
</style>