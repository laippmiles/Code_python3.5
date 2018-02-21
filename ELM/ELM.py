from numpy import *
from csv import *
from sigFun import sig
from pinv import pinv
#注：python矩阵是从0开始算的
#####设置相关参数########
trainData_name = r"C:\Users\Administrator\Desktop\python3.5\ELM\diabetes\diabetes-train"+"1"+".csv"
testData_name = r"C:\Users\Administrator\Desktop\python3.5\ELM\diabetes\diabetes.csv"
#读取某地址文件时前面加r来避免转义
#trainData = mat(loadtxt(open(trainData_name),delimiter=","))
#提取csv的数据 ,delimiter:分隔符；
#testData = mat(loadtxt(open(testData_name),delimiter=","))
##导入数据集
traindata = [];
for t in (reader(open(trainData_name))):
    traindata.append(t)
traindata = mat(traindata);
P = traindata[:,1:traindata.shape[1]]
T = traindata[:,0]
print(P)

#隐含神经元的个数
nHiddenNeurons = 20
#输入层的神经元个数
nInputNeurons = P.shape[1]
#初始训练集的大小
NumberofTrainingData = traindata.shape[0];
#print(NumberofTrainingData)



Iw = mat(random.rand(nHiddenNeurons, nInputNeurons) * 2 - 1); # 随机生成区间-1,1之间的随机矩阵
bias = mat(random.rand(1, nHiddenNeurons));
H = sig(P, Iw, bias, NumberofTrainingData)  # 样本数*隐含神经元个数
OutputWeight= pinv(H) * T;
Y = (H * OutputWeight);

#print(Y)