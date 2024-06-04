from google.cloud import bigquery
import os

def transform_data():
    client = bigquery.Client()

    query = f"""
    INSERT INTO `{os.environ['DATASET_ID']}.processed_table`
    SELECT 

    FROM `{os.environ['DATASET_ID']}.raw_table`
    """

    query_job = client.query(query)

    query_job.result()

    print("Transformation query completed")

if __name__ == "__main__":
    transform_data()
