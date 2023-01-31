# Creating the Internet Gateway
resource "aws_internet_gateway" "z5-internet-gateway" {
  vpc_id = var.vpc_id
  tags = {

    Environment = "${var.environment}",
    Module      = "Network",
    Name        = "${var.internetGatewayName}-${var.environment}",
  }
}
