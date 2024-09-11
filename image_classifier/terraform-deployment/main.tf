provider "azurerm" {
  features {}

  # Set your subscription ID here
  subscription_id = "your azure subscription id"
}


# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "dogvsmuffin_rg"
  location = "West Europe"
}

# Azure Container Registry (ACR)
resource "azurerm_container_registry" "acr" {
  name                = "dogvsmuffinacr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# App Service Plan
resource "azurerm_service_plan" "app_service_plan" {
  name                = "dogvsmuffin_service_plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}

# Linux Web App (App Service) with Docker container
resource "azurerm_linux_web_app" "web_app" {
  name                = "muffinvschihuahua"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.app_service_plan.id

  site_config {
    always_on = true
  }

  identity {
    type = "SystemAssigned"  # Enables managed identity
  }

  # Docker settings are handled by Azure automatically, no need to set app_settings manually
}

# Outputs
output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}