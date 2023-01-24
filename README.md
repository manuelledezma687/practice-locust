locust -f main.py
pip install locust

HEADLESS MODE
locust -f --headless -u 100 --run-time 1h30m
locust -f --headless -u 100 --run-time 60 # default unit is seconds



-----
locust -f locust_file.py WebUser MobileUser

class WebUser(User):
    weight = 3
    ...

class MobileUser(User):
    weight = 1