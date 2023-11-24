from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'  # Random secret key

# Initialize Flask-Bootstrap
bootstrap = Bootstrap5(app)


# Login form class
class LoginForm(FlaskForm):
    email = StringField(label='Email', render_kw={'size': 30}, validators=[DataRequired(), Email(message="Please enter a valid email.")])
    password = PasswordField(label='Password', render_kw={'size': 30}, validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    # Create the form
    form = LoginForm()

    # Validate the user's entry when they hit submit. It will be True if validation was successful after the user submitted the form
    if form.validate_on_submit():
        # Depending on the user input, we will return one or the other result
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
