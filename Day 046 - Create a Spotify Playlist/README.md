# Day 46: Creating a Spotify Playlist

## Overview

On Day 46 of learning Python, I focused on creating a Spotify playlist based on the Billboard Hot 100 chart for a specific date. The project involved scraping the Billboard website for song titles and using the Spotify API to create a playlist with those songs. Below are the details of the files created and the steps involved in the project.

## Files and Purpose

### `main.py`

- **Purpose:**
  This script scrapes the Billboard Hot 100 chart for a user-specified date and creates a Spotify playlist with those songs.

- **Key Components:**
  - **Web Scraping:**
    - The script prompts the user to input a date in the format `YYYY-MM-DD`.
    - It then uses `requests` and `BeautifulSoup` to scrape the Billboard Hot 100 chart for that date from the Billboard website.
    - The song titles are extracted from the HTML content and stored in a list.
  
  - **Spotify API Integration:**
    - The script connects to Spotify using the `spotipy` library and `SpotifyOAuth` for authentication.
    - It searches for each song on Spotify using the song titles and the specified year.
    - The script then creates a new private playlist on the user's Spotify account and adds the found songs to the playlist.

- **Important Variables:**
  - `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`: Your Spotify developer credentials.
  - `REDIRECT_URI`: Redirect URI used during OAuth authentication.
  - `SPOTIFY_USER_NAME`: Your Spotify username.
  
- **Workflow:**
  1. **User Input:** The user inputs a date.
  2. **Scraping Billboard:** The script fetches the Billboard Hot 100 chart for that date.
  3. **Spotify Authentication:** The script authenticates with Spotify.
  4. **Song Search:** The script searches for the songs on Spotify.
  5. **Playlist Creation:** The script creates a new playlist and adds the songs.

### `token.txt`

- **Purpose:**
  This file stores the OAuth token information for Spotify authentication. It is generated automatically by the `SpotifyOAuth` object and is used to maintain the session.
