# Dockerfile to Azure VM

Lab to build and deploy a Svelte app from a Dockerfile and deploy it to a VM hosted in Azure.

Naturally, Azure prefers that you deploy containers to services such as Azure Container Instances or App Services, so they don't provide modules for the pipelines to deploy to docker servers as far as I could tell.

I searched for a long time but I could not find a solution. In the end I just ran shell commands from the pipeline to run the container on on the server.

The pipeline uses the Build ID as a tag. It pushes to Docker Hub with a Service Connection configured in Azure DevOps.

www.mischavandenburg.com
