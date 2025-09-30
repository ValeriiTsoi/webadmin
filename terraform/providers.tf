terraform {
  required_providers {
    helm = { source = "hashicorp/helm", version = "~> 2.10" }
    kubernetes = { source = "hashicorp/kubernetes", version = "~> 2.32" }
  }
}

provider "kubernetes" {
  config_path = "/etc/rancher/k3s/k3s.yaml"
}

provider "helm" {
  kubernetes {
    config_path = "/etc/rancher/k3s/k3s.yaml"
  }
}
