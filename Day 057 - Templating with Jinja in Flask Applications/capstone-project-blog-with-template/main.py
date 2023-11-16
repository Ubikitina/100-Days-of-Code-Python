from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


blog_url = "https://api.npoint.io/36e6b7057201bb6b576a"
post_objects = []

response = requests.get(blog_url)
all_posts = None
if response.status_code == 200:
    all_posts = response.json()
    for post in all_posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
else:
    print(f"Error: {response.status_code}")


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/blog/<int:num>')
def get_blog(num):
    found_post = None

    for post in post_objects:
        if post.id == num:
            found_post = post
            break
    return render_template('post.html', post=found_post)

if __name__ == "__main__":
    app.run(debug=True)
