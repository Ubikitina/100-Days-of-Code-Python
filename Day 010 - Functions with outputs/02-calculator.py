# Import necessary modules
from replit import clear
from art import logo

# Function to perform addition
def add(num1, num2):
    return num1+num2

# Function to perform substraction
def substract(num1, num2):
    return num1-num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1*num2

# Function to perform division
def divide(num1, num2):
    return num1/num2


# Define a function that implements a basic calculator
def calculator():
    print(logo) # Print the logo
    # Ask for user inputs
    first_number = float(input("What's the first number?: "))
    
    # Initialize the variable to control the loop
    run_again = "y"

    # Main loop to perform calculations
    while run_again == "y":

        # Print the available operation symbols
        for key in operations:
            print(key)
        
        # Ask for user inputs
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        # Calculate the operation
        result = 0
        if operation_symbol in operations:
            function = operations[operation_symbol]
            result = function(first_number, second_number)
        else:
            # Indicate an error
            print(f"Operation symbol {operation_symbol} not found in the dictionary.")
            result = -1

        # Display the result to the user
        print("{} {} {} = {}".format(str(first_number), operation_symbol, str(second_number), str(result)))

        # Ask the user if they want to continue with the previous result or start a new calculation
        run_again = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ".format(str(result)))
        if run_again == "y":
            first_number = result # Update the first number with the previous result
        else:
            clear() # Clear the terminal screen
            calculator() # Start a new calculation



# Define the available arithmetic operations as a dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


calculator()