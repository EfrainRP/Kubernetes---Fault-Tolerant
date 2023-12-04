from locust import HttpUser, task

class ExampleTest(HttpUser):

    @task
    def home(self):
        self.client.request(method="GET", url="/home")