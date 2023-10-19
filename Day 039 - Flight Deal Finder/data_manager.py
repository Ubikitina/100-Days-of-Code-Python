import requests  # Import the "requests" module for making HTTP requests

SPREADSHEET_ENDPOINT = "ENTER YOUR SPREADSHEET ENDPOINT HERE"
SHEETY_AUTH = "ENTER YOUR SHEETY AUTH HERE"

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self):
        """
        Initializes a new instance of the DataManager class.

        It sets the authentication header for secure communication.

        Parameters:
        None

        Returns:
        None
        """

        # Header to authenticate. By using the header, the authentication is more secure than sending our token via parameters
        self.sheety_headers = {
            "Authorization": SHEETY_AUTH
        }

    def get_spreadsheet_data(self):
        """
        Retrieves all the data from the Google Sheet.

        Parameters:
        None

        Returns:
        list: A list of dictionaries containing the data from the spreadsheet.
        """

        # Send an HTTP GET request to the Sheety API using the defined header to get all the data in the spreadsheet.
        response = requests.get(url=SPREADSHEET_ENDPOINT, headers=self.sheety_headers)
        response.raise_for_status()

        all_spreadsheet_data = response.json()["prices"]
        # pprint(all_spreadsheet_data)
        return all_spreadsheet_data

    def put_spreadsheet_row(self, updated_row):
        """
        Updates a specific row in the Google Sheet.

        Parameters:
        updated_row (dict): The updated row data to be added to the spreadsheet.

        Returns:
        None
        """

        # Define the endpoint for the row
        row_endpoint = SPREADSHEET_ENDPOINT + f"/{updated_row['id']}"

        # New data to be added
        updated_row_dict = {
            "price": updated_row
        }

        # Put request to update the row
        response = requests.put(url=row_endpoint, headers=self.sheety_headers, json=updated_row_dict)
        response.raise_for_status()
        # print(response.text)