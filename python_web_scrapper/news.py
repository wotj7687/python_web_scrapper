import requests
from bs4 import BeautifulSoup

def movie_rank():
    URL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    ranks = soup.find_all("td",{"class":"ac"})
    movies = soup.find_all("div",{"class":"tit3"})
    picture_url = find_url()

    arr = []
    for rank in range(0,len(ranks),3):
        rank_number = ranks[rank].find("img")["alt"]
        movie_name = movies[int(rank/3)].find("a")["title"]
        picture = movie_picture(picture_url,int(rank/3))
        dict = {"rank":rank_number,"movie":movie_name, "picture":picture}
        arr.append(dict)
    return arr

def movie_picture(url,number = 0):
    URL = f"https://movie.naver.com{url[number]}"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    picture = soup.find_all("div", {"class": "poster"})[0].find("img")["src"]
    #retur picture's url
    return picture

def find_url():
    URL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    urls = soup.find_all("div",{"class":"tit3"})
    save_urls = []
    for url in urls:
        save_url = url.find("a")["href"]
        save_urls.append(save_url)
    return save_urls