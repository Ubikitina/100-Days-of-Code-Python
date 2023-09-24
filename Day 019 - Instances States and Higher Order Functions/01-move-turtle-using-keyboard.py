from turtle import Turtle, Screen

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_counter_clockwise():
    tim.left(90)

def move_clockwise():
    tim.right(90)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set up the turtle
tim = Turtle()
screen = Screen()

# Set up key bindings
screen.onkey(key="Up", fun=move_forwards)  # A higher order function is a function that can work with other functions
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Left", fun=move_counter_clockwise)
screen.onkey(key="Right", fun=move_clockwise)
screen.onkey(key="C", fun=clear_drawing)

# Listen for key events
screen.listen()


screen.exitonclick()
