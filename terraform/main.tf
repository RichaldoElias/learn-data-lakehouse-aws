locals {
  cdw          = reverse(split(("/"), path.cwd))
  assets_files = "${path.module}/../assets/db/csv_exports"
}


provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "datalakehouse" {
  bucket = var.s3_bucket_name

  tags = {
    Name        = var.s3_bucket_name
    Environment = var.environment
  }
}

resource "aws_s3_object" "bronze_bucket" {
  bucket = aws_s3_bucket.datalakehouse.id
  key    = "bronze/"
}

resource "aws_s3_object" "silver_bucket" {
  bucket = aws_s3_bucket.datalakehouse.id
  key    = "silver/"
}

resource "aws_s3_object" "gold_bucket" {
  bucket = aws_s3_bucket.datalakehouse.id
  key    = "gold/"
}


resource "aws_s3_object" "assets_files" {
  for_each = fileset(local.assets_files, "*")
  bucket   = aws_s3_bucket.datalakehouse.id
  key      = "assets/${each.value}"
  source   = "${local.assets_files}/${each.value}"
}



