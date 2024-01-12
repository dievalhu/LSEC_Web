from locust import HttpUser, task, between

class MyUserAPI(HttpUser):
    wait_time = between(1, 5)
    base_url = "http://34.125.169.178:4200"

    @task
    def analyze_text_for_videos(self):
        text = "hola"
        response = self.client.post("/logic/analyze-text-videos/", params={"text": text})
        print(f"analyze_text_for_videos - Status Code: {response.status_code}")

    @task
    def get_all_palabras(self):
        response = self.client.get('/crud/palabra/')
        print(f"get_all_palabras - Status Code: {response.status_code}")

    @task
    def get_all_caracteres(self):
        response = self.client.get('/crud/caracter/')
        print(f"get_all_caracteres - Status Code: {response.status_code}")

    @task
    def get_database_config(self):
        response = self.client.get("/logic/database_config")
        print(f"get_database_config - Status Code: {response.status_code}")

    @task
    def analyze_text_for_videos_extended(self):
        text = "hola extended5 aceptar"
        response = self.client.post("/logic/analyze-text-videos/", params={"text": text})
        print(f"analyze_text_for_videos_extended - Status Code: {response.status_code}")
