# Day 38: Workout Tracking with Google Sheets

## Overview
On Day 38, I developed a workout tracking system that integrates with Google Sheets using the Nutritionix API for exercise data and Sheety API to update a Google Sheet. This project allows users to log their workouts and track exercise metrics conveniently.

## Files and Structure

### `main.py`
- **Description:** This script captures workout details from the user, retrieves exercise data from the Nutritionix API, and logs it into a Google Sheet via the Sheety API.

- **Sections:**
  - **Section 1: Nutritionix API Call**
    - **Purpose:** Retrieve exercise details and metrics based on user input.
    - **Details:** Sends a POST request to the Nutritionix API with exercise data and user specifics.
    - **Endpoint:** `https://trackapi.nutritionix.com/v2/natural/exercise`
    - **Parameters:**
      - `query`: User input describing the exercises
      - `gender`, `weight_kg`, `height_cm`, `age`: User-specific details
    - **Authentication:** Header-based (`x-app-id`, `x-app-key`)
    - **Response:** Contains exercise name, duration, and calories burned.

  - **Section 2: Sheety API Call**
    - **Purpose:** Log exercise data into a Google Sheet.
    - **Details:** Sends a POST request to the Sheety API to add a new row with exercise data.
    - **Endpoint:** Defined in `SHEET_ENDPOINT` environment variable
    - **Parameters:**
      - `date`: Current date
      - `time`: Current time
      - `exercise`: Name of the exercise
      - `duration`: Duration of the exercise in minutes
      - `calories`: Calories burned during the exercise
    - **Authentication:** Header-based (`Authorization`)

## How to Use
  1. **Setup:**
     - Replace placeholder values in the script with your actual credentials.
     - Set environment variables for `APP_ID`, `API_KEY`, `SHEETY_AUTH`, and `SHEET_ENDPOINT`.
  2. **Run the Script:**
     - Execute `main.py`.
     - Input the exercises you performed when prompted.
  3. **Check Your Google Sheet:**
     - Verify that the data is correctly logged into your specified Google Sheet.

- **Example Interaction:**
  ```
  Tell me which exercises you did: Running 30 minutes, Cycling 45 minutes
  ```

  - **Expected Output in Google Sheets:**
    
    | Date       | Time     | Exercise | Duration | Calories |
    |------------|----------|----------|----------|----------|
    | 14/08/2024 | 16:49:43 | Running  | 30       | 300      |
    | 14/08/2024 | 16:49:43 | Cycling  | 45       | 400      |
   

## Notes
- **API Keys and Authentication:** Ensure your API keys and tokens are stored securely and are not hardcoded in the script for production use.
- **Error Handling:** The script includes basic error handling using `response.raise_for_status()` to catch and raise exceptions for unsuccessful requests.
