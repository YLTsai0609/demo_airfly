from airfly.model.airflow import AirflowTask


def print_hi():
    return "hi"


class HeadTask(AirflowTask):
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)

    def inflow(self):
        pass

    def outflow(self):
        pass

    def run(self):
        print("hello, I am HeadTask")


class FollowedTask_concurrent_1(AirflowTask):
    upstreams = HeadTask
    operator_class = "PythonOperator"
    params = dict(python_callable=print_hi)

    def inflow(self):
        pass

    def outflow(self):
        pass

    def run(self):
        print("hello, I am FollowedTask_concurrent_1")
