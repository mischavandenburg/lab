<script lang="ts">
  import logo from "./assets/svelte.svg";
  import Counter from "./lib/Counter.svelte";
</script>

<main class="text-center">
  <img class="mx-auto mt-[10%]" src={logo} alt="Svelte Logo" />
  <h1 class="p-3 text-lg font-bold">Hello Typescript!</h1>

  <Counter />

  <p class="p-2 mt-10 text-sm">
    Visit <a href="https://svelte.dev">svelte.dev</a> to learn how to build Svelte apps.
  </p>

  <p class="p-2 text-sm text-gray-500">
    Check out <a href="https://github.com/sveltejs/kit#readme">SvelteKit</a> for the officially supported framework, also powered by Vite!
  </p>
</main>

<style>
  a {
    @apply text-blue-700;
  }
  a:hover {
    @apply underline;
  }
</style>
