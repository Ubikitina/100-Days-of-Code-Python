# Day 9: Dictionaries, Nesting, and Secret Auction Project

Welcome to Day 9 of your Python learning journey! On this day, I focused on mastering dictionaries, nesting, and creating a fun Secret Auction project. Below is an overview of the files I created, along with explanations of what each script does.

## Files in This Folder

### `01-grading-program.py`

This script assigns grades to students based on their scores using dictionaries.

- **Key Concepts**:
  - Dictionaries and key-value pairs.
  - Conditional statements for assigning grades.

- **How it Works**:
  - The script starts with a dictionary `student_scores` containing the names of students and their respective scores.
  - An empty dictionary `student_grades` is created to store the grades.
  - A loop iterates over the `student_scores` dictionary, and based on the score, assigns a grade (e.g., "Outstanding", "Exceeds Expectations") to each student.
  - The final dictionary `student_grades` is printed, showing each student’s grade.

- **Example Usage**:
  - The script processes predefined student scores and outputs their corresponding grades.

### `02-dictionary-in-list.py`

This script demonstrates how to nest dictionaries within a list and how to add new items to the nested structure.

- **Key Concepts**:
  - Nesting dictionaries inside a list.
  - Defining and using functions to modify nested data structures.

- **How it Works**:
  - The `travel_log` is a list containing dictionaries, each representing a country with the number of visits and cities visited.
  - The function `add_new_country()` allows the user to add a new country to the `travel_log`.
  - When the function is called with the country name, number of visits, and a list of cities, a new dictionary is created and added to `travel_log`.

- **Example Usage**:
  - The script adds "Russia" to the `travel_log` and then prints the updated list.

### `bid_auction.py`

This is the main script for the Secret Auction project, where participants can place bids, and the highest bidder wins.

- **Key Concepts**:
  - Dictionaries for storing and retrieving data.
  - Loops and user input handling.
  - Clearing the console screen for better user experience.

- **How it Works**:
  - The script starts by displaying a logo (imported from `art.py`) and a welcome message.
  - A loop runs to collect bids from multiple users. Each user's name and bid amount are stored in a dictionary.
  - The screen is cleared after each bid to keep the auction secret.
  - Once there are no more bidders, the script determines the highest bid and prints the winner's name and bid amount.

- **Example Usage**:
  - Users input their names and bids one by one. After all bids are collected, the script announces the winner.

- `art.py`: This file contains ASCII art used in the `bid_auction.py` script. The art in this file is imported and displayed at the start of the Secret Auction project.

- `flowchart.png`: This image is a flowchart used to develop the `bid_auction.py` script. Visual representation of the logic and flow of the auction program. Refer to this flowchart to understand the logical flow and decision-making process in the `bid_auction.py` script.


## How to Run the Scripts

1. **Ensure you have Python installed** on your system.
2. **Navigate to the folder** containing these files in your terminal or command prompt.
3. Run each script by typing `python <script_name>.py` (e.g., `python bid_auction.py`).
4. Follow the on-screen instructions for each project.

