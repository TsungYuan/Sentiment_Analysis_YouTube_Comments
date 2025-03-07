from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.ETL.load.store_data import test_log
from dotenv import load_dotenv
import logging
import time
import sys
import os

# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
# Add the project root to sys.path
sys.path.insert(0, project_root)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

default_args = {
    'owner': 'David',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='test_log',
    default_args=default_args,
    description='test log, this is the first task that we write',
    start_date=datetime(2025, 3, 6),
    schedule_interval='@daily'
) as dag:
    task_test = PythonOperator(
        task_id = 'test_log',
        python_callable=test_log
    )

    task_test