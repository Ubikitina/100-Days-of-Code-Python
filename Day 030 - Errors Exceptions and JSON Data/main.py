# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text+5)

# try:
#     file = open("a_file.txt")  # Try to open the file "a_file.txt"
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]  # Attempt to access a dictionary key
# except FileNotFoundError:  # If a FileNotFoundError occurs, create the file "a_file.txt" in write mode ("w")
#     file = open("a_file.txt", "w")  # This will create the file if it doesn't exist
#     file.write("Something")  # Write "Something" to the file
# except KeyError as error_message:
#     # If a KeyError occurs, print a message indicating which key caused the error
#     print(f"The key {error_message} does not exist.")
# else:
#     # If no exceptions occurred, read the content of the file and print it
#     content = file.read()
#     print(content)
# finally:
#     # Finally block is always executed, close the file and print a closing message
#     file.close()
#     print("File was closed")



# How to raise our own error
# height = float(input("Height: "))  # Prompt the user to enter their height in meters
# weight = int(input("Weight: "))  # Prompt the user to enter their weight in kilograms
#
# # Check if the entered height is valid (not over 3 meters)
# if height > 3:
#     # Raise a ValueError with an error message if the height is invalid
#     raise ValueError("Human Height should not be over 3 meters.")
#
# # Calculate the Body Mass Index (BMI) using the entered height and weight
# bmi = weight/height**2
# print(bmi)  # Print the calculated BMI



# fruits = ["Apple", "Pear", "Orange", "Banoffee"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("Fruit pie")
#   else:
#     print(fruit + " pie")
#
# make_pie(4)



# facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
# # Catch the KeyError exception
# for post in facebook_posts:
#   try:
#     total_likes = total_likes + post['Likes']
#   except KeyError:
#     pass
#
#
# print(total_likes)
