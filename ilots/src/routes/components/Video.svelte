<script>
    export let type
    export let img
    export let legend
</script>

<div class={"base "+type}>
    {#each img as im, i}
    <div class="card">
        <video muted playsinline autoplay loop disablepictureinpicture>
            <source src="{im}" type="video/mp4" />
            Your browser does not support the video tag.
          </video>   
        <p class="legend">{legend[i]}</p>     
    </div>
    {/each}
</div>



<style>
    .legend {
        line-height: 1.2rem;
        font-size: var(--font-size-sm);
        color: whitesmoke;
        font-weight: 400;
        border-left: 2px solid #D66819;
        padding-left: 5px;
    }

    video {
        display: block;
        width: 100%;
        margin-bottom: 1rem;
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
    
    @media screen and (max-width: 550px) {
        .base {
            margin-inline: auto;
            display: block;
        }
    }
    
</style>