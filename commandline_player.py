from player import Player


class CommandlineHumanPlayer(Player):

    def play(self) -> str:

        user_choice: str = input("Enter rock, paper or scissors: ")
        return user_choice 
