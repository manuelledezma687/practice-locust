from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/#ratings")
        # self.client.get("https://fivestarscarservice.com/")
        #  https://fivestarscarservice.herokuapp.com/ratings