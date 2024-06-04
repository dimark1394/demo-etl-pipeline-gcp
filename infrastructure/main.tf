provider "google" {
    project = var.project_id
    region = "europe-west-4"
}

resource "google_storage_bucket" "data_lake" {
    name = var.bucket_name
    location = var.bucket_location
}

resource "google_bigquery_dataset" "data_warehouse" {
  dataset_id = var.dataset_id
  location = var.dataset_location
}

resource "google_bigquery_table" "processed_data" {
  dataset_id = google_bigquery_dataset.data_warehouse.dataset_id
  table_id = var.table_id
  schema = file("")
}