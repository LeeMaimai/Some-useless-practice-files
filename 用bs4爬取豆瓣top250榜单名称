import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}
contect = requests.get("https://movie.douban.com/top250", headers = headers).text
soup = BeautifulSoup(contect,"html.parser")

all_title = soup.findAll("a")
for title in all_title:
    all_link = soup.findAll("span",attrs = {"class":"title"})
    for link in all_link:
        print(link.string)
