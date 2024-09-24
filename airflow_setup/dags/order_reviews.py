from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator 
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator




@dag(
    start_date=datetime(2024,8,11),
    schedule=None,
    catchup=False,
    tags=['olist_order_reviews'],
)

def order_reviews_postgres_to_gcs():

    export_to_gcs = PostgresToGCSOperator(
        task_id='export_order_reviews_to_gcs',
        postgres_conn_id='pg_conn',
        sql='SELECT review_id,order_id,review_score,review_creation_date,review_answer_timestamp FROM raw.order_reviews;',
        bucket='source_raw',
        filename='data/order_reviews.csv',
        export_format='csv',
        field_delimiter=',',
        gzip=False,  # Set to True if you want the CSV files to be compressed
        gcp_conn_id='gcp_conn',

    )

    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_retail_dataset',
        dataset_id='raw_data',
        gcp_conn_id='gcp_conn',
        project_id='alt-school-project-425214'
    )

    load_to_bigquery = BigQueryInsertJobOperator(
    task_id='load_to_bigquery',
    configuration={
        "load": {
            "sourceUris": ["gs://source_raw/data/order_reviews.csv"], 
            "destinationTable": {
                "projectId": "alt-school-project-425214",
                "datasetId": "raw_data",
                "tableId": "order_reviews",
            },
            "schema": {
                "fields": [
                    {"name": "review_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "order_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "review_score", "type": "INTEGER", "mode": "REQUIRED"},
                    # {"name": "review_comment_title", "type": "STRING", "mode": "NULLABLE"},
                    # {"name": "review_comment_message", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "review_creation_date", "type": "TIMESTAMP", "mode": "REQUIRED"},
                    {"name": "review_answer_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"}
                  ]
            },
            "sourceFormat": "CSV",
            "writeDisposition": "WRITE_TRUNCATE",
            "maxBadRecords": 5,
        }
    },
    gcp_conn_id='gcp_conn',
    project_id='alt-school-project-425214',
    )

    # Set task dependencies
    export_to_gcs >> create_retail_dataset >> load_to_bigquery


order_reviews_postgres_to_gcs()

