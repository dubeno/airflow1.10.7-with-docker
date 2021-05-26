from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'Naresh',
    'depends_on_past': False,
    'start_date': datetime(2021, 5, 1),
    'email': ['airflow@abc.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@hourly',
}

dag = DAG("helloworld",default_args=default_args, schedule_interval=None)
t1 = BashOperator(
    task_id='bash_example',
    # "test.sh" is a file under "/opt/scripts"
    bash_command="echo Helloworld ",
    dag=dag)

def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    print(kwargs)
    print(ds)
    return 'Helloworld with PythonOperator'

t2 = PythonOperator(
    task_id='python_example',
    provide_context=True,
    python_callable=print_context,
    dag=dag
)

t1 >> t2
