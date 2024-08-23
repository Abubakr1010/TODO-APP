from locust import HttpUser, task, between



class LoginUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def login(self):
        self.client.post("/login/", json={"email": "jackmax4@gmail.com", "password": "1251"})

