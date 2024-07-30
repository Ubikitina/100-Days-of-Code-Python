# Day 60: Make the Contact Form Work

## Goal

Yesterday, we upgraded our blog website with Bootstrap styling. The remaining task is to make the contact form on the Contact Page functional. This involves learning how to handle HTML form submissions and processing the submitted data in a Flask server to send an email.

By following these steps, the contact form on the upgraded blog website will be fully functional, allowing user data submission and email notifications to the website owner.

## Steps to Achieve the Goal

### Learning forms and POST requests

This section includes the explanation of the [learning-forms-and-post-requests](./learning-forms-and-post-requests/) folder.

#### 1. Create an HTML Form from Scratch
- **Create a new PyCharm Project:** Name it `html-forms`. It should contain a `main.py` and an `index.html` in the templates folder.
- **Flask Application Setup:** Create a Flask application that serves the `index.html` page with an `<h1>` to verify it's working.
- **Challenge:** Create an HTML form in `index.html` to render a webpage form.

#### 2. Handle POST Requests with Flask
- **Update HTML Form:** Modify the form to send a "POST" request to the path `/login` using action and method attributes.
  - Resources:
    - [Form Method](https://www.w3schools.com/tags/att_form_method.asp)
    - [Form Action](https://www.w3schools.com/tags/att_form_action.asp)

- **Catch POST Request in Flask:** 
  - Assign `name` attributes to form inputs.
  - Create a decorator in `main.py` to handle POST requests and return a string.
  - Flask documentation for methods parameter: [HTTP Methods](https://flask.palletsprojects.com/en/2.3.x/quickstart/#http-methods)

#### 3. Use the Flask Request Object
- **Challenge:** Use Flask's `request` object to retrieve the form data and send it back to the client as an `<h1>`.
  - Documentation: [Flask Request Object](https://flask.palletsprojects.com/en/2.3.x/quickstart/#the-request-object)
  - Hint: [Stack Overflow](https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask)

- **Dynamic URL Generation:** Use `url_for` for dynamically generating URLs in the form's action attribute, making the server path adaptable.

### Applying Knowledge to the Blog Website
Now let's appply the knowedge to [blog-project-getting-the-contat-form-work](./blog-project-getting-the-contact-form-work/).

1. **Download Starting Code:** Obtain the code from this lesson's resources, which includes a simplified `contact.html`.
2. **Add "/form-entry" Route:** Update `main.py` to receive form data.
3. **Challenge:** Print user-entered information and return a `<h1>` with "Successfully sent your message".

4. **Combine Routes:** Merge `/contact` and `/form-entry` under the `/contact` route, handling GET and POST requests appropriately.
   - Use `request.method` to determine the request type.
   - Documentation: [HTTP Methods](https://flask.palletsprojects.com/en/2.3.x/quickstart/#http-methods)

5. **Update contact.html:** Instead of returning a new `<h1>`, update the existing `<h1>` in `contact.html` to display "Successfully sent message" using Jinja templates.
   - Hint: [Jinja Templates](https://jinja.palletsprojects.com/en/3.0.x/templates/#if)

6. **Sending Email with smtplib**
- **Email Setup:** Review lessons from Day 32 on using `smtplib` to send an email when a user submits the contact form.
- **Complete the Form:** Ensure the form sends an email to the website owner with the submitted data.

