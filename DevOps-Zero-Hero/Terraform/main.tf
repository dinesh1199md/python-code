terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.64.0"
    }
  }
}

provider "azurerm" {
   features {}
  client_id       = "****************"
  client_secret   = "****************"
  tenant_id       = "****************"
  subscription_id = "****************"
}

resource "azurerm_resource_group" "My-RG-01" {
  name = "My-RG-01"
  location = "West Europe"
}
