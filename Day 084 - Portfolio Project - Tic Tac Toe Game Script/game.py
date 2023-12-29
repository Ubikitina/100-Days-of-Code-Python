class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Represent the Tic Tac Toe board as a list of 9 empty spaces [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_player = None

    def print_board(self):
        """
        Print the current state of the Tic Tac Toe board.

        The board is displayed in a 3x3 grid format with cell values separated by '|'.
        Horizontal lines separate the rows to enhance visibility.

        Example:
        1 | 2 | 3
        ----------
        4 | 5 | 6
        ----------
        7 | 8 | 9
        """
        for i in range(0, 9, 3): # Loop through the rows of the board in increments of 3 (0, 3, 6)
            print(" | ".join(self.board[i:i + 3])) # create a sublist of the board list containing three eleemnts separated by |
            if i < 6: # Check if it's not the last row (i < 6) to print a horizontal line separating rows
                print("----------")

    def is_winner(self, symbol):
        """
        Check if the specified symbol has won the game.

        This method examines the Tic Tac Toe board to determine if the specified symbol
        has formed a winning combination in any row (both horizontal and vertical) or
        diagonals.

        Parameters:
        - symbol (str): The symbol to check for a win ('X' or 'O').

        Returns:
        bool: True if the specified symbol has won, False otherwise.
        """

        # Check rows, both horizontal and vertical, for the specified symbol
        for i in range(3):
            if all(self.board[i * 3 + j] == symbol for j in range(3)) or \
               all(self.board[i + j * 3] == symbol for j in range(3)):
                return True

        # Check diagonals
        return all(self.board[i] == symbol for i in [0, 4, 8]) or \
               all(self.board[i] == symbol for i in [2, 4, 6])

    def is_board_full(self):
        """
        Check if the Tic Tac Toe board is completely filled.

        This method examines the Tic Tac Toe board to determine if all cells are occupied
        by either 'X' or 'O', indicating that the game has ended in a tie.

        Returns:
        bool: True if the board is full, indicating a tie, False otherwise.
        """
        return " " not in self.board

    def make_move(self, position):
        """
        Make a move on the Tic Tac Toe board.

        This method allows the current player to make a move by placing their symbol ('X' or 'O')
        at the specified position on the board.

        Parameters:
        - position (int): The position on the board where the move is to be made (1-9).

        Returns:
        bool: True if the move is successfully made, False if the position is already occupied.
        """
        if self.board[position] == " ":
            self.board[position] = self.current_player.symbol
            return True
        else:
            print("Invalid move. The position is already occupied.")
            return False

    def switch_player(self, player1, player2):
        """
        Switch the current player in the Tic Tac Toe game.

        This method toggles the current player between two players, allowing each player
        to take turns making moves.

        Parameters:
        - player1 (Player): The first player object with a unique symbol 'X' or 'O'.
        - player2 (Player): The second player object with a unique symbol 'X' or 'O'.
        """
        self.current_player = player1 if self.current_player == player2 else player2

    def play(self, player1, player2):
        self.current_player = player1 # Set the starting player

        # Game loop
        while True:
            self.print_board() # Display the current state of the board

            # Prompt the current player for a move
            position = int(input(f"{self.current_player.name}, enter your move (1-9): ")) - 1

            # Check if the move number is valid
            if 0 <= position <= 8:
                # Check if the position is empty
                if self.make_move(position):
                    # Check for a winner after each move
                    if self.is_winner(self.current_player.symbol):
                        self.print_board()
                        print(f"Congratulations, {self.current_player.name}! You won!")
                        break
                    # Check if it is the end of the game with a tie
                    elif self.is_board_full():
                        self.print_board()
                        print("It's a tie!")
                        break
                    # No winner nor end of the tie, let's continue with the game
                    else:
                        self.switch_player(player1, player2)
                else: # The position is not empty, the message will be printed in the make_move() method and we will continue
                    continue
            else: # Print the message for the wrong input number
                print("Invalid input. Please enter a number between 1 and 9.")
