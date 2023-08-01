<script>
    import {gsap} from "gsap";
    import {ScrollTrigger} from "gsap/dist/ScrollTrigger";
    import Lenis from '@studio-freight/lenis';
    import { onMount } from "svelte";


    onMount(() => {
        
    gsap.registerPlugin(ScrollTrigger);

    let tl = gsap.timeline({
        scrollTrigger: {
            trigger:".content",
            start: "top top",
            end: "bottom top",
            pin: true,
            anticipatePin: 1,
            markers: true
        }
    })

    tl.to('.displacement', {
        attr: {
            r: 800
        },
    })
            //smooth scrll 
    const lenis = new Lenis()

    lenis.on('scroll', (e) => {
    console.log(e)
    })

    function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    })


</script>

<div class="content">
    <svg  viewBox="0 0 1440 1024" fill="none" preserveAspectRatio="xMidYmin slice">
        <defs>
            <filter id="displacementFilter">
                <feTurbulence type="fractalNoise" baseFrequency="0.01" numOctaves="1" result="noise" />
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="50" xChannelSelector="R" yChannelSelector="6" />
            </filter>
            <mask id="circleMask">
                <circle cx="600" cy="400" r="0" fill="white" class="displacement"/>
            </mask>
        </defs>
        
        <rect fill="#FDEEC6" width="100%" height="100%" mask="url(#circleMask)"/>
    </svg>
</div>



<style>

.displacement {
    filter: url(#displacementFilter)
}

svg {
    width: 100%;
    height: 100vh;
    position: absolute;
    z-index: -1;
}


</style>