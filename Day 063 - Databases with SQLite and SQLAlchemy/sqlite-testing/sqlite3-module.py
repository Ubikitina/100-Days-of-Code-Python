import sqlite3

# Create a connection to a new database (if the database does not exist then it will be created)
db = sqlite3.connect("books-collection.db")

# Create a cursor which will control our database
cursor = db.cursor()

# Execute a SQL command (query) to create a new table in our database
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Add data to our table by executing an SQL command to do so
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
