from sheety import Sheety

# Print a welcome message to the user
print("Welcome to Maialen's Flight Club.")
print("We find the best flight deals and email you.")

# Prompt the user to enter their first name
print("What is your first name?")
first_name = input()

# Prompt the user to enter their last name
print("What is your last name?")
last_name = input()

# Initialize a variable to check if the entered email addresses match
emails_match = False

# Start a loop that continues until the entered email addresses match
while not emails_match:
    print("What is your email?")
    email = input()

    print("Type your email again.")
    email2 = input()

    # Check if the two entered email addresses match
    if email == email2:
        # Set emails_match to True and create a Sheety object
        emails_match = True
        my_sheety = Sheety()

        # Post a new row of data to a spreadsheet with the user's info
        my_sheety.post_spreadsheet_row(first_name=first_name, last_name=last_name, email=email)
        print("You're in the club")
    else:
        # If the email addresses don't match, ask the user to enter them again
        print("Emails didnt match, please enter them again.")