#带步数统计的汉诺塔
global num;
num=0;
def move(a,b):
    global num  
    #print(a,'->',b)
    num=num+1;

def hanoi(n, src, tmp, fin):
    global num
    if n == 1:
        move(src,fin)
    else:
        hanoi(n-1,src,fin,tmp)
        move(src,fin)
        hanoi(n-1,tmp,src,fin)

n=int(input('n='))
i=1
while(i<=n):
    hanoi(i,'A','B','C')
    print('层数=',i,'步数=',num)
    num=0
    i=i+1
