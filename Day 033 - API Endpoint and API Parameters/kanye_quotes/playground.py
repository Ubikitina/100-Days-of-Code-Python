from tkinter import *
import requests


def get_quote():
    # Send an HTTP GET request to the specified URL and store the response in 'response'
    response = requests.get(url="https://api.kanye.rest")
    # Check if the response has an HTTP status code indicating an error (4xx or 5xx status codes)
    response.raise_for_status()
    # Parse the response content as JSON and store it in the 'data' variable
    data = response.json()
    # Extract the 'quote' field from the JSON data and store it in the 'quote' variable
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()