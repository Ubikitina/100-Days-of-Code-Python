from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
USERNAME = "enter your email here"
PASSWORD = "enter your password here"
PHONE_NUMBER = "enter your phone number here"

def apply_job():
    """
    Apply for a job by clicking the application button, entering a phone number, and finalizing the application.

    This function locates and clicks the application button, fills in the phone number if necessary, and completes the application process.

    Returns:
        None
    """

    application_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply")  # Find the application button
    application_button.click()  # Click on it
    print("# Application button clicked")

    # Fill in the phone with my phone number
    phone_input = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")  # Find the phone number form
    if phone_input.text == "":  # If there is no phone number entered
        phone_input.send_keys(PHONE_NUMBER)  # Enter my phone number
    print("# Phone entered")

    # Press the send button to finalize the application
    send_button = driver.find_element(by=By.CSS_SELECTOR, value="footer .artdeco-button")  # Find the send button
    if send_button.get_attribute("aria-label") == "Ir al siguiente paso":  # If there are further steps we won't continue
        abort_application()
        print("# Complex application, skipped.")
    else:
        send_button.click()
        print("# Application done")

def abort_application():
    """
    Abort the job application process by closing the application modal.

    This function locates and clicks the "Close" button to close the application modal and then clicks the "Discard" button
    to discard the application.

    Returns:
        None
    """
    # Find and click the "Close" button
    close_button = driver.find_element(By.XPATH, '//button[@aria-label="Descartar"]')
    close_button.click()
    print("# Close button clicked")

    # Find and click the "Discard" button
    discard_button = driver.find_element(by=By.CSS_SELECTOR, value="div .artdeco-modal__actionbar--confirm-dialog button")
    discard_button.click()
    print("# Discarded")


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
# Apply to all the job in the list. We're only going to apply
# to the standard, 1-step applications. All others will be ignored.
# --------------------------------------------------------
# Get all the offers in Linkedin
all_offers = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container").find_elements(By.TAG_NAME, "a")

# For each of the offers, we will try to apply
for offer in all_offers:
    offer.click()  # Click to open the offer
    time.sleep(3)  # Wait until the page loads

    # Try to apply to each of the jobs
    try:
        print(f"\n{offer.text}")
        apply_job()
    except NoSuchElementException:  # If we receive an exception, then abort the application.
        print("# Application not possible: " + offer.text)
        abort_application()


driver.quit()  # Close the browser
