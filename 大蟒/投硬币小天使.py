import random
a1=random.randint(0,99)   #输出乱炖整数
print(a1)
if(a1%2 == 0) :           #注意% 和 /的差别
    print('好了少年，去吧')
else :
    print('好了少年，撤吧')

input('Press any key to exit')
