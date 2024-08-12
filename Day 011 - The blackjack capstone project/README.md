# Day 11: Blackjack Game

Welcome to Day 11 of your Python learning journey! Today, I created a Blackjack game, applying the knowledge of functions with outputs, user input handling, and game logic. Below is an overview of the files I created and how they contribute to the Blackjack project.

## Files in This Folder

### `Blackjack_Flowchart.pdf`

This PDF file contains a flowchart that outlines the logic and flow of the Blackjack game. It was used as a reference to plan and develop the game’s logic.

### `blackjack.py`

This script implements a basic Blackjack game where the user plays against the computer (dealer).

- **Key Concepts**:
  - Functions with outputs for game logic.
  - Handling user input and game flow.
  - Calculating scores and managing game states.

- **How it Works**:
  - **Functions**:
    - `deal_cards()`: Returns a random card from the deck.
    - `calculate_score(cards_list)`: Calculates the score based on the current hand of cards.
    - `ask_want_to_play()`: Asks the user if they want to start a new game.
    - `is_end_of_game(user_score, computer_score)`: Determines if the game should end.
    - `print_current_status(user_cards, computer_cards)`: Displays the current status of the game.
    - `print_final_status(user_cards, computer_cards)`: Displays the final status of the game.
    - `compare(user_score, computer_score)`: Compares scores to determine the winner.
  
  - **Game Flow**:
    - The user is prompted to start a new game.
    - Two cards are dealt to both the user and the computer.
    - The user decides whether to draw more cards or hold.
    - The computer draws cards until its score is at least 17.
    - The game compares scores to determine the winner and displays the results.
    - The user is asked if they want to play again.

- **Example Usage**:
  - Run the script to start a Blackjack game.
  - Follow the on-screen prompts to draw cards, hold, and view the results.
  - The game continues until the user decides to stop.

### `art.py`

This file contains the ASCII art used to display the Blackjack game logo.It is imported into `blackjack.py` to print the game logo at the start of the game.


## How to Run the Script

1. **Ensure you have Python installed** on your system.
2. **Navigate to the folder** containing these files in your terminal or command prompt.
3. Run the script by typing `python blackjack.py`.
4. Follow the on-screen instructions to play the game.
