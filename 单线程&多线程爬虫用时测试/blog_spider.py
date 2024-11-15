import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","cookie":
"SUB=_2AkMQaYpaf8NxqwFRmf4UxG3kaYp_yw_EieKmNXuBJRMxHRl-yT9vqk45tRB6O-mktZ4SdC-l3gWuDfA8caJAvjbGVqLp; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWz.7W4DCgSvURiKhOJ2qL6; _s_tentry=passport.weibo.com; Apache=4572911322826.356.1731528049755; SINAGLOBAL=4572911322826.356.1731528049755; ULV=1731528049757:1:1:1:4572911322826.356.1731528049755:"}

urls = [f"https://www.cnblogs.com/#p{page})"
        for page in range(1, 50+1)]
# print(urls)
def craw(url):
    r = requests.get(url,headers=headers)
    print(url,len(r.text))

craw(urls[0])
