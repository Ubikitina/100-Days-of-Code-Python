# Day 8: Function Parameters and Caesar Cipher Project

Welcome to Day 8 of your Python learning journey! In this session, I focused on understanding function parameters and applied the knowledge to create a Caesar Cipher. Below is an overview of the files, along with brief descriptions of each.

## Files in This Folder

### `01-paint-area-calculator.py`

This script calculates the number of paint cans required to cover a wall, based on its height, width, and the coverage area of the paint.

- **Key Concepts**:
  - Function definition and parameters.
  - Using the `math.ceil()` function to round up to the nearest whole number.

- **How it Works**:
  - The function `paint_calc()` takes the height, width, and coverage area as inputs.
  - It calculates the total number of paint cans needed and prints the result.

- **Example Usage**:
  - The user is prompted to input the height and width of the wall.
  - The script outputs the number of paint cans required to cover the area.

### `02-prime-number-checker.py`

This script checks whether a given number is a prime number.

- **Key Concepts**:
  - Loops and conditional statements.
  - Basic understanding of prime numbers.

- **How it Works**:
  - The function `prime_checker()` takes a number as input and checks if it is divisible by any number other than 1 and itself.
  - It then prints whether the number is prime or not.

- **Example Usage**:
  - The user is prompted to input a number.
  - The script checks and outputs whether the number is a prime number.

### `03-caesar-cipher.py`

This script implements a Caesar Cipher, a basic encryption technique where each letter in a text is shifted by a certain number of positions in the alphabet.

- **Key Concepts**:
  - String manipulation.
  - Loops and conditionals.
  - Function parameters and return values.

- **How it Works**:
  - The script defines a function `caesar()` that takes a `text`, `shift`, and `cipher_direction` as inputs.
  - Depending on the direction ('encode' or 'decode'), it shifts the letters in the text and prints the encrypted or decrypted message.
  - The script handles cases where the shift exceeds the length of the alphabet and allows the user to continue encoding or decoding multiple messages.

- **Example Usage**:
  - The user is prompted to input a message and a shift number, and to select whether to encode or decode the message.
  - The script then outputs the encoded or decoded message and asks if the user wants to continue.

- `art.py` file: This file contains ASCII art used in the `03-caesar-cipher.py` script. The art in this file is imported and displayed in the Caesar Cipher project to enhance the user experience.

## How to Run the Scripts

1. **Ensure you have Python installed** on your system.
2. **Navigate to the folder** containing these files in your terminal or command prompt.
3. Run each script by typing `python <script_name>.py` (e.g., `python 01-paint-area-calculator.py`).
4. Follow the on-screen instructions for each script.

