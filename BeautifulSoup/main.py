from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
data = response.text
soup = BeautifulSoup(data, "html.parser")



articles = soup.find_all(name="span", class_="titleline")
article_titles =[]
article_links = []

for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")] 


max_value = max(article_upvotes)  # Find the largest number in list1

for num, item1, item2 in zip(article_upvotes, article_titles, article_links):
    if num == max_value:
        print(f"Most Upvotes: {num}")
        print(f"Title: {item1}")
        print(f"Link: {item2}")

# import lxml
# import codecs


# with codecs.open("website.html", 'r', encoding='utf-8',
#                  errors='ignore') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# a_tags = soup.find_all(name="a")

# for text in a_tags:
#     print(text.getText())