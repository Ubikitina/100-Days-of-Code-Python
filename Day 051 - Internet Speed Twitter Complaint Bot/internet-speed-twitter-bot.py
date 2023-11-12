from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set the Twitter URL, username, and password as constants
TWITTER_URL = "https://twitter.com/"
USERNAME = "ENTER YOUR USERNAME"
PASSWORD = "ENTER YOUR PASSWORD"

# Set promised internet speeds as constants
PROMISED_DOWN = 100
PROMISED_UP = 100

INTERNET_SPEED_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
        chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

        # Create a Chrome web driver instance with the specified options.
        self.driver = webdriver.Chrome(options=chrome_options)

        # Create properties
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Open the specified URL in the Chrome browser.
        self.driver.get(INTERNET_SPEED_URL)
        time.sleep(3)

        # Accept cookies
        cookies_accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_accept_button.click()

        # Close banner
        banner_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/a')
        banner_button.click()

        # Click on "Go" button
        go_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        go_button.click()

        # Wait until the speed is measured
        time.sleep(55)

        # Close the pop-up
        popup_close_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        popup_close_button.click()

        # Extract the results
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        # print(f"The actual download is {self.down}.")
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        # print(f"The actual upload is {self.up}.")

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            tweet = f"Hey Internet Provider, why is my interned speed {self.down} down / {self.up} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"

            # Open the specified URL in the Chrome browser.
            self.driver.get(TWITTER_URL)

            time.sleep(2)

            # Find and click the accept cookies button
            accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
            accept_cookies.click()

            # Find and click the sign-in button
            sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
            sign_in_button.click()

            # Pausing the script for 2 seconds until the page loads
            time.sleep(2)

            # Fill in the login form
            user_form = self.driver.find_element(By.CSS_SELECTOR, 'div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu')  # Find username field
            user_form.click()  # Enable the form
            user_form_input = self.driver.find_element(By.CSS_SELECTOR, "input")  # Find the input element
            user_form_input.send_keys(USERNAME)  # Enter the username

            # Find and click next button
            next_button = self.driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-1m3jxhj.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
            next_button.click()

            # Pausing the script for 2 seconds until the page loads
            time.sleep(2)

            # Fill in the password form
            password_form_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')  # Search the password form element
            password_form_input.send_keys(PASSWORD)  # Enter the password

            # Find and click the login button
            log_in_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')  # Search log in button
            log_in_button.click()  # Click the button

            # Fill in the tweet form
            tweet_form = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div')
            tweet_form.click()  # Enable the form
            tweet_form_input = self.driver.find_element(By.CSS_SELECTOR, "input")  # Search the input element
            tweet_form_input.send_keys(tweet)

            # Find and click the post button
            post_button = self.driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')
            post_button.click()


# Create an instance of the InternetSpeedTwitterBot class
internet_speed_bot = InternetSpeedTwitterBot()

# Call the two methods in order
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()