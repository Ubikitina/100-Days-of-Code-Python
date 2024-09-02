# Day 51: Internet Speed Twitter Complaint Bot

## Overview

On Day 51 of learning Python, I developed an Internet Speed Twitter Complaint Bot. This script automates the process of checking your internet speed and tweeting a complaint to your internet service provider (ISP) if the speed falls below the promised rate. The project uses Selenium for web automation, interacting with both a speed test website and Twitter.

## File Created

### `internet-speed-twitter-bot.py`

This script automates two key tasks:

1. **Internet Speed Check**: It navigates to a speed test website, measures the download and upload speeds, and stores the results.
2. **Twitter Complaint**: If the measured speeds are below the promised levels, it logs into Twitter and posts a complaint tweet to the ISP.

#### Key Features:
- **Automated Internet Speed Test**: Uses Selenium to interact with [Speedtest.net](https://www.speedtest.net/) and extract the download and upload speeds.
- **Automated Twitter Login**: Logs into Twitter using Selenium, which allows for posting tweets programmatically.
- **Conditional Complaint Tweet**: Tweets a complaint to the ISP if the internet speed is below the promised levels.

#### Script Flow:
1. **Initialize the Bot**:
   - Sets up the Chrome WebDriver with options to keep the browser open after script execution.
   - Initializes properties to store download and upload speeds.

2. **Get Internet Speed** (`get_internet_speed` method):
   - Navigates to Speedtest.net.
   - Handles cookies and pop-ups.
   - Starts the speed test and waits for the results.
   - Extracts the download and upload speeds from the test results.

3. **Tweet at Provider** (`tweet_at_provider` method):
   - If the download or upload speed is below the promised rate, a complaint tweet is composed.
   - Logs into Twitter and posts the tweet.

#### Usage:
1. **Set Up Credentials**:
   - Replace `"ENTER YOUR USERNAME"` and `"ENTER YOUR PASSWORD"` with your Twitter username and password.
   - Update `PROMISED_DOWN` and `PROMISED_UP` with the promised download and upload speeds from your ISP.

2. **Run the Script**:
   ```bash
   python internet-speed-twitter-bot.py
   ```
   - The script will automatically check your internet speed and tweet a complaint if the speed is below the expected rate.

3. **Manual CAPTCHA Handling**:
   - If Twitter prompts for CAPTCHA during login, manual intervention may be required to solve it.

#### Example Tweet:
If the actual speeds are lower than the promised speeds, the bot will tweet something like:
```
Hey Internet Provider, why is my internet speed 85.4 down / 23.7 up when I pay for 100 down / 100 up?
```

## Important Notes:
- **WebDriver Requirements**: Ensure that the Chrome WebDriver is installed and correctly set up on your system.
- **Twitter API Alternative**: Due to recent changes in Twitter's API policies, this script uses Selenium for web automation instead of direct API calls.
- **Ethical Considerations**: Automating complaints should be done responsibly. Ensure that you use such scripts in accordance with Twitter's and your ISP's terms of service.
