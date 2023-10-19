# Import necessary modules or classes from my project
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BIO"

# Create instances of DataManager, FlightSearch, and NotificationManager classes
my_data_manager = DataManager()
my_flight_search = FlightSearch()
my_notification_manager = NotificationManager()

# Get the current data from the spreadsheet
sheet_data = my_data_manager.get_spreadsheet_data()

# Loop through each item in the data retrieved from the spreadsheet
for item in sheet_data:
    # Check if the 'iataCode' field is empty for the current item
    if item["iataCode"] == '':
        item["iataCode"] = my_flight_search.get_iata_code(item["city"])  # If 'iataCode' is empty, search for the corresponding IATA code using FlightSearch
        my_data_manager.put_spreadsheet_row(item)  # Update the data in the spreadsheet with the new 'iataCode'

# Retrieve the current data from the spreadsheet again
sheet_data = my_data_manager.get_spreadsheet_data()  # [{'city': 'Palma, Majorca', 'iataCode': 'PMI', 'lowestPrice': 21, 'id': 2}, {'city': 'Alicante', 'iataCode': 'ALC', 'lowestPrice': 24, 'id': 3}, ...]

# Iterate through the data retrieved from the spreadsheet
for item in sheet_data:
    # Search the cheapest flights from the origin city specified to the destination with 'iataCode'
    flight_found = my_flight_search.get_flights(origin_city_code=ORIGIN_CITY_IATA,destination_city_code=item["iataCode"])

    # Check if the flight found is cheaper than the 'lowestPrice' listed in the Google Sheet
    if flight_found.price < item["lowestPrice"]:
        # Compose a message to send
        text_to_send = f"Lower price alert! Only {flight_found.price}€ to fly from {flight_found.origin_city}-{flight_found.origin_airport} to {flight_found.destination_city}-{flight_found.destination_airport}, from {flight_found.departure_date} to {flight_found.return_date}."
        # Send an SMS using Twilio
        my_notification_manager.send_message(text_to_send=text_to_send)

        # Update the spreadsheet with the new 'lowestPrice'
        item["lowestPrice"] = flight_found.price
        my_data_manager.put_spreadsheet_row(item)




