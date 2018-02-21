# coding:utf-8
import re
import requests
# 获取网页内容
r = requests.get('https://downloads.khinsider.com/game-soundtracks/album/rune-factory-3-nds-gamerip-')
data = r.text

print ('\n获取链接中URL:' )
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url ,data)
count = 1
for url in link:
    if '.mp3'in url:
        #print(url)
        #print('search download link')
        rnext = requests.get(url)
        datanext = rnext.text
        Downloadlink = re.findall(res_url, datanext)
        for Downloadurl in  Downloadlink:
                if '.mp3'in Downloadurl:
                    if count % 2 == 1:
                        print(Downloadurl)
                        break
        count = count + 1