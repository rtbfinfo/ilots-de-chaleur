<script>
    import * as d3 from "d3"
    import Map from "./components/Map.svelte";
    import geoJson from "./components/liege_secteur.geojson"

    let projection = d3.geoEquirectangular;

    let geoGenerator = d3.geoPath()
                       .projection(projection)

    let u = d3.select('#content g.map')
              .selectAll("path")
              .data(geoJson.features)
              .join('path')
              .attr('d', geoGenerator);
</script>


<div id="content">
    <svg width="800px" height="400px">
      <g class="map"></g>
    </svg>
  </div>