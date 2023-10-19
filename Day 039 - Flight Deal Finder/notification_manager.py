from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ENTER ACCOUNT SID HERE" # Find your Account SID and Auth Token at twilio.com/console and set the environment variables. See http://twil.io/secure
TWILIO_AUTH_TOKEN = "ENTER TOKEN HERE"
TWILIO_VIRTUAL_NUMBER = 'ENTER TRIAL VIRTUAL NUMBER HERE'  # Paste here the trial number
TWILIO_VERIFIED_NUMBER = 'ENTER VERIFIED NUMBER HERE'  # Phone number used to sign up in twilio, as we are using the free trial service, this phone number must be listed in the Verified Caller IDs list.


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self):
        """
        Initializes a new instance of the NotificationManager class.

        It creates a Twilio client to send SMS messages.

        Parameters:
        None

        Returns:
        None
        """
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # Create the client to send the SMS using twilio

    def send_message(self, text_to_send):
        """
        Sends an SMS message with the provided text.

        Parameters:
        text_to_send (str): The text of the SMS message to be sent.

        Returns:
        None
        """
        # Create the SMS message
        message = self.client.messages \
            .create(
            body=text_to_send,
            from_=TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER
        )

        # Check SMS sending status
        print(message.status)
