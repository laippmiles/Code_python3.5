import numpy
a = numpy.array([[0,1,2,3,4,5]])
#每行要用一个[]，否则好像并不是真正的矩阵
#创建一个数组
print(a)
print(a.ndim)
#显示数组维度，即数组的秩
print(a.shape)
#输出结果为（行数，列数）
print(a.shape[0])
#输出行数
print(a.shape[1])
#输出列数
b = a.copy().reshape(2,3)
#先复制一个数组a给b，再将b转为2维数组
print(b)
b[0][1] = 2233
#索引从0开始，可以对矩阵复制
print(b)
print(a)
a = a.clip(0,2)
#过滤数字中不在区间的元素，改为离区间末端最近的数
print(a)