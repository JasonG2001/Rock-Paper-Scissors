import cv2
import time
from keras.models import load_model
import numpy as np


def run():    
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()
    TIME_LIMIT = 4
    options = ["Rock", "Paper", "Scissors", "Nothing"]
    while time.time() < start_time + TIME_LIMIT: 
        countdown = int((start_time + TIME_LIMIT)) - int(time.time())
        timer = "{:02d}".format(countdown)
        print(timer, end="\r")
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        user_selection = options[prediction.argmax()]
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return user_selection

if __name__ == "__main__":
    run()



