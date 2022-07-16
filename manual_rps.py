import random

def get_computer_choice():
    OPTIONS = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(OPTIONS)
    return computer_choice 

def get_user_choice():
    user_choice = input("Enter rock, paper or scissors: ").capitalize()
    return user_choice 

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Rock"):
        return "user"
    else:
        return "computer"

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(user_choice, computer_choice)

if __name__ == "__main__":
    play()