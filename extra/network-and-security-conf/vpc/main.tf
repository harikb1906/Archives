variable "environment" {}

# creating VPC for z5 deployment
resource "aws_vpc" "z5-vpc-tf" {
  cidr_block           = var.vpcCIDRblock
  instance_tenancy     = var.vpcinstanceTenancy
  enable_dns_support   = var.vpcdnsSupport
  enable_dns_hostnames = var.vpcdnsHostNames
  tags = {
    Environment                                 = "${var.environment}",
    Name                                        = "${var.vpcName}-${var.environment}",
    "kubernetes.io/cluster/${var.cluster_name}" = "shared"
  }
}
