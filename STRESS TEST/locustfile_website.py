from locust import HttpUser, task, between

class MyUserWebsite(HttpUser):
    wait_time = between(1, 5)
    host = "http://ecuadoriansignlanguagefenedif.000webhostapp.com"

    @task
    def access_website(self):
        self.client.get("/")
