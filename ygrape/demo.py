import requests
import random
import time
while True:
    url = 'http://127.0.0.1:8000/api/?name=s1&value=' + str(random.uniform(20,23))
    url2 = 'http://127.0.0.1:8000/api/?name=s2&value=' + str(random.uniform(65, 75))
    requests.get(url)
    requests.get(url2)
    time.sleep(5)

