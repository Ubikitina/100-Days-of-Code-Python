from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, URL


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    body = TextAreaField("Task Description", validators=[DataRequired()])
    status = SelectField("Status", choices=[('To do', 'To do'), ('In progress', 'In progress'), ('Done', 'Done')],
                         validators=[DataRequired()])
    submit = SubmitField("Submit Task")


# Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")

# Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

# Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_text = TextAreaField("Add your comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

