import time

def get_prediction():
    import run_model

get_prediction()


while secs:
    secs = 5
    timer = "{:02d}".format(secs)
    print(timer, end="\r")
    secs -= 1
    pass

t = 5
start_time = time.time()
while time.time() < start_time + t:
    timer = int((start_time + t)) - int(time.time())
    print(timer, end="\r")
    pass



