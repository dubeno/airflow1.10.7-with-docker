# airflow-with-docker

# Docker Build:
    docker build -t naresh240/airflow .
   
  Optionally install Extra Airflow Packages and/or python dependencies at build time :
  
    docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" -t naresh240/airflow .
    docker build --rm --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t naresh240/airflow .
  or combined
    
    docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t naresh240/airflow .
# Run airflow
  By **default**, docker-airflow runs Airflow with **SequentialExecutor** :
  
    docker run -d -p 8080:8080 puckel/docker-airflow webserver
  If you want to run another executor, use the other docker-compose.yml files provided in this repository.
  
  For **LocalExecutor** :
  
    docker-compose -f docker-compose-LocalExecutor.yml up -d
  For **CeleryExecutor** :
    
    docker-compose -f docker-compose-CeleryExecutor.yml up -d
  NB : If you want to have DAGs example loaded (default=False), you've to set the following environment variable :
  <LOAD_EX=n/>
    
    docker run -d -p 8080:8080 -e LOAD_EX=y naresh240/airflow
# Scale the number of workers
    docker-compose -f docker-compose-CeleryExecutor.yml scale worker=5
# Running other airflow commands
  If you want to run other airflow sub-commands, such as <list_dags/> or <clear/> you can do so like this:
    
    docker run --rm -ti naresh240/airflow airflow list_dags
  or with your docker-compose set up like this:
  
    docker-compose -f docker-compose-CeleryExecutor.yml run --rm webserver airflow list_dags
  You can also use this to run a bash shell or any other command in the same environment that airflow would be run in:
    
    docker run --rm -ti naresh240/airflow bash
    docker run --rm -ti naresh240/airflow ipython
