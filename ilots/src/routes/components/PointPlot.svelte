<script>
    import * as d3 from "d3"

    export let point_data;
    export let value_yscale;

    $: width = 700;
    $: height = 700;

    let XScale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.NOMBRE_HAB)),d3.median(point_data.map(d => d.properties.NOMBRE_HAB)),d3.max(point_data.map(d => d.properties.NOMBRE_HAB))])
        .range([0,350,700])

    let yScale =d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.raster_value)),d3.median(point_data.map(d => d.properties.raster_value)),d3.max(point_data.map(d => d.properties.raster_value))])
        .range([0,350,700])

    let color_scale = d3.scaleLinear()
        .domain([d3.min(point_data.map(d => d.properties.raster_value)),d3.median(point_data.map(d => d.properties.raster_value)),d3.max(point_data.map(d => d.properties.raster_value))])
        .range(["blue","white","red"])

</script>

<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div class="wrapper">
    <svg width={width} height={width/2}>
    <g>
        {#each point_data as temp}
        <circle r="2.5"
        cx={XScale(temp.properties.NOMBRE_HAB)} 
        cy={yScale(temp.properties.raster_value)}
        fill={color_scale(temp.properties.raster_value)} 
        style="opacity:2;"/>
        {/each}
    </g>
    </svg>
</div>


<style>
    .wrapper {
        max-width: 500rem;
        margin-inline: auto;
    }
</style>