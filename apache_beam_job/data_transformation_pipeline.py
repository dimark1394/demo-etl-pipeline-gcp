import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.bigquery import ReadFromBigQuery
import apache_beam.transforms.combiners as combiners

def run_transformation_pipeline(project, bucket, dataset_id, raw_table_id, transformed_table_id):
    options = PipelineOptions(
        runner='DataflowRunner',
        project=project,
        region='us-central1',
        temp_location=f'gs://{bucket}/temp',
        staging_location=f'gs://{bucket}/staging'
    )

    raw_table = f"{project}:{dataset_id}.{raw_table_id}"
    transformed_table = f"{project}:{dataset_id}.{transformed_table_id}"

    with beam.Pipeline(options=options) as p:
        # Read from raw table
        raw_data = (
            p
            | 'ReadFromBigQuery' >> ReadFromBigQuery(table=raw_table)
        )

        # Calculate average salary per location
        avg_salary_per_location = (
            raw_data
            | 'ExtractLocationSalaryPairs' >> beam.Map(lambda row: (row['location'], row['salary']))
            | 'CombinePerLocation' >> combiners.Mean.PerKey()
            | 'FormatToDict' >> beam.Map(lambda location_avg: {'location': location_avg[0], 'average_salary': location_avg[1]})
        )

        # Write transformed data to new table
        _ = (
            avg_salary_per_location
            | 'WriteToBigQuery' >> WriteToBigQuery(
                table=transformed_table,
                schema={
                    'fields': [
                        {'name': 'location', 'type': 'STRING', 'mode': 'NULLABLE'},
                        {'name': 'average_salary', 'type': 'FLOAT', 'mode': 'NULLABLE'}
                    ]
                },
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
            )
        )

if __name__ == '__main__':
    project = 'etl-pi'
    bucket = 'employee_bucket_demo'
    dataset_id = 'employee_dataset'
    raw_table_id = 'raw_data_table'
    transformed_table_id = 'avg_salary_per_location'
    
    run_transformation_pipeline(project, bucket, dataset_id, raw_table_id, transformed_table_id)
