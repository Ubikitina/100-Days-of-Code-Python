# Day 40: Flight Club Project - Python Learning

- [Day 40: Flight Club Project - Python Learning](#day-40-flight-club-project---python-learning)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Improvements from Day 39 to Day 40](#improvements-from-day-39-to-day-40)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
    - [1. Register Users](#1-register-users)
    - [2. Search for Flights and Send Notifications](#2-search-for-flights-and-send-notifications)
    - [3. Check the Google Spreadsheet](#3-check-the-google-spreadsheet)
  - [Project Workflow](#project-workflow)
  - [Technologies Used](#technologies-used)
  - [Conclusion](#conclusion)


## Overview
This project, titled **Flight Club**, is an automated system that tracks and alerts users about the best flight deals. The system fetches flight data, compares it to a predefined threshold, and notifies users via email and SMS when cheaper flights are available. The project interfaces with various APIs and services, such as Google Sheets, Twilio for SMS notifications, and a flight search service for retrieving flight data.

## Project Structure
Here's a brief description of each file in the project:

- **customer_registration_command.py**: This script manages user registration. It collects user details such as first name, last name, and email, and then stores this information in a Google Sheet using the Sheety API.

- **data_manager.py**: Handles all interactions with the Google Sheets. It retrieves and updates data in the sheet, including both user information and flight prices.

- **Flight Deals_sample_spreadsheet.xlsx**: A sample spreadsheet that simulates the Google Sheet used in this project. It stores data such as destination cities, IATA codes, and the lowest recorded flight prices.

- **flight_data.py**: Defines the `FlightData` class, which encapsulates details about a flight, including price, origin, destination, and travel dates.

- **flight_search.py**: Interacts with the Tequila Kiwi API to search for flights. It retrieves IATA codes for cities and searches for flights based on specified criteria.

- **main.py**: The main script that integrates all components. It fetches data from the Google Sheet, searches for flights, compares prices, and sends notifications to users if a cheaper flight is found.

- **notification_manager.py**: Manages the sending of notifications. It uses Twilio to send SMS messages and the `smtplib` library to send emails to registered users.

- **sheety.py**: A simple wrapper around the Sheety API for interacting with Google Sheets. It is used to add new rows to the sheet and to retrieve data.

## Improvements from Day 39 to Day 40

1. **User Registration Feature**: Day 40 introduced a new script, `customer_registration_command.py`, that allows users to register by entering their first name, last name, and email. This information is then stored in the Google Sheet.

2. **Data Separation and Management** Day 39 data handling was rudimentary, with all flight-related data being managed directly in the `main.py` script. Day 40 data handling responsibilities were abstracted into the `data_manager.py` file. This improvement enhances code organization and reusability by centralizing all Google Sheets interactions.

3. **Enhanced Notification System** Day 39 notification system only supported SMS alerts. Day 40 added email notifications to the system. The `notification_manager.py` was updated to handle both SMS and email alerts, allowing for more versatile user communication.

4. **IATA Code Retrieval** On Day 39, the IATA code retrieval was integrated directly within the `main.py` script. On Day 40, this functionality was moved to the `flight_search.py` file, providing a clear separation of concerns and improving the modularity of the code.

5. **Refined Flight Search Logic** On Day 39, the flight search functionality was less flexible, with a focus on direct flights only. Day 40 enhanced the search logic to handle cases where no direct flights are found by introducing a fallback mechanism to search for flights with stopovers. This increases the chances of finding cheaper flights.

6. **Better Error Handling** especially in the `flight_search.py` script. This ensures that the system continues to function smoothly even when no flights are found or when API errors occur.

7. **Refactored Codebase** Day 39 code was more monolithic, with less attention to modularity and reusability. Day 40: The codebase was refactored to improve structure, readability, and maintainability. Functions were better organized, and classes were used to encapsulate related functionalities.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed on your machine.
- A Google Sheets API key (Sheety) for managing data storage.
- A Kiwi Tequila API key for searching flights.
- Twilio credentials for sending SMS notifications.
- An email account with an app password for sending email notifications.

## Setup and Installation

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:
    ```bash
    pip install requests twilio
    ```

3. Set up environment variables for sensitive information (API keys, authentication tokens, etc.). You can use the following environment variables:
    - `SPREADSHEET_ENDPOINT`: The endpoint URL for your Google Sheets API (Sheety).
    - `SHEETY_AUTH`: The authorization token for Sheety.
    - `TEQUILA_API_KEY`: Your Kiwi Tequila API key.
    - `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token.
    - `TWILIO_VIRTUAL_NUMBER`: The Twilio phone number you want to send SMS from.
    - `TWILIO_VERIFIED_NUMBER`: The verified phone number where you want to receive SMS.
    - `MY_EMAIL`: Your email address for sending notifications.
    - `EMAIL_PASS`: The app password for your email account.

4. Update the placeholder values in the code with your actual API keys and tokens.


## Usage

### 1. Register Users
Run the `customer_registration_command.py` script to allow users to register for the Flight Club. They will be asked to provide their first name, last name, and email address.

```bash
python customer_registration_command.py
```

### 2. Search for Flights and Send Notifications
Run the `main.py` script to search for flights, compare prices, and send notifications to users if better deals are found.

```bash
python main.py
```

### 3. Check the Google Spreadsheet
The Google Spreadsheet (managed via Sheety) will store the flight deals and user information. You can check it to verify the data or update it manually if needed.


## Project Workflow

1. **User Registration**: Users register by providing their name and email, which is stored in the Google Sheet.
2. **Flight Search**: The script fetches the list of destination cities and their corresponding IATA codes. If a city's IATA code is missing, it will fetch it from the Kiwi Tequila API.
3. **Price Comparison**: The script searches for flights between the origin city and the destination cities and compares the prices with the lowest price stored in the Google Sheet.
4. **Notification**: If a cheaper flight is found, an SMS and/or email notification is sent to all registered users.
5. **Update Spreadsheet**: The lowest price in the Google Sheet is updated with the new deal if a cheaper flight is found.

## Technologies Used

- **Python**: The core programming language used for scripting.
- **Google Sheets API (Sheety)**: For managing data storage in a Google Sheet.
- **Kiwi Tequila API**: For searching flights and fetching IATA codes.
- **Twilio API**: For sending SMS notifications.
- **SMTP**: For sending email notifications.

## Conclusion
Day 40's version of the Flight Club project represents a significant improvement in terms of functionality, code organization, and user interaction compared to Day 39. The enhancements make the project more robust, user-friendly, and easier to maintain.