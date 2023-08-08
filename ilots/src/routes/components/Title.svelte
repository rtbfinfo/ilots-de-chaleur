<script>
    import { contourDensity } from "d3";

    export let content
</script>

<div class="wrapper">
    <h1>
        {content}
    </h1>
</div>



<style>
    .wrapper {
        max-width: 90rch;
        margin-inline: auto;
        margin-block: 1rem;
        padding-inline: 1rem;
    }
    h1 {
        line-height: 1.7rem;
        font-size: var(--font-size-lg);
        color: whitesmoke;
        font-weight: 600;
    }
</style>