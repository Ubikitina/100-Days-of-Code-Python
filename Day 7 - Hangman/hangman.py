import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Create a variable called 'lives' to keep track of the number of lives left. 
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
display = []
for _ in range(len(chosen_word)):
    display.append("_")

print(f"{' '.join(display)}")

list_of_used_letters = []
# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    if guess in list_of_used_letters:
        print("You've already guessed "+ guess)
    else:
        list_of_used_letters.append(guess)


    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
    if not guess in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        lives = lives - 1
        
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives == 0:
            end_of_game = True
            print("You lose!")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    
    # Check if it is the end of the game
    if not "_" in display:
        end_of_game = True
        print("You win!")
    
    

