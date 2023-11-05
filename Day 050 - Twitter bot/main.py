# This Python script utilizes the Selenium web automation framework to simulate the process of logging into a Twitter
# account and posting a tweet automatically.
#
# This could also be done using the Twitter API. However, due to recent changes within the company, API usage has been
# restricted, and I wanted to see if I could achieve the same results using Selenium. The conclusion is that it is
# indeed possible.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the Twitter URL, username, and password as constants
TWITTER_URL = "https://twitter.com/"
USERNAME = "ENTER YOUR USERNAME"
PASSWORD = "ENTER YOUR PASSWORD"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(TWITTER_URL)

time.sleep(2)

# --------------------------------------------------------
# Sign in
# --------------------------------------------------------
# Find and click the accept cookies button
accept_cookies = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
accept_cookies.click()

# Find and click the sign in button
sign_in_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
sign_in_button.click()

# Pausing the script for 2 seconds until the page loads
time.sleep(2)

# Fill in the login form
user_form = driver.find_element(By.CSS_SELECTOR, 'div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu')  # Find username field
user_form.click()  # Enable the form
user_form_input = driver.find_element(By.CSS_SELECTOR, "input")  # Find the input element
user_form_input.send_keys(USERNAME)  # Enter the username

# Find and click next button
next_button = driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-1m3jxhj.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
next_button.click()

# Pausing the script for 2 seconds until the page loads
time.sleep(2)

# Fill in the password form
password_form_input = driver.find_element(By.CSS_SELECTOR, "input")  # Search the password form element
password_form_input.send_keys(PASSWORD)  # Enter the password

# Find and click the login button
log_in_button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')  # Search log in button
log_in_button.click()  # Click the button

# --------------------------------------------------------
# Write and post a tweet
# --------------------------------------------------------
# Fill in the tweet form
tweet_form = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
tweet_form.click()  # Enable the form
tweet_form_input = driver.find_element(By.CSS_SELECTOR, "input")  # Search the input element
tweet_form_input.send_keys("Hey this is a Tweet")

# Find and click the post button
post_button = driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')
post_button.click()