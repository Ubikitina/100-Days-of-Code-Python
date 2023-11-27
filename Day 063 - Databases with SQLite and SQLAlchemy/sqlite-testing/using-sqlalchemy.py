# Using SQLAlchemy
# Writing SQL commands are complicated and error-prone. It would be much better if we could just write Python code
# and get the compiler to help us spot typos and errors in our code. That's why SQLAlchemy was created.
# SQLAlchemy is defined as an ORM (Object Relational Mapping) library. This means that it's able to map the
# relationships in the database into Objects.
# - Fields become Object properties.
# - Tables can be defined as separate Classes and each row of data is a new Object.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of Flask application
app = Flask(__name__)

# --------------------------------------------------------------------------------------------------------
# CREATE THE DATABASE
# --------------------------------------------------------------------------------------------------------

# Configure the Flask application to use an SQLite database named new-books-collection.db
# The SQLALCHEMY_DATABASE_URI configuration parameter specifies the URI (Uniform Resource Identifier) for the database.
# In this case, it's an SQLite database.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create an instance of the SQLAlchemy class. This instance will be used to interact with the database
db = SQLAlchemy()
# Initialise the Flask app with the SLQAlchemy extension. We do it to set up the database integration with the Flask application
db.init_app(app)

# --------------------------------------------------------------------------------------------------------
# CREATE THE TABLE
# --------------------------------------------------------------------------------------------------------

# Book class inherits from db.Model. db.Model represents a model for the database table db defined. In SQLAlchemy, tables are classes
class Book(db.Model):
    # We define each of the columns as attributes of the class
    id = db.Column(db.Integer, primary_key=True)  # It is an integer and the primary key
    title = db.Column(db.String(250), unique=True, nullable=False)  # Length set to 250 characters, unique and not nullable.
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: The method __repr__ allows each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
# It uses Flask's application context to execute the database creation
with app.app_context():
    db.create_all()

# --------------------------------------------------------------------------------------------------------
# CREATE A RECORD
# --------------------------------------------------------------------------------------------------------
# Within the application context
with app.app_context():
    # Create a new instance of the Book class representing a book with specified attributes (id, title, author, rating)
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # Note: When creating new records, the primary key fields is optional. you can also write:
    # new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3), the id field will be auto-generated

    # Add this book to the database session (db.session)
    db.session.add(new_book)
    # Commit the changes to persist the new book record in the database
    db.session.commit()


# --------------------------------------------------------------------------------------------------------
# READ RECORDS
# --------------------------------------------------------------------------------------------------------

# Read all records
with app.app_context():
    # db.select(Book).order_by(Book.title) is a "query" to select things from the database
    # We are executing a query during a database session. It returns a Result object
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Then we use scalars() to get the individual elements rather than entire rows
    all_books = result.scalars()

# Read a particular record by query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # To get a single element we can use scalar() instead of scalars()


# --------------------------------------------------------------------------------------------------------
# UPDATE RECORDS
# --------------------------------------------------------------------------------------------------------
# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# --------------------------------------------------------------------------------------------------------
# DELETE RECORDS
# --------------------------------------------------------------------------------------------------------
# Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    # You can also delete by querying for a particular value e.g. by title or one of the other properties. The get_or_404() method is quite handy
