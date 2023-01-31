variable "vpc_id" {}
variable "subnets-pvt" {}
variable "subnets-pub" {}
variable "internet_gateway_id" {}
variable "environment" {}
variable "nat_gw" {}
variable "routeTableName" {
     default = "z5-route-table"
}
variable "destinationCIDRblock" {
    default = "0.0.0.0/0"
}

