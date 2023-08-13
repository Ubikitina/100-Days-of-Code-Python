import sys
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while True:
    # Initialize an empty string to store the user's input
    user_entry = ""

    # Create an infinite loop to repeatedly ask the user for their choice until a proper choice is entered.
    while True:
        # Prompt the user to enter their choice and convert it to lowercase
        user_entry = input("What would you like? (" + my_menu.get_items() + "): ").lower()

        # Check if the user's input is for reporting or switching off
        if user_entry == "report" or user_entry == "off":
            break  # Exit the loop because a valid choice is entered

        # Check if the user's input is in the list of valid coffee choices
        user_drink = my_menu.find_drink(user_entry)  # Returns a MenuItem object with the drink-related attributes
        if user_drink is not None:
            break  # Exit the loop because a valid coffee choice is entered

    # Depending on the user entry, do the corresponding actions
    if user_entry == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    elif user_entry == "off":
        sys.exit()

    # User wants coffee
    else:
        # If there are enough resources
        if my_coffee_maker.is_resource_sufficient(user_drink) and my_money_machine.make_payment(user_drink.cost):
            my_coffee_maker.make_coffee(user_drink)
