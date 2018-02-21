from LoadCsvData import loadcsv
name = 'Iris.csv'
(Lable,Data) = loadcsv(name)
#print(Lable)
#print(Data)
plength = Data[:,2]
is_setosa = (Lable == 0)
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa:{0}.'.format(max_setosa))
print('Minimum of others:{0}.'.format(min_non_setosa))

#去掉0类（setosa）后再做二分类（有点多分类的意思了 ）
Lable = Lable[~is_setosa]
Data = Data[~is_setosa]
is_Virginica = (Lable == 2)
