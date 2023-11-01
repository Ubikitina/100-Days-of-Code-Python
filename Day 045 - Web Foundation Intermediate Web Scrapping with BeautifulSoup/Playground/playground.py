from bs4 import BeautifulSoup

# Open a file for reading
with open('website.html', 'r', encoding="utf-8") as file:
    # Read the entire contents of the file into a string
    website_contents = file.read()

# print(website_contents)

soup = BeautifulSoup(website_contents, "html.parser")

# Examples of contents that we can print
print(soup.title)  # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)  # Angela's Personal Site
print(soup.a)  # <a href="https://www.appbrewery.co/">The App Brewery</a>
print(soup.li)  # <li>The Complete iOS App Development Bootcamp</li> , only returns the first element of the list

# print(soup.prettify())  # Identes properly the code

all_anchor_tags = soup.find_all(name="a")  # Create a list with all the anchor tags
print(all_anchor_tags)

# How to get the content of the list
for tag in all_anchor_tags:
    # print(tag.getText())  # This will get the text of all the tags
    print(tag.get("href"))  # This will print the URL of all the tags

heading = soup.find(name="h1", id="name")  # With find, we only find the first result that matches the criteria
print(heading)  #

section_heading = soup.find(name="h3", class_="heading")  # Same as above. In this case, we add an underscore to class word so that it does not collide with the regular class word.
print(section_heading)

# CSS selector
company_url = soup.select_one(selector="p a")  # Select the "a" (anchor tag) element inside a "p" (paragraph). The select one only selects the first
print(company_url)

name = soup.select_one(selector="#name")  # We can find id-s by using #
print(name)

headings = soup.select(".heading")  # We can select the class of headings like this, by using a dot . In this case, as we only use "select", all the results will be selected in a list.
print(headings)