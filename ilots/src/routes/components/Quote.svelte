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
        max-width: 50rem;
        margin-inline: auto;
        margin-block: 1rem;
        font-size: 20px;
        color: whitesmoke;
        font-weight: 200;
        font-family: var(--font-title);
        text-align: center;
        padding-inline: 1rem;
        font-style: italic;
    }
</style>