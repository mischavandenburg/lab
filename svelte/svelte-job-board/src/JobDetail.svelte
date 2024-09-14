<script>
    import { onMount } from "svelte";

    export let id;
    let job = null;

    onMount(async () => {
        // In a real app, you'd fetch this data from your API based on the id
        job = {
            id: id,
            title: "Senior DevOps Engineer",
            company: "TechCorp",
            location: "Amsterdam, Netherlands",
            tags: ["AWS", "Kubernetes", "Docker"],
            description:
                "We are looking for a Senior DevOps Engineer to join our team. The ideal candidate will have extensive experience with AWS, Kubernetes, and Docker.",
            requirements: [
                "5+ years of experience in DevOps",
                "Strong knowledge of AWS services",
                "Experience with Kubernetes and Docker",
                "Familiarity with CI/CD pipelines",
            ],
            salary: "€80,000 - €120,000",
        };
    });
</script>

{#if job}
    <div class="job-detail">
        <h1>{job.title}</h1>
        <h2>{job.company}</h2>
        <p class="location">{job.location}</p>
        <div class="tags">
            {#each job.tags as tag}
                <span class="tag">{tag}</span>
            {/each}
        </div>
        <h3>Description</h3>
        <p>{job.description}</p>
        <h3>Requirements</h3>
        <ul>
            {#each job.requirements as requirement}
                <li>{requirement}</li>
            {/each}
        </ul>
        <h3>Salary Range</h3>
        <p>{job.salary}</p>
    </div>
{:else}
    <p>Loading...</p>
{/if}

<style>
    .job-detail {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 20px;
    }
    h1 {
        margin: 0 0 10px 0;
        color: #333;
    }
    h2 {
        margin: 0 0 10px 0;
        color: #666;
    }
    .location {
        font-style: italic;
        color: #888;
    }
    .tags {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin: 10px 0;
    }
    .tag {
        background-color: #e0e0e0;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 0.8em;
    }
    h3 {
        margin: 20px 0 10px 0;
        color: #444;
    }
    ul {
        margin: 0;
        padding-left: 20px;
    }
</style>
