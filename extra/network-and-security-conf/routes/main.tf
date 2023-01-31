# Creating the Route Table
resource "aws_route_table" "z5-route-table" {
 vpc_id = var.vpc_id
 tags = {
        Environment= "${var.environment}",
        Name= "${var.routeTableName}-${var.environment}-main",
  }
}

resource "aws_route_table" "pub-subnet-route-table" {
  vpc_id = var.vpc_id
   tags = {
        Environment= "${var.environment}",
        Name= "${var.routeTableName}-${var.environment}-pub"
  }
}

# Creating Internet Access
resource "aws_route" "z5-internet-access" {
  route_table_id         = aws_route_table.pub-subnet-route-table.id
  destination_cidr_block = var.destinationCIDRblock
  gateway_id             = var.internet_gateway_id
}


resource "aws_route" "z5-nat-gw" {
  route_table_id         = aws_route_table.z5-route-table.id
  destination_cidr_block = var.destinationCIDRblock
  nat_gateway_id             = var.nat_gw.id
}

# Associating the Route Table with the Subnets

resource "aws_route_table_association" "subnet-pvt-association" {
  count = length(var.subnets-pvt)
  subnet_id      = var.subnets-pvt[count.index].id
  route_table_id = aws_route_table.z5-route-table.id
}

resource "aws_route_table_association" "subnet-pub-association" {
  count = length(var.subnets-pub)
  subnet_id      = var.subnets-pub[count.index].id
  route_table_id = aws_route_table.pub-subnet-route-table.id
}