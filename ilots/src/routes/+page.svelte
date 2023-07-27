<script>
    import * as d3 from "d3"
    import { onMount } from "svelte";
    import { fade } from "svelte/transition";
  
    import Scrolly from "./components/scrolly.svelte";
    import Map from "./components/Map.svelte";
    import MapDensity from "./components/Map_density.svelte";


    export let data 
    const secteur = data.secteur
    const temp = data.temp

  
    let currentStep;
    $: value = "NOMBRE_HAB"
    const steps = ["<p>Step 0!</p>", 
								 "<p>Step 1?</p>", 
								 "<p>Step 2.</p>"];
  
  $: if (currentStep == 0) {
    value = "NOMBRE_HAB"
  } else if (currentStep == 1) {
    value = "REVENU_MOYEN"
  } else if (currentStep == 2) {
    value="raster_value"
  }
</script>


<section>
  <div class="chart" transition:fade={{duration:5000}}>
    <Map
    geometry_data={secteur.features}
    complete_geo={secteur}
    point_data={temp.features}
    legend={value}
    />
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
    width: 90%;
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
