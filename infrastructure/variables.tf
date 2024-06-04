variable "project_id" {
  description = "The GCP project ID"
}

variable "region" {
  description = "The GCP region"
}

variable "bucket_name" {
  description = "The name of the Cloud Storage bucket"
}

variable "bucket_location" {
  description = "The location of the Cloud Storage bucket"
}

variable "dataset_id" {
  description = "The BigQuery dataset ID"
}

variable "dataset_location" {
  description = "The location of the BigQuery dataset"
}

variable "table_id" {
  description = "The BigQuery table ID"
}