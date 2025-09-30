resource "helm_release" "webadmin" {
  name      = "webadmin"
  namespace = var.namespace
  chart     = "${path.module}/../helm/webadmin"

  set {
    name  = "webadmin.image"
    value = var.webadmin_image
  }
  set {
    name  = "auth.image"
    value = var.auth_image
  }
  set {
    name  = "webadmin.nodePort"
    value = var.webadmin_nodeport
  }
  set {
    name  = "auth.nodePort"
    value = var.auth_nodeport
  }
}
