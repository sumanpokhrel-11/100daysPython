from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

movie_link = response.text
soup = BeautifulSoup(movie_link, "html.parser")
# print(soup.prettify())

movies = [movie.getText() for movie in soup.find_all("h3", class_ = "listicleItem_listicle-item__title__BfenH")]
# print(movies[::-1])


with open("100daysbootcamp\day 45\movies.txt", mode='w') as file:
    for movie in movies[::-1]:
        file.write(f"{movie} \n")