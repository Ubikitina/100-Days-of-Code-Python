# The original proposal for day 50 was to create the below Tinder bot. However, I didn't want to pursue this project,
# so I've opted for an alternative one that interacts with Twitter instead. Nevertheless, I'm leaving here the code
# for the proposed solution with line-by-line comments explaining what it does.
# The original code can be found in https://gist.github.com/angelabauer/5c47e3b2d3f8d6a80c8c92d2892774be

# Importing the necessary modules from the Selenium and time libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Setting your Facebook login email and password
FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"

# Setting the path to your Chrome WebDriver executable
chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Opening the Tinder website in a new Chrome window
driver.get("http://www.tinder.com")

# Pausing the script for 2 seconds until the page loads
sleep(2)

# Finding the login button on the Tinder website and clicking it
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

# Pausing the script for 2 seconds until the page loads
sleep(2)

# Finding the Facebook login button in the Tinder login modal and clicking it
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# Pausing the script for 2 seconds until the page loads
sleep(2)

# Storing the current window handle (main Tinder window)
base_window = driver.window_handles[0]

# Switching to the newly opened Facebook login window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)  # Printing the title of the Facebook login window

# Finding the email and password fields in the Facebook login window
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

# Entering your Facebook login email and password
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)  # Simulating pressing the Enter key to submit the login form

# Switching back to the main Tinder window
driver.switch_to.window(base_window)
print(driver.title)  # Printing the title of the main Tinder window

# Pausing the script for 5 seconds until the page loads
sleep(5)

# Finding and clicking on the "Allow Location" button and notifications button in the Tinder modal
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Finding and clicking on the "Cookies" button
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Looping 100 times to simulate "liking" profiles on Tinder
for n in range(100):
    sleep(1)  # Pausing the script for 1 second until the page loads
    try:
        # Finding and clicking on the "Like" button
        # print("called")  # Debug
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            # Handling the "It's a Match" popup if it appears
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            # If no match or popup, element won't be found. Then, pause for 2 seconds until the page loads.
            sleep(2)

# Quitting the Chrome WebDriver, closing the browser (all tabs)
driver.quit()