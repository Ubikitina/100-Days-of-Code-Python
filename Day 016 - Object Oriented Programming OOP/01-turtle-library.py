# Import the turtle module
import turtle

# Create a turtle object named 'timmy'
timmy = turtle.Turtle()

# Print the turtle object, showing its memory location
print(timmy)  # Prints "<turtle.Turtle object at 0x000002213E258F70>"

# Set the shape of the turtle to "turtle"
timmy.shape("turtle")

# Set the color of the turtle's pen (outline) to black and fill color to purple
timmy.color("black", "purple")

# Initialize a flag for more moves
more_move = True

# Start a loop for receiving move input and performing actions
while more_move:
    # Ask the user for a move choice
    user_input = input("Select a move: 'forward', 'backward', 'left' or 'right': ")

    # Check the user's input and execute corresponding actions
    if user_input == 'forward':
        timmy.forward(100)
    elif user_input == 'backward':
        timmy.backward(100)
    elif user_input == 'left':
        timmy.left(90)
    elif user_input == 'right':
        timmy.right(90)

    # Ask the user if they want to make another move
    if input("Another move? Select 'y' or 'n': ") != 'y':
        more_move = False

# Create a turtle screen named 'my_screen'
my_screen = turtle.Screen()
# Print the height of the turtle screen's canvas
print(my_screen.canvheight)

# Wait for a click on the screen and then close it
my_screen.exitonclick()
