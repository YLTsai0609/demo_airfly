# This file is auto-generated by airfly 0.7.2
from airflow.models import DAG
from airflow.operators.python import PythonOperator

from multifile.edge_1 import print_hi
from multifile.edge_2 import print_hi
from multifile.final import print_hi
from multifile.followed import print_hi
from multifile.head import print_hi

with DAG("miltifile") as dag:
    multifile_edge_1_EdgeTask1 = PythonOperator(
        task_id="multifile.edge_1.EdgeTask1", python_callable=print_hi
    )
    multifile_edge_2_EdgeTask2 = PythonOperator(
        task_id="multifile.edge_2.EdgeTask2", python_callable=print_hi
    )
    multifile_final_Final1 = PythonOperator(
        task_id="multifile.final.Final1", python_callable=print_hi
    )
    multifile_followed_FollowedTask_concurrent_2 = PythonOperator(
        task_id="multifile.followed.FollowedTask_concurrent_2", python_callable=print_hi
    )
    multifile_followed_FollowedTask_concurrent_3 = PythonOperator(
        task_id="multifile.followed.FollowedTask_concurrent_3", python_callable=print_hi
    )
    multifile_head_FollowedTask_concurrent_1 = PythonOperator(
        task_id="multifile.head.FollowedTask_concurrent_1", python_callable=print_hi
    )
    multifile_head_HeadTask = PythonOperator(
        task_id="multifile.head.HeadTask", python_callable=print_hi
    )
    multifile_edge_1_EdgeTask1 >> multifile_edge_2_EdgeTask2
    (
        multifile_followed_FollowedTask_concurrent_2
        >> multifile_followed_FollowedTask_concurrent_3
    )
    multifile_followed_FollowedTask_concurrent_3 >> multifile_final_Final1
    multifile_head_HeadTask >> multifile_followed_FollowedTask_concurrent_2
    multifile_head_HeadTask >> multifile_head_FollowedTask_concurrent_1

