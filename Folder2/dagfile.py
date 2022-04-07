# General

from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()

from datetime import datetime, timedelta

 

# Documentation

with open(ROOT_DIR/'README.md', "r") as f:

                print(f.readline())

                __doc__ = f.readline()

 

# Airflow

from airflow.models import DAG

from airflow.operators.dummy_operator import DummyOperator

from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

from airflow.operators.check_operator import ValueCheckOperator

 

# Config Spark

from dmutils.sparkres import sparksubres

 

 

dag = DAG (

    dag_id="dl_zonastecnicas",

    max_active_runs=1,

    tags=["etl", "prod"],

    start_date=datetime(2021, 10, 1),

    schedule_interval="45 10 10 * *",

    template_searchpath=str(ROOT_DIR/"sql/"),

    default_args={

        "owner": "sbandoni",

        "email": ["datamanagementmkt@teco.com.ar"],

        'email_on_failure': True,

        'retries': 2,

        'retry_delay': timedelta(minutes=5)

    },

    user_defined_filters={"ym": lambda x: x[:6]}

)

 

dag.doc_md = __doc__

 

entry = DummyOperator(

    task_id="entry-point",

    dag=dag,

)

 

insert = SparkSubmitOperator(

    task_id="insert_into_table",

    application= str(ROOT_DIR / "tasks/insert_dl_zonastecnicas.py"),

    application_args=[

        "--periodo", "{{ next_ds_nodash | ym }}",

    ],

    spark_binary="bin/spark-submit",

    dag=dag,

    **sparksubres["sparklow"],

)

 

check_tabla = ValueCheckOperator(

    task_id="check_tabla",

    sql="""

        SELECT

                                                               CASE WHEN max(mes) = '{{ next_ds_nodash | ym }}'

                THEN 1 ELSE 0 END as fecha

        FROM

            data_lake_analytics.dl_zonastecnicas

    """,

    conn_id="beeline_jdbc",

    pass_value=1,

    dag=dag,

)

 

entry >> insert >> check_tabla