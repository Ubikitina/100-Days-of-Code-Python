from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

# Print the program logo
print(logo)
# Display a welcome message
print("Welcome to the secret auction program.")

# Initialize a variable to control the loop
other_bidders = "yes"

# Create an empty dictionary to store bids
bids_dictionary = {}

# Execute a loop as long as there are other bidders
while other_bidders == "yes":
    # Ask the user for their name and convert it to lowercase
    name = input("What is your name?: ").lower()

    # Ask the user for their bid and convert it to an integer
    bid = int(input("What's your bid?: $"))

    # Store the user's bid in the dictionary with their name as the key
    bids_dictionary[name] = bid

    # Ask the user if there are any other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    # Clear the screen
    clear()

# Find the bidder with the highest bid
max_key = max(bids_dictionary, key=bids_dictionary.get)
max_value = bids_dictionary[max_key]

# Display the winner's name and bid
print("The winner is {} with a bid of ${}.".format(max_key, str(max_value)))