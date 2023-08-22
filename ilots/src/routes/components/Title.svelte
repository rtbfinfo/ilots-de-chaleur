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

<style>

    .wrapper {
        max-width: 120rch;
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

    @media (max-width: 400px) {
        h1 {
            padding-top: 5rem;
        }
        .wrapper {
            margin-bottom: 4rem;
        }
    }

</style>