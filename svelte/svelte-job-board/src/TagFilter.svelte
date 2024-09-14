<script>
    import { createEventDispatcher } from 'svelte';
  
    export let tags = [];
    let selectedTags = [];
    const dispatch = createEventDispatcher();
  
    function toggleTag(tag) {
      selectedTags = selectedTags.includes(tag)
        ? selectedTags.filter(t => t !== tag)
        : [...selectedTags, tag];
      dispatch('tagSelect', selectedTags);
    }
  </script>
  
  <div class="tag-filter">
    {#each tags as tag}
      <button
        class:selected={selectedTags.includes(tag)}
        on:click={() => toggleTag(tag)}
      >
        {tag}
      </button>
    {/each}
  </div>
  
  <style>
    .tag-filter {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 20px;
    }
    button {
      padding: 5px 10px;
      border: 1px solid #ccc;
      border-radius: 20px;
      background-color: white;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    button.selected {
      background-color: #007bff;
      color: white;
    }
  </style>