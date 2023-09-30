import turtle
import pandas
BACKGROUND_IMAGE = "blank_states_img.gif"

# Create a screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set the screen dimensions (optional)
screen.setup(width=725, height=491)

# Set the background image (replace 'background.gif' with your image file)
screen.bgpic(BACKGROUND_IMAGE)

# Hide the default turtle cursor
turtle.hideturtle()
turtle.penup()

# Create the data frame out of the csv file
states_data_frame = pandas.read_csv("50_states.csv")
# Create a list of the states. This list will be used to track the ones already answered.
list_of_states = states_data_frame["state"].to_list()
# Create the scoring
number_of_states_guessed = 0

# Loop that will keep asking the state until the users guesses all of them
while number_of_states_guessed < 50:
    # Ask the user a state and convert the answer into titlecase
    answer_state = screen.textinput(title=f"{number_of_states_guessed}/50 States Correct", prompt="What's another state's name?").title()

    # Exit the game if the user types exit
    if answer_state == "Exit":
        # Save the missing states to a .csv
        with open("missing_states.csv", mode='w') as file:
            for item in list_of_states:
                file.write(f"{item}\n")
        break

    # Check if the answer is contained in the list
    if answer_state in list_of_states:
        number_of_states_guessed += 1  # Increase the score
        list_of_states.remove(answer_state)  ## Remove the guessed state from the list of remaining ones

        # Write correct guesses onto the map
        x_cor = int(states_data_frame[states_data_frame.state == answer_state].x.iloc[0])
        y_cor = int(states_data_frame[states_data_frame.state == answer_state].y.iloc[0])
        turtle.goto(x_cor, y_cor)
        turtle.write(answer_state, align="center", font=("Courier", 9, "normal"))



# # Start the main loop to keep the screen open
# turtle.mainloop()

