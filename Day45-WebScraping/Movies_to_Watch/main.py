import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
titles = []
# Write your code below this line 👇
response = requests.get(URL)
movies_html = response.text

# Parse movies_html with soup.
soup = BeautifulSoup(movies_html, "html.parser")
# print(soup.prettify)

movies = soup.find_all(name="h3", class_="title")
# print(movies)

titles = [movie.getText() for movie in movies]
titles.reverse()  # Reverse the list to ascend from 1 to 100
# print(titles)

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")
print("...Movies written to file 'movies.txt'")
