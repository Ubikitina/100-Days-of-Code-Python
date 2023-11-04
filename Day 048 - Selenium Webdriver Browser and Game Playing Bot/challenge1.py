from selenium import webdriver
from selenium.webdriver.common.by import By

PYTHON_URL = "https://www.python.org/"

# --------------------------------------------------------
# Create a web driver instance
# --------------------------------------------------------

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()  # Create a 'chrome_options' object to configure Chrome driver options.
chrome_options.add_experimental_option("detach", True)  # Add an experimental option to keep the browser open after program execution.

# Create a Chrome web driver instance with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Open the specified URL in the Chrome browser.
driver.get(PYTHON_URL)

# --------------------------------------------------------
# CHALLENGE (FIRST TRIAL): Extract the upcoming events data
# --------------------------------------------------------

# Find elements by using XPath
time_elements = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')  # By inspecting the element in Chrome, we can right click and copy its XPath
# print(time_elements.text)

# Split the elements found
lines = time_elements.text.strip().split('\n')
# Create a dictionary that will store the formatted data
event_dict = {}

# Organize the data in dictionaries and add them to event_dict
for i in range(0, len(lines), 2):
    date = lines[i]
    event = lines[i + 1]

    event_dict[i] = {
        "date": date,
        "event": event
    }

# print(event_dict)

# --------------------------------------------------------
# CHALLENGE (SOLUTION): Extract the upcoming events data
# --------------------------------------------------------

# We will use find_elements to find more than one element. In addition, we will use the class name "event-widget" and inside this class, search for a "time" tag.
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")  # Return the list of event times

# This time we will also use the class name "event-widget" and inside this class, search for a li element, and inside it, search for a a element
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Create a dictionary that will store the formatted data
event_dict = {}

# Include content to this dictionary
for i in range(len(event_times)):
    # Create the dictionary
    event_dict[i] = {
        "time": event_times[i].text,
        "name": event_titles[i].text
    }

print(event_dict)




driver.quit()  # Closes the entire Chrome program, all the tabs