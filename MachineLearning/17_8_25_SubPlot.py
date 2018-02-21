import matplotlib.pyplot as plot
import scipy
#读取分离以下CSV格式数据
Data = scipy.genfromtxt('Iris.csv',delimiter=",")
lable = Data[:,0]
Data = Data[:,1:]
#print(lable)
#print(Data)
i = 0
for m in range(3):
    for n in range(3):
        if m!=n:
            plot.subplot(231 + i)
            i = i + 1
            print(m,n,i)
            for t,marker,c in zip(range(3),">ox","rgb"):
                plot.scatter(Data[lable == t, m], Data[lable == t, n], marker=marker, c=c)
plot.show()