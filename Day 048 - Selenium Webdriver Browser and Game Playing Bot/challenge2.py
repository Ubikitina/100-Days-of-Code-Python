from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(WIKIPEDIA_URL)

# --------------------------------------------------------
# How to click on a element - Option 1
# --------------------------------------------------------

# Find elements by id
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Let's click on the count
article_count.click()

# --------------------------------------------------------
# How to click on a element - Option 2
# --------------------------------------------------------
driver.get(WIKIPEDIA_URL) # Let's go back to the main page

# This time we will search by using the text in the hyperlink
all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
all_portals.click()

# --------------------------------------------------------
# Using the search bar
# --------------------------------------------------------
driver.get(WIKIPEDIA_URL) # Let's go back to the main page

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)  # This will type Python in the search bar and then will press the enter button


# driver.quit()  # Closes the entire Chrome program, all the tabs