resource "aws_subnet" "z5-vpc-subnets-pvt" {
  count = length(var.subnetCIDRblocks-pvt)
  vpc_id                  = var.vpc_id
  cidr_block              = var.subnetCIDRblocks-pvt[count.index]
  map_public_ip_on_launch = var.mapPublicIP
  availability_zone       = element(data.aws_availability_zones.available.names,count.index)
  tags = {
    Environment = "${var.environment}",
    Name        = "${var.vpcSubnetName}-${var.environment}-pvt-${count.index}",
    "kubernetes.io/cluster/${var.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "z5-vpc-subnets-pub" {
  count = length(var.subnetCIDRblocks-pub)
  vpc_id                  = var.vpc_id
  cidr_block              = var.subnetCIDRblocks-pub[count.index]
  map_public_ip_on_launch = var.mapPublicIP
  availability_zone       = element(data.aws_availability_zones.available.names,count.index)
  tags = {
    Name        = "${var.vpcSubnetName}-${var.environment}-pub-${count.index}",
    "kubernetes.io/cluster/${var.cluster_name}" = "shared",
    Environment = "${var.environment}",
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}