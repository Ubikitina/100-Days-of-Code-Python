import random
import tkinter

# Constants
ORANGE = "#F77F00"
BLUE = "#003049"
RED = "#66101F"
YELLOW = "#EAE2B7"
FONT_NAME = "Tahoma"


def start_game():
    global time_counter

    # Remove the labels to clear the screen
    welcome_label.grid_remove()
    explanation_label.grid_remove()
    start_button.grid_remove()

    # Start the coundown
    count_down(time_counter)

    # Show the new screen with the game
    time_label.grid(row=3, column=0)
    score_label.grid(row=3, column=1)
    instruction_label.grid(row=4, column=0, columnspan=2)
    word_label.grid(row=5, column=0, columnspan=2)
    entry.grid(row=6, column=0, columnspan=2)


def count_down(time_counter):
    global score
    # Update the timer display on the canvas with the current time
    time_label.config(text=f"Countdown: {time_counter} s")

    if time_counter > 0:
        global timer
        # Schedule a callback to update the countdown timer after 1000 milliseconds (1 second)
        timer = window.after(1000, count_down, time_counter - 1)  # This will update the timer
    else:
        # Once the time is expired, remove the current elements
        time_label.grid_remove()
        score_label.grid_remove()
        instruction_label.grid_remove()
        word_label.grid_remove()
        entry.grid_remove()

        # Show the end of game screen
        end_label.config(text=f"End of game. Your score is: {score}")
        end_label.grid(row=7, column=0, columnspan=2)

def check_typing(event):
    global score

    # Check if the typed word and the expected word are the same
    typed_word = entry.get().strip().lower()
    expected_word = word_label['text']
    if typed_word == expected_word: # If they match, increment the score
        score += 1 # Increment the score
        score_label.config(text=f"Score: {score}") # Update the score label

    # Update word and clear the text
    word_label.config(text=random.choice(word_list))
    entry.delete(0, tkinter.END)  # Clear the entered text

word_list = ["abject", "absent", "adamant", "adhesive", "adjoining", "air", "allow", "anger", "anxious", "approval", "army", "arrange", "attend", "auspicious", "awake", "bait", "balance", "bashful", "birthday", "blade", "blind", "books", "border", "borrow", "bounce", "boundary", "building", "busy", "cable", "cactus", "camera", "can", "care", "cent", "changeable", "chickens", "chunky", "classy", "closed", "club", "coil", "colour", "comfortable", "confused", "connection", "cook", "cows", "crate", "cushion", "damage", "damaged", "deafening", "dear", "decorous", "deeply", "delightful", "design", "detect", "direction", "dirty", "disagreeable", "dispensable", "disturbed", "dolls", "door", "drag", "dress", "early", "elastic", "elated", "elite", "employ", "encouraging", "end", "endurable", "engine", "enormous", "equal", "excite", "excuse", "existence", "experience", "fall", "fang", "fear", "fierce", "fire", "fish", "fixed", "flag", "flaky", "flower", "fluttering", "fold", "follow", "food", "forgetful", "form", "fowl", "fragile", "freezing", "fresh", "friends", "fumbling", "functional", "future", "giddy", "good", "goofy", "government", "governor", "grandiose", "greasy", "guard", "guttural", "heap", "heartbreaking", "helpless", "history", "hole", "homely", "hospital", "hurried", "hydrant", "hysterical", "ignore", "ill", "illegal", "include", "income", "inconclusive", "inexpensive", "ink", "interrupt", "kick", "kind", "kneel", "laborer", "lackadaisical", "lacking", "laughable", "launch", "lean", "learn", "license", "light", "loss", "luxuriant", "meeting", "men", "mend", "middle", "military", "miniature", "mixed", "mom", "muddled", "multiply", "murky", "nappy", "nervous", "nest", "nice", "night", "nippy", "nonstop", "note", "number", "nutritious", "obedient", "obscene", "occur", "office", "outrageous", "painstaking", "park", "part", "pass", "pear", "peep", "pinch", "pleasure", "plot", "poison", "polite", "possessive", "prefer", "price", "pricey", "probable", "punch", "quizzical", "rail", "railway", "rate", "recondite", "record", "refuse", "religion", "replace", "representative", "request", "rescue", "right", "road", "rod", "room", "root", "rule", "saw", "scandalous", "scattered", "scorch", "scrawny", "scream", "selective", "servant", "settle", "shallow", "shave", "shock", "simplistic", "ski", "slim", "snake", "snotty", "society", "sock", "sofa", "special", "spell", "spooky", "spring", "squeal", "squealing", "squirrel", "start", "stay", "steam", "steel", "sticks", "stingy", "stocking", "stranger", "strong", "succeed", "suggest", "summer", "supply", "suspect", "swanky", "sweet", "teaching", "team", "ten", "tense", "tenuous", "test", "thankful", "thoughtless", "throne", "tick", "tip", "tire", "trains", "treatment", "tremble", "tremendous", "trot", "try", "twist", "ultra", "unnatural", "unpack", "untidy", "upbeat", "uptight", "useful", "various", "vengeful", "voiceless", "volleyball", "wail", "wait", "wander", "wash", "watch", "waves", "whistle", "wipe", "wobble", "womanly", "wonderful", "workable", "worm", "wrong", "yam", "yawn", "yoke", "youthful"]

