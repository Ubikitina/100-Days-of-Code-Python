import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 43.263012  # Search here: https://www.latlong.net/
MY_LONG = -2.934985
MY_EMAIL ="maigt3st@gmail.com"
MY_PASSWORD = "ADD_HERE_THE_PASSWORD"

#Your position is within +5 or -5 degrees of the ISS position.
def is_IIS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return ((MY_LAT-5) <= iss_latitude <= (MY_LAT+5)) and ((MY_LONG-5) <= iss_longitude <= (MY_LONG+5))

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


while True:

    time.sleep(60)  # Run the code every 60 seconds.

    #If the ISS is close to my current position and it is currently dark
    if is_IIS_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure our connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="maigt3st@yahoo.com",
                msg="Subject:Look Up\n\nInternational Space Station is above you in the sky."
            )








