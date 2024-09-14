<script>
    import JobCard from './JobCard.svelte';
    export let jobs = [];
  </script>
  
  <div class="job-list">
    {#if jobs.length > 0}
      {#each jobs as job (job.id)}
        <JobCard {job} />
      {/each}
    {:else}
      <p>No jobs found matching the selected criteria.</p>
    {/if}
  </div>
  
  <style>
    .job-list {
      display: grid;
      gap: 20px;
    }
  </style>