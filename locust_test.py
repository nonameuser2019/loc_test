from locust import HttpUser, TaskSet, task


#locust -f locust_test.py --web-host=localhost --web-port=5000 --host=https://platform.masterservice.company

class UserBehavior(TaskSet):
    def on_start(self):
        self.client.get('/')

    @task(5)
    def search(self):
        self.client.get('/search/?search=753420', proxies='67.207.83.225:80')

    @task(3)
    def change_auto(self):
        self.client.get('/audi/a4/a4-allroad-8kh-b8?year=2010&body_type_id=29&car_id=1158')

    @task(1)
    def change_language(self):
        self.client.get('/ua')

    @task(1)
    def go_to_about_us(self):
        self.client.get('/about-us')

    @task(1)
    def go_to_about_us(self):
        self.client.get('/ua/about-us')

    @task(1)
    def go_to_goods_category(self):
        self.client.get('/tovary-2693')

    @task(2)
    def go_to_payment_page(self):
        self.client.get('/payment_delivery')

    @task(2)
    def go_to_forum_page(self):
        self.client.get('/autoguide')

    @task(5)
    def come_back_to_main_page(self):
        self.client.get('/')





class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_weight = 1000
    max_weight = 8000