<script>
    import Img from "./Img.svelte";
    import { fade } from 'svelte/transition';

export let images
let index = -1;

let names_img = ["Revêtement","Isolation","Pelouse","Point d'eau","Voitures","Fontaines","Ombres","Arrosage","Toitures","Toitures et façades", "Brumisateurs","Arbres"]
</script>

<div class="base">
    <div class="selection">
        {#each names_img as img, i }
        <div class="{index == i ? "sel" : "choices"}"
        transition:fade
        on:click={() => {
            index = i
        }}>{img}</div>
        {/each}

    </div>
    <div class="illu">
        <div class="fond img">                
            {#key index}
            <img 
            in:fade= {{delay: 250}}
            out:fade
            src={images.at(index)} 
            alt="canetons"
            />
            {/key}
        </div>
        <div class="img">
            <img 
            src={images.at(-1)} 
            alt="canetons"
            />
        </div>
    </div>

</div>


<style>
    .choices {
        margin:0.5rem;
        background-color: var(--dark-blue);
        font-size: var(--font-size-base);
        font-family:  'Montserrat', sans-serif;
        padding:1rem;
        color: whitesmoke;
        text-align: center;
        border-radius: 1.5rem;
        width: fit-content;
        cursor: pointer;
        transition: all 500ms;
    }
    .sel {
        margin:0.5rem;
        background-color: green;
        font-size: var(--font-size-base);
        font-family:  'Montserrat', sans-serif;
        padding:1rem;
        color: whitesmoke;
        text-align: center;
        border-radius: 1.5rem;
        width: fit-content;
        cursor: pointer;
        transition: all 500ms;
    }
    .choices:hover{
        background-color: var(--light-orange);
    }
    .choices:active{
        background-color: rgb(136, 222, 136);
    }
    img {
        display: block;
        width: 100%;
    }
    .illu {
        position: relative;
        scroll-snap-align: end;
    }
    .base {
        margin-inline: auto;
        display: flex;
        gap: 2rem;
        margin-bottom: 5rem;
        scroll-snap-type: y mandatory;
    }
    .big {
        max-width: 100%;
    }
    .img {
        flex-basis: 60%;
        z-index: 100;
    }
    .selection {
        flex-basis: 40%;
        margin-left: 2%;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        justify-content: end;
    }
    .fond {
        position: absolute;
    }

    /* div {
        border: 2px solid red
    } */

    @media (max-width: 400px) {
        .base {
            display: block;
        }
    }
</style>