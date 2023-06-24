// deploy a simple aks cluster with one node pool

param location string = resourceGroup().location

resource aksCluster 'Microsoft.ContainerService/managedClusters@2023-03-02-preview' = {
  name: 'coffeecluster'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    kubernetesVersion: '1.25.6'
    enableRBAC: true
    dnsPrefix: 'akscluster'
    agentPoolProfiles: [
      {
        name: 'nodepool1'
        mode: 'System'
        count: 1
        vmSize: 'Standard_DS2_v2'
        osType: 'Linux'
        osDiskSizeGB: 30
      }
    ]
  }
}
