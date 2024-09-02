# Day 50: Twitter Bot and Alternative Project

## Overview

On Day 50 of learning Python, I developed a Twitter Bot using Selenium to automate the process of logging into Twitter and posting a tweet. This was an alternative to a previously planned Tinder Bot project, which I decided not to pursue. Both projects are included in this folder, showcasing different web automation techniques using Python and Selenium.

## Files Created

### `main.py` (Twitter Bot)

This script automates the process of logging into Twitter and posting a tweet using Selenium.

- **Key Features**:
  - **Twitter Login**: Automates the process of logging into a Twitter account.
  - **Post a Tweet**: After logging in, the script posts a predefined tweet.
  - **Captcha Handling**: While the script can navigate the login process, manual intervention may be required if Twitter prompts for a CAPTCHA.

- **Script Flow**:
  1. **Setup**: Configures the Chrome WebDriver with options to keep the browser open after execution.
  2. **Navigation**: Opens Twitter in a Chrome browser and navigates through the login process.
  3. **Tweeting**: Posts a predefined tweet once logged in.

- **Usage**:
  1. Update the script with your Twitter credentials by replacing `"ENTER YOUR USERNAME"` and `"ENTER YOUR PASSWORD"` with your actual username and password.
  2. Modify the tweet content in the `tweet_form_input.send_keys("Hey this is a Tweet")` line to your desired message.
  3. Run the script:
     ```bash
     python main.py
     ```
  4. If prompted with a CAPTCHA during login, solve it manually.

### `original_project_for_day_50\main.py` (Tinder Bot)

This script was the original plan for Day 50, which automates interactions with Tinder using Selenium. However, it was not pursued, and a Twitter Bot was created instead. The script is included here for reference and learning purposes.

- **Key Features**:
  - **Facebook Login**: Automates logging into Tinder using Facebook credentials.
  - **Automated Swiping**: Simulates "liking" profiles on Tinder in a loop.
  - **Popup Handling**: Handles common popups such as "It's a Match" and permission requests.

- **Script Flow**:
  1. **Setup**: Configures the Chrome WebDriver and navigates to Tinder.
  2. **Facebook Login**: Switches to the Facebook login window, enters credentials, and logs in.
  3. **Tinder Interaction**: Handles popups and automates swiping through profiles.

- **Usage**:
  1. Update the script with your Facebook credentials by replacing `"YOUR FACEBOOK LOGIN EMAIL"` and `"YOUR FACEBOOK PASSWORD"` with your actual credentials.
  2. Set the correct path to your ChromeDriver in `chrome_driver_path`.
  3. Run the script:
     ```bash
     python main.py
     ```
  4. The script will automatically swipe right on Tinder profiles 100 times.

## Important Notes

- **WebDriver Configuration**: Both scripts use Chrome WebDriver, which must be installed and properly configured on your system.
- **Ethical Considerations**: Automating interactions on social media platforms should be done responsibly and within the bounds of the platform’s terms of service.
- **Learning Outcome**: These projects demonstrate how to use Python and Selenium for web automation, which can be extended to other web tasks beyond social media.
