from airfly.model.airflow import AirflowTask


def print_hi():
    return "hi"


class EdgeTask1(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)

    def inflow(self):
        pass

    def outflow(self):
        pass
