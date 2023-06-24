// create a keyvault

param location string = resourceGroup().location

resource kv 'Microsoft.KeyVault/vaults@2023-02-01' = {
  name: 'mischacoffekeyvault866'
  location: location
  properties: {
    sku: {
      name: 'standard'
      family: 'A'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
  }
}
