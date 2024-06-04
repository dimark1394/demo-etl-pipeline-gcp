from google.cloud import bigquery
from faker import Faker
import os

def generate_fake_data(num_rows=1000):
    """_summary_

    Args:
        num_rows (int, optional): The numver of rows for fake data generation. Defaults to 1000.
    
    Returns: 

    """
    fake = Faker()
    data = []

    for _ in range(num_rows):
        data.append({
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "birthdate": fake.date_of_birth().isoformat(),
            "location": fake.city,
            "salary": fake.random_number(digits=5, fix_len=True)
        })
    return data

def upload_fake_data_to_bigquery(data):
    client = bigquery.Client()
    dataset_id = os.environ['DATASET_ID']
    table_id = f"{dataset_id}.raw_table"

    schema = [
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("address", "STRING"),
        bigquery.SchemaField("email", "STRING"),
        bigquery.SchemaField("phone_number", "STRING"),
        bigquery.SchemaField("birthdate", "DATE"),
        bigquery.SchemaField("location", "STRING"),
        bigquery.SchemaField("salary", "INTEGER")
    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table, exists_ok=True)

    errors = client.insert_rows_json(table, data)

    if errors:
        raise Exception(f"Errors occured while inserting rows: {errors}")
    
if __name__ == "__main__":
    num_rows = int(os.getenv('NUM_ROWS', '1000'))
    fake_date = generate_fake_data
    upload_fake_data_to_bigquery()

