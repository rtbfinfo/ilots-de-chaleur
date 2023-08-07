<script>
    export let content
    export let type

</script>
<div class="wrapper">
    <p>{content}</p>
</div>

<style>
        .wrapper {
        max-width: 90rch;
        margin-inline: auto;
        margin-block: 2rem;
        line-height: 1.7rem;
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 400;
    }
</style>