<script>
    export let type
    export let img
</script>

<div class={"base "+type}>
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
    .base {
        margin-inline: auto;
        display: flex;
        padding: 1rem;
        gap: 2rem;
        margin-bottom: 5rem;;
    }
    .inline {
        max-width: 90rch;
    }
    .big {
        max-width: 100%;
    }
    .middle {
        max-width: 170rch;
    }
    .card {
        width: 100%;
        height: auto;
    }
    
    
</style>