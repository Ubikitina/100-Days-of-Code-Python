from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

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


with app.app_context():
    db.create_all()


def to_dict(self):
    #Method 1.
    dictionary = {}
    # Loop through each column in the data record
    for column in self.__table__.columns:
        #Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary

    # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

# ----------------------------------------------------------------
# HTTP GET - Read Record
# ----------------------------------------------------------------


# API call to get a random cafe from the database
@app.route("/random", methods=["GET"])
def get_random_cafe():
    # Execute a database query to select all records from the "Cafe" table.
    result = db.session.execute(db.select(Cafe))
    # Retrieve all cafes from the query result, converting them to scalar values.
    all_cafes = result.scalars().all()
    # Choose a random cafe from the list of all cafes.
    random_cafe = random.choice(all_cafes)
    # return f"Random cafe {random_cafe.name}, located at {random_cafe.location}"  # Debug

    # Method 1 to create and return the JSON
    # Serialize the random_cafe object into a dictionary
    # serialized_cafe = {
    #     "cafe":{
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #         'has_sockets': random_cafe.has_sockets,
    #         'has_toilet': random_cafe.has_toilet,
    #         'has_wifi': random_cafe.has_wifi,
    #         'id': random_cafe.id,
    #         'img_url': random_cafe.img_url,
    #         'location': random_cafe.location,
    #         'map_url': random_cafe.map_url,
    #         'name': random_cafe.name,
    #         'seats': random_cafe.seats
    #     }
    # }
    #
    # # Use jsonify to convert the dictionary into a JSON response
    # return jsonify(serialized_cafe)

    # Method 2 to create and return the JSON
    #Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=to_dict(random_cafe))


# Read all records
@app.route("/all", methods=["GET"])
def get_all_cafes():
    # Execute a database query to select all records from the "Cafe" table ordered by name.
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # Retrieve all cafes from the query result, converting them to scalar values.
    all_cafes = result.scalars().all()

    # Convert each of the cafes into a dictionary and add them to a list
    list_of_cafe_dicts = []
    for cafe in all_cafes:
        list_of_cafe_dicts.append(to_dict(cafe))

    # Jsonify the list of dictionaries
    return jsonify(list_of_cafe_dicts)

@app.route("/search", methods=["GET"])
def search_cafe():
    query_location = request.args.get("loc")
    # Execute a database query to select all records from the "Cafe" table that belong to a particular location.
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Retrieve all cafes from the query result, converting them to scalar values.
    all_cafes = result.scalars().all()

    # If the result is not empty
    if all_cafes:
        # Convert each of the cafes into a dictionary and add them to a list
        list_of_cafe_dicts = []
        for cafe in all_cafes:
            list_of_cafe_dicts.append(to_dict(cafe))

        # Jsonify the list of dictionaries
        return jsonify(list_of_cafe_dicts)

    # If the result is empty
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# ----------------------------------------------------------------
# HTTP POST - Create Record
# ----------------------------------------------------------------
@app.route("/add", methods=["POST"])
def post_new_cafe():
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
    return jsonify(response={"success": "Successfully added the new cafe."})


# ----------------------------------------------------------------
# HTTP PUT/PATCH - Update Record
# ----------------------------------------------------------------
# Updating the price of a cafe based on a particular id:
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
# Define a route in the Flask application that accepts HTTP PATCH requests to update the price of a cafe.
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
# Define the function to handle the PATCH request, taking the cafe_id as a parameter.
def patch_new_price(cafe_id):
    # Extract the new_price from the request's query parameters.
    new_price = request.args.get("new_price")
    # Retrieve the cafe object from the database
    cafe = db.session.get(Cafe, cafe_id)

    # Retrieve the cafe object from the database with the given cafe_id or return a 404 error if not found.
    # This is another way of doing it, if we use this line, then we do not need to add the "else" statement below.
    # cafe = db.get_or_404(Cafe, cafe_id)

    if cafe:  # if the cafe object was found
        cafe.coffee_price = new_price  # Update the coffee_price attribute with the new_price
        db.session.commit()  # Commit the changes to the database
        return jsonify(response={"success": "Successfully updated the price."}), 200  # Return a JSON response
    else:  # if the cafe object was not found
        print("not found")
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404  # Return a JSON response


# ----------------------------------------------------------------
# HTTP DELETE - Delete Record
# ----------------------------------------------------------------
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
# Define the function to handle the DELETE request, taking the cafe_id as a parameter.
def delete_cafe(cafe_id):
    # Retrieve the API key from the request's query parameters
    api_key = request.args.get("api-key")
    print(api_key)

    # Check if the API key matches the expected value
    if api_key == "TopSecretAPIKey":
        print(cafe_id)
        # Retrieve the cafe object from the database
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        print(cafe)

        # Check if the cafe object was found in the database
        if cafe:
            db.session.delete(cafe)  # Delete the cafe object from the database
            db.session.commit()  # Commit the changes to the database
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200  #  Return a JSON response indicating the success

        else: # If the cafe object was not found, return a JSON response with a "Not Found" error message and a status code 404 (Not Found)
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    else:  # If the API key is incorrect, return a JSON response with a "Forbidden" error message and a status code 403 (Forbidden)
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
