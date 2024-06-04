from google.cloud import bigquery

def upload_to_bigquery(bucket_name, blob_name, dataset_id, table_id):
    client = bigquery.Client()

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1

    uri = f"gs://{bucket_name}/{blob_name}"

    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    print(f"Starting job {load_job.job_id}")

    load_job.result()  # Waits for the job to complete
    print(f"Job finished: {load_job.job_id}")

if __name__ == "__main__":
    # Set the parameters
    bucket_name = "employee_bucket_demo"
    blob_name = "employee_data.csv"
    dataset_id = "employee_dataset"
    table_id = "raw_data_table"

    # Call the function to upload the CSV to BigQuery
    upload_to_bigquery(bucket_name, blob_name, dataset_id, table_id)