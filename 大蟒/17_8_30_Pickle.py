import pickle
listdata = 'listdata.txt'
list = ['apple','pie','pen']

f = open(listdata,'wb')
pickle.dump(list,f)
#dump只能接受二进制信息，所以open函数部分要写明'wb','rb'
f.close()

del list

f = open(listdata,'rb')
list = pickle.load(f)
print(list)

