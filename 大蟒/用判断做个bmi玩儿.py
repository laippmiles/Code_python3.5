weight=float(input('体重（kg）:'))
height=float(input('身高（cm）:'))
bmi = weight/((height/100)*(height/100))
if bmi<18.5:
    print('瘦子')
elif 18.5<=bmi<25:
    print('正常人')
elif bmi>28 and bmi<32:
    print('胖子')
else:
    print('死胖子')

#不像C,数值范围在python中有两种写法。现在我们可以愉快地说人话嘞
#用if的时候记得带好冒号
#^2这种写法只能用作int
