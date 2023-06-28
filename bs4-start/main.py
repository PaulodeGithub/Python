from bs4 import BeautifulSoup
import lxml
import codecs


with codecs.open("website.html", 'r', encoding='utf-8',
                 errors='ignore') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

a_tags = soup.find_all(name="a")

for text in a_tags:
    print(text.getText())