from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

# Create an instance of the Flask application
app = Flask(__name__)
# Set the 'SECRET_KEY' configuration parameter for the Flask app. It is used for various security-related purposes, such as session management.
app.config['SECRET_KEY'] = 'Enter your secred key here'
# Create an instance of CKEditor and associate it with the Flask app. This allows the CKEditor to be used in the Flask app to handle rich text editing.
ckeditor = CKEditor(app)
# Create an instance of Bootstrap5 and associate it with the Flask app. Bootstrap is a  front-end framework, and Flask-Bootstrap integrates it with Flask applications.
bootstrap = Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# Define a form class, which extends FlaskForm.
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    # Define a CKEditorField named 'body' for the blog content.
    # CKEditorField is a rich text editor for handling formatted text.
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # Execute a select query on the database for all rows in the "BlogPost" table
    result = db.session.execute(db.select(BlogPost))
    # The scalars() method is used to convert the result into a scalar query
    # The all() method retrieves all the rows as a list
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


#  add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    # Create an instance of the CreatePostForm
    form = CreatePostForm()

    # Check if the form has been submitted and is valid
    if form.validate_on_submit():

        # Create a new BlogPost instance with data from the form
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )

        # Add the new post to the database session
        db.session.add(new_post)
        db.session.commit()  # Commit the changes to the database
        # Redirect to the "get_all_posts" view
        return redirect(url_for("get_all_posts"))
    # If the form is not submitted, render the "make-post.html" template
    return render_template("make-post.html", form=form)

# edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # Retrieve the blog post with the specified 'post_id' from the database. If the post is not found, return a 404 error.
    post = db.get_or_404(BlogPost, post_id)

    # Create an instance of the 'CreatePostForm' for editing the blog post. Populate the form fields with the current values.
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )

    # Check if the form has been submitted and is valid.
    if edit_form.validate_on_submit():
        # Update the blog post with the new values from the form
        # HTML forms (WTForms included) do not accept PUT, PATCH or DELETE methods. So while this would normally be a
        # PUT request (replacing existing data), because the request is coming from a HTML form, you should accept the
        # edited post as a POST request.
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data

        # Commit the changes to the database
        db.session.commit()
        # Redirect to the 'show_post' view for the edited post
        return redirect(url_for("show_post", post_id=post.id))

    # If the form is not submitted, render the 'make-post.html' template with the edit form and indicate it's an edit operation
    return render_template("make-post.html", form=edit_form, is_edit=True)

# delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    # Retrieve the blog post with the specified 'post_id' from the database. If the post is not found, return a 404 error.
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)  # Delete the retrieved blog post from the database session.
    db.session.commit()  # Commit the changes to the database.
    return redirect(url_for('get_all_posts'))  # Redirect to the 'get_all_posts' view

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
