# This solution is the same as main.py, however, it is improved not to be dependant on the name of the items
# used for the upgrade.
# Sourcec code used to develop this improved solution: https://gist.github.com/TheMuellenator/e131152b991844bb8fae5581c9a8c94e

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

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)

# Set a timeout of 5 seconds from now
timeout_to_upgrade = time.time() + 5

# End of the game after 5 minutes
timeout_to_end_game = time.time() + 60*5

# Click on the cookie
while True:
    cookie.click()

    # Check if 5 seconds timeout has completed
    if time.time() > timeout_to_upgrade:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade only if affordable_upgrades is not empty
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            # print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Set another timeout for the next round
        timeout = time.time() + 5

    # Check if 5 minutes timeout has completed to end the game
    if time.time() > timeout_to_end_game:
        score = driver.find_element(By.ID, value="cps").text.split(": ")[1]
        print(f"Game ended with {score} cookies/second score.")
        break