score = 0
time_counter = 60
timer = None

# Create the main window
window = tkinter.Tk()
window.title("Typing Speed Test")
# window.geometry("700x250")
window.config(padx=50, pady=50, bg=BLUE)  # Configure window background color

# -----------------------------------------------------------------------------------------------------
# Start screen elements
# -----------------------------------------------------------------------------------------------------
# Add a label to explain the game
welcome_label = tkinter.Label(window, text="Welcome to the Typing Speed Test!", font=(FONT_NAME, 14), fg=YELLOW, bg=BLUE)
welcome_label.grid(row=0, column=0, columnspan=2)

explanation_label = tkinter.Label(window,
                                  text="In this game we give you one minute to write the words that appear on the screen. \n"\
                                       "When the time is up, we will show you the number of words you have been able to write correctly. \n"\
                                       "Are you ready? Press Start to begin",
                                  font=(FONT_NAME, 10),
                                  fg=YELLOW,
                                  bg=BLUE)
explanation_label.grid(row=1, column=0, columnspan=2)

# Create the start button
start_button = tkinter.Button(text="Start", command=start_game, highlightthickness=0)
start_button.grid(row=2, column=0, columnspan=2)  # Use the grid geometry manager

# -----------------------------------------------------------------------------------------------------
# Game screen elements
# -----------------------------------------------------------------------------------------------------
# Create a Label for the time counter
time_label = tkinter.Label(window, text=f"Countdown: {time_counter} s", font=(FONT_NAME, 14), fg=YELLOW, bg=BLUE)

# Create a Label for the score
score_label = tkinter.Label(window, text=f"Score: {score}", font=(FONT_NAME, 14), fg=YELLOW, bg=BLUE)

# Add a label to explain the game
instruction_label = tkinter.Label(window, text="Type the word and press enter:", font=(FONT_NAME, 10), fg=YELLOW, bg=BLUE)

# Add a random word to the window
word_label = tkinter.Label(window, text=random.choice(word_list), font=(FONT_NAME, 14), fg=ORANGE, bg=BLUE)

# Add an entry
entry = tkinter.Entry(window, font=(FONT_NAME, 14))
entry.bind("<Return>", check_typing)

# -----------------------------------------------------------------------------------------------------
# Final screen elements
# -----------------------------------------------------------------------------------------------------
end_label = tkinter.Label(window, text=f"End of game. Your score is: {score}", font=(FONT_NAME, 14), fg=ORANGE, bg=BLUE)




# Start the Tkinter event loop
window.mainloop()
