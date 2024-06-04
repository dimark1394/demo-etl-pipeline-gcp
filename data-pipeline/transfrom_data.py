from google.cloud import bigquery

def process_and_create_table(dataset_id, raw_table_id, processed_table_id):
    """Process data from a raw table, calculate average salary per location,
    and create a new table with the processed data.

    Args:
        dataset_id (str): ID of the BigQuery dataset.
        raw_table_id (str): ID of the raw data table.
        processed_table_id (str): ID of the processed data table.
    """
    client = bigquery.Client()

    # Define the query to process data and calculate average salary per location
    query = f"""
    CREATE OR REPLACE TABLE `{client.project}.{dataset_id}.{processed_table_id}` AS
    SELECT location, AVG(salary) as avg_salary
    FROM `{client.project}.{dataset_id}.{raw_table_id}`
    GROUP BY location
    """

    # Run the query to create the processed table
    query_job = client.query(query)
    query_job.result()  # Waits for the job to complete.

    print(f"Processed data and created table {dataset_id}.{processed_table_id}")

if __name__ == "__main__":
    process_and_create_table('employee_dataset', 'raw_data_table', 'average_salary')