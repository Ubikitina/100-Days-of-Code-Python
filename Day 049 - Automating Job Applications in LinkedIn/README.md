# Day 49: Automated Job Applications on LinkedIn

## Overview

On Day 49 of learning Python, I focused on automating the process of applying for jobs on LinkedIn using Selenium. This was achieved by creating two scripts: `apply-all.py` and `apply-one.py`. These scripts help in automating the application process for jobs that have a simple one-step application procedure, which significantly reduces the time and effort required to apply for multiple jobs.

## Files Created

### `apply-all.py`

This script is designed to apply for all job listings on a LinkedIn search results page that allows for simple, one-step applications.

- **Key Features**:
  - **Automatic Job Application**: It identifies and clicks the "Apply" button for each job listing, enters the phone number if required, and submits the application.
  - **Captcha Handling**: It pauses to allow manual captcha solving if prompted.
  - **Skip Complex Applications**: The script identifies complex application processes (multiple steps) and skips them.
  - **Abort Functionality**: If the job application process is complex or fails at any point, the script can abort and move on to the next listing.

- **Script Flow**:
  1. Set up and configure the Chrome WebDriver.
  2. Navigate to LinkedIn and sign in using provided credentials.
  3. Loop through all job offers on the search results page, attempting to apply to each one.
  4. Close the browser after all applications are processed.

### `apply-one.py`

This script is tailored to apply to a single, specific job listing on LinkedIn.

- **Key Features**:
  - **Targeted Job Application**: The script specifically selects a job listing with a straightforward application process.
  - **Automatic Job Application**: It automates the process of clicking the "Apply" button, entering the phone number, and submitting the application.
  - **Captcha Handling**: As with `apply-all.py`, this script pauses to allow manual captcha solving if needed.

- **Script Flow**:
  1. Set up and configure the Chrome WebDriver.
  2. Navigate to LinkedIn and sign in using provided credentials.
  3. Locate and open the targeted job listing.
  4. Apply to the job by entering the phone number and submitting the application.

## Usage Instructions

### Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Selenium**: Install Selenium using pip (`pip install selenium`).
- **ChromeDriver**: Download and install ChromeDriver that matches your version of Chrome.

### Running the Scripts

1. **Edit the Scripts**:
   - Replace `"enter your email here"`, `"enter your password here"`, and `"enter your phone number here"` with your actual LinkedIn credentials and phone number.

2. **Execute the Scripts**:
   - To apply to all jobs on a search results page, run `apply-all.py`:
     ```bash
     python apply-all.py
     ```
   - To apply to a specific job, run `apply-one.py`:
     ```bash
     python apply-one.py
     ```

3. **Captcha Handling**:
   - If prompted with a CAPTCHA, solve it manually and press Enter to continue.

### Important Notes

- **Browser Options**: The scripts are configured to keep the Chrome browser open after execution. This can be helpful for debugging or if you want to manually inspect the process.
- **LinkedIn Policies**: Be mindful of LinkedIn's terms of service. Automating actions on the platform could potentially violate these terms, so use these scripts responsibly.
