from flask import Flask, render_template

app = Flask(__name__)  # Create an instance of this class


@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def home():  # This function returns the message we want to display in the user’s browser
    return render_template('angela.html')



# To run it by using our standard run and stop buttons in PyCharm, we will use the below code
if __name__ == "__main__":
    app.run(debug=True)  # This will allow us to run our app in debug mode
