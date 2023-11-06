from bs4 import BeautifulSoup
# import lxml # backup parser in case html.parser doesn't work
import requests

# EXERCISE 2
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_rows = soup.find_all(class_="athing")

link_tags = [r.find(class_="titleline").find("a") for r in article_rows]
titles = [x.getText() for x in link_tags]
links = [x.get("href") for x in link_tags]
upvotes_text = soup.find_all(class_="score")
upvotes = [x.getText().split()[0] for x in upvotes_text]

# Print article title with most upvotes
i = upvotes.index(max(upvotes))
print(titles[i])

# # EXERCISE 1
# WEBSITE_FILEPATH = "website.html"

# with open(WEBSITE_FILEPATH) as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # Print string of the first title tag in document
# print(soup.title.string)

# # Prettify document
# print(soup.prettify())

# # Find all anchor tags and print their text and href attributes
# anchor_tags = soup.find_all(name="a")
# for a in anchor_tags:
#     print(a.getText())
#     print(a.get("href"))

# # Find with CSS selector
# company_url = soup.select_one(selector="p a")
# print(company_url)
