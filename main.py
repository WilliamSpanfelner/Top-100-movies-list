import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")

movies_list = soup.find_all(name="h3", class_="title")

movies_descending = [movie.getText().split(maxsplit=1) for movie in movies_list]
top_100_movies = sorted([[int(number[:-1]), title] for number, title in movies_descending])

with open("movies.txt", "w") as file:
    for movie in top_100_movies:
        file.write(f"{movie[0]}) {movie[1]}\n")

