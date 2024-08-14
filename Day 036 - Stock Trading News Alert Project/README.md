# Day 36: Stock Trading News Alert

## Overview
On Day 36, I created a Stock Trading News Alert system that checks for significant stock price changes and sends relevant news updates via SMS. This project integrates with the Alpha Vantage API for stock data and the News API for recent news articles. The Twilio API is used to send SMS alerts to a specified phone number.

## Files and Structure

### `main.py`
- **Description:** This script monitors the stock price of a specific company (Tesla Inc) and sends SMS alerts with the latest news if there is a significant change in the stock price.

- **Key Features:**
  - **Stock Price Monitoring:**
    - Retrieves daily stock prices for Tesla Inc (TSLA) from the Alpha Vantage API.
    - Calculates the percentage change in the closing price between the last two trading days.
  - **Threshold Check:**
    - If the percentage change in stock price is greater than 1%, the script fetches news articles related to the company.
  - **News Retrieval:**
    - Uses the News API to fetch the latest news articles about Tesla Inc.
    - Formats the top 3 articles into a readable format for SMS notifications.
  - **SMS Alerts:**
    - Sends SMS alerts with the stock price change percentage and news articles using the Twilio API.

- **How to Use:**
  1. **API Key and Token Setup:** Replace the placeholder values for `STOCK_API_KEY`, `NEWS_API_KEY`, `TWILIO_ACCOUNT_SID`, and `TWILIO_AUTH_TOKEN` with your actual API keys and Twilio credentials.
  2. **Run the Script:** Execute `main.py` to check the stock price and send SMS alerts if significant changes are detected.
  3. **Environment Variables:** For security, it's recommended to use environment variables to store sensitive data. Set up environment variables for API keys and Twilio credentials.

- **Example Output:**
  - If there is a significant stock price change, the script sends an SMS with a format similar to the following:
    ```
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    ```

## Notes
- **API Usage:**
  - The Alpha Vantage API and News API both have rate limits. Ensure you adhere to their usage policies to avoid any interruptions.
- **Twilio Trial Account:**
  - If using a Twilio trial account, ensure the recipient phone number is listed in the Verified Caller IDs list.
