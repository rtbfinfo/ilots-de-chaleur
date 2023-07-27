<script>
    import * as d3 from "d3"
    import { onMount } from "svelte";
    import Scrolly from "./components/scrolly.svelte";
    import Map from "./components/Map.svelte";
    import MapDensity from "./components/Map_density.svelte";
    export let data 
    const { secteur } = data
  

   console.log(secteur)

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

    $:  selected = "Liege"
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

    function Change () {
          promise = loadData()
    }

    let currentStep;
    let value = "NOMBRE_HAB"
    const steps = ["<p>Step 0!</p>", 
								 "<p>Step 1?</p>", 
								 "<p>Step 2.</p>"];
  
  $: if (currentStep == 0) {
    // Do something here
  } else if (currentStep == 1) {
    let value = "REVENU_MOYEN"
    promise = loadData()
  } else if (currentStep == 2) {
    // Or do something here!
  }
</script>



<div>
  <select bind:value={selected} id="selector" on:change={Change}>
    <option value="Liege">Liège</option>
    <option value="Namur">Namur</option>
    <option value="Mons">Mons</option>
    <option value="Charleroi">Charleroi</option>
    <option value="Tournai">Tournai</option>
  </select>
  <p>{selected}</p>
</div>

{#if selected !== "test"}
  {#await promise}
  <p>Load</p>
  {:then [secteur,LST, compl_data]}
    <Map geometry_data={secteur}
    point_data={LST}
    complete_geo={compl_data} />

    <MapDensity geometry_data={secteur}
    complete_geo={compl_data} 
    legend= value/> 
  {/await}
{/if}

<section>
  <div class="chart">
  {#if selected !== "test"}
    {#await promise}
      <p>Load</p>
    {:then [secteur,LST, compl_data]}
      <MapDensity geometry_data={secteur}
      complete_geo={compl_data} 
      legend= "NOMBRE_HAB"/> 
    {/await}
  {/if}
  </div>

	<Scrolly bind:value={currentStep}>
		{#each steps as text, i}
			<div class="step" class:active={currentStep === i}>
				<div class="step-content">
					{@html text}
				</div>
			</div>
		{/each}
	</Scrolly>
</section>

<iframe width="100%" height="500" frameborder="0"
  src="https://observablehq.com/embed/e5aea952f9339a61@142?cells=graph"></iframe>



<style>
    :root {
    --dark-blue : #144265;
    --light-blue: #0D738A;
    --redish : #DC351F;
    --light-orange: #D66819;
    --dark-orange: #DA4D1A;
  }

  :global(body) {
    background-color: rgb(174, 195, 207);
  }

  .chart {
    background: whitesmoke;
    width: 100%;
    height: 100%;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
    position: sticky;
    top: 10%;
    margin: auto;
    z-index: -100;
  }

  .step {
    height: 90vh;
    display: flex;
    place-items: center;
    justify-content: center;
  }

  .step-content {
    background: whitesmoke;
    color: #ccc;
    padding: .5rem 1rem;
    transition: background 500ms ease, color 500ms ease;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, .2);
  }

	.step.active .step-content {
		background: white;
		color: black;
	}

</style>
