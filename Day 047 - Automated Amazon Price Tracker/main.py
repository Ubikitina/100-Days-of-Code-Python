import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# This is the URL of the Amazon product that we want to track
PRODUCT_URL = "https://www.amazon.es/kindle-paperwhite-16-gb-ahora-con-una-pantalla-de-68-y-luz-calida-ajustable-con-publicidad/dp/B09TMF6742/?_encoding=UTF8"
TARGET_PRICE = 155.0

# Email credentials to send the email
MY_EMAIL = "enter here your email"
MY_PASSWORD = "enter here your password"


## ---------------------------------------------------------------------------------------
## GETTING DATA FROM THE WEB
## ---------------------------------------------------------------------------------------

# Define custom headers for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9,eu;q=0.8',  # Adjust the language as needed
}

# Send the GET request with the custom headers to get the HTML of the website
response = requests.get(PRODUCT_URL, headers=headers)
web_page_content = response.text  # Get its code

# Create a soup to interact with the HTML code
soup = BeautifulSoup(web_page_content, "lxml")

# Get the price of the product from the HTML code
price_whole = soup.find(name='span', class_="a-price-whole").getText().strip().replace(",", "")
price_fraction = soup.find(name='span', class_="a-price-fraction").getText().strip()

# Convert the obtained data into a numerical (float) value
price = float(f"{price_whole}.{price_fraction}")


## ---------------------------------------------------------------------------------------
## EMAIL ALERT WHEN PRICE IS BELOW A PRESET VALUE
## ---------------------------------------------------------------------------------------

# We want to get an email when the price of our product is below a certain value (TARGET_PRICE)
if price < TARGET_PRICE:
    # Get the product name
    product_name = soup.find('span', {'id': 'productTitle'}).getText().strip()

    # Use the smtp module to email yourself
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure our connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)  # Login

        # Send the email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon price alert!\n\n{product_name} is now {price} €.\n{PRODUCT_URL}".encode("utf-8")
        )
