from urllib.request import urlopen
from urllib.error import URLError,HTTPError
import re
#正则表达式
from bs4 import BeautifulSoup
#BeautifulSoup是好东西啊。
html = "http://www.heibanke.com/lesson/crawler_ex00/"
s = html
flagnumlist = 1
flagn = 1
while True:
    try:
    #在网络出问题的时候我可不想直接看到报错
        v = urlopen(s)
        #urlopen：创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。
    except (HTTPError,URLError) as e:
        print("网络出问题啦")
        break

    try:
    #读取失败的时候也不想
        bs = BeautifulSoup(v.read(),"lxml")
        #read()：读取整个文件
        #后面的"laml"说明用lxml来进行编译
        numlist = (bs.h3)
        # 我们只需要标签为h3那句话就够了
    except AttributeError as e:
        print("咦为嘛读取失败了...")
        break

    if flagnumlist ==1:
        print('Type of numlist:',type(numlist))
        flagnumlist = 0
        #好吧，numlist的类型是<class 'bs4.element.Tag'>，TAG类型？啥玩意？
    numlist = ''.join(numlist)
    #join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串，看样子这货可以处理上面那个东西
    n = re.findall(r'([0-9])',numlist)
    #re：正则表达式，检索numlist里头的数字。r''的意思是不对框内的文字进行转义
    if flagn ==1:
        print('Type of n:',type(n))
        flagn = 0
        #很好，n是个普通的列表
    n = ''.join(n)
    if n=='':
        break
        #找不到数字？找不到就对了我们找到出口啦
    s = html + n
    #如果找到数字串就去下一个网址吧
    print(numlist)
    print(s)