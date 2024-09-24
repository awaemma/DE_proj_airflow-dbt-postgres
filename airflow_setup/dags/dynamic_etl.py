from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# Define your default_args
default_args = {
    'start_date': datetime(2024, 8, 16),
    'retries': 1,
}

# List of tables to process
tables = ['products', 'sellers', 'geolocation','customers','order_items','order_payments'
          ,'order_reviews','orders','product_category_name_translation']

# Schema name
schema = 'raw'
bucket_name = 'pg_raw_data01'
gcp_conn_id = 'gcp_conn'
project_id = 'alt-school-project-425214'
postgres_conn_id = 'pg_conn'

# Initialize the DAG
with DAG('dynamic_dag_pg_to_bq',
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    for table in tables:
        with TaskGroup(group_id=f'process_{table}') as tg:
            # Task to extract data from Postgres and upload to GCS
            extract_to_gcs = PostgresToGCSOperator(
                task_id=f'extract_{table}_to_gcs',
                postgres_conn_id=postgres_conn_id,
                sql=f'SELECT * FROM {schema}.{table};',  # Include the schema in the SQL query
                bucket=bucket_name,
                filename=f'{table}.csv',
                export_format='csv',
                gcp_conn_id=gcp_conn_id,  # Updated to use your custom connection ID
            )

            # Task to load data from GCS to BigQuery
            load_to_bigquery = GCSToBigQueryOperator(
                task_id=f'load_{table}_to_bigquery',
                bucket=bucket_name,
                source_objects=[f'{table}.csv'],
                destination_project_dataset_table=f'{project_id}.{schema}.{table}',
                source_format='CSV',
                autodetect=True,
                write_disposition='WRITE_TRUNCATE',
                gcp_conn_id=gcp_conn_id,  # Updated to use your custom connection ID
            )

            # Set task dependencies
            extract_to_gcs >> load_to_bigquery
