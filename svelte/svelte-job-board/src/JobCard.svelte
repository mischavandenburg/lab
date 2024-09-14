<script>
    import { Link } from "svelte-routing";
    export let job;
</script>

<div class="job-card">
    <Link to={`/job/${job.id}`}>
        <h2>{job.title}</h2>
    </Link>
    <p class="company">{job.company}</p>
    <div class="tags">
        {#each job.tags as tag}
            <span class="tag">{tag}</span>
        {/each}
    </div>
</div>

<style>
    .job-card {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 15px;
        background-color: #f9f9f9;
    }
    h2 {
        margin: 0 0 10px 0;
        color: #333;
    }
    .company {
        font-style: italic;
        color: #666;
    }
    .tags {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin-top: 10px;
    }
    .tag {
        background-color: #e0e0e0;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 0.8em;
    }
</style>
