import requests
from bs4 import BeautifulSoup

# Since websites change very frequently, use this link from the Internet Archive's Wayback machine. That way your work will match the solution video.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Get the content of a online web
response = requests.get(URL)
yc_web_page = response.text  # Get its HTML code

# Create a soup to interact with the HTML code
soup = BeautifulSoup(yc_web_page, "html.parser")

# Get all the list of the movies
all_movies = soup.find_all(name="h3", class_="title")  # Get all the titles included inside h3 section, title class.

# Create a list of movies
list_of_movies = []

# Get the text and add to the list of movies
for movie in all_movies:
    list_of_movies.append(movie.getText())

# Reverse the list so that it starts from 1 to 100
list_of_movies.reverse()

# Specify the file path where you want to save the list
file_path = 'movies.txt'

# Open the file in write ('w') mode
with open(file_path, 'w', encoding='utf-8') as file:
    # Iterate through the list and write each element to the file
    for movie in list_of_movies:
        file.write(str(movie) + '\n')