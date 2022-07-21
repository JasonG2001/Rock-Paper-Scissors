import random

from player import Player

class ComputerPlayer(Player):

    OPTIONS = ["Rock", "Paper", "Scissors"]
    
    def play(self) -> str:
        computer_choice: str = random.choice(self.OPTIONS)
        return computer_choice 
