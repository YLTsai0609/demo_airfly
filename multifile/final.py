from airfly.model.airflow import AirflowTask

from .followed import FollowedTask_concurrent_3
from .head import HeadTask


def print_hi():
    return "hi"


class Final1(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)
    upstreams = HeadTask

    def inflow(self):
        pass

    def outflow(self):
        pass


class Final1(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)
    upstreams = FollowedTask_concurrent_3

    def inflow(self):
        pass

    def outflow(self):
        pass
