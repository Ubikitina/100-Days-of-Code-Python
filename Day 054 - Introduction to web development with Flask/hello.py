# Documentation can be found in https://flask.palletsprojects.com/en/3.0.x/quickstart/
from flask import Flask  # Import Flask class

app = Flask(__name__)  # Create an instance of this class


@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def hello_world():  # This function returns the message we want to display in the user’s browser
    return '<p>Hello, World!</p>'

@app.route("/bye")
def say_bye():
    return "Bye!"

# Commands to run this in our terminal:
# Set the environment variables:
# set FLASK_APP=hello.py
# $env:FLASK_APP="hello.py"
# Ensure that the terminal is in the folder of hello.py, or if not, go to the folder by using cd
# Run flask --app hello run command

# Another way to run it by using our standard run and stop buttons in PyCharm
if __name__ == "__main__":
    app.run()