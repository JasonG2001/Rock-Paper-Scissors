from computer_vision_player import ComputerVisionPlayer
from player import Player
from computer_player import ComputerPlayer

class Game:

    def __init__(self, player1: Player, player2: Player, number_to_win: int):
        
        self.player1: Player = player1
        self.player2: Player = player2
        self.number_to_win: int = number_to_win

    def run(self) -> None:
        player1_wins: int = 0
        player2_wins: int = 0
        while player1_wins < self.number_to_win and player2_wins < self.number_to_win:
            player1_choice: str = self.player1.play()
            player2_choice: str = self.player2.play()
            
            print(f"Player 1 has played {player1_choice}")
            print(f"Player 2 has played {player2_choice}")
            
            winner: str = self.get_winner(player1_choice, player2_choice)
            if winner == "Player 1":
                player1_wins += 1
            elif winner == "Player 2":
                player2_wins += 1
            print(f"Player 1 points: {player1_wins}")
            print(f"Player 2 points: {player2_wins}")
        if player2_wins == self.number_to_win:
            print("Player 2 wins")
        else:
            print("Player 1 wins")

    def get_winner(self, player1_choice: str, player2_choice: str) -> str:
        if player1_choice == player2_choice:
            print("draw")
            return "draw"
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or (player1_choice == "Scissors" and player2_choice == "Paper") or (player1_choice == "Paper" and player2_choice == "Rock"):
            print("Player 1 wins")
            return "Player 1"
        else:
            print("Player 2 wins")
            return "Player 2"


def main():
    player1: Player = ComputerPlayer() 
    player2: Player = ComputerVisionPlayer(3)
    game: Game = Game(player1, player2, 2) 
    game.run()

if __name__ == "__main__":
    main()


