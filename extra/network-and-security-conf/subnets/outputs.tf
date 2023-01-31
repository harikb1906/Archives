# output "subnet-a-id" {
#   value       = aws_subnet.z5-vpc-subnet-tf-a.id
#   description = "Subnet id"
# }

# output "subnet-b-id" {
#   value       = aws_subnet.z5-vpc-subnet-tf-b.id
#   description = "Subnet id"
# }

# output "subnet-c-id" {
#   value       = aws_subnet.z5-vpc-subnet-tf-c.id
#   description = "Subnet id"
# }


output "subnets-pvt" {
  value = aws_subnet.z5-vpc-subnets-pvt
}

output "subnets-pub" {
  value = aws_subnet.z5-vpc-subnets-pub
}