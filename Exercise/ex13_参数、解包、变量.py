#一个可以接受参数的脚本
#这种脚本的参数在Run菜单下面的Edit Configuration界面中的script parameter中输入。
from sys import argv

script,first,second,third = argv
print("The script is called :",script)#这个参数是自动载入的，不用填。填了报错
print("Your first variable is :",first)
print("Your second variable is :",second)
print("Your third variable is :",third)