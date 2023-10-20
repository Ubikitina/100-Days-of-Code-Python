from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = "ENTER ACCOUNT SID HERE" # Find your Account SID and Auth Token at twilio.com/console and set the environment variables. See http://twil.io/secure
TWILIO_AUTH_TOKEN = "ENTER TOKEN HERE"
TWILIO_VIRTUAL_NUMBER = 'ENTHER PHONE NUMBER HERE'  # Paste here the trial number
TWILIO_VERIFIED_NUMBER = 'ENTHER PHONE NUMBER HERE'  # Phone number used to sign up in twilio, as we are using the free trial service, this phone number must be listed in the Verified Caller IDs list.

MY_EMAIL ="ENTER EMAIL HERE"
EMAIL_PASS = "ENTER EMAIL APP PASSWORD HERE"  # Special password, to be checked in your email provider web


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


    def send_emails(self, address_to, subject, body):
        """
       Send an email with a specified subject and body to the recipient's email address using the Gmail SMTP server.

       Parameters:
           address_to (str): The recipient's email address.
           subject (str): The subject of the email.
           body (str): The content or body of the email.
       """

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure our connection
            connection.login(user=MY_EMAIL, password=EMAIL_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=address_to,
                msg=f"Subject:{subject}\n\n{body}".encode('utf-8')
            )


# Code to test this class
# my_notification_manager = NotificationManager()
# my_notification_manager.send_emails(subject="Hello", address_to="maialen@email.com", body="This is an email")