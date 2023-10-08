import smtplib
import datetime as dt
import random

my_email ="maigt3st@gmail.com"
password = "ADD_HERE_THE_PASSWORD"

# Get the current date and time
now = dt.datetime.now()
day_of_the_week = now.weekday()  # Extract the day from the current date

if day_of_the_week == 6:  # If the day of the week is sunday
    # Pick a random sentence from the file
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    # Send it via email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure our connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="maigt3st@yahoo.com",
            msg="Subject:Sunday Motivational Quote\n\n"+random_quote
        )
