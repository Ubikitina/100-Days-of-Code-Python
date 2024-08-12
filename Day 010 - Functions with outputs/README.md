# Day 10: Functions with Outputs

Welcome to Day 10 of your Python learning journey! On this day, I explored functions with outputs and applied my knowledge to create practical programs like a days-in-month calculator and a basic calculator. Below is an overview of the files I created, along with explanations of what each script does.

## Files in This Folder

### `01-days-in-month.py`

This script calculates the number of days in a given month of a specified year, taking into account whether the year is a leap year.

- **Key Concepts**:
  - Functions with return values.
  - Leap year calculations.

- **How it Works**:
  - The script defines a function `is_leap(year)` that checks if a given year is a leap year.
  - Another function `days_in_month(year, month)` uses `is_leap(year)` to determine the number of days in a given month.
  - The user is prompted to input a year and a month, and the script outputs the number of days in that month for the specified year.

- **Example Usage**:
  - The user inputs a year (e.g., 2020) and a month (e.g., 2 for February), and the script outputs "29" (since 2020 is a leap year).

### `02-calculator.py`

This script implements a basic calculator that can perform addition, subtraction, multiplication, and division operations. 

- **Key Concepts**:
  - Functions with outputs.
  - Dictionaries to map operations to functions.
  - Recursion for restarting the calculator.

- **How it Works**:
  - The script imports a logo from `art.py` and uses it to display a title for the calculator.
  - Functions are defined for each arithmetic operation: `add`, `subtract`, `multiply`, and `divide`.
  - The `calculator()` function handles the main logic, including getting user input, performing calculations based on the selected operation, and allowing the user to continue with the previous result or start a new calculation.
  - If the user chooses to continue, the result of the last calculation is used as the first number for the next operation.

- **Example Usage**:
  - The user inputs a first number, selects an operation (e.g., "+"), inputs a second number, and the script outputs the result.
  - The user can choose to continue with the previous result or start a new calculation.


## How to Run the Scripts

1. **Ensure you have Python installed** on your system.
2. **Navigate to the folder** containing these files in your terminal or command prompt.
3. Run each script by typing `python <script_name>.py` (e.g., `python 02-calculator.py`).
4. Follow the on-screen instructions for each script.
