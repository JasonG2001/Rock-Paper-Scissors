import cv2
import time
from keras.models import load_model
import numpy as np
import random

def run():    
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
        options = ["Rock", "Paper", "Scissors", "Nothing"]
        user_selection = options[prediction.argmax()]

        def get_computer_choice():
            OPTIONS = ["Rock", "Paper", "Scissors"]
            computer_choice = random.choice(OPTIONS)
            print(f"computer plays {computer_choice}")
            return computer_choice 

        def get_prediction():
            print(f"You play {user_selection}")
            return user_selection

        def get_winner(prediction, computer_choice):
            if prediction == computer_choice:
                print("draw")
                return "draw"
            elif (prediction == "Rock" and computer_choice == "Scissors") or (prediction == "Scissors" and computer_choice == "Paper") or (prediction == "Paper" and computer_choice == "Rock"):
                print("you win")
                return "user"
            else:
                print("computer wins")
                return "computer"

        def play():
            prediction = get_prediction()
            computer_choice = get_computer_choice()
            get_winner(prediction, computer_choice)
        play()

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return user_selection

run()
