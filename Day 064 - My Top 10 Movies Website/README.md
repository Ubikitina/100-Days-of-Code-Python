# Day 64 - My Top 10 Movies Website

## Overview
This project is a website where you can list and manage your top 10 favorite movies of all time. It allows users to add, edit, and delete movies from their list, as well as sort and rank movies based on their ratings.

Technologies used: Flask, WTForms, SQLite, and SQLAlchemy.


## Features

### View Movie List
1. Query the data using Flask-SQLAlchemy when you visit the home page.
2. Display each movie entry correctly on the home page using Jinja templates.

![](./img/01.gif)

### Edit Movie Rating and Review
1. Create a `RateMovieForm` using WTForms.
2. Render the form in `edit.html`.
3. Validate and update the corresponding movie entry in the database upon form submission.



### Delete Movies
1. Implement the delete functionality for each movie entry.
2. Allow the user to delete movies from the database by clicking the delete button on the back of the movie card.

![](./img/02.gif)

### Add New Movies
1. Render the `add` page with a WTForm that contains one field for the movie title.
2. Use the requests library to search The Movie Database API for movies matching the title.
3. Render `select.html` with the results.
4. Use the selected movie's ID to fetch detailed data from the API.
5. Populate the database with the new movie entry and redirect to the `edit.html` page for additional data input (rating and review).

![](./img/03.gif)

### Sort and Rank Movies
1. Implement functionality to sort and rank movies by rating.
2. Update the home page to display the movie rankings correctly.




## Installation

### Download the Starting Project
1. Download the starting `.zip` files from the lesson's resources.
2. Unzip the project and open it in PyCharm.

### Setup Virtual Environment
1. PyCharm may prompt you to create a new virtual environment and install the dependencies listed in `requirements.txt`. Agree and click OK.
2. If not prompted, set up a virtual environment manually:
    - Go to `File -> Settings -> Project -> Python Interpreter`.
    - Click `Add Interpreter -> Add Local Interpreter`.
    - Leave the default settings and click OK.

### Install Dependencies
1. Open the Terminal in PyCharm (bottom left).
2. Install the required packages:
    - On Windows: `python -m pip install -r requirements.txt`
    - On macOS: `pip3 install -r requirements.txt`

### Verify Installation
1. Ensure there are no red underlines in `main.py`.
2. If you still see any red underlines, reload the virtual environment by going to `File -> Reload All from Disk`.

### API usage
This project uses the API of https://www.themoviedb.org/. Add your `MOVIE_DB_API_KEY` in [main.py](main.py) to test the project.

## Resources
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [WTForms Documentation](https://wtforms.readthedocs.io/en/2.3.x/)
- [Bootstrap-Flask Documentation](https://bootstrap-flask.readthedocs.io/en/stable/)
- [The Movie Database API Documentation](https://developers.themoviedb.org/3/getting-started/introduction)

