# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# Generate letters
for _ in range(nr_letters): # the underscore is used as a variable name in situations where the value of the variable isn't going to be used or referenced within the loop
    password += random.choice(letters)

# Generate symbols
for _ in range(nr_symbols):
    password += random.choice(symbols)

# Generate numbers
for _ in range(nr_numbers):
    password += random.choice(numbers)

print("Eazy Level")
print("Here is your password: " + password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
char_list = list(password)  # Convert string to a list of characters
random.shuffle(char_list)       # Shuffle the list in-place
password = ''.join(char_list)  # Convert the list back to a string

print("Hard Level")
print("Here is your password: " + password)
