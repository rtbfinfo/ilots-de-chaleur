<script>
    import * as d3 from "d3"
    import AnimScrolly from "./AnimScrolly.svelte";
    import { point } from "turf";


    export let point_data
    export let Belgium_geo
    export let secteurs_geo

    let width = 700;
    let height = 700;

    $: projection = d3.geoMercator()
    .fitExtent([[0, -500], [width , height *2]], Belgium_geo);

    $: geoGenerator = d3.geoPath(projection)

    const listCity = ["Liège","Charleroi","Namur","Mons"]

    let hover;
    let selected;
    $: other = {...point_data}
    let geo =   {...secteurs_geo}
    let data_map;

    $: if (selected) {
        if (selected == "Liège") {
        selected == "liege"
    }
    data_map = other.features.map(d => d.properties).filter(d => d.city == (selected == "Liège" ? "liege" : selected.toLowerCase()))
    //.filter(d => d.REVENU_MOYEN !== null)
    geo.features = secteurs_geo.features.filter(d => d.properties.city == (selected == "Liège" ? "liege" : selected.toLowerCase()))
       
    }
</script>


<section>
    <div class="chart"   bind:clientWidth={width}>
        <div id="content">
            <svg width={width} height="100vh">
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
            point_data={data_map}
            secteurs_geo={geo}
            width={width}
            belgium_geo={Belgium_geo}/>
        {/if}
    </div>
</section>


<style> 
    .chart {
    /* background: whitesmoke; */
    width: 100%;
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