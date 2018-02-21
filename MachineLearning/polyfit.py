import scipy
data = scipy.genfromtxt('web_traffic.tsv',delimiter="\t")
[m,n] = data.shape
print('行数：',m,'列数：',n)
#可以用Matlab法求矩阵尺寸，就是size要改成XX.shape
#print(data.shape)
Num_Nan = scipy.sum(scipy.isnan(data))
print('Nan个数：',Num_Nan)
i = 0
while i < n:
    y = data[:,i]
    data_after = data[~scipy.isnan(y)]
    [m,n] = data_after.shape
    print('去除第',i+1,'列含Nan的数据')
    print('行数：',m,'列数：',n)
    i = i + 1

#画坐标图
x = data_after[:,0]
y = data_after[:,1]
fp1 , residuals , rank , sv , rcond = scipy.polyfit(x,y,1,full=True)
#设定full=Ture的话可以获得模型的更多细节
print('拟合参数： k = ',fp1[0],'b = ',fp1[1])
f1 = scipy.poly1d(fp1)
from 计算误差 import error
print('计算1阶误差:',error(f1,x,y))
print('polyfit提供的计算误差:',residuals)
#以上为计算1阶拟合

fp2 = scipy.polyfit(x,y,2)
f2 = scipy.poly1d(fp2)
print('计算2阶误差:',error(f2,x,y))

fp3 = scipy.polyfit(x,y,3)
f3 = scipy.poly1d(fp3)
print('计算3阶误差:',error(f3,x,y))

fp4 = scipy.polyfit(x,y,4)
f4 = scipy.poly1d(fp4)
print('计算4阶误差:',error(f4,x,y))

fp5 = scipy.polyfit(x,y,5)
f5 = scipy.poly1d(fp5)
print('计算5阶误差:',error(f5,x,y))

fp10 = scipy.polyfit(x,y,10)
f10 = scipy.poly1d(fp10)
print('计算10阶误差:',error(f10,x,y))

fp100 = scipy.polyfit(x,y,100)
f100 = scipy.poly1d(fp100)
print('计算100阶误差:',error(f100,x,y))

#poly1d ：组建多项式
#画新的显示图
fx = scipy.linspace(0,x[-1],1000)
import matplotlib.pyplot as plot
#计算2阶拟合

Setlinewidth = 2
plot.plot(fx,f1(fx),color = 'yellow',linewidth = Setlinewidth)
plot.plot(fx,f2(fx),color = 'red',linewidth = Setlinewidth)
plot.plot(fx,f3(fx),color = 'blue',linewidth = Setlinewidth)
plot.plot(fx,f4(fx),color = 'green',linewidth = Setlinewidth)
plot.plot(fx,f5(fx),color = 'purple',linewidth = Setlinewidth)
plot.plot(fx,f10(fx),color = 'lightsalmon',linewidth = Setlinewidth)
plot.plot(fx,f100(fx),color = 'moccasin',linewidth = Setlinewidth)

#关于颜色与线型设定见 http://blog.csdn.net/qq_26376175/article/details/67637151
plot.legend(['d=%i' % f1.order], loc="upper left")
from ShowPicture import show2d,ShowPlot

show2d(x,y)
ShowPlot()