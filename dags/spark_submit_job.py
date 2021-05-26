from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 5, 1)
}
dag = DAG('spark_submit_job', default_args=args, schedule_interval=None)

spark_submit = BashOperator(
    task_id='spark_submit_task',
    bash_command="spark-submit --master local \
                  --deploy-mode client \
                  --jars /usr/local/spark/spark-submit-eks-cluster-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
                  --driver-class-path /usr/local/spark/spark-submit-eks-cluster-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
                  --class com.cloudtechmasters.App \
                  /usr/local/spark/spark-submit-eks-cluster-0.0.1-SNAPSHOT-jar-with-dependencies.jar",
    dag=dag
)

spark_submit
