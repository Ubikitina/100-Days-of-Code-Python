from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Cafe form class
class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe name', validators=[DataRequired()])
    cafe_location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_strength_rating = SelectField(label='Wifi Strength Rating', validators=[DataRequired()], choices=[('❌', '❌'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')])
    power_socket_availability = SelectField(label='Power Socket Availability', validators=[DataRequired()], choices=[('❌', '❌'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# Define a route for the root URL ("/")
@app.route("/")
def home():
    # Render the "index.html" template and return the result
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},{form.cafe_location.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_strength_rating.data},{form.power_socket_availability.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# Define a route for the "/cafes" URL
@app.route('/cafes')
def cafes():
    # Open the CSV file 'cafe-data.csv' in read mode with specific encoding
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        # Create a CSV reader object with comma as the delimiter
        csv_data = csv.reader(csv_file, delimiter=',')
        # Initialize an empty list to store rows from the CSV file
        list_of_rows = []
        # Iterate through each row in the CSV file and append it to the list
        for row in csv_data:
            list_of_rows.append(row)

        print(list_of_rows)

    # Render the 'cafes.html' template, passing the list of rows as a variable named 'cafes'
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
