from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# user_loader callback: This callback is used to reload the user object from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
# UserMixin is used for authentication purposes. As per Flask-Login documentation: To make implementing a user class
# easier, you can inherit from UserMixin, which provides default implementations for all of the properties and methods,
# such as is_authenticated, is_active, is_anonymous, get_id().
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Passing True or False if the user is authenticated.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    # Check if the request method is POST (form submission).
    if request.method == "POST":

        # If the user enters an email that already exists in the database, we will redirect them to the login page
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))  # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user: # If the user already exists, show a flash message to let them know they have already registered
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login')) # Redirect them to the login page where the flash message will be shown


        # Get the password entered by the user and hashing and salting it
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        # Create a new User instance with data from the registration form.
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password
        )

        # Add the new user to the database session.
        db.session.add(new_user)
        db.session.commit()  # Commit the changes to the database
        login_user(new_user)  # Uses Flask-Login's login_user function to log in a user immediately after they have successfully registered

        # Render the 'secrets.html' template upon successful registration
        return render_template("secrets.html", name=request.form.get('name'))

    # Render the 'register.html' template for GET requests
    return render_template("register.html", logged_in=current_user.is_authenticated)   # Passing True or False if the user is authenticated.


@app.route('/login', methods=["GET", "POST"])
def login():
    # If it is a post request
    if request.method == "POST":
        email = request.form.get('email')  # Get the email from the form
        password = request.form.get('password')  # Get the password from the form

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # Check if the user exists
        if user:
            # Check stored password hash against entered password hashed. If the password is correct, then
            if check_password_hash(user.password, password):
                login_user(user)  # By using the method from flask_login
                return redirect(url_for('secrets'))
            else:  # If the password is not correct
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
        else:
            # Use the Flask's flash function to store a message in a session variable. The flash function is a part of
            # Flask's messaging system. It takes the string message as an argument and stores temporary messages in the
            # session, which can be retrieved and displayed on subsequent requests. It is typically used to provide
            # feedback or notifications to the user.
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated)  # Passing True or False if the user is authenticated.


@app.route('/secrets')
@login_required  # By adding this, only logged-in users can access the route
def secrets():
    # We can use the module current_user from flask_login to get the name of the current user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()  # We can use the logout_user() from flask_login to log out
    return redirect(url_for('home'))


@app.route('/download')
@login_required  # By adding this, only logged-in users can access the route
def download():
    # The method send_from_directory() will download the cheat_sheet.pdf file when the user clicks on the "Download Your File" button
    return send_from_directory('static', path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
