from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago 
from datetime import datetime
from spotify_etl import extract_spotify_data


default_args = {
  'owner':'airflow',
  'depends_on_past':False,
  'start_date':datetime(2025,2,2),
  'email':['airflow@example.com'],
  'email_on_failure':False,
  'email_on_retry':False,
  'retries':1,
  'retry_delay':timedelta(minutes=1)
}



dag = DAG(
  'spotify_dag',
  default_args=default_args,
  description='very 1st ETL '
)


run_etl = PythonOperator(
  task_id='complete_spotify_etl',
  python_callable=extract_spotify_data,
  dag=dag,
)

run_etl
