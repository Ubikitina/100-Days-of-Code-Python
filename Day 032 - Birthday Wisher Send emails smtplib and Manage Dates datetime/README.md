# Day 32: Sending Emails with Python (Birthday Wisher & Motivational Quotes)

## Overview
On Day 32 of learning Python, I explored how to send emails using the `smtplib` library and how to manage dates using the `datetime` module. This day culminated in the creation of two projects:
1. **Birthday Wisher**: Automatically sends birthday emails to people on their special day.
2. **Sending Motivational Quotes**: Sends a random motivational quote every Sunday.

## Files and Structure

### Project Structure
```
📁 Day 32 Projects
├── 📄 playground.py
├── 📁 Birthday_wisher
│   ├── 📄 birthdays.csv
│   ├── 📄 main.py
│   └── 📁 letter_templates
│       ├── 📄 letter_1.txt
│       ├── 📄 letter_2.txt
│       └── 📄 letter_3.txt
└── 📁 Sending_motivational_quotes
    ├── 📄 main.py
    └── 📄 quotes.txt
```

### `playground.py`
- **Description:**
  - A script to experiment with sending emails using `smtplib` and handling dates with `datetime`.
  - The commented-out code shows how to send a simple email, while the active code demonstrates extracting and printing various date components such as the current year, month, and day of the week.
  - Also includes an example of creating a `datetime` object for a specific date.

### Birthday Wisher
#### Files:
- **`birthdays.csv`**: A CSV file containing names, email addresses, and birth dates of people to whom birthday emails will be sent.


- **`main.py`**
  - **Description:**
    - The main script that reads the birthday information from `birthdays.csv` and sends a personalized birthday email if today matches any of the birth dates.
    - Uses the `smtplib` library to send the email and `pandas` to handle the CSV data.
    - The email content is randomly selected from one of three templates in the `letter_templates` folder.
  
  - **Key Functions:**
    - **Reading Birthdays**: Loads birthday data and checks if today matches any birthday.
    - **Sending Emails**: Sends an email using a randomly chosen letter template with the person's name inserted.

- **`letter_templates/`**
  - A folder containing text files used as templates for birthday emails.
  - **Example Template (`letter_1.txt`):**
    ```
    Dear [NAME],

    Happy birthday!

    All the best for the year!

    Angela
    ```

### Sending Motivational Quotes
#### Files:
- **`main.py`**
  - **Description:**
    - A script that sends a random motivational quote every Sunday.
    - The script checks the current day of the week, and if it’s Sunday, it picks a random quote from `quotes.txt` and sends it via email using `smtplib`.

  - **Key Functions:**
    - **Sending Quotes**: Selects a random quote and sends it if the current day is Sunday.

- **`quotes.txt`**
  - A text file containing a list of motivational quotes, each on a new line.
  - **Example Content:**
    ```
    "When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love..."  - Marcus Aurelius
    "Either you run the day or the day runs you." - Jim Rohn
    ```

## How to Use

### 1. **Setting Up Email Credentials**
   - For both projects, you need to replace the placeholder `"ADD_HERE_THE_PASSWORD"` in the `main.py` scripts with your actual email password.
   - Be cautious with handling credentials. Consider using environment variables or secure storage for your passwords.

### 2. **Running the Birthday Wisher**
   - Ensure that the `birthdays.csv` file is populated with relevant data.
   - Execute `main.py` within the `Birthday_wisher` folder. If today matches any birthday in the CSV, an email will be sent automatically.

### 3. **Running the Motivational Quotes Sender**
   - Make sure `quotes.txt` contains the motivational quotes you wish to send.
   - Execute `main.py` within the `Sending_motivational_quotes` folder on a Sunday to send a motivational quote.

### 4. **Testing and Customization**
   - You can test these scripts by temporarily modifying the date checks or adding print statements.
   - Customize the email templates and quotes to match your preferences.
