# Tic Tac Toe Game Project

## Goal
Using my knowledge of Python programming, I will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line. It should be a 2-player game, with one person playing as "X" and the other as "O".

## Project Implementation

### Classes

#### `TicTacToe` Class
- Manages the overall game, including the board and player turns.
- Methods:
  - `print_board`: Displays the current state of the Tic Tac Toe board.
  - `is_winner`: Checks if a player has won the game.
  - `is_board_full`: Checks if the game board is completely filled.
  - `make_move`: Allows a player to make a move on the board.
  - `switch_player`: Switches the current player between two players.
  - `play`: Initiates and manages the gameplay.

#### `Player` Class
- Represents a player in the game.
- Attributes:
  - `name`: Player's name.
  - `symbol`: Player's symbol ('X' or 'O').

### Reflection Time
I approached the project by first defining the classes (`TicTacToe` and `Player`) and their methods. Creating the game logic involved checking for a winner, a full board, and allowing players to make moves. Implementing the command-line interface for player input and displaying the board was straightforward.

**Challenges:**
- Managing player turns and switching between 'X' and 'O'.
- Checking for a winner in rows, columns, and diagonals.


### Today's Learnings
- Applied object-oriented programming concepts to design and implement a game.
- Improved problem-solving skills by addressing challenges in player turns and winning conditions.
- Understanding the importance of organizing code into classes and methods for better readability and maintainability.

### Potential Improvements for the Future
- Explore advanced AI algorithms for a more challenging single-player experience.
- Incorporate a graphical user interface for a more interactive game.