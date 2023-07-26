<script>
    import Map from "./components/Map.svelte";
    import MapDensity from "./components/Map_density.svelte";
    import * as d3 from "d3"
    import * as turf from "turf";
    import { onMount } from "svelte";

    let cities_object = [
      {
        name : "Liege",
        secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/liege_revenu_densite%2520(1).json",
        lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/liege_sel_centroid.json"
      },
      {
        name : "Charleroi",
        secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/charleroi_revenu_densite%2520(1).json",
        lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/charleroi_centroid.json"
      },
      {
        name : "Namur",
        secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/namur_revenu_densite%2520(1).json",
        lst :"https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/namur_sel_centroid.json"
      },
      {
        name : "Mons",
        secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/mons_revenu_densite%2520(1).json",
        lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/mons_sel_centroid.json"

      },
      {
        name : "Tournai",
        secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/tournai_revenu_densite%2520(1).json",
        lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/tournai_sel_centroid.json"

      }
    ]

    $:  selected = null

    // $: LST_link= cities_object.filter(data => data.name === selected)[0].lst
    // $: secteur_link= cities_object.filter(data => data.name === selected)[0].secteur



    // loading the data
    async function loadData() {
    
    selected = selected
    let LST_link = cities_object.filter(data => data.name === selected)[0].lst
    let secteur_link = cities_object.filter(data => data.name === selected)[0].secteur

    console.log(secteur_link)

    const res = await fetch(secteur_link)
    const resp = await fetch(LST_link)
    const secteur = await res.json()
    console.log()
    const compl_datas = await resp.json()

    return [secteur.features, compl_datas.features, secteur]
    }


  
    let promise = loadData()


</script>

<div>
  <select bind:value={selected} id="selector" on:change={() => {
    promise = loadData()
  }}>
    <option value="Liege">Liège</option>
    <option value="Namur">Namur</option>
    <option value="Mons">Mons</option>
    <option value="Charleroi">Charleroi</option>
    <option value="Tournai">Tournai</option>
  </select>
  <p>{selected}</p>
</div>

{#if selected}
  {#await promise}
  <p>Load</p>
  {:then [secteur,LST, compl_data]}
    <Map geometry_data={secteur}
    point_data={LST}
    complete_geo={compl_data} />

    <MapDensity geometry_data={secteur}
    complete_geo={compl_data} 
    legend= "NOMBRE_HAB"/> 
  {/await}
{/if}

<style>
  .test {
    display: flex;
    width: 100%;
    height: 100% ;
  }
</style>