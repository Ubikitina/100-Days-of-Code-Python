# Day 45: Web Scraping with BeautifulSoup

## Overview

On Day 45 of learning Python, I focused on web scraping using the BeautifulSoup library. I worked on various projects that involved extracting and processing data from HTML web pages. I learned how to extract, process, and store data from HTML pages. Below are the details of the files created and the purpose of each project.

## Projects and Files

### 100 Movies to Watch

- **Files:**
  - `main.py`
  - `movies.txt`
  - `README.md`

- **Description:**
  The goal of this project was to scrape a list of the top 100 movies of all time from a website and save the list in a text file in ascending order. The script uses BeautifulSoup to parse the HTML content and extract movie titles. The final list is saved in the `movies.txt` file.

- **Code Explanation (`main.py`):**
  - The script sends an HTTP request to a specific URL (using the Wayback Machine to ensure consistency).
  - It then uses BeautifulSoup to parse the HTML and extract all movie titles.
  - The titles are stored in a list, reversed to ensure correct order, and then written to `movies.txt`.

- **Output (`movies.txt`):**
  - Contains the list of 100 movies, ordered from 1 to 100.

- **Readme (`README.md`):**
  - Provides an overview of the project's objective, the importance of using the Internet Archive's URL, and a brief solution outline.

### Playground

- **Files:**
  - `playground.py`
  - `website.html`

- **Description:**
  This is a sandbox environment where I experimented with various BeautifulSoup functionalities. The `website.html` file is a simple HTML page used as a source for practicing different web scraping techniques.

- **Code Explanation (`playground.py`):**
  - The script reads the contents of `website.html`.
  - It demonstrates how to use BeautifulSoup to navigate and manipulate the HTML structure, including extracting elements by tag name, class, and id.
  - Various methods such as `find_all`, `select_one`, and `getText()` are used to showcase the versatility of BeautifulSoup.

### Tech News Scraper

- **Files:**
  - `main.py`

- **Description:**
  In this project, the goal was to scrape articles from a news website (Hacker News) and identify the article with the most votes.

- **Code Explanation (`main.py`):**
  - The script sends an HTTP request to the Hacker News website to retrieve the latest articles.
  - It then parses the HTML to extract the titles, links, and vote counts of the articles.
  - The script determines which article has the highest number of votes and prints its title, link, and vote count.
