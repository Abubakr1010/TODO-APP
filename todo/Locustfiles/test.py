from locust import HttpUser, task, between


# Login Performance test
class LoginUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def login(self):
        self.client.post("/login/", json={"email": "jackmax4@gmail.com", "password": "1251"})
        # locust -f todo/Locustfiles/test.py


