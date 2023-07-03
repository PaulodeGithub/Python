import requests
from bs4 import BeautifulSoup
import codecs

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL
response = requests.get(URL)

# Create a BeautifulSoup object with the response text
soup = BeautifulSoup(response.text, "html.parser")

# Find the movie titles using h3 selectors
all_titles = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_titles]
movies = movie_titles[::-1]
print(movies)

with codecs.open("movies.text", mode="w",  encoding='utf-8') as file:
    for n in movies:
         file.write(f"{n}\n")
    
print("Scraping complete. Check the movies.txt file.")


