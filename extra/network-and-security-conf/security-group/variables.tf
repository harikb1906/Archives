variable "securityGroupName" {
    default = "z5-security-group-dev-test"
}
variable "ingressCIDRblock" {
    type = list
    default = [ "0.0.0.0/0"]
}
variable "egressCIDRblock" {
    type = list
    default = [ "0.0.0.0/0" ]
}

variable "environment" {}