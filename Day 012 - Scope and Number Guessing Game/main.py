#Number Guessing Game Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def guess_result(guess, random_number):
    if guess == random_number:
        return "You got it! The answer was {}".format(str(random_number))
    elif guess > random_number:
        return "Too high."
    else:
        return "Too low."

# Include an ASCII art logo.
print(logo)

print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

print("# DEBUG # Number: " + str(random_number))

number_attempts = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while not (difficulty == "easy" or difficulty == "hard"):
    print("Enter a correct difficulty.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    number_attempts = EASY_LEVEL_TURNS
else:
    number_attempts = HARD_LEVEL_TURNS

while number_attempts > 0:
    print("You have {} attemps remaining to guess the number.".format(number_attempts))
    number_attempts = number_attempts - 1
    guess = int(input("Make a guess: "))
    print(guess_result(guess, random_number))
    if guess == random_number:
        number_attempts = 0
    elif number_attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
