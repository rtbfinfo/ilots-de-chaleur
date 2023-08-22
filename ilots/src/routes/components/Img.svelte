<script>
    export let type
    export let img
    export let legend
    export let alt

</script>

<div class={"base "+type}>
    {#each img as im, i}
    <div class="card">
        <img 
        src={im} 
        alt="test"
        />
        <p class="legend">{legend[i]}</p>
    </div>
    {/each}
</div>



<style>
    .legend  {
        line-height: 1.2rem;
        font-size: var(--font-size-sm);
        color: whitesmoke;
        font-weight: 400;
        border-left: 2px solid #D66819;
        padding-left: 5px;
    }
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
        max-width: 50%;
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
    @media screen and (max-width: 400px) {
        .base {
            margin-inline: auto;
            display: block;
        }
    }
    
    
</style>