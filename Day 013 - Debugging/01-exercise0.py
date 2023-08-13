############DEBUGGING#####################

# EXERCISE 1:
# Function with a bug
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
#       # Reason for the bug: the range function does not reach the upper limit.
#       # We would need to fix it by writing: range(1, 21)
# my_function()

# EXCERCISE 1 FIXED:
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# EXERCISE 2:
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num]) # The error is produced whenever dice_num is 6. dice_num should be between 0 and 5. This can be fixed by setting randint(0,5)

# EXERCISE 2 FIXED:
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# EXERCISE 3:
# # Play Computer
# year = int(input("What's your year of birth?")) # Problem: 1994 is not included in any of the conditions
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# EXERCISE 3 FIXED:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994: # Solution: we include 1994 by adding = sign
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


# EXERCISE 4:
# # Fix the Errors
# age = input("How old are you?") # Age is string, however, we need int to compare below
# if age > 18:
# print("You can drive at age {age}.") # Indentation error. Also formatting error, a "f" is missing so that it prints the age

# EXERCISE 4: FIXED
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


# EXERCISE 5:
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # A comparison "==" is used instead of assigning the value with "="
# total_words = pages * word_per_page
# print(total_words)

# EXERCISE 5 FIXED:
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # Fixed "==" to "="
# total_words = pages * word_per_page
# print(total_words)


# EXERCISE 6:
# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # Identation error
#   print(b_list)

# mutate([1,2,3,5,8,13])

# EXERCISE 6 FIXED:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) # Corrected
#   print(b_list)

# mutate([1,2,3,5,8,13])