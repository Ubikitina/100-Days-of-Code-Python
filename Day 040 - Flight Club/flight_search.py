import requests  # Import the "requests" module for making HTTP requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "ENTER API KEY HERE"

class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """

    def __init__(self):
        """
        Initializes a new instance of the FlightSearch class.

        It sets the API key in the header for secure authentication.

        Parameters:
        None

        Returns:
        None
        """

        # Header to authenticate. By using the header, the authentication is more secure than sending our token via parameters
        self.tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }



    def get_iata_code(self, city_name):
        """
        Retrieves the IATA code for a given city name.

        Parameters:
        city_name (str): The name of the city for which you want to obtain the IATA code.

        Returns:
        str: The IATA code for the specified city.
        """

        query = {
            "term": city_name,
            "location_types": "city"
        }

        # Send an HTTP GET request to the Sheety API using the defined header.
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=self.tequila_headers)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code


    def get_flights(self, origin_city_code, destination_city_code):
        """
        Searches for available flights between two cities and retrieves flight details.

        Parameters:
        origin_city_code (str): The IATA code of the origin city.
        destination_city_code (str): The IATA code of the destination city.

        Returns:
        FlightData: An instance of the FlightData class containing flight details.
        """

        # Define a dictionary with query parameters for the Tequila API
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),  # Tomorrow
            "date_to": (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y"),  # 6 months from now
            "max_stopovers": 0,  # the number of stopovers the user want to do
            "ret_from_diff_city": "false",
            "one_for_city": 1,  # It returns the cheapest flight to every city
            "nights_in_dst_from": 7,  # the minimal length of stay in the destination
            "nights_in_dst_to": 30,  # the maximal length of stay in the destination
            "curr": "EUR"  # The currency of the price we get back should be in GBP
        }

        # Send an HTTP GET request to the Sheety API using the defined header.
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=self.tequila_headers)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]

            # print(data)  # Print for debugging

            # Create a FlightData object with the retrieved flight details
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                departure_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=0,
                via_city=""
            )

            # Print flight information for debugging
            print(f"{flight_data.destination_city}: {flight_data.price}€, from {flight_data.departure_date} to {flight_data.return_date}")

            return flight_data

        except IndexError:
            # If no direct flights are found, search for flights with 1 stopover
            print(f"No flights found for {destination_city_code} with 0 stopovers. Searching for 1 stopovers.")

            # Update the max_stopovers parameter to 1
            query["max_stopovers"] = 1

            # Send an HTTP GET request to the Sheety API using the defined header.
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=self.tequila_headers)
            response.raise_for_status()

            try:
                data = response.json()["data"][0]

                # print(data)  # Print for debugging

                # Create a FlightData object for flights with 1 stopover
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    departure_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )

                # Print flight information for debugging
                print(f"{flight_data.destination_city}: {flight_data.price}€, from {flight_data.departure_date} to {flight_data.return_date}")

                return flight_data

            except IndexError:
                # If no flights are found with 1 stopover, indicate that no flights are available
                print(f"No flights found for {destination_city_code} with 1 stopovers.")

                return None





# Code for class testing purposes
# my_class = FlightSearch()
# my_class.get_flights(origin_city_code="BIO", destination_city_code="PAR")