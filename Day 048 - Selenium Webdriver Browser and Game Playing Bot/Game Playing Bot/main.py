from selenium import webdriver
from selenium.webdriver.common.by import By
import time

COOKIE_GAME_URL = "https://orteil.dashnet.org/experiments/cookie/"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(COOKIE_GAME_URL)

# --------------------------------------------------------
# Search the cookie and click on it
# --------------------------------------------------------
# Find the cookie element on the screen
cookie = driver.find_element(By.ID, value="cookie")

# Set a timeout of 10 seconds from now
timeout_to_upgrade = time.time() + 5

# End of the game after 5 minutes
timeout_to_end_game = time.time() + 60*5

# Click on the cookie
while True:
    cookie.click()

    # Check if 5 seconds timeout has completed
    if time.time() > timeout_to_upgrade:
        # Select the price to buy. We will always buy the most expensive one.
        if driver.find_element(By.ID, value="buyTime machine").get_attribute("class") == "":  # Check if the time machine is available to buy. When it is available to buy, its class is empty. If not, then the class is "grayed".
            driver.find_element(By.ID, value="buyTime machine").click()
        elif driver.find_element(By.ID, value="buyPortal").get_attribute("class") == "":  # Same for the portal
            driver.find_element(By.ID, value="buyPortal").click()
        elif driver.find_element(By.ID, value="buyAlchemy lab").get_attribute("class") == "":  # Same for the alchemy lab
            driver.find_element(By.ID, value="buyAlchemy lab").click()
        elif driver.find_element(By.ID, value="buyShipment").get_attribute("class") == "":  # Same for the shipment
            driver.find_element(By.ID, value="buyShipment").click()
        elif driver.find_element(By.ID, value="buyMine").get_attribute("class") == "":  # Same for the mine
            driver.find_element(By.ID, value="buyMine").click()
        elif driver.find_element(By.ID, value="buyFactory").get_attribute("class") == "":  # Same for the factory
            driver.find_element(By.ID, value="buyFactory").click()
        elif driver.find_element(By.ID, value="buyGrandma").get_attribute("class") == "":  # Same for the grandma
            driver.find_element(By.ID, value="buyGrandma").click()
        elif driver.find_element(By.ID, value="buyCursor").get_attribute("class") == "":  # Same for the cursor
            driver.find_element(By.ID, value="buyCursor").click()

        timeout_to_upgrade = time.time() + 5  # Set another timeout for the next round

    # Check if 5 minutes timeout has completed to end the game
    if time.time() > timeout_to_end_game:
        score = driver.find_element(By.ID, value="cps").text.split(": ")[1]
        print(f"Game ended with {score} cookies/second score.")
        break


driver.quit()  # Closes the entire Chrome program, all the tabs