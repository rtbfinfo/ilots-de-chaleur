<script>
    export let type
    export let img
</script>

<div class={type}>
    {#each img as im}
    <div class="card">
        <img 
        src={im} 
        alt="canetons"
        />
    </div>
    {/each}
</div>



<style>
    img {
        display: block;
        width: 100%;
    }
    .inline {
        max-width: 90rch;
        margin-inline: auto;
        display: flex;
        padding: 1rem;
        gap: 2rem;
    }
    .multiple {
        margin-inline: auto;
        max-width: 100%;
        display: flex;
        padding: 1rem;
        gap: 2rem;
    }
    .card {
        width: 100%;
        height: auto;
    }
    
</style>