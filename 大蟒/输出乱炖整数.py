import random
j=0                           #奇数个数
o=0                           #偶数个数
i=100
while(i>0) :

    a1=random.randint(0,99)   #输出乱炖整数
    print(a1)
    if(a1%2 == 0) :           #注意% 和 /的差别
        o=o+1
    else :
        j=j+1
    i=i-1

print(j,o)

input('Press any key to exit')
