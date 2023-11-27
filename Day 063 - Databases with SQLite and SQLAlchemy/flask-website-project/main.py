from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


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

# Configure the Flask application to use an SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
# Create an instance of the SQLAlchemy class. This instance will be used to interact with the database
db = SQLAlchemy()
# Set up the database integration with the Flask application
db.init_app(app)

# Create the database table
class Book(db.Model):
    # We define each of the columns as attributes of the class
    id = db.Column(db.Integer, primary_key=True)  # It is an integer and the primary key
    title = db.Column(db.String(250), unique=True, nullable=False)  # Length set to 250 characters, unique and not nullable.
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: The method __repr__ allows each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<{self.title} - {self.author} - {self.rating}/10>'


# Create table schema in the database. Requires application context.
# It uses Flask's application context to execute the database schema creation
with app.app_context():
    db.create_all()


all_books = []


@app.route('/')
def home():
    # Read all records
    # We are executing a query during a database session. It returns a Result object
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Then we use scalars() to get the individual elements rather than entire rows
    all_books = result.scalars()

    # Render the "index.html" template and return the result
    return render_template("index.html", all_books=all_books)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # Create a database record
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        # Add this book to the database session (db.session)
        db.session.add(new_book)
        # Commit the changes to persist the new book record in the database
        db.session.commit()

        # Return back to home page
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # Update record
        book_id = request.form["id"]  # Recover the id of the record to be edited
        book_to_update = db.get_or_404(Book, book_id)  # Get the record to be edited
        book_to_update.rating = request.form["rating"]  # Set a new value for the rating attribute
        db.session.commit()  # Commit the change to the database to so that it persists
        return redirect(url_for('home'))  # Return the home page

    # If we receive a GET request:
    book_id = request.args.get('id')  # Get the book id
    book_selected = db.get_or_404(Book, book_id)  # Get the book record to be edited
    return render_template("edit_rating.html", book=book_selected)  # Show the editing page and send the selected book


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # Delete a record by ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

