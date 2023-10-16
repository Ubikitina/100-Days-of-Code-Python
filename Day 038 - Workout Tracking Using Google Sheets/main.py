import requests  # Import the "requests" module for making HTTP requests
from datetime import datetime  # Datetime module to get today's date and time
import os  # os module to set authentication id and passwords as environment variables and avoid having them in the code below

# Set the constants
GENDER = "female"
WEIGHT_KG = 60
HEIGHT_CM = 167
AGE = 20

# Set the authentication information for the Nutritionix API call
APP_ID = os.environ.get("APP_ID")  # We do not want to display such authentication codes in the code. Alternatively, we store them in environment variables
API_KEY = os.environ.get("API_KEY")

# Set the authentication information for the Sheety API call
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")

# Define the API endpoint URLs
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
spreadsheet_endpoint = os.environ.get("SHEET_ENDPOINT")

# Prompt the user for exercise input
exercise_text = input("Tell me which exercises you did: ")


## ==========================================================================================
## SECTION 1 - Nutritionix API call
## ==========================================================================================

# Authentication token. By using the header, the authentication is more secure than sending our token via parameters
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Create a dictionary with the necessary parameters for the API call
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send an HTTP POST request to the Nutritionix API using the defined headers and parameters
response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
response.raise_for_status()

# Get the JSON response from the API to the console into a data variable
data = response.json()["exercises"]
# print(data)



## ==========================================================================================
## SECTION 2 - Sheety API call
## ==========================================================================================

# Get today's day and time
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")  # 16:49:43 format

# Header to authenticate. By using the header, the authentication is more secure than sending our token via parameters
sheety_headers = {
    "Authorization": SHEETY_AUTH
}

# Get the data to enter the spreadsheet. We need a for loop because the user might entered more than one input in one sentence.
for exercise in data:

    # Create a dictionary with the necessary parameters for the API call
    new_row_data = {
        "sheet1": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send an HTTP POST request to the Sheety API using the defined headers and parameters. This will add a row in the spreadsheet.
    response = requests.post(url=spreadsheet_endpoint, json=new_row_data, headers=sheety_headers)
    response.raise_for_status()
    # print(response.json())