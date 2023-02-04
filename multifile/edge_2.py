from airfly.model.airflow import AirflowTask

from .edge_1 import EdgeTask1


def print_hi():
    return "hi"


class EdgeTask2(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)
    upstreams = EdgeTask1

    def inflow(self):
        pass

    def outflow(self):
        pass
