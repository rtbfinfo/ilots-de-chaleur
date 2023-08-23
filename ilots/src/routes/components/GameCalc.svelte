<script>
    import Img from "./Img.svelte";
    import { fade } from 'svelte/transition';

export let images
export let base
let placeholder = "choissisez..."
let index = -1;

let names_img = ["Revêtement clair","Isolation","Pelouse","Point d'eau","Moins de voitures","Fontaines","Ombres","Arrosage","Toitures","Toitures et façades", "Brumisateurs","Arbres"]
</script>

<div class="base">
    <div class="card">
        <a name="game"></a>
        {#if  base == "http://rtbfmedia.be/rtbfinfo/ICU_pics/Gamecalc_mobile_webp/"}
            <div class="selection">
                <select id="game" bind:value={index}>
                    {#if placeholder}
                    <option value="" disabled selected>{placeholder}</option>
                    {/if}
                    {#each names_img as img, i }
                    <option transition:fade
                    value={i}
                    >{img}</option>
                    {/each}
                </select>
            </div>
        {:else}
        <div class="selection">
            <div class="selection">
                {#each names_img as img, i }
                <div class="{index == i ? "sel" : "choices"}"
                transition:fade
                on:click={() => {
                    index = i
                }}>{img}</div>
                {/each}
            </div>
        </div>
        {/if}

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
    <div class="middle">
        <p class="legend">Source : Ademe, agence de la transition écologique en France</p>
    </div>
</div>


<style>
    #game {
        color: whitesmoke;
        background-color: var(--dark-blue);
        border-radius: 0.5rem;
        padding: 0.5rem;
        border: 1px var(--dark-blue) solid;
    }
    .choices {
        margin:0.5rem;
        background-color: var(--dark-blue);
        font-size: var(--font-size-base);
        font-family:  'Montserrat', sans-serif;
        padding:0.5rem;
        color: whitesmoke;
        text-align: center;
        border-radius: 0.5rem;
        width: fit-content;
        cursor: pointer;
        transition: all 500ms;
    }
    .sel {
        margin:0.5rem;
        background-color: #7FBC7F;
        font-size: var(--font-size-base);
        font-family:  'Montserrat', sans-serif;
        padding:0.5rem;
        color: whitesmoke;
        text-align: center;
        border-radius: 0.5rem;
        width: fit-content;
        cursor: pointer;
        transition: all 500ms;
    }
    .choices:hover{
        background-color: var(--light-orange);
    }
    .choices:active{
        background-color: 7FBC7F;
    }
    img {
        display: block;
        width: 100%;
        border-radius: 0.5rem;
    }
    .illu {
        position: relative;
        scroll-snap-align: end;
    }
    .base {
        max-width: 80rem;
        margin-inline: auto;
        gap: 1rem;
        margin-bottom: 5rem;
        scroll-snap-type: y mandatory;
        padding-top: 1.5rem;
        border-radius: 0.5rem;
    }
    .base .card {
        width: 100%;
        background-color: #7fbc7f87;
        padding-top: 1.5rem;

    }

    .base .middle {
        padding: 1em;
    }
    .legend {
        line-height: 1.2rem;
        font-size: var(--font-size-sm);
        color: whitesmoke;
        font-weight: 400;
        border-left: 2px solid #D66819;
        padding-left: 5px;
    }
    .img {
        flex-basis: 60%;
        z-index: 100;
    }
    .selection {
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        justify-content: center;
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