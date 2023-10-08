import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL ="maigt3st@gmail.com"
MY_PASSWORD = "ADD_HERE_THE_PASSWORD"

# Create a tuple from today's month and day using datetime
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

# Use pandas to read the birthdays.csv into a Pandas DataFrame
birthdays_df = pd.read_csv("birthdays.csv")

# Use dictionary comprehension to create a dictionary. They key is a tuple of month and day, and the value is the entire row content formatted into a key-value dictionary
birthdays_dict = {(row['month'], row['day']): row.to_dict() for (_, row) in birthdays_df.iterrows()}

# Compare if today's month/day tuple matches one of the keys in birthday_dict
if today_tuple in birthdays_dict:

    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter_templates_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    random_letter = random.choice(letter_templates_list)

    with open(random_letter, "r") as file:
        letter_content = file.read()

    letter_content = letter_content.replace("[NAME]", birthdays_dict[today_tuple]['name'])

    # Send the letter generated to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure our connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today_tuple]['email'],
            msg="Subject:Happy Birthday!\n\n"+letter_content
        )



