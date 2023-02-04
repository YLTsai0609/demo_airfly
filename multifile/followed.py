from airfly.model.airflow import AirflowTask

from .head import HeadTask


def print_hi():
    return "hi"


class FollowedTask_concurrent_2(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)
    upstreams = HeadTask

    def inflow(self):
        pass

    def outflow(self):
        pass


class FollowedTask_concurrent_3(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)
    upstreams = FollowedTask_concurrent_2

    def inflow(self):
        pass

    def outflow(self):
        pass
