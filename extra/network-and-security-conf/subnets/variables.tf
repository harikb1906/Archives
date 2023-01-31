variable "cluster_name" {}
variable "vpc_id" {}
variable "environment" {}
variable "region" {}

variable "vpcSubnetName" {
     default = "z5-subnet"
}

variable "mapPublicIP" {
    default = false
}

variable "subnetCIDRblocks-pvt" {
    type        = list(string)
    default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
    description = "List of private subnet CIDR blocks"
}

variable "subnetCIDRblocks-pub" {
    type        = list(string)
    default     = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
    description = "List of public subnet CIDR blocks"
}

