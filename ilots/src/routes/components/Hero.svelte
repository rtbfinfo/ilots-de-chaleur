<script>
    export let title
    export let subtitle
    // export let participants

</script>
<div class="wrapper">
    <h1>{title}</h1>
    <h3>{subtitle}</h3>
</div>

<!-- {#each participants as person}
    <p>{person.nom}</p>
{/each} -->

<style>
        .wrapper {
        font-size: var(--font-size-base);
        color: whitesmoke;
        font-weight: 600;
        text-align: center;
        height: 100vh;
        background-color: var(--dark-orange);
        margin: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-inline: 1rem;
    }   


    h1 {
        margin-top: 0;
        font-size: var(--font-size-xxxl);
        max-width: 100rch;
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: var(--dark-blue);
    }

    h3 {
        font-size: var(--font-size-lg);
    }
</style>