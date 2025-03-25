from airflow import DAG
from airflow.providers.google.cloud.transfers.s3_to_gcs import S3ToGCSOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import logging

# Configurations
S3_CONN_ID = 'my_aws_conn'
GCS_CONN_ID = 'google_cloud_default'
S3_BUCKET = 'upstart-bucket'
GCS_BUCKET = 's3-external-files-bucket'  
S3_PREFIX = 'data/'
GCS_RAW_PATH = f"gs://{GCS_BUCKET}/external_data/"  

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    's3_to_gcs_transform_parquet',
    default_args=default_args,
    description='Transfer CSV from S3 to GCS and convert to Parquet',
    schedule_interval=None,
    catchup=False,
)


s3_to_gcs = S3ToGCSOperator(
    task_id="s3_to_gcs",
    apply_gcs_prefix=True,
    bucket=S3_BUCKET,
    prefix=S3_PREFIX,
    aws_conn_id=S3_CONN_ID,
    gcp_conn_id=GCS_CONN_ID,
    dest_gcs=GCS_RAW_PATH,
    replace=True,
    dag=dag,
)


s3_to_gcs 