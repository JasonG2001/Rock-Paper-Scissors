import cv2
import time
from keras.models import load_model
import numpy as np
import run_model


def countdown_and_show_video_capture(time_limit, capture):
    start_time = time.time()
    while time.time() < start_time + time_limit:
        countdown = int((start_time + time_limit)) - int(time.time())
        timer = "{:02d}".format(countdown)
        print(timer, end="\r")
        _, frame = capture.read()
        cv2.imshow('frame', frame)
    else:
        pass

def open_video_capture():
    capture = cv2.VideoCapture(0)
    return capture

def read_prediction(capture):
    _, frame = capture.read()
    cv2.imshow('frame', frame)
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1

    options = ["Rock", "Paper", "Scissors", "Nothing"]
    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image
    prediction = model.predict(data)
    user_selection = options[prediction.argmax()]
    return user_selection

def free_capture_resources(capture):
    capture.release()
    cv2.destroyAllWindows()

def get_prediction():
    USER_SELECTION_TIME_LIMIT = 10
    capture = open_video_capture()
    countdown_and_show_video_capture(USER_SELECTION_TIME_LIMIT, capture)
    outcome = read_prediction(capture)
    free_capture_resources(capture)
    return outcome




print(get_prediction())


