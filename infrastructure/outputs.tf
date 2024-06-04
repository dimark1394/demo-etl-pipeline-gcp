output "bucket_name" {
  value = google_storage_bucket.employee_bucket.name
}

output "dataset_id" {
  value = google_bigquery_dataset.employee_dataset.dataset_id
}
