from art import logo, vs
from game_data import data
import random
from replit import clear

# Initialize the score variable to 0
current_score = 0

# Select randomly each of the celebrities to be compared
celebrity_A = random.choice(data)
celebrity_B = random.choice(data)
while celebrity_A == celebrity_B:
    celebrity_B = random.choice(data)

game_over = False

# Print the logo
print(logo)

while not game_over:

    # DEBUG
    #print(celebrity_A)
    #print(celebrity_B)

    # Establish who is the winner
    winner = {}
    if celebrity_A['follower_count'] > celebrity_B['follower_count']:
        winner = celebrity_A
    else:
        winner = celebrity_B # TODO: What happens if draw?

    # Print celebrity information to the user
    print(f"Compare A: {celebrity_A['name']}, a {celebrity_A['description']} from {celebrity_A['country']}")
    print(vs)
    print(f"Against B: {celebrity_B['name']}, a {celebrity_B['description']} from {celebrity_B['country']}")

    # Ask the user to select the winner
    user_selection_letter = None
    while user_selection_letter not in ['A', 'B']: # While loop until the user selects a proper option 'A' or 'B'
        user_selection_letter = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # Determine which celebrity dictionary has been selected by the user
    user_selection = {}
    if user_selection_letter == "A":
        user_selection = celebrity_A
    elif user_selection_letter == "B":
        user_selection = celebrity_B


    # Check if user is right or wrong
    if user_selection == winner:
        current_score = current_score+1
        clear()
        print(logo)
        print("You're right! Current score: {}".format(current_score))
        celebrity_A = winner
        celebrity_B = random.choice(data)
        while celebrity_A == celebrity_B:
            celebrity_B = random.choice(data)
    else:
        clear()
        print(logo)
        print("Sorry that's wrong. Final score: {}".format(current_score))
        game_over = True
