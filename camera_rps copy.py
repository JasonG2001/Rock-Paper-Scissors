import run_model
import random

def get_computer_choice():
    OPTIONS = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(OPTIONS)
    print(f"Computer plays {computer_choice}")
    return computer_choice 

def get_prediction():
    user_outcome = run_model.run()
    print(f"You play {user_outcome}")
    return user_outcome 

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
    NUMBER_TO_WIN = 3
    computer_wins = 0
    user_wins = 0
    while computer_wins < NUMBER_TO_WIN and user_wins < NUMBER_TO_WIN:
        prediction = get_prediction()
        computer_choice = get_computer_choice()
        winner = get_winner(prediction, computer_choice)
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
    if computer_wins == NUMBER_TO_WIN:
        print("You lose")
    else:
        print("You win")

if __name__ == "__main__":
    play()

