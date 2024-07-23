from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import random
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, URL, Length

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for securely signing the session cookie and other security-related needs
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Initialize the Bootstrap 5 extension with the Flask app for using Bootstrap in templates
Bootstrap5(app)


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# Cafe form class
class CafeForm(FlaskForm):
    name = StringField(label='Cafe name', validators=[DataRequired(), Length(max=250)])
    map_url = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(), Length(max=500)])
    img_url = StringField(label='Cafe Image (URL)', validators=[DataRequired(), URL(), Length(max=500)])
    loc = StringField(label='Location', validators=[DataRequired(), Length(max=250)])
    seats = StringField(label='Seats e.g. 50+', validators=[DataRequired(), Length(max=250)])
    toilet = BooleanField(label='There is a bathroom')
    wifi = BooleanField(label='There is Wifi')
    sockets = BooleanField(label='There are sockets')
    calls = BooleanField(label='Calls can be answered')
    coffee_price = StringField(label='Coffee Price', validators=[Length(max=250)])
    submit = SubmitField('Submit')

# Search form class
class SearchForm(FlaskForm):
    search_item = StringField(label='', validators=[DataRequired()], render_kw={"placeholder": "Search for a cafe"})
    submit = SubmitField('Submit')

# Create an application context for the 'app' instance.
with app.app_context():
    # Create all database tables defined in SQLAlchemy models
    db.create_all() # It is equivalent to running the SQL 'CREATE TABLE' statements


def to_dict(self):
    dictionary = {}
    # Loop through each column in the data record
    for column in self.__table__.columns:
        #Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary


# Define a route for the root URL ("/")
@app.route("/")
def home():
    # Render the "index.html" template and return the result
    return render_template("index.html")



# Get a random cafe from the database
@app.route("/random", methods=["GET"])
def get_random_cafe():
    # Execute a database query to select all records from the "Cafe" table.
    result = db.session.execute(db.select(Cafe))
    # Retrieve all cafes from the query result, converting them to scalar values.
    all_cafes = result.scalars().all()
    # Choose a random cafe from the list of all cafes.
    random_cafe = random.choice(all_cafes)

    # Convert the random_cafe data record to a json dictionary of key-value pairs.
    return render_template("random.html", cafe=to_dict(random_cafe))


# Read all records
@app.route("/all", methods=["GET", "POST"])
def get_all_cafes():
    search_form = SearchForm()

    if search_form.validate_on_submit():
        cafe_loc = request.form.get("search_item").title()
        result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_loc))
        all_cafes = result.scalars().all()
        if all_cafes:
            # Convert each of the cafes into a dictionary and add them to a list
            list_of_cafe_dicts = []
            for cafe in all_cafes:
                list_of_cafe_dicts.append(to_dict(cafe))

            return render_template("cafes.html", search_form=search_form, cafes=list_of_cafe_dicts)
        else:
            flash("Cafes in this area are not currently available.", 'error')
            return redirect(url_for('get_all_cafes'))


    # Execute a database query to select all records from the "Cafe" table ordered by name.
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # Retrieve all cafes from the query result, converting them to scalar values.
    all_cafes = result.scalars().all()

    # Convert each of the cafes into a dictionary and add them to a list
    list_of_cafe_dicts = []
    for cafe in all_cafes:
        list_of_cafe_dicts.append(to_dict(cafe))

    return render_template('cafes.html', search_form=search_form, cafes=list_of_cafe_dicts)



@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    # Create an instance of the CafeForm
    form = CafeForm()

    # Check if the form is submitted and passes all validations
    if form.validate_on_submit():
        # Create a new cafe by getting the values send via API request (this request has been launched by imitating a form)
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )

        # Add the new_cafe object to the database session.
        db.session.add(new_cafe)
        # Commit the changes made in the session to the database
        db.session.commit()
        return redirect(url_for('get_all_cafes'))

    return render_template('add.html', form=form)


@app.route("/report-closed/<int:cafe_id>", methods=["GET", "DELETE", "POST"])
# Define the function to handle the DELETE request, taking the cafe_id as a parameter.
def delete_cafe(cafe_id):
    # Retrieve the cafe object from the database
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()

    # Check if the cafe object was found in the database
    if cafe:
        db.session.delete(cafe)  # Delete the cafe object from the database
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('get_all_cafes'))

    else:
        return redirect(url_for('get_all_cafes'))



if __name__ == '__main__':
    app.run(debug=True)
