
from locust import HttpUser, task, between

class MyUserIP(HttpUser):
    wait_time = between(1, 5)
    host = "http://34.125.169.178:4200"

    @task
    def make_request_to_ip(self):
        self.client.get("/")
