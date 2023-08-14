<script>
    export let type
    export let img
</script>

<div class={"base "+type}>
    {#each img as im}
    <div class="card">
        <video muted playsinline autoplay loop disablepictureinpicture>
            <source src="{im}" type="video/mp4" />
            Your browser does not support the video tag.
          </video>        
    </div>
    {/each}
</div>



<style>
    video {
        display: block;
        width: 100%;
    }
    .base {
        margin-inline: auto;
        display: flex;
        padding: 1rem;
        gap: 2rem;
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