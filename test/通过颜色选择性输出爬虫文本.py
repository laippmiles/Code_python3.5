from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
html1 = BeautifulSoup(html,"lxml")
#print(html1)
redList = html1.findAll("span",{"class":"red"})
greenList = html1.findAll("span",{"class":"green"})
i=0
for red in redList:
    while( i < len(greenList)):
        print(greenList[i].get_text(),':')
        i=i+1
        break
    print(red.get_text())
    print('\n')