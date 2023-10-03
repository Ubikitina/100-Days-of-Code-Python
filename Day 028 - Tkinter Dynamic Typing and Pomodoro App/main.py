import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Reset the timer to its initial state.

    This function resets the global 'reps' variable to 0, cancels the timer using the 'after_cancel' method of the window,
    and updates the timer_label, checkmark_label, and canvas item (timer_text) to their initial states.

    This is typically used to reset the timer when starting a new cycle or session.
    """
    global reps
    window.after_cancel(timer)  # Cancel the current timer to stop it from running
    reps = 0  # Reset the 'reps' count to 0
    timer_label.config(text="Timer", fg=GREEN)  # Reset the timer_label text to "Timer" and set its text color to GREEN
    checkmark_label.config(text="")   # Clear the checkmark_label text
    canvas.itemconfig(timer_text, text="00:00")  # Update the canvas item (timer_text) to display "00:00" as the timer value



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Start the timer for a Pomodoro session.

    This function manages the Pomodoro timer based on the 'reps' variable, which represents the current session or break.
    - If reps is odd (e.g., 1, 3, 5), it sets the timer for a work session.
    - If reps is a multiple of 8 (e.g., 8, 16, 24), it sets the timer for a long break.
    - Otherwise (reps is even and not a multiple of 8), it sets the timer for a short break.

    The function updates the timer_label to indicate the current session type and its color (GREEN for work, RED for a long break, PINK for a short break).

    Parameters:
    None

    Returns:
    None
    """
    global reps
    reps += 1  # Increment the 'reps' count

    # Determine the session type based on 'reps' and set the timer accordingly
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Start a countdown timer and update the display.

    This function initiates a countdown timer for the specified duration in seconds and updates the timer display
    on the canvas. It also manages the timer callback using the 'after' method of the window.

    Parameters:
    count (int): The duration of the countdown timer in seconds.

    Returns:
    None
    """
    minutes = int(count // 60)  # Calculate the number of minutes
    seconds = int(count % 60)   # Calculate the remaining seconds
    # Update the timer display on the canvas with the current time in the format "mm:ss"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
        global timer
        # Schedule a callback to update the countdown timer after 1000 milliseconds (1 second)
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer() # When the countdown reaches 0, start the timer for the next session (work or break)

        # If the reps count is even, add a checkmark (✓) to the checkmark_label
        if reps % 2 == 0:
            checkmark_label.config(text=checkmark_label.cget("text") + "✓")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()  # Create the main application window
window.title("Pomodoro")  # Set the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Configure window padding and background color

# Create a canvas widget for drawing graphics
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Load an image
tomato_img = tkinter.PhotoImage(file="tomato.png")  # Create an image on the canvas using the loaded image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Create a text element on the canvas
canvas.grid(row=1, column=1)  # Use the grid geometry manager to position the canvas in the window

# Create the timer label
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)  # Use the grid geometry manager

# Create the checkmark label
checkmark_label = tkinter.Label(font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=2, column=1)  # Use the grid geometry manager

# Create the start button
start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)  # Use the grid geometry manager

# Create the reset button
reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)  # Use the grid geometry manager

window.mainloop()