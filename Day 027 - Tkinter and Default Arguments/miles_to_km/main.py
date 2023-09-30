from tkinter import *


def button_clicked():
    """
        Callback function for the Calculate button.
        Converts the input miles to kilometers and updates the result label.
    """
    number_in_miles = float(input.get())
    result = round(number_in_miles * 1.60934)  # To simplify the program, we round to the nearest whole number
    result_label.config(text=str(result))

# Create the main tkinter window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=20)

# Equal to label
equal_to_label = Label(text="is equal to", font=("Arial", 14, "bold"))
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=5, pady=5)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

# Km label
km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

# Result label
result = 0
result_label = Label(text=str(result), font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=5, pady=5)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)



# Start the main event loop, which allows the window to respond to user interactions.
window.mainloop()  # This line of code always has to be at the very end of the program
