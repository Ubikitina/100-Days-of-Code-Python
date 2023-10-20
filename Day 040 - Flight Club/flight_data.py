class FlightData:
    """
    Represents flight data with details about price, origin, destination, and travel dates.
    """

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, departure_date, return_date, stop_overs, via_city):
        """
        Initializes a new instance of the FlightData class with flight details.

        Parameters:
        price (float): The price of the flight.
        origin_city (str): The city where the flight originates.
        origin_airport (str): The airport in the origin city.
        destination_city (str): The destination city.
        destination_airport (str): The airport at the destination.
        departure_date (str): The date of departure in the format "yyyy-mm-dd".
        return_date (str): The return date in the format "yyyy-mm-dd".
        stop_overs (int): The number of stopovers during the flight.
        via_city (str): The city where the flight has stopovers if any.

        Returns:
        None
        """

        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city