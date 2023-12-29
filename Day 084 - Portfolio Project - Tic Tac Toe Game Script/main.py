from player import Player
from game import TicTacToe

# Initialize players
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")

# Initialize the game
game = TicTacToe()

# Start the game
game.play(player1, player2)