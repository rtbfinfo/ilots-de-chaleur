<script>
    import * as d3 from "d3"
    import * as turf from "turf";
    import Map from "./components/Map.svelte";
    import { onMount } from "svelte";

    const width = 500;
    const height = 500;
    onMount(async () => {

   Promise.all([
    d3.json("https://gist.githubusercontent.com/Yheloww/b871de29011161706a3ae896690f65f7/raw/90e0574e594379bee3907f062048726526ff88b6/liege_sel_centroid.json"),
    d3.json('https://gist.githubusercontent.com/Yheloww/0911856da6fcefb8c8e8289a44e498b5/raw/4d2f32b6cefcf342a573e6296c488ae61a1062dd/liege_secteur%2520(1).json')
   ]).then(function([centroid, secteur]) {

    let projection = d3.geoMercator()
        .fitExtent([[25, 25], [width, height]], secteur);;

        let color_scale = d3.scaleLinear()
        .domain([20,35,50])
        .range(["blue","white","red"])

        let geoGenerator = d3.geoPath()
                       .projection(projection)

        const svg = d3.select("#content")
        .append("svg")
        .attr("width", width)
        .attr("height", 700);

        // cercle
        svg.append('g').selectAll('path')
        .data(centroid.features)
        .enter().append("circle", ".pin")
        .attr("r", 1.7)
        .attr("fill", d => color_scale(d.properties.raster_value))
        .attr("transform", function(d) {
    return "translate(" + projection([
      d.properties.centroid_lon,
      d.properties.centroid_lat
        ]) + ")";
        });

  svg.append('g').selectAll('path')
        .data(secteur.features)
        .enter().append('path')
        .style("stroke", "black")
        .style("fill", "none")
        .style('stroke-width', 0.4 )
        .attr('d', geoGenerator)
           
   })

})

 
</script>


<div id="content">
  
  </div>