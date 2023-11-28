from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# Constants
MOVIE_DB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_DB_API_KEY = "ENTER YOUR PERSONAL KEY HERE"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# Create a Flask web application instance
app = Flask(__name__)

# Set the secret key of the app. The secret key is used to secure session cookies and others in a Flask application
app.config['SECRET_KEY'] = 'ENTER YOUR SECRET HERE'
# Configure the Flask application to use an SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"

# Initialize Bootstrap 5 (front-end framework) for the Flask application
Bootstrap5(app)

# Create an instance of the SQLAlchemy class. This instance will be used to interact with the database
db = SQLAlchemy()
# Set up the database integration with the Flask application
db.init_app(app)

# Create the database table
class Movie(db.Model):
    # We define each of the columns as attributes of the class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(255), nullable=True)


    # Optional: The method __repr__ allows each object to be identified by its attributes when printed.
    def __repr__(self):
        return f'<{self.title} - {self.year} - {self.rating}/10>'


# It uses Flask's application context to create database schema
with app.app_context():
    db.create_all()

# Flask-WTF form designed for users to submit their ratings and reviews for a movie
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

# Flask-WTF form designed for users to search their movie
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# Using code/DB Viewer, add a new entry to the database
# After doing so, we will comment the code to avoid receiving errors for trying to create duplicate records.
# Create a database record
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     # Add this movie to the database session (db.session)
#     db.session.add(new_movie)
#     # Commit the changes to persist the new movie record in the database
#     db.session.commit()
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    # We get the result ordered by movie rating
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    # Convert result into a Python list
    all_movies = result.scalars().all()

    # Another way to convert the result into a Python list
    # movies_list = [movie for movie in all_movies]
    # print(movies_list)

    # Iterate over the collection of movie objects
    for i in range(len(all_movies)):
        # Update the ranking attribute of each movie based on its position in the list
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # If we receive a GET request:
    form = RateMovieForm() # Create WTForm
    movie_id = request.args.get('id')  # Get the movie id
    movie_selected = db.get_or_404(Movie, movie_id)  # Get the movie record to be edited

    # If we receive a POST request:
    if request.method == "POST":
        # Update record
        movie_selected.rating = float(form.rating.data)  # New rating
        movie_selected.review = form.review.data  # New review
        db.session.commit()  # Commit the change to the database to so that it persists
        return redirect(url_for('home'))  # Return the home page

    return render_template("edit.html", movie=movie_selected, form=form)  # Show the editing page and send the selected book



@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    # Delete a record by ID
    movie_to_delete = db.get_or_404(Movie, movie_id)
    # Alternative way to select the movie to delete.
    # movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/add", methods=['GET', 'POST'])
def add():
    # Create the find movie form by using the Flask-WTF class
    form = FindMovieForm()

    # Check if the form has been submitted and is valid
    if form.validate_on_submit():
        # Retrieve the movie title entered by the user from the form.
        movie_title = form.title.data
        # Make a GET request to The Movie Database (TMDB) API to search for movies based on the user's input
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        # Parse the JSON response and extract the "results" key
        data = response.json()["results"]
        # print(data)
        return render_template("select.html", options=data)


    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    # Retrieve the movie API ID from the query parameters of the HTTP request
    movie_api_id = request.args.get("id")

    # Check if a movie API ID was provided
    if movie_api_id:
        # Construct the URL to fetch detailed information
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"

        # Make a GET request to The Movie Database (TMDB) API to get detailed information
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        # print(data)

        # Create a new Movie object with information extracted from the API response
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0], # Extract the year from the release_date
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )

        # Add the new movie to the database session and commit the changes to the database
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
