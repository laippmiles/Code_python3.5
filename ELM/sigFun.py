from math import exp
from numpy import *
def sig(tData, Iw, bias, num):
    '''
    tData:样本矩阵：样本数*特征数
    Iw:输入层到第一个隐含层的权重：隐含层神经元数*特整数
    bias:偏置1*隐含神经元个数
    '''
    v = tData * Iw.T   #样本数*隐含神经元个数
    bias_1 = ones((num, 1)) * bias
    v = v + bias_1
    H = 1./(1+exp(-v))
    return H
