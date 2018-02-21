import requests
from urllib.request import urlopen
from urllib.error import URLError,HTTPError

i=1
name = input("输入用户名: ")

try:
    v = urlopen("http://www.heibanke.com/lesson/crawler_ex01/")
except (HTTPError, URLError) as e:
    print("网络出问题啦")
    exit()

while i<=30 :
    data = {"username": name,
            "password": i}
    request = requests.post("http://www.heibanke.com/lesson/crawler_ex01/",data)
    res = "密码错误" in request.text
    if (res):
        print("猜密码为",i,"密码是错误的")
        i = i + 1
        continue
    else :
        print("猜中啦，密码为",i,)
        i = 31