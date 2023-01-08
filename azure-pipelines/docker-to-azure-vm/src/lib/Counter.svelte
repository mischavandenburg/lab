<script lang="ts">
  import { slide } from "svelte/transition";
  let visible = false;
  let count: number = 0;
  const increment = () => {
    count += 1;
  };
</script>

<button
  on:mouseenter={() => {
    visible = true;
  }}
  on:mouseleave={() => {
    visible = false;
  }}
  id="button_a"
  class="border-black transition-all duration-300 border-2 rounded-2xl p-[10px]"
  on:click={increment}
>
  count is: <span class="font-bold">{count}</span>
</button>
{#if visible}
  <p class="mt-5 text-gray-600" in:slide={{ duration: 200 }} out:slide={{ duration: 200 }}>Click to increment value by 1!</p>
{/if}

<style>
  #button_a:hover {
    @apply rounded-lg;
    @apply bg-amber-100;
  }
</style>
