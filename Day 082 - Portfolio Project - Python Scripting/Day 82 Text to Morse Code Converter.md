# Goal
Create a text-based (command line) program that takes any String input and converts it into Morse Code. Morse Code is a method used in telecommunication to encode text characters as sequences of two different signal durations, called dots and dashes.



# Specifications
- Input: The program should accept a user-provided string as input.
- Output: The program should output the Morse Code equivalent of the input string.
- Morse Code Mapping: Define a mapping between each alphabet (A-Z) and each digit (0-9) to its Morse Code representation. I will use the International Morse Code standard for reference.
- Case Insensitivity: The program should be case-insensitive, meaning it should treat uppercase and lowercase letters the same way.
- Programming Language: Python




# Reflection Time
To develop this program, the first step I took was to gather information from Wikipedia about Morse Code. Using this information, I constructed a Python dictionary where the keys represent letters and digits, and the values represent their corresponding Morse Code.

Next, I created a method that converts letters into Morse Code and implemented a simple input/output mechanism. Initially, the program accepted a single letter as input, returning the Morse Code equivalent. Eventually, I extended the program to handle entire phrases, converting them into Morse Code.

Regarding the challenges encountered, I want to highlight the handling of invalid characters—those that are neither alphabetical characters, digits, nor spaces. Since I couldn't find their Morse Code equivalents, my program responds to such characters by printing an error message indicating that they are not accepted characters.

## Today's learnings
I learned about Morse Code and gained experience in constructing a Python dictionary for mapping characters to Morse Code representations. Additionally, I encountered challenges related to handling invalid characters and implemented error handling for such cases.


## Potential improvements for the future
If I was to tackle this project again, I might consider the following improvements:
- Input Validation: Strengthen input validation to handle edge cases more robustly, ensuring a smoother user experience.
- Testing: Implement more comprehensive testing with various inputs to identify and address potential issues. It is highly advisable to include testing code as part of my programming project.
