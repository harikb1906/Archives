variable "cluster_name" {}
variable "vpcName" {
     default = "z5-vpc"
}
variable "vpcinstanceTenancy" {
    default = "default"
}
variable "vpcdnsSupport" {
    default = true
}
variable "vpcdnsHostNames" {
    default = true
}
variable "vpcCIDRblock" {
    default = "10.0.0.0/16"
}
