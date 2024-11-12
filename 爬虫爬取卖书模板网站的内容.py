#完成了第一个爬虫，调用requests和bs4里的BeautifulSoup，具体步骤是：先request网站，拿到源码，再用BeautifulSoup()分析源码，做text分类，再去网站->检查->元素(F12)里找到需要的内容的规律，比如都是放在<p>里的，接着用soup.findAll("p")拿到想要的内容，for in语句做最后处理并输出，就成功了


from http.client import responses

from bs4 import BeautifulSoup
import requests
contect = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(contect,"html.parser")

all_prices = soup.findAll("p", attrs={"class":"price_color"})
for price in all_prices:
    print(price.string) #全部字符串
    # print(price.string[2:]) #用切片方式

all_titles = soup.findAll("h3")
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        print(link.string)
