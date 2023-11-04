from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
USERNAME = "enter your email here"
PASSWORD = "enter your password here"
PHONE_NUMBER = "enter your phone number here"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(LINKEDIN_URL)


# --------------------------------------------------------
# Sign in
# --------------------------------------------------------
# This time we will search by using the text in the hyperlink
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Fill in the login form
user = driver.find_element(By.ID, "username")  # Search username field
user.send_keys(USERNAME)  # Enter username data
password = driver.find_element(By.ID, "password")  # Search password field
password.send_keys(PASSWORD)  # Enter password data
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')  # Search sign in button
sign_in_button.click()  # Click the button

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# --------------------------------------------------------
# Apply to one job in the list
# --------------------------------------------------------
# While LinkedIn offers a straightforward 'simple application' feature, many companies supplement it with extra
# questions on the application form. These additional questions can vary in terms of quantity and content. To
# simplify our process, we'll opt for job listings that do not include these supplementary questions.
appropriate_job = driver.find_element(By.LINK_TEXT, "Distributed Systems Engineer - Rust")  # Select a job offer without the supplementary questions
appropriate_job.click()  # Open it

time.sleep(2)  # We will wait 2 secons until the page loads
application_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply")  # Find the application button
application_button.click()  # Click on it

# Fill in the phone with my phone number
phone_input = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3756191775-9-phoneNumber-nationalNumber")  # Another option could be (by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
phone_input.send_keys(PHONE_NUMBER)

# Press the send button to finalize the application
sent_button = driver.find_element(by=By.CSS_SELECTOR, value="footer .artdeco-button")
sent_button.click()