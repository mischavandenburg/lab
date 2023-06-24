resource myFirstDeploymentScript 'Microsoft.Resources/deploymentScripts@2020-10-01' = {
  name: 'myFirstDeploymentScript'
  location: resourceGroup().location

  // can be AzurePowershell or Azure CLI
  kind: 'AzurePowerShell'

  // the script will be run in a container. We need to provide a Managed Identity to give the script the required permissions
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '/subscriptions/01234567-89AB-CDEF-0123-456789ABCDEF/resourcegroups/deploymenttest/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myscriptingid': {}
    }
  }
  properties: {
    azPowerShellVersion: '3.0'

    // in Bicep we use ''' to indicate multi line string
    scriptContent: '''
      $output = 'Hello Learner!'
      Write-Output $output

     // the $DeploymentScriptOutputs variable is created to return output back to the Bicep template
     // It needs to be a hash table
      $DeploymentScriptOutputs = @{}
      $DeploymentScriptOutputs['text'] = $output
    '''
    retentionInterval: 'P1D'
  }
}

output scriptResult string = myFirstDeploymentScript.properties.outputs.text
