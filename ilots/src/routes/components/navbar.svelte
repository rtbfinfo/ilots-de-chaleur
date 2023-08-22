<script>
    import Fa from 'svelte-fa/src/fa.svelte'
    import { fade } from "svelte/transition";
    import { onMount } from "svelte";
    
    let y

    onMount(() => {
        let processScroll = () => {
          let docElem = document.documentElement,
            docBody = document.body,
            scrollTop = docElem["scrollTop"] || docBody["scrollTop"],
              scrollBottom = (docElem["scrollHeight"] || docBody["scrollHeight"]) - window.innerHeight,
            scrollPercent = scrollTop / scrollBottom * 100 + "%";
            document.getElementById("progress-bar").style.setProperty("--scrollAmount", scrollPercent);
        }
        document.addEventListener("scroll", processScroll)
    })
  
    </script>
  
  <svelte:window bind:scrollY={y} />
  
  {#if y > 50}
  
  <div id="progress-bar"></div>
  <nav class="fixed-nav-bar" in:fade>
  
        <a class="brand" href="https://rtbfmedia.be/rtbfinfo/ICU_pics/rtbf.svg" rel="noreferrer" target="_blank">
          <img src="./rtbf.svg" alt="RTBF Logo" />
        </a>
        
        <div class="share">
        <!-- svelte-ignore a11y-missing-content -->

        <a href="https://www.facebook.com/sharer/sharer.php?u=https://www.rtbf.be/article/11243914" rel="noreferrer" target="_blank" alt="Facebook Logo">
            <img src="https://rtbfmedia.be/rtbfinfo/ICU_pics/facebook.svg" alt="facebook Logo" />
        </a>
        <!-- svelte-ignore a11y-missing-content -->
        <a href="https://twitter.com/intent/tweet?text=https://www.rtbf.be/article/11243914" rel="noreferrer" target="_blank" alt="Twitter Logo">
            <img src="https://rtbfmedia.be/rtbfinfo/ICU_pics/twitter.svg" alt="twitter Logo" />
        </a>
    </div>
  
      </nav>
  
      {/if}
  
      
  
      <style>
  .fixed-nav-bar {
      position: fixed;
      align-items: flex-end;
      justify-content: flex-end;
      top: 0;
      left: 0;
      z-index: 9998;
      width: 100%;
      height: 40px;
      background-color: var(--light-orange);
      box-shadow: 0px 0px 10px gray;
      display: flex;
      line-height: 50px;
      opacity: 0.7;
    }
    
    nav img {
      height: 30px;
      transform: translateY(15%);
    }
    
    nav .brand {
      flex: 1;
      align-self: flex-start;
      height: 40px;
      margin-left: 20px;
    }
  .share{
      flex: -1;
      align-self: flex-end;
      height: 30px;
      margin-left: 20px;
      transform: translateY(-30%);
    }
  
    /* Progress bar */
  #progress-bar {
      --scrollAmount: 0%;
      width: var(--scrollAmount);
      background: linear-gradient(to right, #be3a0b var(--scrollAmount), transparent 0);
      width: 100%;
      
      height: 3px;
      position: fixed;
      top: 0;
      z-index:10000;
      margin-top: 37px;
    }
  
      </style>