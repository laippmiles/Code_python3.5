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

from ShowPicture import show2d,ShowPlot

show2d(x,y)
ShowPlot()
#上面的图要关掉才能接着往下跑
#拟合曲线
fp1 , residuals , rank ,sv , rcond = scipy.polyfit(x,y,1,full=True)
print('拟合参数： k = ',fp1[0],'b = ',fp1[1])