<script>
    export let title
    export let subtitle
    let width;
    let height;
    let radius= 375;
    $: hauteur = height/2;
    import {gsap} from "gsap";
    import {ScrollTrigger} from "gsap/dist/ScrollTrigger";
    import { onMount } from "svelte";
 

    $: if (width < 400) {
        radius= 175
        hauteur= height/2
    }
    onMount(() => {


        gsap.registerPlugin(ScrollTrigger);

        let tl = gsap.timeline({
            scrollTrigger: {
                trigger:"#circle",
                start: "top top",
                end: "bottom top",
                scrub: true,
                anticipatePin: 1,
            }
        })

        tl.to('circle', {
            scale : 2.5,
            transformOrigin: "center center"
        })
        })

</script>


<svelte:window bind:innerHeight={height}></svelte:window>

<!-- 
<svg width={width} height={height}>
    <circle id="circle" cx={width/2} cy={height/2} r={radius} fill="var(--light-orange)"/>
</svg> -->

<div class="wrapper" bind:clientWidth={width}>
    <p class="decrypte">Décrypte</p>
    <h1 class=moyen>{title}</h1>
    <h1 class="big">Les pauvres au <span class=chaud>chaud</span>, les riches au <span class="froid">frais</span></h1>
    <h3>{subtitle}</h3>
    <h4>Journalistes: Ambroise Carton et Marie-Laure Mathot</h4>
    <h4>Data et web dev: Héloïse Feldmann</h4>
    <div class="mouse_wheel">
        <div class="anim-scroll"></div>
        <div class="anim-scroll--wheel"></div>
    </div>
    <svg width={width} height={height}>
        <circle id="circle" cx={width/2} cy={height/2} r={radius} fill="var(--light-orange)"/>
    </svg>
    <div class='video'>
        <video muted playsinline autoplay loop disablepictureinpicture>
            <source src="https://rtbfmedia.be/rtbfinfo/ICU_pics/liege.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video> 
    </div>
</div>

<style>
    .video {
        width: 100%;
        position:absolute;
        z-index: -100;
        
    }
    video {
        width: 100%;
        height: 100vh;
        object-fit: cover;
    }
    svg{
        position:absolute;
        z-index: -1;
        opacity: 0.9;
        filter:blur(2.5rem)
    }
        .wrapper {
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 600;
        text-align: center;
        height: 100vh;
        margin: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-inline: 1.5rem;
        backdrop-filter: blur(3rem);
        position: relative;
        text-shadow: 1px 1px 10px rgb(165, 158, 158);
    }   

    .big {
        font-size: var(--font-size-xxl);
        font-family: var(--font-title);
        color: white;
    }

    h3 {
        font-size: var(--font-size-md);
        /* border-bottom: 4px solid var(--dark-orange); */
        padding-bottom: 2rem;
        max-width: 120rch;
        font-weight: 400;
    }

    h4{
        margin-block: 0;
        font-weight: 400;
        font-family: var(--font-title);
    }
    
    .froid {
        color: var(--light-blue);
    }
    .chaud {
        color: var(--redish);
        
    }
    
    .moyen {
        max-width: 60rch;
        font-size: var(--font-size-base);
        font-family: var(--font-title);

    }

    .decrypte {
        font-weight: 200;
        margin-bottom: 2rem;
    }
    
    .mouse_wheel {
    align-items: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    z-index: 1;
    position: absolute;
        bottom: 10%;
    }
    .anim-scroll {
    border: 2px solid #fff;
    border-radius: 22px;
    height: 40px;
    position: relative;
    width: 20px;
    z-index: 1;
    }
    .anim-scroll--wheel {
    animation: scroll 2.5s ease infinite;
    background: #fff;
    border-radius: 30px;
    height: 8px;
    left: calc(50% - 1.5px);
    position: absolute;
    right: 50%;
    top: 8px;
    width: 3px;
    }
    @keyframes scroll {
    0% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(16px);
    }
    51% {
        opacity: 1;
    }
    100% {
        opacity: 0;
        transform: translateY(0);
    }
    }
    </style>