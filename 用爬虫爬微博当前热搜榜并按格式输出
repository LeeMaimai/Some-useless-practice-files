import requests
from lxml import etree

url = 'https://s.weibo.com/top/summary'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","cookie":
"SUB=_2AkMQaYpaf8NxqwFRmf4UxG3kaYp_yw_EieKmNXuBJRMxHRl-yT9vqk45tRB6O-mktZ4SdC-l3gWuDfA8caJAvjbGVqLp; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWz.7W4DCgSvURiKhOJ2qL6; _s_tentry=passport.weibo.com; Apache=4572911322826.356.1731528049755; SINAGLOBAL=4572911322826.356.1731528049755; ULV=1731528049757:1:1:1:4572911322826.356.1731528049755:"}

response = requests.get(url,headers=headers)
content = response.content.decode('utf8')

html = etree.HTML(content)
#爬取
events = html.xpath('//tr/td[@class="td-02"]/a/text()')[1:]
hots =html.xpath('//tr/td[@class="td-02"]/span/text()')
hrefs = html.xpath('//tr/td[@class="td-02"]/a/@href')[1:]
# test
# print(events)
# print(hots)
# print(hrefs)

# 合并
weibo = []

for events,hots,hrefs in zip(events,hots,hrefs):
    H = "http://s.weibo.com" + hrefs
    eg = {}
    eg = {
        "事件":events,
          "热度":hots,
          "链接":H
          }

    weibo.append(eg)
    print(eg)
