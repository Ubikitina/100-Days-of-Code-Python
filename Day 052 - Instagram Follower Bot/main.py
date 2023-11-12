from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Set the Instagram URL, username, and password as constants
INSTAGRAM_URL = "https://www.instagram.com/"
USERNAME = "ENTER YOUR USERNAME"
PASSWORD = "ENTER YOUR PASSWORD"


class InstaFollower:
    def __init__(self):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
        chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

        # Create a Chrome web driver instance with the specified options.
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        # Open the specified URL in the Chrome browser.
        self.driver.get(INSTAGRAM_URL)
        time.sleep(2)

        # Find and click the accept cookies button
        accept_cookies = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        accept_cookies.click()

        # Enter username and password and login
        user_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')  # Find the input element
        user_input.send_keys(USERNAME)  # Enter the username
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')  # Search the password form element
        password_input.send_keys(PASSWORD)  # Enter the password
        password_input.send_keys(Keys.ENTER)  # Click enter to log in
        time.sleep(3)

    def find_followers(self):
        # Open the profile you want to copy the followers from. In this case, we will select the "following" list instead of "followers", but it should work with any of them.
        self.driver.get("https://www.instagram.com/c.tangana/following/")
        time.sleep(4)

        # Follow all of them
        while True:
            time.sleep(1)
            # Instead of scrolling down, we will use a TAB key and switch between elements till 'Follow' name found,
            # when found just click on it and keep to the next followers.
            element = self.driver.switch_to.active_element  # Search the active element
            try:
                if element.text == 'Follow':  # If the text of the element is "Follow"
                    element.click()  # Then, click on it
                    print("Clicking on Follow")
                element.send_keys(Keys.TAB)  # Press the tab to go to the next active element
            except ElementNotInteractableException:  # We will skip any of the exceptions
                continue
            except ElementClickInterceptedException:
                continue


# Create an instance of the bot class
bot = InstaFollower()

# Call the methods in order
bot.login()
bot.find_followers()