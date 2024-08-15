# Day 39: Flight Deal Finder

## Overview
On Day 39, I developed a Flight Deal Finder project that searches for flight deals and sends alerts when a flight price is lower than the one recorded in a Google Sheet. This project uses several APIs, including the Kiwi Tequila API for flight data and the Twilio API for sending SMS notifications.

## Files and Structure

### Project Structure
```
📁 Day 39 Projects
├── 📄 main.py
├── 📄 data_manager.py
├── 📄 flight_data.py
├── 📄 flight_search.py
├── 📄 notification_manager.py
└── 📄 Flight Deals_sample_spreadsheet.xlsx
```

### 1. `main.py`
- **Description:** The main entry point of the project. It integrates all the modules to search for flight deals and send notifications when a deal is found.
  
- **Key Functions:**
  - Retrieves and updates IATA codes in the Google Sheet.
  - Searches for flights and compares prices with those listed in the sheet.
  - Sends an SMS alert via Twilio if a cheaper flight is found.

### 2. `data_manager.py`
- **Description:** Manages the interaction with the Google Sheet where flight information is stored.
  
- **Functions:**
  - `get_spreadsheet_data()`: Retrieves all data from the Google Sheet.
  - `put_spreadsheet_row(updated_row)`: Updates a specific row in the Google Sheet with new data.

### 3. `flight_data.py`
- **Description:** Represents flight data with details about price, origin, destination, and travel dates.
  
- **Key Class:**
  - `FlightData`: Stores and organizes the details of a flight, including price, origin, destination, and travel dates.

### 4. `flight_search.py`
- **Description:** Interacts with the Kiwi Tequila API to search for flights and retrieve IATA codes for cities.
  
- **Functions:**
  - `get_iata_code(city_name)`: Retrieves the IATA code for a given city name.
  - `get_flights(origin_city_code, destination_city_code)`: Searches for flights between two cities and returns flight details.

### 5. `notification_manager.py`
- **Description:** Manages the sending of SMS notifications using the Twilio API.
  
- **Functions:**
  - `send_message(text_to_send)`: Sends an SMS message with the provided text.

### 6. `Flight Deals_sample_spreadsheet.xlsx`
- **Description:** A sample Google Sheet that stores city names, IATA codes, and the lowest recorded prices for flights to those cities.
  
- **Column Structure:**
  - `City`: The name of the city.
  - `IATA Code`: The IATA code for the city.
  - `Lowest Price`: The lowest recorded price for flights to the city.
  - `ID`: The unique identifier for each row in the sheet.

## Setup Instructions

### Prerequisites
- **APIs and Services:**
  - [Kiwi Tequila API](https://docs.kiwi.com/): For flight searches.
  - [Sheety API](https://sheety.co/): To interact with Google Sheets.
  - [Twilio API](https://www.twilio.com/): For sending SMS notifications.
  
- **Environment Variables:**
  - Set up the following environment variables in your system or `.env` file:
    - `SHEET_ENDPOINT`: The endpoint URL for your Google Sheet.
    - `SHEETY_AUTH`: The authorization token for Sheety API.
    - `TEQUILA_API_KEY`: Your Kiwi Tequila API key.
    - `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token.
    - `TWILIO_VIRTUAL_NUMBER`: The virtual number from which SMS will be sent.
    - `TWILIO_VERIFIED_NUMBER`: The verified phone number to receive SMS notifications.

### Running the Project
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <folder>
   ```

2. **Install Required Packages:**
   ```bash
   pip install requests twilio
   ```

3. **Configure the Spreadsheet:**
   - Create a Google Sheet similar to `Flight Deals_sample_spreadsheet.xlsx`.
   - Set the endpoint in the `SHEET_ENDPOINT` environment variable.

4. **Run the Script:**
   ```bash
   python main.py
   ```

### Example Workflow
1. **Update IATA Codes:** If a city does not have an IATA code, the script will search for and update it in the sheet.

2. **Search for Flight Deals:** The script searches for flights from your origin city to all destinations listed in the sheet.

3. **Send Notifications:** If a flight is found cheaper than the listed price, an SMS notification is sent.

## Notes
- **Error Handling:** The script includes basic error handling using `response.raise_for_status()` to catch and raise exceptions for unsuccessful requests.
- **API Limits:** Be aware of API request limits, especially with free tiers of services like Twilio and Sheety.



## Concepts Learned

1. **API Integration:** Understanding how to interact with third-party APIs using HTTP requests. Managing API authentication using headers and environment variables. Parsing and handling JSON data returned from API responses.
   
2. **Object-Oriented Programming (OOP):** Creating and using classes (`DataManager`, `FlightSearch`, `FlightData`, `NotificationManager`) to structure code. Encapsulation of functionality within methods to keep the code modular and reusable.

3. **Environment Variables:** Using environment variables to securely manage sensitive information like API keys and authentication tokens.

4. **Error Handling:** Implementing error handling in HTTP requests using `response.raise_for_status()` to manage unsuccessful API calls.

5. **Working with Dates and Times:** Using the `datetime` module to manipulate and format dates for API queries. Calculating date ranges for flight searches.

6. **Automation with Google Sheets:** Automating the process of updating and retrieving data from Google Sheets via the Sheety API.

7. **Sending SMS Notifications:** Using the Twilio API to send SMS messages as alerts when certain conditions are met (e.g., when a flight deal is found).

8. **Data Handling and Iteration:** Iterating through data structures (lists and dictionaries) to process and update information in the spreadsheet.

## Libraries Used

1. **requests:**
   - For making HTTP requests to external APIs (e.g., Sheety API, Kiwi Tequila API).
   - Used to send `GET`, `POST`, and `PUT` requests to interact with web services.

2. **datetime:**
   - Part of Python's standard library, used for manipulating and formatting date and time objects.
   - Used for calculating date ranges for flight searches.

3. **twilio:**
   - A third-party library to interact with the Twilio API.
   - Used to send SMS messages from a Python script, facilitating notifications about flight deals.

4. **os:**
   - Part of Python's standard library, used to interact with the operating system.
   - Used to retrieve environment variables, which store sensitive information like API keys and authentication tokens.
