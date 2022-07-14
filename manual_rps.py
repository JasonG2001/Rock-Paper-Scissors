import random

options = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    print(f"Computer plays {random.choice(options)}") 

choice = input("Enter rock, paper or scissors: ")
def get_user_choice(choice):
    print(choice.capitalize())

get_user_choice(choice)
get_computer_choice()