variable "region" {
    description = "The AWS region to deploy resources in"
    type = string
    default = "af-south-1" # Cape Town
}

variable "s3_bucket_name" {
    description = "The name of the S3 bucket to create"
    type = string
    default = "r_e_learn_datalakehouse" # Change this to a unique bucket name
  
}