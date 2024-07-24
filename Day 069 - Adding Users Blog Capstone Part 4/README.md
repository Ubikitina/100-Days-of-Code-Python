# Day 69 - Adding Users to Our Blog Project
This project aims to add user authentication to a blog, allowing users to sign up, log in, and comment on blog posts. Once completed, this project will be a fully functional blog website ready for publication and launch.



## Features

1. User Registration
2. User Login and Logout
3. User Authentication and Authorization
4. Admin-only access to certain routes

## Demo

### User Registration

![](./img/User%20Registration.gif)


### User Login and Logout

![](./img/Login%20and%20Logout.gif)



### Admin Privileges
The first registered user has admin privileges. Additional buttons (Create New Post, Edit Post, Delete) are visible only to the admin.

![](./img/Admin%20Priviledges.gif)


### Adding Comments to Blog Posts
![](./img/Comment.gif)



## Requirements

### Requirement 1 - Register New Users

Users should be able to register for the blog website via the `/register` route.

1. **Create a WTForm**: Create a `RegisterForm` in `forms.py`.

2. **Create a User Table**: Add a `User` table to your `blog.db` to store user data.

3. **User Registration**:
   - Use the data from the registration form to create a new user entry in the `User` table.
   - Hash and salt the user's password using `Werkzeug`.

4. **Render the Registration Form**: Use `Bootstrap-Flask`'s `render_form()` macro to display the form on `register.html`.

### Requirement 2 - Login Registered Users

Registered users should be able to log in via the `/login` route.

1. **Login Functionality**:
   - Users should be able to log in using their credentials.
   - Refer to `Flask-Login` documentation for implementation details.

2. **Auto-login After Registration**: Add code in the `/register` route to log in users automatically after successful registration and redirect them to the home page.

3. **Handle Existing Email**: If a user tries to register with an email that already exists, redirect them to the `/login` route with a flash message prompting them to log in instead.

4. **Login Error Handling**: If the user's email does not exist or the password is incorrect, redirect them back to the `/login` route with a flash message indicating the issue.

5. **Update Navbar**: Modify the navbar to display appropriate links based on whether the user is logged in or not.
   - If logged in, show:
     ```
     <li><a href="/logout">LOG OUT</a></li>
     <li><a href="#">My Dashboard</a></li>
     ```
   - If not logged in, show:
     ```
     <li><a href="/login">LOG IN</a></li>
     <li><a href="/register">REGISTER</a></li>
     ```

6. **Logout Route**: Implement the `/logout` route to log users out and redirect them to the home page.

### Requirement 3 - Protect Routes

The first registered user will be the admin and will have additional privileges.

1. **Admin User Identification**: The first user's id will be 1. Use this to control the visibility of "Create New Post," "Edit Post," and "Delete" buttons in `index.html` and `post.html`.

2. **Route Protection**:
   - Users can still manually access restricted routes like `/edit-post`, `/new-post`, or `/delete` even if buttons are hidden.
   - Write a custom Python decorator `@admin_only` to protect these routes.
   - If `current_user`'s id is 1, allow access; otherwise, return a 403 error (not authorized).

### Requirement 4 - Allow Any User to Add Comments to BlogPosts

Allow users to leave comments on blog posts.

1. **Create a CommentForm**: Create a `CommentForm` in `forms.py` with a single `CKEditorField` for users to write their comments.

2. **Create a Comment Table**: Add a `Comment` table to `blog.db` with `id` and `text` properties. The `id` is the primary key, and `text` holds the comment content.

3. **User-Comment Relationship**: Establish a One-to-Many relationship between the `User` table (Parent) and the `Comment` table (Child). One User can have many Comment objects.

4. **BlogPost-Comment Relationship**: Establish a One-to-Many relationship between the `BlogPost` table (Parent) and the `Comment` table (Child). Each BlogPost can have many associated Comment objects.

5. **Re-create Database**:
   - After updating the database schema, delete the existing `blog.db`.
   - Restart the Flask server and re-register your first user as the admin.
   - Create a new blog post and another user (a blog reader) who will comment on the posts.

6. **Authenticated Comments Only**:
   - Update the `/post/<int:post_id>` route to allow only logged-in users to comment.
   - Display a flash message and redirect unauthenticated users to the `/login` route if they attempt to comment.

7. **Display Comments**:
   - Update `post.html` to display all comments associated with the blog post.
   - Use `flask-gravatar` to add Gravatar images to the comments section.



## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/blog-capstone-project.git
   cd blog-capstone-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Ensure `blog.db` is in the project directory.
   - Run any necessary migrations or initial setup scripts.

5. Run the application:
   ```
   flask run
   ```

6. Access the application:
   - Open your web browser and go to `http://127.0.0.1:5000`.

