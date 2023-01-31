output "vpc_id" {
  value       = aws_vpc.z5-vpc-tf.id
  description = "The id of vpc created"
}

output "vpc" {
    description = "vpc resource attributes"
  value = aws_vpc.z5-vpc-tf
}