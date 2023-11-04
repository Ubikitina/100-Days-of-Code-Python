from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_PRODUCT_URL = "https://www.amazon.com/-/es/910-001949-Logitech-Rat%C3%B3n-inal%C3%A1mbrico-M705/dp/B003P7X38Q"
PYTHON_URL = "https://www.python.org/"


# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)


# --------------------------------------------------------
# Open Amazon and get data from a product
# --------------------------------------------------------

# Open the specified URL in the Chrome browser.
driver.get(AMAZON_PRODUCT_URL)

# Find elements by class
price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(price_euro.text)
print(price_cents.text)


# --------------------------------------------------------
# Open Python website and get the search bar
# --------------------------------------------------------

# Open the specified URL in the Chrome browser.
driver.get(PYTHON_URL)

# Find elements by name: The search bar can be found by using the name "q" in the HTML code
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)  # This prints "input" because the search bar is an input
print(search_bar.get_attribute("placeholder"))  # This prints "Search"

# Find elements by id
button = driver.find_element(By.ID, value="submit")
print(button.size)  # Prints {'height': 40, 'width': 46}

# Find elements by CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)  # Prints docs.python.org

# Find elements by using XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')  # By inspecting the element in Chrome, we can right click and copy its XPath
print(bug_link.text)  # Prints Submit Website Bug

# To find a list of elements we can use driver.find_elements instead.

# --------------------------------------------------------
# Close the tabs in Chrome
# --------------------------------------------------------

# driver.close()  # Closes the active tab. If there's only one tab, this will effectively close the entire browser

driver.quit()  # Closes the entire Chrome program, all the tabs

# --------------------------------------------------------
# Discussion: Selenium vs BeautifulSoup
# Selenium is better suited for tasks involving user interaction, dynamic web pages, and testing web applications,
# while BeautifulSoup is better for extracting data from static HTML documents efficiently.