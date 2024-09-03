# Day 55: HTML and URL Parsing in Flask & Higher Lower Game

## Overview

On Day 55 of learning Python, I explored HTML and URL parsing in Flask, which is essential for creating dynamic web applications. I also built a "Higher or Lower" game using Flask, further applying my knowledge of web development and decorators. The day involved understanding how Flask can handle routes with dynamic content and how to use decorators to enhance the functionality of functions.

**Summary:**

- **HTML and URL Parsing**: Learned how to serve HTML content using Flask and how to create dynamic URLs that change based on user input.
- **Python Decorators with `*args` and `**kwargs`**: Gained a deeper understanding of how decorators can be used to modify functions with varying arguments.
- **Higher or Lower Game**: Applied Flask knowledge to build an interactive game, reinforcing concepts of routing, dynamic content, and web development in Python.


## Files Created

### `args-and-kwargs-in-decorators.py`

This script focuses on the use of `*args` and `**kwargs` in Python decorators. It includes:

- **User Class**: A simple class to represent a user with a `name` attribute and a login status (`is_logged_in`).
- **Decorator Function**: `is_authenticated_decorator`, which checks if a user is logged in before allowing access to a function.
- **Example Function**:
  - `create_blog_post(user)`: This function simulates creating a blog post, but it only executes if the user is authenticated (logged in).
  
This script demonstrates how to use `*args` to pass a variable number of arguments to a decorator.

### `loggin-decorator-exercise.py`

This script demonstrates the use of decorators for logging function calls. It includes:

- **Logging Decorator**: `logging_decorator`, which prints the function name, its arguments, and its return value whenever the function is called.
- **Example Function**:
  - `a_function(a, b, c)`: A simple function that multiplies three numbers and returns the result.
  
The script is designed to help understand how decorators can be used to automatically log function calls, which is particularly useful for debugging and monitoring.

### `hello.py`

This script builds on the previous Flask examples, introducing HTML rendering and URL parsing. It includes:

- **Custom Decorators**: 
  - `make_bold`, `make_emphasis`, and `make_underlined`, which modify the text output of functions by wrapping them in HTML tags.
- **Routes**:
  - `/`: Displays a welcome message with some HTML elements, including an image.
  - `/bye`: Displays a stylized "Bye!" message using the custom decorators.
  - `/username/<name>/<int:number>`: Displays a personalized greeting based on the `name` and `number` provided in the URL.

The script showcases how to create dynamic routes that change their content based on user input from the URL.


### `higher-or-lower-game/server.py`

This script implements a simple "Higher or Lower" guessing game using Flask. It includes:

- **Random Number Generation**: A random number between 0 and 9 is generated at the start of the script.
- **Routes**:
  - `/`: Displays a welcome message and prompts the user to guess a number, accompanied by a GIF.
  - `/<int:number>`: Checks the user's guess against the random number and returns a response indicating whether the guess was too high, too low, or correct. Each response is styled with a different color and includes a relevant GIF.

The script demonstrates how to use Flask to create a simple, interactive web-based game.

## Flask Application Instructions

To run any of the Flask applications (`hello.py` or `server.py`):

1. **Set Environment Variable**:
   - On Windows: `set FLASK_APP=hello.py` or `set FLASK_APP=server.py`
   - On macOS/Linux: `export FLASK_APP=hello.py` or `export FLASK_APP=server.py`
   - On PowerShell: `$env:FLASK_APP="hello.py"` or `$env:FLASK_APP="server.py"`

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory containing the script.

3. **Run the Flask Application**:
   - Use the command: `flask --app hello run` or `flask --app server run`
   - Alternatively, run the script directly in an IDE like PyCharm by setting `__name__ == "__main__"` and using the run button.

4. **Access the Web App**:
   - Open a web browser and go to `http://127.0.0.1:5000/` to interact with the application.
   - For the Higher or Lower game, visit `http://127.0.0.1:5000/` to start guessing the number.
