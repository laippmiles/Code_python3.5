import math
import sys
str = input()
data = str.split(' ')
num = int(data[0])
flag = data[1]

if num<=0 or num>1000:
  sys.exit()
if num < 3:
    print(flag)
    print(num-1)
else:
    turn = 1
    while ((num+1)/2 - turn**2) >= 0:
        turn = turn + 1
    turn = turn -1
    for i in range(1,turn+1):
        print(' '*(i-1)+flag * ((turn - (i-1))*2-1)+' '*(i-1),end = '\n')

    for i in range(1,turn):
        print(' '*(turn-1-i)+flag * (2*i+1)+' '*(turn-1-i),end = '\n')

    print(num + 1 - 2*(turn**2))