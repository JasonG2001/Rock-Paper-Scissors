import run_model
import random

computer_wins = 0
user_wins = 0

def final_winner(computer_wins, user_wins):
    while computer_wins < 3 and user_wins < 3:

        def get_computer_choice():
            OPTIONS = ["Rock", "Paper", "Scissors"]
            computer_choice = random.choice(OPTIONS)
            return computer_choice 

        def get_prediction():
            return run_model.run() 

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

        if __name__ == "__main__":
            play()

    if computer_wins > user_wins:
        print("computer wins overall")
    else:
        print("user wins overall")

final_winner(computer_wins, user_wins)