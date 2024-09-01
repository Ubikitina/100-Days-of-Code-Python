# Day 47: Selenium WebDriver and Game Playing Bot

## Overview

On Day 47, I focused on learning how to use Selenium WebDriver, a powerful tool for automating web browsers. Selenium is often used for testing web applications, web scraping, and automating repetitive tasks on the web. I practiced with various challenges and eventually created a bot to play an online game.

### Files Created

- **challenge1.py**: Extracting upcoming events data from the Python.org website.
- **challenge2.py**: Interacting with Wikipedia's main page, including clicking links and using the search bar.
- **challenge3.py**: Filling out and submitting a form on a sample newsletter website.
- **playground.py**: A playground for experimenting with Selenium, extracting data from Amazon and Python.org.
- **Game Playing Bot**
  - **main.py**: A bot that plays the Cookie Clicker game, purchasing upgrades automatically.
  - **main-improved.py**: An improved version of the Cookie Clicker bot, which dynamically selects upgrades based on affordability rather than specific names.

## Learning Outcomes

- **Selenium WebDriver Basics**: Learned how to create and manage WebDriver instances, interact with web elements, and automate browser actions.
- **Web Scraping with Selenium**: Extracted information from websites using various methods like CSS selectors, XPath, and element attributes.
- **Automating User Actions**: Automated clicks, form submissions, and navigation on web pages.
- **Game Automation**: Applied the knowledge to automate gameplay in a simple online game, including strategic purchase decisions for in-game upgrades.

## File Descriptions

### 1. challenge1.py
- **Purpose**: Extract upcoming events data from the Python.org website.
- **Key Concepts**: Using Selenium with XPath and CSS Selectors to scrape and organize data.

### 2. challenge2.py
- **Purpose**: Interact with elements on Wikipedia, including clicking links and performing searches.
- **Key Concepts**: Automating clicks on elements by ID, CSS selectors, and link text; using the search bar.

### 3. challenge3.py
- **Purpose**: Fill out and submit a form on a mock newsletter website.
- **Key Concepts**: Locating form fields by name, automating text input, and clicking submission buttons.

### 4. playground.py
- **Purpose**: Experiment with Selenium by extracting product prices from Amazon and interacting with elements on Python.org.
- **Key Concepts**: Combining multiple Selenium skills, including scraping, form interaction, and dynamic web elements.

### 5. Game Playing Bot
#### - main.py
  - **Purpose**: Automate playing the Cookie Clicker game, clicking the cookie and purchasing upgrades.
  - **Key Concepts**: Automating repeated actions, conditional logic for upgrade purchases, and timing functions.

#### - main-improved.py
  - **Purpose**: A more advanced version of the Cookie Clicker bot that adapts to different upgrade options dynamically.
  - **Key Concepts**: Dynamic element selection based on game state, improved upgrade logic, and better performance handling.

## How to Run

1. **Install Selenium**: Ensure you have Selenium installed in your environment.
   ```bash
   pip install selenium
   ```
2. **WebDriver Setup**: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure it is in your system's PATH.

3. **Run the Scripts**: You can run each script individually using Python.
   ```bash
   python challenge1.py
   python challenge2.py
   python challenge3.py
   python playground.py
   python Game\ Playing\ Bot/main.py
   python Game\ Playing\ Bot/main-improved.py
   ```

4. **Observe the Automation**: Watch as Selenium automates your web browser according to the script instructions.
