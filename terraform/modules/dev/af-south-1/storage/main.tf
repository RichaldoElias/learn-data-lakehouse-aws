
resource "aws_s3_bucket" "datalakehouse" {
  bucket = var.s3_bucket_name

  tags = {
    Name        = var.s3_bucket_name
    Environment = "data-lakehouse"
  }
}



# Uncomment below to set ACL to private (default is private)
# Review code

# data "aws_s3_bucket_acl" "datalakehouse_acl" {
#   bucket = aws_s3_bucket.datalakehouse.id
# }

# resource "aws_s3_bucket_acl" "datalakehouse_acl" {
#   bucket = aws_s3_bucket.datalakehouse.id
#   acl    = "private"
# }