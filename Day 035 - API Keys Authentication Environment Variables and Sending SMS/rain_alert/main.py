# Import the 'requests' library, which allows making HTTP requests
import requests

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

# Variables for API access
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")  # We may not want to display such authentication codes in the code.
                                         # Alternatively, we can store them in environment variables by doing
                                         # export OWM_API_KEY=and_the_key_here
                                         # Then, we retrieve it from the environment variable by using os.environ.get

# Variables for sending the SMS, they have also been set as environment variables to avoid having to display in the code
account_sid = os.environ.get("SMS_ACCOUNT_SID") # Find your Account SID and Auth Token at twilio.com/console and set the environment variables. See http://twil.io/secure
auth_token = os.environ.get("SMS_ACCOUNT_TOKEN")

# We define the parameters for making the API call
parameters = {
    "lat": 42.240601,  # lat and lon correspond to the latitude and longitude where we want to check the weather
    "lon": -8.720727,
    "appid": api_key  # With this code we identify ourselves as consumers of the API.
}

# Send an HTTP GET request to the specified URL and store the response in the 'response' variable
response = requests.get(url=OWM_Endpoint, params=parameters)

# Check if the response has an HTTP status code indicating an error (4xx or 5xx status codes)
response.raise_for_status()

# Extract the data in JSON format
weather_data = response.json()
# print(weather_data)

# Get the weather ID code
weather_id = int(weather_data["weather"][0]["id"])
print(weather_id)

# According to https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2, if id is <700, then there's a bad weather, so umbrella is needed.
if weather_id < 700:
    print("Bring an Umbrella")  # Printing in the console just to ensure that we've entered the if statement

    # Create the client to send the SMS using twilio
    client = Client(account_sid, auth_token)

    # Create the SMS message
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+12054306870',  # Paste here the trial number
        to='+123456789'  # Phone number used to sign up in twilio, as we are using the free trial service, this phone number must be listed in the Verified Caller IDs list.
    )

    # Check SMS sending status
    print(message.status)




