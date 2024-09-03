# Day 53: Web Scraping Capstone Project - Data Entry Job Automation

## Overview

On Day 53 of learning Python, I developed a Web Scraping Capstone project aimed at automating data entry tasks. This project involves scraping rental property listings from a Zillow clone website and automating the process of entering that data into a Google Form. The automation is implemented using both BeautifulSoup (for web scraping) and Selenium (for form filling).

## Files Created

### `main.py`

This script performs the following tasks:

1. **Web Scraping**:
   - Scrapes property listings (URLs, prices, and addresses) from the Zillow Clone website.
   - Extracts relevant data using BeautifulSoup.

2. **Data Entry Automation**:
   - Automates the process of entering the scraped data into a Google Form using Selenium.
   - Fills out the form fields with the scraped data (address, price, and URL) and submits the form.

### `Responses_Generated_in_Google_Drive.xlsx`

- **Purpose**: This file stores the responses that were automatically submitted to the Google Form. Each entry in this file corresponds to a rental listing scraped from the Zillow Clone website.

## Script Breakdown

### 1. Web Scraping with BeautifulSoup

- **Target Website**: Zillow Clone URL (`https://appbrewery.github.io/Zillow-Clone/`)
- **Libraries Used**: `requests`, `BeautifulSoup` from `bs4`
  
#### Steps:
1. **Send HTTP GET Request**: The script sends a GET request to the Zillow Clone website to retrieve the HTML content.
2. **Parse HTML**: BeautifulSoup is used to parse the HTML and locate rental property listings.
3. **Extract Data**: 
   - **URLs**: Extracted from the `href` attribute of the property listing links.
   - **Prices**: Extracted from the specified span class within each property listing.
   - **Addresses**: Extracted from the `address` tag within each property listing.

### 2. Data Entry Automation with Selenium

- **Target Platform**: Google Form (URL to be provided by the user)
- **Libraries Used**: `selenium` (WebDriver, By)

#### Steps:
1. **Setup Selenium WebDriver**: Configures the Chrome WebDriver to keep the browser open after execution.
2. **Loop Through Scraped Data**: For each rental property:
   - **Open Google Form**: Navigates to the Google Form URL.
   - **Fill Form Fields**: Enters the scraped address, price, and URL into the appropriate form fields.
   - **Submit Form**: Automatically submits the form.
3. **Repeat**: The process repeats for each rental listing, filling out and submitting the form until all data has been entered.

### Example Usage

1. **Update URLs**:
   - Replace `"ENTER YOUR FORM URL HERE"` in the `GOOGLE_FORM_URL` variable with your Google Form URL.
   
2. **Run the Script**:
   ```bash
   python main.py
   ```
   - The script will scrape the rental listings and automatically fill out and submit the Google Form for each listing.

3. **View Results**:
   - The form responses are collected in a Google Sheet, which can be downloaded as an Excel file (`Responses_Generated_in_Google_Drive.xlsx`).

## Important Notes:

- **WebDriver Requirements**: Ensure that Chrome WebDriver is installed and configured correctly on your system.
- **Google Form Fields**: The form fields' XPaths in the script need to match the fields in your Google Form. Ensure the XPaths used in the script correspond to your form structure.
- **Usage Limitations**: This script is intended for educational purposes. Ensure that any data scraping or form submission complies with the respective website’s terms of service.
- **Network Reliability**: Internet connection stability is crucial as the script involves live interactions with web pages.
