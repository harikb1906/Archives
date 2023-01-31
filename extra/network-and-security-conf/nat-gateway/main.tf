resource "aws_eip" "nat" {
  vpc      = true
}

resource "aws_nat_gateway" "nat_gw" {
  # count = 1
  allocation_id = aws_eip.nat.id
  subnet_id     = var.subnets-pub[0].id

  tags = {
    Name = "${var.ngw-name}-${var.environment}"
  }
}