#coding:utf-8
#py2默认编码是ASCII，py3默认已经是utf-8了，因此上一句话写不写没差
print("How old are you?",end=' '),
#py2是不支持end参数的
age = input()
print("How tall are you?",end=' '),
height = input()
print("How much do you weigh?",end=' '),
weight = input()

if weight[:1].isdigit():
    #通常体重至少有两位数，判断前两位是否为数字即可知道回答是不是透露体重了
    print("so , you are %r old , %r cm tall and %r heavy ╮(╯▽╰)╭ ."%(age,height,weight))
else:
    print("so , you are %r old , %r cm tall ╮(╯▽╰)╭ ." % (age, height))
    print("And about weigh your answer is : %r" %weight)
    #这里%前不要加逗号

#py3似乎是不会给你字符串里的特殊符号加转义符的，py2会加