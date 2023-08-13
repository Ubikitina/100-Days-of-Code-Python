import sys

# Define the menu items along with their ingredients and cost.
MENU = {
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18, }, "cost": 1.5, },
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24, },
        "cost": 3.0,
    },
}

# Define available resources including water, milk, coffee, and money.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Define the possible user entries
user_entry_list = ["espresso", "latte", "cappuccino", "report", "off"]


def calculate_change(qu, di, nick, pen, user_selection):
    """
    Calculate the change to return to the user based on inserted coins.

    Args:
        qu (int): Number of quarters.
        di (int): Number of dimes.
        nick (int): Number of nickels.
        pen (int): Number of pennies.
        user_selection (str): Selected coffee item.

    Returns:
        float: Change to be returned to the user.
    """
    total_user_money = (qu * 25 + di * 10 + nick * 5 + pen * 1) / 100
    coffee_cost = MENU[user_selection]["cost"]
    return total_user_money - coffee_cost


def update_resources(user_selection):
    """
    Update the resources after a coffee is purchased.

    Args:
        user_selection (str): Selected coffee item.
    """
    resources["water"] = resources["water"] - MENU[user_selection]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[user_selection]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_selection]["ingredients"]["coffee"]
    resources["money"] = resources["money"] + MENU[user_selection]["cost"]


def print_resources():
    """Print the current available resources."""
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}g".format(resources["coffee"]))
    print("Money: ${:.2f}".format(resources["money"]))


def are_enough_resources(user_selection):
    """
    Check if there are enough resources for the selected coffee.

    Args:
        user_selection (str): Selected coffee item.

    Returns:
        bool: True if there are enough resources, False otherwise.
    """
    enough_water = False
    enough_milk = False
    enough_coffee = False

    if resources["water"] - MENU[user_selection]["ingredients"]["water"] >= 0:
        enough_water = True

    if resources["milk"] - MENU[user_selection]["ingredients"]["milk"] >= 0:
        enough_milk = True

    if resources["coffee"] - MENU[user_selection]["ingredients"]["coffee"] >= 0:
        enough_coffee = True

    if enough_water and enough_milk and enough_coffee:
        return True
    elif not enough_water:
        print("Sorry there is not enough water.")
        return False
    elif not enough_milk:
        print("Sorry there is not enough milk.")
        return False
    else:
        print("Sorry there is not enough coffee.")
        return False


# Start

while True:
    # Initialize an empty string to store the user's input
    user_entry = ""

    # Create an infinite loop to repeatedly ask the user for their choice
    while True:
        # Prompt the user to enter their choice and convert it to lowercase
        user_entry = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Check if the user's input is in the list of valid choices
        if user_entry in user_entry_list:
            break  # Exit the loop if a valid choice is entered
        else:
            # Print an error message if the user's input is not valid
            print("Invalid choice. Please enter 'espresso', 'latte', or 'cappuccino'.")

    # User wants coffee
    if user_entry == "espresso" or user_entry == "latte" or user_entry == "cappuccino":
        # If there are enough resources
        if are_enough_resources(user_entry):  # then we ask for the money
            print("Please, insert coins.")
            quarters = int(input("how many quarters?: "))  # 25 cents each
            dimes = int(input("how many dimes?: "))  # 10 cents each
            nickles = int(input("how many nickles?: "))  # 5 cents each
            pennies = int(input("how many pennies?: "))  # 1 cent each
            change = calculate_change(quarters, dimes, nickles, pennies, user_entry)
            if change >= 0:
                print("Here is ${:.2f} in change.".format(change))
                # Discount the goods from resources
                update_resources(user_entry)
                print("Here is your {} ☕. Enjoy!".format(user_entry))
            else:
                print("Sorry that's not enough money. Money refunded.")

    # User wants to see the report
    elif user_entry == "report":
        print_resources()

    elif user_entry == "off":
        sys.exit()
