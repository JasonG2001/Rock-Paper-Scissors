import random

options = ["Rock", "Paper", "Scissors"] #Options for the computer to choose from
computer_choice = random.choice(options)

def get_computer_choice():
    print(f"Computer plays {computer_choice}") #This gives the computer option

user_choice = input("Enter rock, paper or scissors: ")
def get_user_choice():
    print(f"You play {user_choice.capitalize()}") #This gives the user option

get_user_choice()
get_computer_choice()

def get_winner():
    if user_choice.capitalize() == computer_choice:
        print("Draw")
    elif (user_choice.capitalize() == "Rock" and computer_choice == "Scissors") or (user_choice.capitalize() == "Scissors" and computer_choice == "Paper") or (user_choice.capitalize() == "Paper" and computer_choice == "Rock"):
        print("You win")
    else:
        print("You lose")

get_winner()