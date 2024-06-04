# Demo Data Engineering (BigQuery, CI/CD Cloud Build, Terraform)

This project is a demonstration on how to create a simple data engineering pipeline
utilizing the following:

- IaC (Infrastructure as Code) with Terraform: To deploy the various resources we are going to need and create BigQuery tables.
- Cloud Build (CI/CD): To create triggers and initiate the deployment of our infrastructure and our data pipeline.
- Python: Is the programming language we use to create our data pipeline.

## The concept

The concept of this data engineering project is to create an ETL pipeline and through Cloud Build be able to actually control the deployment of our infrastructure and our code which happens in two different triggers to isolate them.

- First we use the Faker python library to generate 10000 rows of random employee data along with their salaries.
- The data then is converted to a CSV and uploaded to a GCS bucket in its raw format.
- Then we fill a dataset table in BigQuery that contains the raw data. This table is created during the deployment step of our infrastructure.
- Then we do a simple process to our data utilizing Python and SQL and create an average salary per location table.

The fun thing is that all of the above are written in Python while also utilizing the ability of Cloud Build to create containers that are connected to our GCP platform and run our code through there.

## Steps to recreate the project

The data flow of the project consists of the following steps.

1. First we need to create our Cloud Build instance and enable the APIs such as (BigQuery).
2. Then we need to create a service principal with the necessary roles to handle the creation of BigQuery tables, buckets, etc.
3. After that we set up triggers in which we connect our github to Cloud Studio, and trigger them through pushes to the code we do in a specific branch (infra branch for infrastructure code, data-pipeline for Python code).

## Benefits of this architecture

There many benefits for this type of architecture

1. Seperate pipelines for the deployment of infra and Python code.
2. No need to set up complicated things. It just works!
3. Monitor the deployment and each step of the process.
4. Room to grow! We can do more things through our CI/CD pipelines like testing our code, create complex logic in BigQuery and many more.

## Limitations

Of course the some many limitations as well

1. Security: While not unsecure as everything is behind your GCP some variables are hardcoded for the purposes of the demonstration (like GCS blobs uris, dasaset names, etc.) This can be fixed by passing values to them through Secret Manager or similar tools.
2. Limitations of cloud build for the process of large files.
3. Cost? Maybe if our pipelines take too long to deploy we are going to have some issues with it.
