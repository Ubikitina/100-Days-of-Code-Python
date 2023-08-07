# Print a welcome message to the user.
print("Welcome to the tip calculator.")

# Get the total bill amount from the user as a string.
total_bill = input("What was the total bill? $")
# Check if the entered total bill is a valid number (consisting only of digits).
if not total_bill.isdigit():
    print("Error, the total bill should be a number")
    exit() # Exit the program if the input is not valid

# Get the desired tip percentage from the user as a string.
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
# Check if the entered tip percentage is valid (either 10, 12, or 15).
if not int(tip_percentage) in (10, 12, 15):
    print("Error, the tip should be 10, 12 or 15")
    exit() # Exit the program if the input is not valid

# Get the number of people to split the bill from the user as a string.
number_of_people = input("How many people to split the bill? ")
# Check if the entered number of people is a valid number (consisting only of digits).
if not number_of_people.isdigit():
    print("Error, the number of people should be a number")
    exit() # Exit the program if the input is not valid

# Calculate the tip amount based on the total bill and tip percentage.
tip = (float(total_bill)*int(tip_percentage)/100)
# Calculate the total amount to be paid by each person after splitting the bill.
each_person_total = (float(total_bill) + tip)/int(number_of_people)

# Display the amount each person should pay, formatted with two decimal places.
print("Each person should pay: $" + "{:.2f}".format(each_person_total))