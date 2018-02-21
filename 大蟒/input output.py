name=input('Type your name:')
#输入一串文本
print('Hello,',name)
#带变量的print。注意不像C，不是printf
a=int(input('a ='))
#输入一个int，前面要加声明要不默认的并不是数
b=int(input('b ='))
print('a =',a ,'b =',b ,'a + b=',a+b)

#以下为输入整个数组的一个方法
s=input('定义分隔符:')
print('用',s,'分隔多个数据')
str=input()
#先以字符形式保存输入的所有数据，分隔符在上面已经定义过
array=[n for n in str.split(s)]
#利用split将数据分隔开（在spilt的()中可以随意自定义分隔符，现在用的是变量s）
print('array=',array)
#这个用来作窗口停留（谁叫我们不会写UI呢）
exit = input('please enter any key to exit.')
