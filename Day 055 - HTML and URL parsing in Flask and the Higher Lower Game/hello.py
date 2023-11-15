# Documentation can be found in https://flask.palletsprojects.com/en/3.0.x/quickstart/
from flask import Flask  # Import Flask class

app = Flask(__name__)  # Create an instance of this class

def make_bold(function):  # This is a decorator
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):  # This is a decorator
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):  # This is a decorator
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def hello_world():  # This function returns the message we want to display in the user’s browser
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media3.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>')

@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")  # By using <>, we are creating a variable. If we enter a name in the URL, this name will be displayed in the screen after the "Hello"
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

# Commands to run this in our terminal:
# Set the environment variables:
# set FLASK_APP=hello.py
# $env:FLASK_APP="hello.py"
# Ensure that the terminal is in the folder of hello.py, or if not, go to the folder by using cd
# Run flask --app hello run command

# Another way to run it by using our standard run and stop buttons in PyCharm
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)  # This will allow us to run our app in debug mode