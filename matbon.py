import random
import cv2
import time
from keras.models import load_model
import numpy as np

class Players:
    
    def human(self):
        self.options = ["rock", "paper", "scissors", "nothing"]
        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        start_time = time.time()
        TIME_LIMIT = 4
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
            
            self.user_choice = self.options[prediction.argmax()]
            
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
        print(f"You have played {self.user_choice}")
        return self.user_choice


    def computer(self):
        self.comp_options = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(self.comp_options)

        print(f"Computer plays {self.computer_choice}")
        return self.computer_choice


class Scoreboard:

    def __init__(self, computer_points, player_points):
        self.computer_points = computer_points
        self.player_points = player_points

    def add_points(self):
        self.computer_points += 1
        