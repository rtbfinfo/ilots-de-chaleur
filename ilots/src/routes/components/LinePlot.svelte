<script>
    import * as d3 from "d3";
    export let MAR; 
    import { onMount } from "svelte";
    import Map from "./Map.svelte";

    let liege = MAR.filter(d => d.city == "Liège")
    let Charleroi = MAR.filter(d => d.city == "Charleroi")


    $: width = 500;
    let height = 800;

    const margin = {top: 20, right:120, left:20, bottom:30};

    

    const parseTime = d3.timeParse("%Y-%m-%d");

    $: xScale = d3.scaleTime()
                  .domain(d3.extent(liege, d => parseTime(d.year)))
                  .range([0, width])
    $: yScale = d3.scaleLinear([10,30], 
                                [height, 0])

    $: liege_line = d3.line()
             .x((d) => xScale(parseTime(d.year)))
             .y((d) => yScale(d["Tave MPI"]))
             .curve(d3.curveCatmullRom)(liege)

    $: Charleroi_line = d3.line()
            .x((d) => xScale(parseTime(d.year)))
            .y((d) => yScale(d["Tave MPI"]))
            .curve(d3.curveCatmullRom)(Charleroi)
</script>


<!-- <div bind:clientHeight={height}></div> -->

<div class="chart" bind:clientWidth={width}>
    <svg width={width} height=800>
        <g>
            <path
            d="{liege_line}"
            stroke="red"
            fill="none"/>
        </g>
        <g>
            <path
            d="{Charleroi_line}"
            stroke="white"
            fill="none"/>
        </g>
    </svg>
</div>


<style>
    .chart {
        max-width: 50%;
        margin-inline: auto;
    }
</style>