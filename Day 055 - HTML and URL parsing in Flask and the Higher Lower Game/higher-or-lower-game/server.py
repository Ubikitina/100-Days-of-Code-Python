from flask import Flask  # Import Flask class
import random

random_number = random.randint(0, 9)
print(random_number)  # Used for debugging

app = Flask(__name__)  # Create an instance of this class

@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def hello_world():  # This function returns the message we want to display in the user’s browser
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:number>")  # Define a route for handling requests with an integer parameter in the URL
def check_number(number):
    # Check if the provided number matches the randomly generated number
    if number == random_number:  # Return HTML with a success message and an image
        return ('<h1 style="color: green; font-weight: bold;">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    elif number > random_number:  # Return HTML with a too high message and an image
        return ('<h1 style="color: purple; font-weight: bold;">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:  # Return HTML with a too low message and an image
        return ('<h1 style="color: red; font-weight: bold;">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')


# To run it by using our standard run and stop buttons in PyCharm, we will use the below code
if __name__ == "__main__":
    app.run(debug=True)  # This will allow us to run our app in debug mode


