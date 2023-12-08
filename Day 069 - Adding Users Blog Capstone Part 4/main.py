from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something_else'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# user_loader callback: This callback is used to reload the user object from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# For adding profile images to the comment section by using Gravatar
# Gravatar is a service that associates images with email addresses. If an image is registered with the provided email on Gravatar, it will be displayed; otherwise, a default image will be shown.
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    # Bidirectional One-to-Many relationship between the two tables Users (Parent) and BlogPost (Child).
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    #Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="posts")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # One to Many relationship between each BlogPost object (Parent) and Comment object (Child). Where each BlogPost can have many associated Comment objects.
    comments = relationship("Comment", back_populates="parent_post")


# Create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    # Bidirectional One-to-Many relationship between the two tables Users (Parent) and BlogPost (Child).
    # This will act like a List of BlogPost objects attached to each User.
    posts = relationship("BlogPost", back_populates="author")  # The "author" refers to the author property in the BlogPost class.

    # Parent relationship with the Comment table: One to Many relationship Between the User Table (Parent) and the Comment table (Child). One User can be linked to Many Comment objects.
    comments = relationship("Comment", back_populates="comment_author")  # "comment_author" refers to the comment_author property in the Comment class.


# New table to store user comments in the database
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)

    # Child relationship with the User table: One to Many relationship Between the User Table (Parent) and the Comment table (Child). One User can be linked to Many Comment objects.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))   # "users.id" The users refers to the tablename of the Users class.
    comment_author = relationship("User", back_populates="comments")  # "comments" refers to the comments property in the User class.

    # One to Many relationship between each BlogPost object (Parent) and Comment object (Child). Where each BlogPost can have many associated Comment objects.
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")

    text = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()

#Create admin-only decorator
def admin_only(f): # Define a decorator function named admin_only that takes a function f as an argument
    # Use the wraps decorator from the functools module to preserve the original function's metadata
    @wraps(f)
    # Define an inner function. It takes any number of positional and keyword arguments
    def decorated_function(*args, **kwargs):
        # Check if the ID of the current user (assuming current_user is part of a Flask login manager)
        #If id is not 1 then return abort with 403 error. Also abort when user is not authenticated
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)  # 403 is a Forbidden error
        #Otherwise, the user is an admin, so continue with the route function by passing any provided *args and **kwargs
        return f(*args, **kwargs)
    # Return the decorated function (decorated_function) with the admin-checking logic added
    return decorated_function

# Register new users into the User database
# Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()  # Create an instance of the RegisterForm class. RegisterForm class has been created by me in forms.py file.

    # Check if the form has been submitted (POST request)
    if form.validate_on_submit():
        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))  # For more explanations and comments in all this code, please refer to day 68 code.


        # Generate a hashed and salted password using the generate_password_hash function from Flask-Bcrypt
        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256', # this is the hashing method used
            salt_length=8
        )

        # Create a new user instance using the data from the form and the hashed password
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        #This line will authenticate the user with Flask-Login
        login_user(new_user)

        # Redirect to the 'get_all_posts' route
        return redirect(url_for("get_all_posts"))

    # If the form is not submitted, then redirect to 'register.html' template, passing the form instance to the template for display.
    return render_template("register.html", form=form, current_user=current_user)


# Retrieve a user from the database based on their email.
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()  # Create a LoginForm instance.

    # If it is a POST request
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))  # Note, email in db is unique so will only have one result.
        user = result.scalar()

        # If the user exists and the password is valid
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:  # Password incorrect
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
        else:  # User does not exist
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))


    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()  # Add the CommentForm to the route

    # Manage a POST request by only allowing logged-in users to comment on posts
    if comment_form.validate_on_submit():
        # Check if the user is not authenticated (logged in)
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")  # Flash a message informing the user to login or register
            return redirect(url_for("login"))  # Redirect the user to the login page

        # Create a new Comment object with the data from the comment form
        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        # Add the new comment to the database
        db.session.add(new_comment)  # First add to the current session
        db.session.commit()  # Then commit it to the database

    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)



@app.route("/new-post", methods=["GET", "POST"])
@admin_only  # Use a decorator so only an admin user can create a new post
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only  # Use a decorator so only an admin user can create a new post
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only  # Use a decorator so only an admin user can create a new post
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
