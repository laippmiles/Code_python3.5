from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import lxml
html = urlopen("http://www.jianshu.com/p/a3f8df948395/comments/1738347")
ind = BeautifulSoup(html.read(),"lxml")
print(ind.body.h1)
