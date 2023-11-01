# The goal is to extract all the articles from a news website and only print the one who have most votes

from bs4 import BeautifulSoup
import requests

# Get the content of a online web
response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text  # Get its HTML code

# Create a soup to interact with the HTML code
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# Create three lists where we will store the titles, links and votes for each of the articles
article_titles = []
article_links = []
article_votes = []

# Get all the titles and links by using soup
all_anchor_tags = soup.find_all(name="span", class_="titleline")  # Get all the news anchor tags that are included inside span section, titleline class.
for tag in all_anchor_tags:  # For each of the tags
    # print(tag)
    article_titles.append(tag.getText())  # Add the title of each article to the list of titles
    article_links.append(tag.find("a").get("href"))  # Add the link of each article to the list of links

# Get all the scores
all_scores = soup.find_all(name="span", class_="score")  # By using span tag and score class
for score in all_scores:
    article_votes.append(int(score.getText().split()[0])) # Add the score of each article to the list of scores

# Printing for debugging
# for i in range(len(article_titles)):
#     print(f"Title: {article_titles[i]} / Votes: {article_votes[i]} / Link: {article_links[i]}")

# Find the index of the highest number
index_of_highest = article_votes.index(max(article_votes))

# Print the information of the highest voted article
print(article_titles[index_of_highest])
print(article_links[index_of_highest])
print(f"Number of votes: {article_votes[index_of_highest]}")