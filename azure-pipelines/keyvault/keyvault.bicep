@description('Location of the resource.')
param location string = resourceGroup().location

@description('Name of the KeyVault. Must be unique.')
param keyVaultName string

@description('KeyVault SKU')
@allowed([
  'standard'
  'premium'
])
param keyVaultSku string = 'standard'

resource kv 'Microsoft.KeyVault/vaults@2023-02-01' = {
  name: keyVaultName
  location: location
  properties: {
    sku: {
      name: keyVaultSku
      family: 'A'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
  }
}
