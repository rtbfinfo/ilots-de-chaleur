<script>
    export let title
    export let subtitle
    $: width = 500
    // export let participants
    import {gsap} from "gsap";
    import {ScrollTrigger} from "gsap/dist/ScrollTrigger";
    import { onMount } from "svelte";
 
    onMount(() => {


        gsap.registerPlugin(ScrollTrigger);

        let tl = gsap.timeline({
            scrollTrigger: {
                trigger:"#circle",
                start: "top top",
                end: "bottom top",
                scrub: true,
                // pin: true,
                anticipatePin: 1,
                markers: true
            }
        })

        tl.to('circle', {
            scale : 3,
            transformOrigin: "center center"
        })
        })



</script>
<svg width={width} height=950>
    <circle id="circle" cx={width/2} cy={400} r=350 fill="var(--dark-orange)"/>
</svg>
<div class="wrapper" bind:clientWidth={width}>
    <h1>{title}</h1>
    <h3>{subtitle}</h3>
   
</div>

<!-- {#each participants as person}
    <p>{person.nom}</p>
{/each} -->

<style>
    svg{
        position:absolute;
        /* z-index: -1; */
        opacity: 0.5;
        /* filter:blur(3rem) */
    }
        .wrapper {
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 600;
        text-align: center;
        height: 100vh;
        /* background-color: var(--dark-orange); */
        margin: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-inline: 1rem;
        backdrop-filter: blur(3rem);
    }   


    h1 {
        margin-top: 8rem;
        font-size: var(--font-size-xxxl);
        max-width: 100rch;
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: white;
        margin-bottom: 8rem;
    }

    h3 {
        font-size: var(--font-size-lg);
        border-bottom: 4px solid var(--dark-orange);
        padding-bottom: 2rem;
        max-width: 150rch;
    }
</style>