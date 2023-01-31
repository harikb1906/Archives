data "external" "name-generator" {
  program = ["python3", "${path.module}/external/name-generator.py"]
}

output "genetated-name-via-python" {
  value = data.external.name-generator.result.name
}
