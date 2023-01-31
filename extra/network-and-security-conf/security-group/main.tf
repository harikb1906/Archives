variable "vpc_id" {}

# Creating the Security Group
resource "aws_security_group" "z5-security-group" {
  vpc_id      = var.vpc_id
  name        = "${var.securityGroupName}-${var.environment}"
  description = "Z5 VPC Security Group"

  # allow ingress of port 80
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
  }

  # allow ingress of port 8080
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
  }

  # allow ingress of port 5701
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 5701
    to_port     = 5701
    protocol    = "tcp"
  }

  # allow ingress of port 9090
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
  }

  # allow ingress of port 443
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
  }

  # allow ingress of port 8125
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 8125
    to_port     = 8125
    protocol    = "tcp"
  }

  # allow ingress of port 8126
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 8126
    to_port     = 8126
    protocol    = "tcp"
  }

  # allow ingress of port 51678
  ingress {
    cidr_blocks = var.ingressCIDRblock
    from_port   = 51678
    to_port     = 51678
    protocol    = "tcp"
  }

  # allow egress of all ports
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name        = "${var.securityGroupName}-${var.environment}"
    Description = "Z5 VPC Security Group-${var.environment}"
  }
}

