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
    tags=['olist_products'],
)

def products_postgres_to_gcs():

    export_to_gcs = PostgresToGCSOperator(
        task_id='export_products_to_gcs',
        postgres_conn_id='pg_conn',
        sql='SELECT * FROM raw.products;',
        bucket='source_raw',
        filename='data/products.csv',
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
            "sourceUris": ["gs://source_raw/data/products.csv"],
            "destinationTable": {
                "projectId": "alt-school-project-425214",
                "datasetId": "raw_data",
                "tableId": "products",
            },
            "schema": {
                "fields": [
                    {"name": "product_id", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "product_category_name", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "product_name_lenght", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_description_lenght", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_photos_qty", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_weight_g", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_length_cm", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_height_cm", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "product_width_cm", "type": "INTEGER", "mode": "NULLABLE"}
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

    
products_postgres_to_gcs()

