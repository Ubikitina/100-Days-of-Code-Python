# Import the necessary libraries
import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"  # Define a background color for the GUI
current_card = {}  # Initialize a dictionary to store the current flashcard data


def remove_card_and_show_next():
    """
    Remove the current card from the data and show the next card.
    """
    data_list_of_dict.remove(current_card)  # Remove the current card from the list
    modified_data_df = pd.DataFrame(data_list_of_dict)  # Create a new DataFrame without the removed card
    modified_data_df.to_csv("data/words_to_learn.csv", index=False)  # Save the updated DataFrame to a CSV file
    next_card()  # Show the next flashcard

def next_card():
    """
    Display the next flashcard.
    """
    # Global variables that are accessed in this function
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)  # Cancel the previous flip timer (if any)
    card_canvas.itemconfig(canvas_image, image=card_front_image)  # Set up the front image of the card

    # Check if there are more flashcards to display
    if len(data_list_of_dict) > 0:
        current_card = random.choice(data_list_of_dict)  # Select a random flashcard
        card_canvas.itemconfig(title_text, text="French", fill="#000000")
        card_canvas.itemconfig(word_text, text=current_card["French"], fill="#000000")  # Display the French word
        flip_timer = window.after(3000, func=flip_card)  # Start a timer to flip the card after 3 seconds
    else:  # If there are no more flashcards to display, it is the end of the game
        card_canvas.itemconfig(title_text, text="No more cards available.", fill="#000000")
        card_canvas.itemconfig(word_text, text="Congrats!", fill="#000000")


def flip_card():
    """
    Flip the flashcard to reveal the English translation.
    """
    card_canvas.itemconfig(canvas_image, image=card_back_image)
    card_canvas.itemconfig(title_text, text="English", fill="#FFFFFF")
    card_canvas.itemconfig(word_text, text=current_card["English"], fill="#FFFFFF")


# ---------------------------- PREPARE DATA ------------------------------- #
raw_data_df = None  # Initialize a variable to hold the raw data DataFrame
try:  # Try to read data from a learning CSV file
    raw_data_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    raw_data_df = pd.read_csv("data/french_words.csv")   # If the learning CSV file doesn't exist, read from the original CSV file
finally:
    # Convert the DataFrame to a list of dictionaries
    data_list_of_dict = raw_data_df.to_dict(orient="records")  # Will look like [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},...]

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()  # Create the main application window
window.title("Flashy")  # Set the title of the window
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure window padding

flip_timer = window.after(3000, func=flip_card)  # Set an initial timer to flip the first card after 3 seconds

# Create a canvas widget for drawing graphics
card_canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)  # Create a canvas
card_front_image = tkinter.PhotoImage(file="images/card_front.png")  # Create an image on the canvas using the loaded image
card_back_image = tkinter.PhotoImage(file="images/card_back.png")  # Create an image on the canvas using the loaded image
canvas_image = card_canvas.create_image(400, 263, image=card_front_image)
title_text = card_canvas.create_text(400, 150, text="",  font=("Arial", 40, "italic"))  # Create a text element on the canvas
word_text = card_canvas.create_text(400, 263, text="",  font=("Arial", 60, "bold"))  # Create a text element on the canvas
card_canvas.grid(row=0, column=0, columnspan=2)  # Use the grid geometry manager to position the canvas in the window

# Create a "right" button
right_image = tkinter.PhotoImage(file="images/right.png")  # Load the "right" button image
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=remove_card_and_show_next)
right_button.grid(row=1, column=1)

# Create a "wrong" button
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()  # Show the first flashcard


window.mainloop()  # Start the main event loop of the tkinter application
