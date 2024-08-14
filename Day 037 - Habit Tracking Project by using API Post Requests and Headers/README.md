# Day 37: Habit Tracking with API Requests

## Overview
On Day 37, I developed a habit tracking system using the Pixela API. This project involves creating a user account, setting up a graph, and managing data points (or "pixels") through various HTTP methods including POST, PUT, and DELETE requests. The Pixela API is used to track habits and visualize progress.

## Files and Structure


### `main.py`
- **Description:** This script interacts with the Pixela API to manage habit tracking through various endpoints. The script demonstrates how to create a user, set up a graph, and manage data points with different HTTP request methods.

- **Sections:**
  - **Section 1: Create a User**
    - **Purpose:** Set up a new user account on Pixela.
    - **Details:** This section is commented out as it only needs to be executed once.
    - **Endpoint:** `https://pixe.la/v1/users`
    - **Parameters:** `token`, `username`, `agreeTermsOfService`, `notMinor`
    - **Method:** POST

  - **Section 2: Create a Graph**
    - **Purpose:** Create a new graph to track habits.
    - **Details:** Configures a graph for tracking cycling distances.
    - **Endpoint:** `https://pixe.la/v1/users/{username}/graphs`
    - **Parameters:** `id`, `name`, `unit`, `type`, `color`
    - **Method:** POST
    - **Authentication:** Header-based (`X-USER-TOKEN`)

  - **Section 3: Post a Pixel**
    - **Purpose:** Add a new data point to the graph.
    - **Details:** Posts a pixel for a specific date with a quantity value.
    - **Endpoint:** `https://pixe.la/v1/users/{username}/graphs/{graph_id}`
    - **Parameters:** `date`, `quantity`
    - **Method:** POST
    - **Authentication:** Header-based (`X-USER-TOKEN`)

  - **Section 4: Update a Pixel**
    - **Purpose:** Update an existing pixel in the graph.
    - **Details:** Modifies the value of a pixel for a specific date.
    - **Endpoint:** `https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}`
    - **Parameters:** `quantity`
    - **Method:** PUT
    - **Authentication:** Header-based (`X-USER-TOKEN`)

  - **Section 5: Delete a Pixel**
    - **Purpose:** Delete a specific pixel from the graph.
    - **Details:** Removes a pixel for a specified date.
    - **Endpoint:** `https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}`
    - **Method:** DELETE
    - **Authentication:** Header-based (`X-USER-TOKEN`)

## How to Use
  1. **Setup:**
     - Replace `USERNAME` and `TOKEN` with your Pixela username and token.
  2. **Run the Script:**
     - Execute `main.py` to perform the various operations (create user, create graph, post/update/delete pixels) as needed.
  3. **Comment/Uncomment Sections:**
     - Comment out sections that you do not need to run repeatedly (e.g., user creation) to avoid redundant requests.

- **Example Outputs:**
  - **Graph Creation Success:**
    ```json
    {"message":"Success.","isSuccess":true}
    ```
  - **Pixel Posting Success:**
    ```json
    {"message":"Success.","isSuccess":true}
    ```
  - **Pixel Update Success:**
    ```json
    {"message":"Success.","isSuccess":true}
    ```
  - **Pixel Deletion Success:**
    ```json
    {"message":"Success.","isSuccess":true}
    ```

## Notes
- **API Rate Limits:** Be aware of any rate limits imposed by the Pixela API to avoid hitting request limits.
- **Security:** Ensure that your token and sensitive information are handled securely. Avoid hardcoding sensitive data in your script for production use.
