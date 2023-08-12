import random

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

def print_decision(number):
    if number == 0:
        print(rock)
    elif number == 1:
        print(paper)
    elif number == 2:
        print(scissors)
    else:
        print("Invalid entry")

def who_won(user_number, computer_number):
    if user_number == computer_number:
        print("You have tied this game, try again.")
    elif user_number == 0 and computer_number == 1:
        print("You lose.")
    elif user_number == 0 and computer_number == 2:
        print("You win.")
    elif user_number == 1 and computer_number == 0:
        print("You win.")
    elif user_number == 1 and computer_number == 2:
        print("You lose.")
    elif user_number == 2 and computer_number == 0:
        print("You lose.")
    elif user_number == 2 and computer_number == 1:
        print("You win.")
    else:
        print("Invalid entry")
        print(user_number)
        print(computer_number)
    

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print_decision(user_number)

print("Computer chose:")
computer_number = random.randint(0,2)
print_decision(computer_number)
who_won(user_number, computer_number)



