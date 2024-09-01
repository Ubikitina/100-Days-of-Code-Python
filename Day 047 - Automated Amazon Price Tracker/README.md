# Day 47: Automated Amazon Price Tracker

## Overview

On Day 47 of learning Python, I focused on creating an Automated Amazon Price Tracker. This project uses web scraping to monitor the price of a specified product on Amazon and sends an email alert when the price drops below a target value. Below are the details of the script created and the steps involved in the project.

**Keywords**: Web Scraping, BeautifulSoup, Python Automation, Price Monitoring, Email Notifications, smtplib, lxml Parser.

## Files and Purpose

### `main.py`

- **Purpose:**
  This script automates the process of tracking the price of a specific product on Amazon. If the price drops below a predefined target, the script sends an email notification.

- **Key Components:**
  - **Web Scraping:**
    - The script sends a GET request to the Amazon product page using the `requests` library, including custom headers to mimic a real browser.
    - It uses `BeautifulSoup` with the `lxml` parser to extract the product's price from the HTML content.
  
  - **Price Monitoring:**
    - The script compares the extracted price with a predefined target price (`TARGET_PRICE`).
  
  - **Email Notification:**
    - If the price is below the target, the script sends an email alert using the `smtplib` library.
    - The email includes the product name, the current price, and a link to the product page.

- **Important Variables:**
  - `PRODUCT_URL`: The Amazon product page URL you want to track.
  - `TARGET_PRICE`: The price threshold below which you want to receive an alert.
  - `MY_EMAIL` and `MY_PASSWORD`: Your email credentials used to send the alert.

- **Workflow:**
  1. **Web Request:** The script sends a GET request to the Amazon product page.
  2. **Price Extraction:** The script extracts the product's current price from the page.
  3. **Price Comparison:** The script checks if the current price is below the target price.
  4. **Email Alert:** If the price is below the target, the script sends an email with the product details.

