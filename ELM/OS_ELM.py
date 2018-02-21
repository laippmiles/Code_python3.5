# coding:UTF-8
#################
# OS_ELM
# author : zhiyong_will
# date : 2015.3.22
#################
from csv import DictReader
from numpy import *

#####设置相关参数########
trainData = r"C:\Users\Administrator\Desktop\python3.5\ELM\diabetes\segment_train.csv"
testData = r"C:\Users\Administrator\Desktop\python3.5\ELM\diabetes\segment_test.csv"
#读取某地址文件时前面加r来避免转义
#隐含神经元的个数
nHiddenNeurons = 180
#输入层的神经元个数
nInputNeurons = 19
#初始训练集的大小
NO = 280

#函数
##导入数据集
firstTrainData = []
firstTrainLable = []

# 处理训练样本
for t, row in enumerate(DictReader(open(trainData))):
    Id = row['Id']
    del row['Id']
    del row['I0']

    data = []
    if int(Id) < NO:
        # 处理是否被点击
        if row['Label'] == '1.00000000':
            y = 1
        elif row['Label'] == '2.00000000':
            y = 2
        elif row['Label'] == '3.00000000':
            y = 3
        elif row['Label'] == '4.00000000':
            y = 4
        elif row['Label'] == '5.00000000':
            y = 5
        elif row['Label'] == '6.00000000':
            y = 6
        else:
            y = 7
        del row['Label']
        firstTrainLable.append(y)
        # 处理特征
        for key in row:
            value = float(row[key])
            #index = int(value + key[1:], 16) % D
            data.append(value)

        firstTrainData.append(data)
        continue
    elif int(Id) == NO:#开始训练
        p0 = mat(firstTrainData)
        T0 = zeros((NO, 7))
        #处理样本标签
        for i in range(0, NO):
            a = firstTrainLable[i]
            T0[i][a-1] = 1

        T0 = T0 * 2 - 1
        Iw = mat(random.rand(nHiddenNeurons, nInputNeurons) * 2 - 1)#随机生成区间-1,1之间的随机矩阵
        bias = mat(random.rand(1, nHiddenNeurons))
        from sigFun import sig
        H0 = sig(p0, Iw, bias, NO)#样本数*隐含神经元个数
        M = (H0.T * H0).I
        beta = M * H0.T * T0
    else:#训练剩余的样本,每次训练一条样本
        # 处理label
        if row['Label'] == '1.00000000':
            y = 1
        elif row['Label'] == '2.00000000':
            y = 2
        elif row['Label'] == '3.00000000':
            y = 3
        elif row['Label'] == '4.00000000':
            y = 4
        elif row['Label'] == '5.00000000':
            y = 5
        elif row['Label'] == '6.00000000':
            y = 6
        else:
            y = 7
        del row['Label']
        Tn = zeros((1, 7))
        #处理样本标签
        b = y
        Tn[0][b-1] = 1
        Tn = Tn * 2 - 1
        # 处理特征
        data = []
        for key in row:
            value = float(row[key])
            data.append(value)
        pn = mat(data)
        H = sig(pn, Iw, bias, 1)
        M = M - M * H.T * (eye(1,1) + H * M * H.T).I * H * M
        beta = beta + M * H.T * (Tn - H * beta)

# 计算训练误差
correct = 0
sum = 0
for t, row in enumerate(DictReader(open(trainData))):
    del row['Id']
    del row['I0']

    # 处理是否被点击
    if row['Label'] == '1.00000000':
        y = 1
    elif row['Label'] == '2.00000000':
        y = 2
    elif row['Label'] == '3.00000000':
        y = 3
    elif row['Label'] == '4.00000000':
        y = 4
    elif row['Label'] == '5.00000000':
        y = 5
    elif row['Label'] == '6.00000000':
        y = 6
    else:
        y = 7
    del row['Label']

    # 处理特征
    data = []
    for key in row:
        value = float(row[key])
        data.append(value)

    p = mat(data)
    HTrain = sig(p, Iw, bias, 1)
    Y = HTrain * beta

    # 判断
    if argmax(Y) + 1 == y:
        correct += 1
    sum += 1
print("训练准确性为：%f" % (correct/sum))

# 计算测试误差
correctTest = 0
sumTest = 0
for t, row in enumerate(DictReader(open(testData))):
    del row['Id']
    del row['I0']

    # 处理是否被点击
    if row['Label'] == '1.00000000':
        y = 1
    elif row['Label'] == '2.00000000':
        y = 2
    elif row['Label'] == '3.00000000':
        y = 3
    elif row['Label'] == '4.00000000':
        y = 4
    elif row['Label'] == '5.00000000':
        y = 5
    elif row['Label'] == '6.00000000':
        y = 6
    else:
        y = 7
    del row['Label']

    # 处理特征
    data = []
    for key in row:
        value = float(row[key])
        data.append(value)

    p = mat(data)
    HTrain = sig(p, Iw, bias, 1)
    Y = HTrain * beta

    # 判断
    if argmax(Y) + 1 == y:
        correctTest += 1
    sumTest += 1
print("测试准确性为：%f" % (correctTest/sumTest))