<script>
    export let title
    export let subtitle
    $: width = 500
    $: height= 500
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
                // markers: true
            }
        })

        tl.to('circle', {
            scale : 2.5,
            transformOrigin: "center center"
        })
        })

</script>

<svelte:window bind:innerHeight={height}></svelte:window>


<svg width={width} height={height + height/2}>
    <circle id="circle" cx={width/2} cy={height/2} r=400 fill="var(--light-orange)"/>
</svg>
<div class="wrapper" bind:clientWidth={width}>
    <p class="decrypte">Décrypte</p>
    <h1 class=moyen>{title}</h1>
    <h1 class="big">les pauvres au <span class=chaud>chaud</span>, les riches au <span class="froid">frais</span></h1>
    <h3>{subtitle}</h3>
    <h4>journalistes: Ambroise Carton et Marie-Laure Mathot</h4>
    <h4>data et web dev: Héloïse Feldmann</h4>
</div>

<!-- <div class="test">
    <section class="chapeau">
      <div class="wrapper-text test" data-color="red">
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
          Rerum voluptatem laborum placeat enim adipisci voluptatum! 
          Dicta eos, aspernatur eaque facilis tempore, dolorem animi 
          ratione nobis minima, velit esse ut unde.</p>
        </div>
    </section>
</div> -->

<!-- {#each participants as person}
    <p>{person.nom}</p>
{/each} -->

<style>
    svg{
        position:absolute;
        /* z-index: -1; */
        opacity: 0.6;
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
        padding-inline: 1.5rem;
        backdrop-filter: blur(3rem);
    }   


    .big {
        font-size: var(--font-size-xxl);
        font-family: var(--font-title);
        color: white;
    }

    h3 {
        font-size: var(--font-size-lg);
        /* border-bottom: 4px solid var(--dark-orange); */
        padding-bottom: 2rem;
        max-width: 120rch;
        font-weight: 200;
    }

    h4{
        margin-block: 0;
        font-weight: 200;
        font-family: var(--font-title);
    }
    
    .froid {
        color: var(--light-blue);
    }
    .chaud {
        color: var(--dark-orange)
    }
    
    .moyen {
        max-width: 60rch;
        font-size: var(font-size-lg);
        font-family: var(--font-title);

    }

    .decrypte {
        font-weight: 200;
        margin-bottom: 2rem;
    }
    
    </style>