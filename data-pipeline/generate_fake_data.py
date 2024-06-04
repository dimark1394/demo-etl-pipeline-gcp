from google.cloud import storage
from faker import Faker
import os
import csv 
import random

def generate_fake_data(num_rows=1000):
    """_summary_

    Args:
        num_rows (int, optional): The numver of rows for fake data generation. Defaults to 1000.
    
    Returns: 

    """
    fake = Faker()
    
    cities = [fake.city() for _ in range(20)]
    data = []

    for _ in range(num_rows):
        data.append({
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "birthdate": fake.date_of_birth().isoformat(),
            "location": random.choice(cities),
            "salary": fake.random_number(digits=5, fix_len=True)
        })
    return data

def save_data_to_csv(data, file_path):
    """Save data to a CSV file.

    Args:
        data (list): A list of dictionaries containing the data to save.
        file_path (str): The file path where the CSV should be saved.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def upload_file_to_gcs(file_path, bucket_name, destination_blob_name):
    """Upload a file to Google Cloud Storage.

    Args:
        file_path (str): The path to the file to upload.
        bucket_name (str): The name of the GCS bucket.
        destination_blob_name (str): The destination blob name in the GCS bucket.
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(file_path)

    print(f"File {file_path} uploaded to {destination_blob_name}.")
    
if __name__ == "__main__":
    local_temp_path = "/tmp/employee_data.csv"
    fake_data = generate_fake_data()
    save_data_to_csv(fake_data, local_temp_path)
    upload_file_to_gcs(local_temp_path, "employee_bucket_demo", "employee_data.csv")

