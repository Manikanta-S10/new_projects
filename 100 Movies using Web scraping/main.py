import requests
from bs4 import BeautifulSoup

#url of the target
URL_ENDPOINT = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL_ENDPOINT)
code = response.text

soup = BeautifulSoup(code,"html.parser")
title_list =[ title.getText() for title in soup.find_all(name="h3",class_="title")]

# file handling 
with open("movie.text",mode="a",encoding='utf-8') as file:
    for movie in title_list[::-1]:
        file.write(movie + '\n')



