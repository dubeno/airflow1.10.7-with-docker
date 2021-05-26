from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 5, 1)
}

dag = DAG("print-data-with-spark", default_args=args, schedule_interval=None)

print-data = SparkSubmitOperator(task_id='print-data-spark',
            conn_id: 'spark_default',
            application: '/usr/local/spark/print_data_with_spark.py',
            dag=dag
)

print-data
