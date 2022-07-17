import time
import run_model

def get_prediction():
    t = 5
    start_time = time.time()
    while time.time() < start_time + t:
        timer = int((start_time + t)) - int(time.time())
        print(timer, end="\r")

get_prediction()


