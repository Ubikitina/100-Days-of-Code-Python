# Day 59: Upgraded Blog Project

Welcome to the Upgraded Blog project! By the end of this day, we will have created a fully-functional, multi-page blog website using Flask and Bootstrap. We will upgrade a simple blog with Bootstrap templates, making it mobile responsive and adding various features.

## Table of Contents
- [Day 59: Upgraded Blog Project](#day-59-upgraded-blog-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Step-by-Step Guide](#step-by-step-guide)
    - [Step 1 - Download the Starting Project](#step-1---download-the-starting-project)
    - [Step 2 - Get the Home Page to Work](#step-2---get-the-home-page-to-work)
    - [Step 3 - Fix the Header and Footer](#step-3---fix-the-header-and-footer)
    - [Step 4 - Using Jinja Include for Render Templates](#step-4---using-jinja-include-for-render-templates)
    - [Step 5 - Make the About and Contact Pages Work](#step-5---make-the-about-and-contact-pages-work)
    - [Step 6 - Fetch and Render the Blog Posts from an API](#step-6---fetch-and-render-the-blog-posts-from-an-api)
    - [Step 7 - Rendering Individual Posts](#step-7---rendering-individual-posts)

## Project Overview
In this project, we will upgrade a simple blog with Bootstrap to enhance its design and functionality. We'll use Flask for backend development and integrate Bootstrap templates for a professional look. The blog will be mobile responsive and will feature dynamic content loading.

## Features
- Multi-page website with an interactive navigation bar
- Dynamically generated blog post pages with full-screen titles
- Fully mobile responsive design
- Interactive elements using Bootstrap

## Step-by-Step Guide

### Step 1 - Download the Starting Project
1. Download the Clean Blog Template from [Start Bootstrap](https://startbootstrap.com/previews/clean-blog/).
2. Unzip the downloaded file and rename the folder to "upgraded_blog".
3. Open the project folder in your code editor (e.g., PyCharm).
4. Create the `static` and `templates` folders.
5. Move HTML files to the `templates` folder and other files (CSS, JS, images) to the `static` folder.
6. Create `header.html` and `footer.html` files in the `templates` folder.
7. Create `main.py` in the project root directory.

### Step 2 - Get the Home Page to Work
1. Create a basic Flask application in `main.py`:
   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == "__main__":
       app.run(debug=True)
   ```
2. Run the Flask app and visit [http://localhost:5000](http://localhost:5000) to see the home page.

### Step 3 - Fix the Header and Footer
1. Move the head and navigation code from `index.html` to `header.html`.
2. Move the footer code from `index.html` to `footer.html`.
3. Use Jinja `include` to include the header and footer in `index.html`:
   ```html
   {% include "header.html" %}
   <!-- Page Content -->
   {% include "footer.html" %}
   ```
4. Update paths for static files in `header.html` and `footer.html` using Flask's `url_for` function:
   ```html
   <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
   ```

### Step 4 - Using Jinja Include for Render Templates
1. Repeat the process for `about.html`, `contact.html`, and `post.html` to include the header and footer templates.
2. Ensure the navigation links in `header.html` use Flask's `url_for` to link to the correct routes.

### Step 5 - Make the About and Contact Pages Work
1. Update `main.py` to handle routes for About and Contact pages:
   ```python
   @app.route('/about')
   def about():
       return render_template('about.html')

   @app.route('/contact')
   def contact():
       return render_template('contact.html')
   ```
2. Update the navigation links in `header.html` to point to the correct routes:
   ```html
   <a class="nav-link" href="{{ url_for('about') }}">About</a>
   <a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
   ```

### Step 6 - Fetch and Render the Blog Posts from an API
1. Create a JSON endpoint with blog post data using [npoint.io](https://www.npoint.io/).
2. Fetch the JSON data in `main.py`:
   ```python
   import requests

   @app.route('/')
   def home():
       response = requests.get('https://api.npoint.io/your-endpoint')
       posts = response.json()
       return render_template('index.html', posts=posts)
   ```
3. Update `index.html` to render posts using Jinja:
   ```html
   {% for post in posts %}
   <div class="post-preview">
       <a href="{{ url_for('post', post_id=post['id']) }}">
           <h2 class="post-title">{{ post['title'] }}</h2>
           <h3 class="post-subtitle">{{ post['subtitle'] }}</h3>
       </a>
       <p class="post-meta">Posted by {{ post['author'] }} on {{ post['date'] }}</p>
   </div>
   {% endfor %}
   ```

### Step 7 - Rendering Individual Posts
1. Update `main.py` to handle routes for individual posts:
   ```python
   @app.route('/post/<int:post_id>')
   def post(post_id):
       response = requests.get('https://api.npoint.io/your-endpoint')
       posts = response.json()
       post = next((item for item in posts if item["id"] == post_id), None)
       return render_template('post.html', post=post)
   ```
2. Update `post.html` to render the post details using Jinja:
   ```html
   <header class="masthead" style="background-image: url('{{ url_for('static', filename=post['image']) }}')">
       <div class="container position-relative px-4 px-lg-5">
           <div class="row gx-4 gx-lg-5 justify-content-center">
               <div class="col-md-10 col-lg-8 col-xl-7">
                   <div class="post-heading">
                       <h1>{{ post['title'] }}</h1>
                       <h2 class="subheading">{{ post['subtitle'] }}</h2>
                       <span class="meta">Posted by {{ post['author'] }} on {{ post['date'] }}</span>
                   </div>
               </div>
           </div>
       </div>
   </header>
   <article>
       <div class="container px-4 px-lg-5">
           <div class="row gx-4 gx-lg-5 justify-content-center">
               <div class="col-md-10 col-lg-8 col-xl-7">
                   {{ post['content'] | safe }}
               </div>
           </div>
       </div>
   </article>
   ```

