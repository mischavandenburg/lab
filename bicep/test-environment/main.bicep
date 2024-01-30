// deploy a simple aks cluster with one node pool

@description('Location of the AKS cluster')
param location string = resourceGroup().location

@description('Name of the AKS cluster')
param clusterName string

@description('Kubernetes Version')
param kubernetesVersion string

@description('Enable RBAC')
param enableRBAC bool = true

@description('Enable auto scaling')
param autoScale bool = true

@description('Enable KEDA')
param enableKEDA bool = false

@description('minimum number of nodes')
param minCount int = 1

@description('maximum number of nodes')
param maxCount int = 3

resource aksCluster 'Microsoft.ContainerService/managedClusters@2023-03-02-preview' = {
  name: clusterName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    kubernetesVersion: kubernetesVersion
    enableRBAC: enableRBAC
    dnsPrefix: 'akscluster'
    agentPoolProfiles: [
      {
        name: 'system'
        mode: 'System'
        count: 1
        vmSize: 'Standard_B4ms'
        osType: 'Linux'
        osDiskSizeGB: 30
        enableAutoScaling: autoScale
        minCount: minCount
        maxCount: maxCount
      }
      {
        name: 'workload'
        mode: 'User'
        count: 1
        vmSize: 'Standard_B4ms'
        osType: 'Linux'
        osDiskSizeGB: 30
        enableAutoScaling: autoScale
        minCount: minCount
        maxCount: maxCount
      }
    ]
  }
  workloadAutoScalerProfile: {
      keda: {
        enabled: enableKEDA
      }
}
