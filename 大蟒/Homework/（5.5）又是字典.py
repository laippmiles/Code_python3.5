plain = {'a':1,'b':2,'c':3}
print('plain:',plain)

from collections import OrderedDict
fancy = OrderedDict(plain)
print('fancy:',fancy)

from  collections import defaultdict
def somefor():
    return

dict_of_lists = defaultdict(list)
#先声明是默认字典再挨个赋值
dict_of_lists ['a'] = 'something for a'
print(dict_of_lists['a'])
print(dict_of_lists['b'])