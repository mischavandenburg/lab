module managedCluster 'br/public:avm/res/container-service/managed-cluster:0.1.2' = {
  name: 'managedClusterDeployment'
  params: {
    // Required parameters
    name: 'mischacsmin001'
    primaryAgentPoolProfile: [
      {
        count: 1
        mode: 'System'
        name: 'systempool'
        vmSize: 'Standard_DS2_v2'
      }
    ]
    // Non-required parameters
    location: 'westeurope'
    managedIdentities: {
      systemAssigned: true
    }
  }
}
