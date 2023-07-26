<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import Map from "./components/Map.svelte";
    import { onMount } from "svelte";

    $: width = 700;
    $: height = 700;

    let secteurs =  []
    let LST = []
    $: compl_data = []
    $: compl_LST = []

    onMount(async () => {

      d3.json("https://gist.githubusercontent.com/Yheloww/0911856da6fcefb8c8e8289a44e498b5/raw/4d2f32b6cefcf342a573e6296c488ae61a1062dd/liege_secteur%2520(1).json").then((data) => {
      secteurs = data.features;
      compl_data = data
    })

    d3.json("https://gist.githubusercontent.com/Yheloww/b871de29011161706a3ae896690f65f7/raw/90e0574e594379bee3907f062048726526ff88b6/liege_sel_centroid.json").then((data) => {
      LST = data.features;
      compl_LST = data;
    })

      })

    $: projection = d3.geoMercator()
        .fitExtent([[0, 0], [width, width/2.5]], compl_data);
    
    $: console.log(LST)

    $: geoGenerator = d3.geoPath(projection)

    
    let color_scale = d3.scaleLinear()
        .domain([20,35,50])
        .range(["blue","white","red"])
    
</script>


<div bind:clientWidth={width} bind:clientHeight={height}></div>

<div id="content">
   <svg width={width} height={width/2}>
      <g>
        {#each LST as temp}
          <circle r="1.7"
          cx={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[0]} 
          cy={projection([temp.properties.centroid_lon, temp.properties.centroid_lat])[1]}
          fill={color_scale(temp.properties.raster_value)} 
          />

        {/each}
    </g>
    <g>
        {#each secteurs as data}
          <path d={geoGenerator(data)} 
          style="stroke:black;fill:none;stroke-width:0.4;"/>
        {/each}
    </g>
 
      

  </svg>
  </div>