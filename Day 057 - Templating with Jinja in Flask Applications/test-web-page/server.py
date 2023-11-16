from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)  # Create an instance of this class

def get_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        result = int(response.json()["age"])
        return result
    else:
        print(f"Error: {response.status_code}")
        return None

def get_gender(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()["gender"]
        return result
    else:
        print(f"Error: {response.status_code}")
        return None


@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def home():
    random_number = random.randint(1,10)  # We want this random number to be displayed in the HTML
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)  # We will send the random number as a parameter

@app.route('/guess/<name>')
def predictor(name):
    name = name
    gender = get_gender(name)
    age = get_age(name)
    return render_template('guess-name.html', name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/36e6b7057201bb6b576a"
    response = requests.get(blog_url)
    all_posts = None

    if response.status_code == 200:
        all_posts = response.json()
    else:
        print(f"Error: {response.status_code}")


    return render_template('blog.html', posts=all_posts)




# To run it by using our standard run and stop buttons in PyCharm, we will use the below code
if __name__ == "__main__":
    app.run(debug=True)  # This will allow us to run our app in debug mode
