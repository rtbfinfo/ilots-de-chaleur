<script>
    import { contourDensity } from "d3";

    export let content
    export let index;
    $: width = 500;


    let colours = ["#1D2E3B", "#D66819", "#DC351F","#E7A779","#728A63","#728A63"]
</script>


<div class="wrapper" bind:clientWidth={width}>
    <h1>
        {content}
    </h1>
    <svg width={120} height={120} transform="scale(3)">
        <circle id="circle" cx={45} cy={45} r={20} fill={colours[index]}/>
    </svg>
</div>


<!-- <svg width="{width}" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg" transform="translate({width/4},0)">
    <g filter="url(#filter0_f_28_26)">
    <circle cx="0" cy="0" r="186" fill="url(#paint0_radial_28_26)"/>
    </g>
    <defs>
    <filter id="filter0_f_28_26" x="0" y="0" width="{width/2}" height="{height/2}" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
    <feFlood flood-opacity="0" result="BackgroundImageFix"/>
    <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
    <feGaussianBlur stdDeviation="34" result="effect1_foregroundBlur_28_26"/>
    </filter>
    <radialGradient id="paint0_radial_28_26" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(201 217) rotate(38.5653) scale(189.283)" >
    <stop stop-color="#D66819"/>
    <stop offset="1" stop-color="#D66819" stop-opacity="0.31"/>
    </radialGradient>
    </defs>
</svg>     -->



<style>

    .wrapper {
        max-width: 100ch;
        margin-left: auto;
        margin-block: 1rem;
        padding-inline: 1rem;
        margin-block: 7rem;
        text-align: left;
        margin-inline: auto;
    }
    h1 {
        line-height: 3rem;
        font-size: var(--font-size-xl);
        color: whitesmoke;
        font-weight: 600;
        font-family: var(--font-title);
        padding-top: 5rem;
        position: relative;
    }
    svg {
        position: absolute;
        z-index: -100;
        filter: blur(1rem);
        opacity: 0.95;
        /* border: 2px solid red; */
        top: 5rem;
    }

    @media screen and (max-width: 400px) {
        h1 {
            padding-top: 5rem;
        }
        .wrapper {
            margin-bottom: 2rem;
            margin-block: 5rem;
        }
    }
</style>