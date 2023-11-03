import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "Add here your client id"
SPOTIFY_CLIENT_SECRET = "Add here your client secret"
REDIRECT_URI = 'http://example.com'  # This is the default redirect URI
SPOTIFY_USER_NAME = "Add here your username"


## ---------------------------------------------------------------------------------------
## GETTING DATA FROM THE WEB
## ---------------------------------------------------------------------------------------

# Ask the user for a year in the "YYYY-MM-DD" format
year_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{year_input}/"

# Get the content of a online web
response = requests.get(url)
web_page_content = response.text  # Get its HTML code

# Create a soup to interact with the HTML code
soup = BeautifulSoup(web_page_content, "html.parser")

# Get all the list of the song titles
# all_song_titles = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")  # Get all the titles included inside h3 section, with a determined class.
# An easier way to do so:
all_song_titles = soup.select("li ul li h3")  # Search an h3 item that it is inside a li, and later on inside a ul, and inside a li again

# print(all_song_titles)

song_titles = []

for song in all_song_titles:
    song_titles.append(song.getText().strip())

# print(song_titles)


## ---------------------------------------------------------------------------------------
## CONNECTING TO SPOTIFY AND CREATING THE PLAYLIST
## ---------------------------------------------------------------------------------------

sp = spotipy.Spotify(  # Create a Spotipy client
    auth_manager=SpotifyOAuth(  # Create a SpotifyOAuth instance and pass it to the client creation
        scope="playlist-modify-private",  # Adjust the scope based on your needs
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USER_NAME,
    )
)



# Create an empty list to store all the song URI-s
list_of_song_uris = []
year = year_input.split('-')[0]  # Year that will be used in the search

# Search each song URI in Spotify
for song in song_titles:
    results = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)  # The query used includes the title of the song, the year and limits the results to 1
    try:  # Only if the list of results is not empty will work
        uri_of_the_song = results["tracks"]["items"][0]["uri"]
        list_of_song_uris.append(uri_of_the_song)
    except IndexError:  # If the result is empty, then we will print the name of the song skipped.
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(list_of_song_uris)

# Get the user ID from Spotify
# user_id = sp.current_user()["id"]
# print(sp.current_user())

# Create a new private playlist
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name= f"{year_input} Billboard 100", public=False)

# Get the playlist ID
playlist_id = playlist['id']

# Add the songs to the playlist by using their URI
sp.playlist_add_items(playlist_id, list_of_song_uris)