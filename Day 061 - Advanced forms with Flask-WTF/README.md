# Day 61: Building Advanced Forms with Flask-WTF

## Goals
- **Objective:** Enhance form handling in a Flask application by using the Flask-WTF extension.
- **Focus:** Utilize Flask-WTF to simplify form creation, validation, and security.
- **Task Overview:** Create a secure website with a login page that only grants access to users with the correct credentials.

**Key Benefits of Flask-WTF**
1. **Easy Form Validation:** Automatically ensures correct data format (e.g., valid email structure) without custom validation code.
2. **Less Code:** Reduces the amount of repetitive code needed for multiple forms.
3. **Built-in CSRF Protection:** Prevents Cross-Site Request Forgery attacks, enhancing security.

## Demo
We have created a login web page where: 
- If you log in with non-administrator credentials, you get an access denied screen.
- If you log in with administrator credentials, it shows a secret. The admin credentials are: email `admin@email.com` and password `12345678`.

![](Demo.gif)

## Step-by-step
### Setup Instructions
1. **Download and Prepare:**
   - Download the starting .zip files and open the project in PyCharm.
   - Set up a virtual environment and install dependencies from `requirements.txt`.
2. **Install Flask-WTF:**
   - Use `pip install Flask-WTF` to add the library to the project.
   - Ensure all required packages are installed with `pip install -r requirements.txt`.

### Challenge: Create the Login Route
1. **Form Creation:**
   - Follow the Flask-WTF Quickstart guide to create a login form with email and password fields.
   - Use `StringField` for both fields and set the input size to 30.
   - Add CSRF protection by including `{‌{ form.csrf_token }}` in `login.html` and setting a secret key in `main.py`.
2. **Form Validation:**
   - Switch the password field to a `PasswordField` for obscured input.
   - Dynamically build URLs and better format the form layout using HTML elements.
   - Use `SubmitField` for the submit button.

### Adding Validation
1. **Validators:**
   - Add `DataRequired` validators to ensure both fields are filled.
   - Disable browser default validation using `novalidate` attribute on the form.
   - Implement email validation and password length validation using WTForms validators.

2. **Error Handling:**
   - Loop through validation errors and display them in the form.

### Handling Form Data
1. **Form Submission:**
   - Use `validate_on_submit()` to check form submission and validation.
   - Update `/login` route to validate credentials and redirect to `success.html` or `denied.html`.

### Template Inheritance with Jinja2
1. **Base Template:**
   - Create `base.html` with block areas for title and content.
   - Make `success.html` and `denied.html` inherit from `base.html` and customize their content.

2. **Super Blocks:**
   - Use `{‌{ super() }}` to extend styles in child templates.

### Improving Appearance with Bootstrap-Flask
1. **Install Bootstrap-Flask:**
   - Use `pip install bootstrap-flask` to add Bootstrap styling to the project.
   - Convert HTML files to use Bootstrap templates and load Bootstrap CSS in `base.html`.
2. **Form Rendering:**
   - Utilize `{‌{ render_form(form) }}` to generate form layout and styling automatically.
