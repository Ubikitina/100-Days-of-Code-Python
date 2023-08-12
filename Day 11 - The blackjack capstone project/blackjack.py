############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


# Create a deal_card() function that uses the List below to *return* a random card.
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 is the Ace.
    return random.choice(cards)

# Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
# 0 will represent a blackjack in our game.
def calculate_score(cards_list):
    if len(cards_list) == 2 and 11 in cards_list and 10 in cards_list: # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
        return 0 # Return 0 instead of the actual score to indicate there's a blackjack
    elif cards_list == [11, 11]: # If both are 11, then return 12
        return 12
    elif 11 in cards_list and sum(cards_list) > 21: # The 11 can be counted as 11 or 1. We will count it as 1 if the sum is greater than 21.
        new_list = cards_list.copy()
        index_of_11 = new_list.index(11)
        new_list[index_of_11] = 1
        return sum(new_list)
    else: # Else we will sum all the elements in the list
        return sum(cards_list)

def ask_want_to_play():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        return True
    else:
        return False

def is_end_of_game(user_score, computer_score):
    if user_score == 0 or computer_score == 0 or user_score >= 21: # If the user or computer has a blackjack or user's score is 21 or over
        return True # End of game
    else:
        return False

def print_current_status(user_cards, computer_cards):
    print("    Your cards: {}, current score: {}".format(user_cards, str(calculate_score(user_cards))))
    print("    Computer's first card: {}".format(str(computer_cards[0])))


def print_final_status(user_cards, computer_cards):
    print("    Your final hand: {}, final score: {}".format(user_cards, str(calculate_score(user_cards))))
    print("    Computer's final hand: {}, final score: {}".format(computer_cards, str(calculate_score(computer_cards))))

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃" # If the computer and user both have the same score, then it's a draw. 
    elif computer_score == 0: # If the computer has a blackjack (0), then the user loses.
        return "Computer win with a Blackjack. You lose 😭"
    elif user_score == 0:
        return "You win with a Blackjack! 😎" # If the user has a blackjack (0), then the user wins. 
    elif user_score > 21:
        return "You went over. You lose 😭" # If the user_score is over 21, then the user loses.
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score: # If none of the above, then the player with the highest score wins.
        return "You win! 😁"
    else:
        return "You lose 😤"


want_to_play = ask_want_to_play()

while want_to_play:
    clear() # Clear the console
    print(logo) # Print logo
    user_cards = [] # Start a new game by clearing the cards
    computer_cards = []

    # Deal the user and computer 2 cards each using deal_card() and append().
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    

    # The score needs to be rechecked with every new card drawn
    while not is_end_of_game(calculate_score(user_cards), calculate_score(computer_cards)): # If it is not the end of the game, then use the deal_card() function to add another card to the user_cards List.
        # Print current status
        print_current_status(user_cards, computer_cards)

        user_decision = input("Do you want to draw another card? Select 'y' or 'n': ").lower()

        # Decision is yes, then we continue with another draw for the user
        if user_decision == "y": 
            user_cards.append(deal_cards())

        else: # Once the user is done, it's time to let the computer play. 
            # The computer should keep drawing cards as long as it has a score less than 17.
            while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
                computer_cards.append(deal_cards())
            break # Once the computer finishes, break the loop, it is the end of game 

    # The game is finished, print the final status
    print_final_status(user_cards, computer_cards)
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))

    # Ask the user if they want to restart the game.    
    want_to_play = ask_want_to_play()
