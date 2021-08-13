from bs4 import BeautifulSoup
import requests

URL="https://www.imdb.com/list/ls091520106/"
response =requests.get(URL)

empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

movie_names =soup.find_all(name="h3", class_="lister-item-header")

movies =[]
for movie in movie_names:
    x = movie.find(name="a").getText()
    movies.append(x)

with open("movies.txt", mode="w") as file:
    for n in range(0, len(movies), 1):
        file.write(f"{n+1}){movies[n]}\n")
