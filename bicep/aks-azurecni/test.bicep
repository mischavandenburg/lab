test testAKS 'aks.bicep' = {
  params: {
    clusterName: 'coffee'
    prefix: 'prod'

  }
}

assert testAKS = testAKS.resources.aksCluster.name == 'prod-coffee'
