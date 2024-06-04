provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "employee_bucket" {
  name     = var.bucket_name
  location = var.bucket_location
}

data "local_file" "schema" {
  filename = "../schemas/raw_data_schema.json"
}

locals {
  raw_data_schema = jsondecode(data.local_file.schema.content)
}

resource "google_bigquery_dataset" "employee_dataset" {
  dataset_id = var.dataset_id
  location   = var.dataset_location
}

resource "google_bigquery_table" "raw_data" {
  dataset_id = google_bigquery_dataset.employee_dataset.dataset_id
  table_id   = var.table_id
  schema = {
    fields = local.raw_data_schema
  }
}
