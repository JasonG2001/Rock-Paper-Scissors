import time
import run_model

def get_prediction():
    
    t = 10
    start_time = time.time()
    while time.time() < start_time + t:
        countdown = int((start_time + t)) - int(time.time())
        timer = "{:02d}".format(countdown)
        print(timer, end="\r")
    else:
        pass

get_prediction()


