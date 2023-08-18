<script>
    import { onMount } from "svelte";
    import {gsap} from "gsap";


    let load = true

    onMount(() => {
        load = false
    })
</script>

{#if load}
<p class='loader'>Load</p>
{:else}
<slot />
{/if}


<style>
    @import url('https://fonts.googleapis.com/css2?family=Baskervville&family=Montserrat:wght@200;400;500&display=swap');

    .loader {
        font-size: var(--font-size-xxxl);
        color:whitesmoke;
        text-align: center;
        display: flex;
        justify-content: center;
        animation-name: animation;
        animation-duration: 1s;
        animation-iteration-count: infinite;
        font-family: 'Montserrat', sans-serif;
    }

    @keyframes animation {
        from {transform: scale(0.2);}
        to { transform: scale(2)}
    }
</style>
