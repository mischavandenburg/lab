Example files for using the Azure CSI secret operator with a service principal from a local cluster.

You can only use service principal authentication outside of azure.

Secret needs to be mounted to be able to be synched.

it took me hours to figure out you need to set nodePublisherRef on the volume mount for it to work.
