# Day 54: Introduction to Web Development with Flask and Python Decorators

## Overview

On Day 54 of learning Python, I was introduced to web development with Flask, a popular web framework in Python. Additionally, I deepened my understanding of Python decorators, a powerful feature that allows you to modify the behavior of functions or methods. This day involved working with Flask to create simple web applications and exploring the concept and usage of decorators in Python.

## Files Created

### `python-decorators.py`

This script provides a comprehensive introduction to Python decorators, covering the following concepts:

- **Basic Functions**: Examples of functions with inputs, functionality, and outputs.
- **First-Class Functions**: Demonstrates how functions in Python can be passed as arguments to other functions.
- **Nested Functions**: Illustrates how functions can be defined inside other functions.
- **Returning Functions**: Shows how a function can return another function.
- **Python Decorators**: 
  - Introduction to decorators with a simple example.
  - Practical usage of decorators to add delays before executing functions.

The script explains the concept of decorators and demonstrates their use with clear, step-by-step examples.

### `decorator-exercise.py`

This script demonstrates the practical use of Python decorators to measure the execution time of functions. It includes:

- **Decorator Function**: `speed_calc_decorator` which calculates and prints the time taken by a function to execute.
- **Example Functions**:
  - `fast_function()`: A function with a relatively fast execution time.
  - `slow_function()`: A function with a slower execution time.
  
The script applies the `speed_calc_decorator` to both functions and prints out how long each function takes to run.

### `hello.py`

This script introduces basic web development using the Flask framework. It includes:

- **Flask Setup**: Creation of a basic Flask application.
- **Routes**:
  - `/`: Displays a "Hello, World!" message.
  - `/bye`: Displays a "Bye!" message.
- **Running the App**: Instructions on how to run the Flask app either from the terminal or using PyCharm.

This script serves as a starting point for building more complex web applications with Flask.


## Flask Application Instructions

To run the Flask application in `hello.py`:

1. **Set Environment Variable**:
   - On Windows: `set FLASK_APP=hello.py`
   - On macOS/Linux: `export FLASK_APP=hello.py`
   - On PowerShell: `$env:FLASK_APP="hello.py"`

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory containing `hello.py`.

3. **Run the Flask Application**:
   - Use the command: `flask --app hello run`
   - Alternatively, you can run the script directly in an IDE like PyCharm by setting `__name__ == "__main__"` and using the run button.

4. **Access the Web App**:
   - Open a web browser and go to `http://127.0.0.1:5000/` to see the "Hello, World!" message.
   - Navigate to `http://127.0.0.1:5000/bye` to see the "Bye!" message.

