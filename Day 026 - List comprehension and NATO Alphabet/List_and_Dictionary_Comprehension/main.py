import random
import pandas

"""
======================
List Comprehension
======================
"""

# List comprehension is a concise and expressive way to create lists in Python.
# It allows you to create new lists by applying an expression to each item in an existing iterable (such as a list,
# tuple, or range) and optionally filtering the items based on a condition.
# List comprehensions are often used as a more readable and efficient alternative to traditional for loops for
# creating lists.

# new_list = [new_item for item in list]

# Traditional for loop approach
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)  # [2, 3, 4]

# List comprehension approach
new_list2 = [n+1 for n in numbers]
print(new_list2)  # [2, 3, 4]

# Another example for list comprehension
name = "Maialen"
letters_list = [letter for letter in name]
print(letters_list)  # It prints ['M', 'a', 'i', 'a', 'l', 'e', 'n']

# Create a new list from a range, where the list items are double the values in the range.
my_list = [n*2 for n in range(1,5)]
print(my_list)  # [2, 4, 6, 8]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# I only want names that have 4 letters or fewer
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Names that are longer than 5, in uppercase
long_uppercase_names = [name.upper() for name in names if len(name) > 5]
print(long_uppercase_names)  # ['CAROLINE', 'ELANOR', 'FREDDIE']

# Squared numbers
initial_numbers = [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
squared_numbers = [n**2 for n in initial_numbers]
print(squared_numbers)

# The new list should only contain the even numbers from the list numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Use file1.txt and file2.txt. Create a list called result which contains the numbers that are common in both files
with open("file1.txt", "r") as file:  # Open the text file in read mode
    lines_f1 = file.readlines()  # Read each line and create a list
with open("file2.txt", "r") as file:
    lines_f2 = file.readlines()
result = [int(item) for item in lines_f1 if item in lines_f2]
print(result)

"""
======================
Dictionary Comprehension
======================
"""
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items()}  # This is used to create a new dictionary by using another dictionary
# We can always add an if statement at the end to test some conditions

# Create a dictionary of students and scores, by using the list of names
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {name: random.randint(0, 100) for name in names}
print(students_scores)

# By using the dictionary created, create a dictionary of only students with passed marks
passed_students = {key: value for (key,value) in students_scores.items() if value >= 50}
print(passed_students)

# Create a dictionary that takes each word in the given sentence and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
count_of_letters_per_word_dict = {item: len(item) for item in sentence.split()}
print(count_of_letters_per_word_dict)

# Create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {key: (value * 9/5) + 32 for (key,value) in weather_c.items()}
print(weather_f)


"""
======================
Iterate over Pandas DataFrame
======================
"""

# This is how we iterate over a dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items(): # Looping through dictionaries
    print(key)
for (key, value) in student_dict.items(): # Looping through dictionaries
    print(value)

# Now will iterate over a DataFrame
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
for (key, value) in student_data_frame.items(): # Loop through a data frame
    print(key)
for (key, value) in student_data_frame.items():
    print(value) # We see that this is not useful, it does not provide the result we want

# Pandas has a better way to iterate through rows, by using the iterrows() method
for (index, row) in student_data_frame.iterrows():
    print(row.student)
for (index, row) in student_data_frame.iterrows():
    print(row.score)
