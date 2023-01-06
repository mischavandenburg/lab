# Static Quote App

A simple flask app that displays a quote, built and pushed to Docker Registry with an Azure pipeline. 

I had to do some hacking to update Variable Groups, which is not natively supported. Interestingly, you can read from them in pipelines, but there is no functionality (yet) to update them. So I had to call the CLI from the pipeline.

Used in this blog post:

https://mischavandenburg.com/zet/articles/lab-argocd-azure-pipelines/
