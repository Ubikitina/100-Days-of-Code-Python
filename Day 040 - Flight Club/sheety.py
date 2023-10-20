import requests  # Import the "requests" module for making HTTP requests

SPREADSHEET_ENDPOINT = "ENTER SPREADSHEET ENDPOINT HERE"
SHEETY_AUTH = "ENTER AUTH HERE"

class Sheety:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self):
        """
        Initializes a new instance of the Sheety class.

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


    def post_spreadsheet_row(self, first_name, last_name, email):
        """
        Adds a specific row in the Google Sheet.

        """

        # Define the endpoint for the row
        row_endpoint = SPREADSHEET_ENDPOINT

        # New data to be added
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        # Put request to add the row
        response = requests.post(url=row_endpoint, headers=self.sheety_headers, json=body)
        response.raise_for_status()
        # print(response.text)