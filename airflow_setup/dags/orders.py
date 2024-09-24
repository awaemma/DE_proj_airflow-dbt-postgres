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
    tags=['olist_orders'],
)

def orders_postgres_to_gcs():

    export_to_gcs = PostgresToGCSOperator(
        task_id='export_orders_to_gcs',
        postgres_conn_id='pg_conn',
        sql='SELECT * FROM raw.orders;',
        bucket='source_raw',
        filename='data/orders.csv',
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
            "sourceUris": ["gs://source_raw/data/orders.csv"],
            "destinationTable": {
                "projectId": "alt-school-project-425214",
                "datasetId": "raw_data",
                "tableId": "orders",
            },
            "schema": {
                "fields": [
                    {"name": "order_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "customer_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "order_status", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "order_purchase_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
                    {"name": "order_approved_at", "type": "TIMESTAMP", "mode": "NULLABLE"},
                    {"name": "order_delivered_carrier_date", "type": "TIMESTAMP", "mode": "NULLABLE"},
                    {"name": "order_delivered_customer_date", "type": "TIMESTAMP", "mode": "NULLABLE"},
                    {"name": "order_estimated_delivery_date", "type": "TIMESTAMP", "mode": "NULLABLE"}
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

    
    # gcs_to_raw = aql.load_file(
    #     task_id='gcs_to_raw',
    #     input_file=File(
    #         'gs://source_raw/data/orders.csv',
    #         conn_id='gcp_conn',
    #         filetype=FileType.CSV,
    #     ),
    #     output_table=Table(
    #         name='raw_orders',
    #         conn_id='gcp_conn',
    #         metadata=Metadata(schema='retail')
    #     ),
    #     use_native_support=False,
    # )


orders_postgres_to_gcs()

