import blog_spider
import threading
import time

def single_thread():
    for url in blog_spider.urls:
        blog_spider.craw(url)

def multi_thread():
    threads = []
    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw,args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")

if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:",end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")
