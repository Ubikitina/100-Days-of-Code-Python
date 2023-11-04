from selenium import webdriver
from selenium.webdriver.common.by import By

NEWSLETTER_URL = "http://secure-retreat-92358.herokuapp.com/"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(NEWSLETTER_URL)

# --------------------------------------------------------
# Fill in the form
# --------------------------------------------------------
first_name_field = driver.find_element(By.NAME, "fName")  # Find the first name field
first_name_field.send_keys("Maialen")  # This will type in the form

last_name_field = driver.find_element(By.NAME, "lName")  # Find the last name field
last_name_field.send_keys("Example Last Name")  # This will type in the form

email_field = driver.find_element(By.NAME, "email")  # Find the last name field
email_field.send_keys("test@test.com")  # This will type in the form

# --------------------------------------------------------
# Click on the Sign Up button
# --------------------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "form button")  # The button is inside the form
button.click()



# driver.quit()  # Closes the entire Chrome program, all the tabs