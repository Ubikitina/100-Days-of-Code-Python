import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM_URL = "ENTER YOUR FORM URL HERE"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"


# ----------------------------------------------------------------------------------
# Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address
# ----------------------------------------------------------------------------------
# Send an HTTP GET request to the Zillow Clone URL
response = requests.get(ZILLOW_CLONE_URL)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all rental property divs with the specified class
    all_rentals = soup.find_all('div', class_='StyledPropertyCardDataWrapper')

    # Initialize lists to store rental URLs, prices, and addresses
    list_of_rental_urls = []
    list_of_rental_prices = []
    list_of_rental_addresses = []

    # Loop through each rental property
    for rental in all_rentals:
        # Find the 'a' tag within the rental div and get the value of the 'href' attribute
        rental_url = rental.find('a', {'class': 'StyledPropertyCardDataArea-anchor'})['href']
        list_of_rental_urls.append(rental_url)

        # Find the span tag with the specified class and extract the first 6 characters (price)
        rental_price = rental.find('span', class_='PropertyCardWrapper__StyledPriceLine').text[:6]
        list_of_rental_prices.append(rental_price)

        # Find the 'address' tag within the rental div, strip whitespace, and remove the trailing pipe symbol
        rental_address = rental.find('address').text.strip().replace(' |', '')
        list_of_rental_addresses.append(rental_address)

    # print(list_of_rental_urls)
    # print(list_of_rental_prices)
    # print(list_of_rental_addresses)

# ----------------------------------------------------------------------------------
# Use Selenium to fill in the form
# ----------------------------------------------------------------------------------
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Loop through each element in the lists
for i in range(len(list_of_rental_urls)):
    # Open the specified URL in the Chrome browser.
    driver.get(GOOGLE_FORM_URL)

    # Find the input field for the address using XPath and input the rental address
    address_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_form.send_keys(list_of_rental_addresses[i])

    # Find the input field for the price using XPath and input the rental price
    price_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form.send_keys(list_of_rental_prices[i])

    # Find the input field for the link using XPath and input the rental link
    link_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form.send_keys(list_of_rental_urls[i])

    # Find the submit button using XPath and click on it
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
