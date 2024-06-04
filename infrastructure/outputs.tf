output "bucket_name" {
  value = google_storage_bucket.data_lake.name
}

output "dataset_id" {
  value = google_bigquery_dataset.data_warehouse.dataset_id
}