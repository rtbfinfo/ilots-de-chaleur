<script>
     import * as d3 from "d3"
     let width = 500;
     let  height = 500;

     let numRow = 80;
     let numCols = 80;

     $: fill = "grey"

     $: index = 0;

     let data = d3.range(numCols*numRow)

     $: yscale = d3.scaleBand()
     .range([0,width])
     .domain(d3.range(numRow))

     $: xscale = d3.scaleBand()
     .range([0,width])
     .domain(d3.range(numCols))

     function handleMouse(e,d) {
        index = d;
     }
</script>

<div bind:clientHeight={height} bind:clientWidth={width}></div>

<svg width={width} height={width/2}>
    <g>
        {#each data as d, i}
            <circle
            cx={ xscale(d % numCols)}
            cy={ yscale(Math.floor(d / numCols))}
            r={ width /200}
            fill={i == index ? "orange" : "grey"}
            on:mouseover={(e) => {
                handleMouse(e, d)
            }}
            on:focus={() => {
                fill = "#D66819"
            }}/>

        {/each}
    </g>
</svg>