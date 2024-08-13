# Day 24: File Directories and Paths in Python

## Overview

On Day 24, I focused on learning about file directories, file paths, and file handling in Python. This included practical exercises that involved reading from and writing to files, manipulating paths, and creating a high-score system for a Snake Game. Additionally, I worked on a Mail Merge project that involved generating personalized letters based on a template.

## Concepts Practiced

- **File Handling**: Reading from and writing to text files, handling file paths.
- **Persistence**: Saving and retrieving data (like high scores) to maintain state across game sessions.
- **String Manipulation**: Replacing placeholders in a template with actual values (e.g., names).
- **Directory Management**: Organizing files into appropriate directories for input, output, and processing.

## Project Files

### Add High Score to Snake Game

This project expands on a classic Snake Game by adding a high score feature that is stored and retrieved from a file.

#### Directory Structure
```
/Add_High_Score_to_Snake_Game/
│
├── data.txt
├── food.py
├── main.py
├── scoreboard.py
└── snake.py
```

#### `data.txt`
- **Description**: This file stores the highest score achieved in the Snake Game. The score is read when the game starts and updated if a new high score is achieved.

#### `food.py`
- **Description**: This file contains the `Food` class, which handles the creation and positioning of the food for the snake.
- **Key Features**:
  - **Random Placement**: The food appears at random coordinates within the game screen.

#### `main.py`
- **Description**: This is the main script that initializes the game, sets up the screen, and handles the game loop.
- **Key Features**:
  - **Collision Detection**: The script detects when the snake collides with food, walls, or itself, and updates the game state accordingly.
  - **High Score Management**: The high score is updated and saved to `data.txt` when the game ends.

#### `scoreboard.py`
- **Description**: This file contains the `Scoreboard` class, which displays the current score and high score.
- **Key Features**:
  - **Score Display**: The current score and high score are displayed at the top of the screen.
  - **High Score Persistence**: The high score is read from and written to `data.txt`.

#### `snake.py`
- **Description**: This file defines the `Snake` class, which manages the behavior of the snake, including movement and growth.
- **Key Features**:
  - **Movement Control**: The snake's direction is controlled by the player using the arrow keys.
  - **Collision Handling**: The script handles what happens when the snake collides with itself or the walls.

### Mail Merge Project

This project involves automating the creation of personalized letters using a template and a list of names.

#### Directory Structure
```
/Mail_Merge_Project/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Aang.txt
│       ├── letter_for_Appa.txt
│       ├── letter_for_Katara.txt
│       ├── letter_for_Momo.txt
│       ├── letter_for_Sokka.txt
│       ├── letter_for_Toph.txt
│       ├── letter_for_Uncle Iroh.txt
│       └── Zuko.txt
└── main.py
```

#### `starting_letter.txt`
- **Description**: This is the template letter used for the mail merge. It includes a placeholder `[name]` that will be replaced with actual names from `invited_names.txt`.

#### `invited_names.txt`
- **Description**: This file contains a list of names that will be used to personalize the letters.

#### `Output/ReadyToSend/`
- **Description**: This directory contains the final, personalized letters ready to be sent. Each letter is named after the recipient.

#### `main.py`
- **Description**: This script automates the mail merge process by reading the template and names, replacing the placeholder with actual names, and saving the personalized letters to the output directory.

### File Handling Examples

This section contains simple examples of reading from and writing to files in Python.

#### Files
- **`main.py`**: Demonstrates basic file operations including reading, writing, and appending text to files.
- **`my_file.txt`**: A sample text file used in the examples to demonstrate file reading and writing operations.

#### Key Concepts
- **File Reading**: Using `open()` and `with open()` to read file contents.
- **File Writing**: Writing new content to a file using different modes (`w` for write, `a` for append).
- **File Paths**: Understanding relative and absolute paths in Python.



## How to Run the Projects

### Snake Game with High Score
1. **Navigate to the project directory**:
    ```bash
    cd Add_High_Score_to_Snake_Game
    ```
2. **Run the game**:
    ```bash
    python main.py
    ```
3. **Gameplay**:
    - Control the snake using the arrow keys.
    - Try to achieve a high score, which will be saved automatically.

### Mail Merge
1. **Navigate to the project directory**:
    ```bash
    cd Mail_Merge_Project
    ```
2. **Run the mail merge script**:
    ```bash
    python main.py
    ```
3. **Output**:
    - Personalized letters will be generated and saved in the `Output/ReadyToSend/` directory.

