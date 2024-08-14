# Day 35: API Keys Authentication, Environment Variables, and Sending SMS

## Overview
On Day 35 of my Python learning journey, I focused on securing API keys using environment variables and sending SMS notifications using the Twilio API. The project demonstrates how to access weather data from the OpenWeatherMap API and send an SMS alert if certain weather conditions are met.

## Files and Structure

### `main.py`
- **Description:** This script retrieves weather data for a specific location using the OpenWeatherMap API. If the weather condition indicates rain, the script sends an SMS notification using the Twilio API.

- **Key Features:**
  - **Environment Variables:** 
    - API keys and authentication tokens are stored securely in environment variables to avoid exposing sensitive information in the code.
    - Environment variables are accessed using `os.environ.get()`.
  - **API Request:**
    - The script makes an HTTP GET request to the OpenWeatherMap API to retrieve weather data for a specific latitude and longitude.
    - It checks the response status to ensure the request was successful.
  - **Weather Data Processing:**
    - The weather condition is determined by checking the `weather_id` from the API response.
    - If the weather condition ID is less than 700 (indicating bad weather), a notification is triggered.
  - **Sending SMS with Twilio:**
    - The Twilio API is used to send an SMS alert if the weather condition requires carrying an umbrella.
    - The SMS message includes a brief alert about the weather, and the script prints the message status to confirm it was sent successfully.

## How to Use

1. **Set Up Environment Variables:**
   - Before running the script, ensure the following environment variables are set on your system:
     - `OWM_API_KEY`: Your OpenWeatherMap API key.
     - `SMS_ACCOUNT_SID`: Your Twilio Account SID.
     - `SMS_ACCOUNT_TOKEN`: Your Twilio Auth Token.
   - These can be set in your terminal using:
     ```bash
     export OWM_API_KEY=your_openweathermap_api_key
     export SMS_ACCOUNT_SID=your_twilio_account_sid
     export SMS_ACCOUNT_TOKEN=your_twilio_auth_token
     ```

2. **Run the Script:**
   - Execute `main.py` to check the weather and potentially send an SMS alert.
   - The script will retrieve weather data for the specified location (latitude: 42.240601, longitude: -8.720727) and send an SMS if rain is expected.

3. **Check the Console:**
   - The script will print the `weather_id` to the console, along with a message if an umbrella is needed.
   - It also prints the status of the SMS message to confirm whether it was successfully sent.
