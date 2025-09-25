provider "aws" {
  region = local.location
}

locals {
  cdw         = reverse(split(("/"), path.cwd))
  location    = local.cdw[0]
  environment = local.cdw[1]
}

module "storage" {
  source = "../../modules/${local.environment}/${local.location}/storage"
  s3_bucket_name = module.storage.s3_bucket_name
}