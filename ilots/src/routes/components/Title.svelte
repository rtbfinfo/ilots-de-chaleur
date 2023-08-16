<script>
    import { contourDensity } from "d3";

    export let content
    export let index;
    let width;
    let height;
    let position = 3.2
    let positionY = 12.5
    let radius = 75;

    $: if (width < 400) {
        radius = 37;
        positionY= 7;
        position= 5;
    }

    let colours = ["#1D2E3B", "#D66819", "#DC351F","#E7A779","#728A63","#728A63"]
</script>

<svelte:window bind:innerHeight={height} bind:innerWidth={width}></svelte:window>

<svg width={width} height={height}>
    <circle id="circle" cx={width/position} cy="{positionY}rem" r={radius} fill={colours[index]}/>
</svg>

<div class="wrapper">
    <h1>
        {content}
    </h1>
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
        max-width: 175rch;
        margin-left: auto;
        margin-block: 1rem;
        padding-inline: 1rem;
        margin-bottom: 7rem;
    }
    h1 {
        line-height: 1.9rem;
        font-size: var(--font-size-xl);
        color: whitesmoke;
        font-weight: 600;
        font-family: var(--font-title);
        padding-top: 11rem;
    }
    svg {
        position: absolute;
        z-index: -100;
        filter: blur(1.5rem);
        opacity: 0.95;
    }

    @media (max-width: 400px) {
        h1 {
            padding-top: 5rem;
        }
        .wrapper {
            margin-bottom: 4rem;
        }
    }
</style>