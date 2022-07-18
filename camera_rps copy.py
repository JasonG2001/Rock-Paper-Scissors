import run_model
import random

def get_computer_choice():
    OPTIONS = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(OPTIONS)
    return computer_choice 

def get_prediction():
    return run_model.run() 

def get_winner(prediction, computer_choice):
    if prediction == computer_choice:
        return "draw"
    elif (prediction == "Rock" and computer_choice == "Scissors") or (prediction == "Scissors" and computer_choice == "Paper") or (prediction == "Paper" and computer_choice == "Rock"):
        return "user"
    else:
        return "computer"

def play():
    prediction = get_prediction()
    computer_choice = get_computer_choice()
    print(get_winner(prediction, computer_choice))

if __name__ == "__main__":
    play()