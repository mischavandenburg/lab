<script>
    import { onMount } from 'svelte';
    import TagFilter from './TagFilter.svelte';
    import JobList from './JobList.svelte';
  
    let jobs = [];
    let tags = ['Azure', 'AWS', 'Linux', 'Kubernetes', 'Docker', 'CI/CD'];
    let selectedTags = [];
  
    onMount(async () => {
      // In a real app, you'd fetch this data from your API
      jobs = [
        { id: 1, title: 'Senior DevOps Engineer', company: 'TechCorp', tags: ['AWS', 'Kubernetes', 'Docker'] },
        { id: 2, title: 'Cloud Architect', company: 'CloudSolutions', tags: ['Azure', 'Kubernetes', 'CI/CD'] },
        { id: 3, title: 'Linux System Administrator', company: 'OpenSource Inc', tags: ['Linux', 'Docker'] },
      ];
    });
  
    function handleTagSelect(event) {
      selectedTags = event.detail;
    }
  
    $: filteredJobs = selectedTags.length > 0
      ? jobs.filter(job => selectedTags.every(tag => job.tags.includes(tag)))
      : jobs;
  </script>
  
  <h1>Dutch Kubernetes Freelancers Job Board</h1>
  <TagFilter {tags} on:tagSelect={handleTagSelect} />
  <JobList jobs={filteredJobs} />
  
  <style>
    h1 {
      text-align: center;
      color: #333;
    }
  </style>