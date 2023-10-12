# Import the 'requests' library, which allows making HTTP requests
import requests
from datetime import datetime

#
# # Send an HTTP GET request to the specified URL and store the response in the 'response' variable
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # Print the HTTP status code received in the response
# print(response)
#
# # Check if the response has an HTTP status code indicating an error (4xx or 5xx status codes)
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
#
# print(data)
# print(iss_position)

parameters = {
    "lat": 43.263012,  # Search here: https://www.latlong.net/
    "long": -2.934985,
    "formatted": 0
}

# Send an HTTP GET request to the specified URL with parameters and store the response in 'response'
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# Check if the response has an HTTP status code indicating an error (4xx or 5xx status codes)
response.raise_for_status()
# Parse the response content as JSON and store it in the 'data' variable
data = response.json()
sunrise = data["results"]["sunrise"]
# Split the "sunrise" time to get the hour part
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset = data["results"]["sunset"]
# Split the "sunset" time to get the hour part
sunset_hour = sunset.split("T")[1].split(":")[0]
#print(data)

print(sunrise_hour)
print(sunset_hour)

# Get the current time
time_now = datetime.now()
# Extract the current hour and print it
print(time_now.hour)