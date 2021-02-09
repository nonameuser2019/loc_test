from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.client.get('/')

    @task(1)
    def search(self):
        self.client.get('/search/?search=753420')

    @task(1)
    def change_auto(self):
        self.client.get('/audi/a4/a4-8k2--b8?year=2010')


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_weight = 1000
    max_weight = 3000
