<script>
	import { Router, Link, Route } from "svelte-routing";
	import JobBoard from './JobBoard.svelte';
	import JobDetail from './JobDetail.svelte';
  
	export let url = "";
  </script>
  
  <Router {url}>
	<nav>
	  <Link to="/">Home</Link>
	</nav>
  
	<main>
	  <Route path="/" component={JobBoard} />
	  <Route path="/job/:id" component={JobDetail} />
	</main>
  </Router>
  
  <style>
	main {
	  max-width: 800px;
	  margin: 0 auto;
	  padding: 20px;
	}
	nav {
	  padding: 1em;
	  background-color: #f0f0f0;
	}
	:global(a) {
	  color: #007bff;
	  text-decoration: none;
	}
  </style>