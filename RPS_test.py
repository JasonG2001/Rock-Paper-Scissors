import random
import cv2
import time
from keras.models import load_model
import numpy as np

class RockPaperScissors:

    def __init__(self):
        
        self.user_choices = ["rock", "paper", "scissors", "nothing"]
        self.computer_choices = ["rock", "paper", "scissors"]
        self.user_wins = 0
        self.computer_wins = 0
        self.points_to_win = 3

    
    def get_computer_choice(self):

        self.computer_choice = random.choice(self.computer_choices)
        print(f"Computer plays {self.computer_choice}")
        return self.computer_choice

    
    def get_user_choice(self):

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
            
            self.user_choice = self.user_choices[prediction.argmax()]
            
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
        print(f"You have played {self.user_choice}")
        return self.user_choice

    
    def get_winner(self):

        self.get_user_choice()
        self.get_computer_choice()
        
        if self.user_choice == self.computer_choice:
            
            print("Draw")

        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or (self.user_choice == "scissors" and self.computer_choice == "paper") or (self.user_choice == "paper" and self.computer_choice == "rock"):
            
            self.user_wins += 1
            print("You win this round")

        else:

            self.computer_wins += 1
            print("Computer wins this round") # Also if user selects nothing

        print(f"Your points: {self.user_wins}")
        print(f"Computer points: {self.computer_wins}")


    def play(self):

        while (self.user_wins < self.points_to_win) and (self.computer_wins < self.points_to_win):
            self.get_winner()
        
        if self.computer_wins > self.user_wins:
            
            print("You lose")

        else:

            print("You win")



rps = RockPaperScissors()

if __name__ == "__main__":

    rps.play()