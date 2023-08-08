<script>
    export let content
</script>
<div class="wrapper">
    <p>"{content}"</p>
</div>

<style>
    p {
        text-align: left;
        border-left: 10px solid var(--dark-orange);
        padding-left: 0.5rem;

    }
        .wrapper {
        max-width: 90rch;
        margin-inline: auto;
        margin-block: 1rem;
        font-size: var(--font-size-lg);
        color: whitesmoke;
        font-weight: 200;
        font-family: Georgia, 'Times New Roman', Times, serif;
        text-align: center;
        padding-inline: 1rem;
    }
</style>