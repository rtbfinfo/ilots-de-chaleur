<script>
    import Img from "./Img.svelte";
    import { fade } from 'svelte/transition';

export let images
export let base
let index = -1;

let names_img = ["Revêtement clair","Isolation","Pelouse","Point d'eau","Moins de voitures","Fontaines","Ombres","Arrosage","Toitures","Toitures et façades", "Brumisateurs","Arbres"]
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
            src={base + images.at(index)} 
            alt="canetons"
            />
            {/key}
        </div>
        <div class="img">
            <img 
            src={base + images.at(-1)} 
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
        gap: 1rem;
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

    @media screen and (max-width: 550px) {
        .base {
            display: block;
        }
    }
</style>