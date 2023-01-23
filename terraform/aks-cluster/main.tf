provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "mischa_aks" {
  name     = "${var.prefix}-k8s-resources"
  location = var.location
}

resource "azurerm_kubernetes_cluster" "mischa_aks" {
  name                = "${var.prefix}-k8s"
  location            = azurerm_resource_group.mischa_aks.location
  resource_group_name = azurerm_resource_group.mischa_aks.name
  dns_prefix          = "${var.prefix}-k8s"
  kubernetes_version  = "1.23.12"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_container_registry" "mischa_aks" {
  name                = "containerRegistry1"
  resource_group_name = azurerm_resource_group.mischa_aks.name
  location            = azurerm_resource_group.mischa_aks.location
  sku                 = "Standard"
}

resource "azurerm_role_assignment" "mischa_aks" {
  principal_id                     = azurerm_kubernetes_cluster.mischa_aks.kubelet_identity[0].object_id
  role_definition_name             = "AcrPull"
  scope                            = azurerm_container_registry.mischa_aks.id
  skip_service_principal_aad_check = true
}
