from flask import Flask, render_template, request

app = Flask(__name__)  # Create an instance of this class

@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def home():  # This function returns the message we want to display in the user’s browser
    return render_template('index.html')

# Method to receive data from the form
@app.route("/login", methods=["POST"])
def receive_data():
    # Get the values of 'name' and 'password' from the form in index.html
    username = request.form.get('username')  # We could also access as a dictionary by doing request.from["username"]
    password = request.form.get('password')

    # Do Something
    return f"💪 Success! Form submitted.\nName: {username}, Password: {password}"


# To run it by using our standard run and stop buttons in PyCharm, we will use the below code
if __name__ == "__main__":
    app.run(debug=True)  # This will allow us to run our app in debug mode
