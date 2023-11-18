from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

MY_EMAIL ="ENTER YOUR EMAIL HERE"
MY_PASSWORD = "ENTER YOUR PASSWORD HERE"

app = Flask(__name__)  # Create an instance of this class

blog_url = "https://api.npoint.io/87d700a958900c32f250"
post_objects = []

# Send an HTTP GET request to the specified 'blog_url' to retrieve blog data
response = requests.get(blog_url)

# Initialize the variable 'all_posts' to None
all_posts = None

# If the status code is 200, the response is successful
if response.status_code == 200:
    all_posts = response.json() # Parse the response content as JSON and store it in 'all_posts'
    # Iterate through each post in 'all_posts'
    for post in all_posts:
        # Create a 'Post' object using the data from the current post
        post_obj = Post(
            post["id"],
            post["title"],
            post["subtitle"],
            post["body"],
            post["author"],
            post["date"],
            post["image_url"]
        )
        # Append the 'post_obj' to the 'post_objects' list (assuming it's defined elsewhere)
        post_objects.append(post_obj)
else:
    # If the HTTP response status code is not 200, print an error message
    print(f"Error: {response.status_code}")


@app.route('/')  # Use the route() decorator to tell Flask what URL should trigger our function. We are using '/', so we will be showing the home page
def home():  # This function returns the message we want to display in the user’s browser
    return render_template('index.html', posts=post_objects)

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/blog/<int:num>')
def get_blog(num):
    found_post = None

    for post in post_objects:
        if post.id == num:
            found_post = post
            break
    return render_template('post.html', post=found_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # If data has been sent by the user
    if request.method == "POST":
        # Get the values from the form in contact.html
        name = request.form.get('name')  # We could also access as a dictionary by doing request.from["name"]
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Send the form information entered by the user via email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure our connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Contact Request\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )
        print(f"💪 Success! Form submitted.\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template('contact.html', message_sent=True)
    else:
        return render_template('contact.html', message_sent=False)




# To run it by using our standard run and stop buttons in PyCharm, we will use the below code
if __name__ == "__main__":
    app.run(debug=True)  # This will allow us to run our app in debug mode
