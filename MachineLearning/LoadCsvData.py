def loadcsv(FileName):
    import scipy
    #读取分离以下CSV格式数据
    Data = scipy.genfromtxt(FileName,delimiter=",")
    lable = Data[:,0]
    Data_Without_Lable = Data[:,1:]
    return lable,Data_Without_Lable
    #读取数据部分和Matlab有点不同，标签部分差不多
    #print(lable)
    #print(Data_Without_Lable)
