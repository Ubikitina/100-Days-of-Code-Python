# import smtplib
#
# my_email ="maigt3st@gmail.com"
# password = "ADD_HERE_THE_PASSWORD"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # Secure our connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="maigt3st@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt

# Get the current date and time
now = dt.datetime.now()

# Extract the year, month, and day from the current date and time
year = now.year
month = now.month
day_of_the_week = now.weekday()

# Print the current date and time, year, month, and day of the week
print(now)  # 2023-10-08 12:05:25.003540
print(year)  # 2023
print(month)  # 10
print(day_of_the_week)  # 6, which means it's the 7th day of the week, which is Sunday

# Create a datetime object representing a specific date of birth
date_of_birth = dt.datetime(year=1993, month=12, day=15)
print(date_of_birth)  # 1993-12-15 00:00:00, the hour is set up to a default value