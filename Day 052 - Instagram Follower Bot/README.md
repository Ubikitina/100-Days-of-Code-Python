# Day 52: Instagram Follower Bot

## Overview

On Day 52 of learning Python, I developed an Instagram Follower Bot using Selenium. This bot automates the process of following users on Instagram by navigating to a specific profile and following the accounts they are following. The primary use case for this bot is to grow your Instagram followers by engaging with users who follow similar accounts.

## File Created

### `main.py`

#### Key Features:
- **Automated Instagram Login**: Uses Selenium to log into Instagram using a specified username and password.
- **Follower Automation**: Automates the process of following users by navigating through the "Following" list of a specified Instagram profile.

#### Script Flow:
1. **Initialize the Bot**:
   - Sets up the Chrome WebDriver with options to keep the browser open after the script execution.
   
2. **Login to Instagram** (`login` method):
   - Navigates to Instagram's login page.
   - Handles cookies pop-up.
   - Enters the username and password and logs into the account.

3. **Find and Follow Users** (`find_followers` method):
   - Navigates to the "Following" list of a specified Instagram profile.
   - Iteratively finds and clicks on the "Follow" buttons to follow each user.
   - Uses the TAB key to navigate between elements and detect the "Follow" buttons.

#### Usage:
1. **Set Up Credentials**:
   - Replace `"ENTER YOUR USERNAME"` and `"ENTER YOUR PASSWORD"` with your Instagram username and password.

2. **Specify Target Profile**:
   - Update the profile URL in the `find_followers` method with the profile whose followers you want to follow. The current script targets the "Following" list of the user `c.tangana`.

3. **Run the Script**:
   ```bash
   python main.py
   ```
   - The bot will log into your Instagram account and start following users from the specified profile's "Following" list.

4. **Manual CAPTCHA Handling**:
   - If Instagram prompts for CAPTCHA during login, manual intervention may be required to solve it.

#### Example Usage:
The bot will navigate to the "Following" list of the Instagram profile specified (e.g., `c.tangana/following/`) and will automatically start following each user in that list by clicking the "Follow" button.

## Important Notes:
- **WebDriver Requirements**: Ensure that the Chrome WebDriver is installed and correctly set up on your system.
- **Instagram's Terms of Service**: Use this bot responsibly and in compliance with Instagram’s terms of service. Excessive or inappropriate use may result in your account being flagged or banned.
- **Ethical Considerations**: Automated following can be seen as spammy behavior. It's important to use such scripts responsibly to avoid negative impacts on the Instagram community.
