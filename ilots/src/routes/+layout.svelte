<script>
    import { onMount } from "svelte";
    import {gsap} from "gsap";


    let load = true

    onMount(() => {
        load = false
    })
</script>

{#if load}
<div class="container">
    <p>Chargement</p>
    <div class="preloader"></div> 
  </div>
{:else}
<slot />
{/if}


<style>
    @import url('https://fonts.googleapis.com/css2?family=Baskervville&family=Montserrat:wght@200;400;500&display=swap');

    p {
        font-size: 2em;
        color:#D66819;
        margin-top: 10rem;
    }
    .container{
  max-width: 400px;
  margin:0 auto;
  position: relative;
  text-align: center;
  }
  .preloader {
    margin:  20% auto 0;
    transform: translateZ(0);
  }

.preloader:before,
.preloader:after {
	content: '';
	position: absolute;
	top: 0;
}

.preloader:before,
.preloader:after,
.preloader {
	border-radius: 50%;
	width: 2em;
	height: 2em;
	animation: animation 1.2s infinite ease-in-out;
}

.preloader {
	animation-delay: -0.16s;
}

.preloader:before {
	left: -3.5em;
	animation-delay: -0.32s;
}

.preloader:after {
	left: 3.5em;
}

@keyframes animation {
	0%,
	80%,
	100% {
		box-shadow: 0 2em 0 -1em #D66819;
	}
	40% {
		box-shadow: 0 2em 0 0 #D66819;
	}
}
</style>
