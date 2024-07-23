# Day 67 Project Tasks Summary - RESTFul Routing

## Goal
Add more HTTP routes so that you can create new blog posts, edit posts and delete posts. 

## Project Setup

1. **Download Starting Project**
   - Download the .zip file from the lesson's resources.
   - Unzip and open the project in PyCharm.
   - Create a new virtual environment and install dependencies from `requirements.txt`.

2. **Troubleshooting Setup**
   - If not prompted to create a virtual environment, set it up manually via File -> Settings -> Project -> Python Interpreter.
   - If red underlines persist in `main.py`, install required packages manually using the terminal:
     - Windows: `python -m pip install -r requirements.txt`
     - MacOS: `pip3 install -r requirements.txt`

3. **Database Familiarization**
   - Locate `posts.db` in the project.
   - Use DB Viewer to inspect the database fields and sample posts.

## Requirement 1 - GET Blog Post Items
4. **Fetch All Blog Posts**
   - Modify the home "/" route to load all posts from `posts.db` using Flask-SQLAlchemy.
   - Display all posts on the home page.

5. **Fetch Individual Blog Post**
   - Create a route to fetch and display an individual post by its unique id.

## Requirement 2 - POST a New Blog Post
6. **Load Form to Create a Blog Post**
   - Create a POST route `/new-post` to render `make-post.html`.
   - Display a form with fields for title, subtitle, author, image URL, and content.
   - Use Flask CKEditor package for the content field.

7. **Save New Post to Database**
   - Save form data as a BlogPost object in `posts.db`.
   - Redirect to the home page after saving.
   - Automatically calculate and save the post date.

## Requirement 3 - Edit Existing Blog Posts
8. **Activate Edit Button**
   - Create a route `/edit-post/<post_id>` to edit an existing post.
   - Modify `make-post.html` to differentiate between new and edit post actions.
   - Fix the href for the edit button in `post.html` to pass the post's id.

9. **Auto-populate Form Fields for Editing**
   - Populate form fields with existing post data when editing.
   - Update the post in the database and redirect to the post page after submitting edits.
   - Maintain the original post date.

## Requirement 4 - DELETE Blog Posts
10. **Delete Blog Post**
    - Add a delete button (✘) next to each post on the home page.
    - Create a DELETE route `/delete/<post_id>` to remove the post from the database and redirect to the home page.

You can find the completed project solution in the lesson's resources.