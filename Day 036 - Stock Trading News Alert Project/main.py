import requests  # Import the 'requests' library, which allows making HTTP requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "ENTER_KEY_HERE"
NEWS_API_KEY = "ENTER_KEY_HERE"

TWILIO_ACCOUNT_SID = "ENTER_SID_HERE" # Find your Account SID and Auth Token at twilio.com/console and set the environment variables. See http://twil.io/secure
TWILIO_AUTH_TOKEN = "ENTER_TOKEN_HERE"

# Define the parameters for making the API call by using https://www.alphavantage.co/documentation/#daily
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

# Send an HTTP GET request to the specified URL and store the response in the 'response' variable
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
# Check if the response has an HTTP status code indicating an error (4xx or 5xx status codes)
response.raise_for_status()
# Extract the data in JSON format
stock_data = response.json()


# Get yesterday's closing stock price
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # Calculate yesterday's day
yesterday_closing_stock_price= float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
    # The above could also be done by using list comprehensions and selecting the first element of the list, which
    # corrsesponds to yesterday's date. Doing it this way would make our code robust to changes in the date format.
    # Hint: We can perform list comprehensions on Python dictionaries.
    # e.g. [new_value for (key, value) in dictionary.items()]


# Get the day before yesterday's closing stock price
day_before_yesterday = (datetime.date.today() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")  # Calculate day before yesterday
day_bf_yestrdy_closing_stock_price= float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_prize_difference = abs(yesterday_closing_stock_price-day_bf_yestrdy_closing_stock_price)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (positive_prize_difference / day_bf_yestrdy_closing_stock_price) * 100

# If the stock price difference percentage is greater than 5 then print("Get News") to see why.
if percentage_difference > 1:

    # Define the parameters for making the API call by using https://newsapi.org/docs/endpoints/everything
    parameters = {
        "qinTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    # Make the API call and get the data
    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    news_data = response.json()
    first_three_news = news_data["articles"][:3]  # Get only the first 3 news out of the data by using Python slice operator https://stackoverflow.com/questions/509211/understanding-slice-notation

    # Create a list of articles with the first 3 news pieces of news for the COMPANY_NAME, formatted in a readable way.
    news_formatted = [f"Headline: {item['title']}\nBrief: {item['description']}" for item in first_three_news]  # The list has been created by using list comprehension

    # Send each article as a separate message via Twilio twilio.com/docs/sms/quickstart/python
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # Create the client to send the SMS using twilio

    for item in news_formatted:
        if yesterday_closing_stock_price > day_bf_yestrdy_closing_stock_price:
            text_to_send = STOCK_NAME + ": " + "+" + f"{percentage_difference:.1f}%\n" + item  # We add the headline of "TSLA: +1.6%"
        else:
            text_to_send = STOCK_NAME + ": " + "-" + f"{percentage_difference:.1f}%\n" + item  # We add the headline of "TSLA: -1.6%"

        # Create the SMS message
        message = client.messages \
            .create(
            body=text_to_send,
            from_='+12054306870',  # Paste here the trial number
            to='+123456789'  # Phone number used to sign up in twilio, as we are using the free trial service, this phone number must be listed in the Verified Caller IDs list.
        )
        # Check SMS sending status
        print(message.status)



# The format the message will look like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

