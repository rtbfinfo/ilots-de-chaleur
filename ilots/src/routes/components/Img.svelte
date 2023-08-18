<script>
    export let type
    export let img
    import { useLazyImage as lazyImage } from 'svelte-lazy-image';

</script>

<div class={"base "+type}>
    {#each img as im}
    <div class="card">
        <img 
        data-src={im} 
        alt="canetons"
        use:lazyImage
        />
    </div>
    {/each}
</div>



<style>
    img {
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
    @media (max-width: 400px) {
        .base {
            margin-inline: auto;
            display: block;
        }
    }
    
    
</style>