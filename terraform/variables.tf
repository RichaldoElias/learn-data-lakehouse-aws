variable "s3_bucket_name" {
  description = "The name of the S3 bucket to create"
  type        = string
  default     = "relearndatalakehouse" # Change this to a unique bucket name

}

variable "region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "af-south-1"

}


variable "environment" {
  description = "The environment for the resources"
  type        = string
  default     = "dev"

}