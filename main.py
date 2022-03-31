import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")

movies_list = soup.find_all(name="h3", class_="title")
print(movies_list)

for movie in movies_list:
    print(movie.getText())