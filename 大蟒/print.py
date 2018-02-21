
'''练习

请打印出以下变量的值：

n=123
f = 456.789'''              #多行注释的方法
#s1 = 'Hello, world'
#s2 = 'Hello, \'Adam\''
#s3 = r'Hello, "Bart"'
#s4 = r'''Hello,
#Lisa!

n=123
f=456.789
print('n=',n)
print('f=',f)
print('s1=','Hello,world')
print('s2=',r'Hello,\'Adam\'')
# r''内的字符串不会被转义
print('s3=',"r\'Hello,",'"Bart"')
#想输出单（双）引号的话，外围那个括号相应用双（单）引号电脑先生就不会搞混了
print('s4=',"""r'''Hello,
...Lisa!'''""")

"""输出多行的格式：

''' line1
... line2
... line3'''(括号也能用双引号，视情况啦)"""
