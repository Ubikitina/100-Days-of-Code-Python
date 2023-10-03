import tkinter
from tkinter import messagebox
import random
import pyperclip

WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, string=password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            # Save the passwords in a file
            with open("data.txt", "a") as file:  # the mode "a" opens the file in append mode
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, tkinter.END)  # Delete text from index 0 (start) to the end
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()  # Create the main application window
window.title("Password Manager")  # Set the title of the window
window.config(padx=50, pady=50, bg=WHITE)  # Configure window padding

# Create a canvas widget for drawing graphics
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)  # Create a canvas
logo_img = tkinter.PhotoImage(file="logo.png")  # Create an image on the canvas using the loaded image
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)  # Use the grid geometry manager to position the canvas in the window

# Create the website label
website_label = tkinter.Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0, pady=5)  # Use the grid geometry manager

# Create the username label
username_label = tkinter.Label(text="Email/Username:", bg=WHITE)
username_label.grid(row=2, column=0, pady=5)  # Use the grid geometry manager

# Create the password label
password_label = tkinter.Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0, pady=5)  # Use the grid geometry manager

# Create the generate password button
gen_pwd_button = tkinter.Button(text="Generate Password", command=generate_password, highlightthickness=0)
gen_pwd_button.grid(row=3, column=2)  # Use the grid geometry manager

# Create the add button
add_button = tkinter.Button(text="Add", command=save, highlightthickness=0, width=45)
add_button.grid(row=4, column=1, columnspan=2, pady=5)  # Use the grid geometry manager

# Create an entry component
website_entry = tkinter.Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Create an entry component
username_entry = tkinter.Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(tkinter.END, "maialen@email.com")

# Create an entry component
password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3, column=1)

window.mainloop()