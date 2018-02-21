the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
#apricots是杏子
change = [1,'pennies',2,'dimes',3,'quarters']

#先对第一个列表迭代
for number in the_count:
    print("This is count %d"%number)
#number 不是强制变量名，就...随意取就对了。知道for的运行原理以后就能愉快地接受了这个设定

#再对第二个列表进行迭代
for fruit in fruits:
    print("A fruit of type: %s"%fruit)

for i in change:
    print("I got %r" %i)
    #这个列表内元素种类不止一种，所以要用%r(%s也能显示，整数会被自动转成字符串。可是%d是绝对会报错的)

element = []

for j in range(0,6):
    print("Add %d to the list"%j)
    element.append(j)

for num,k in zip(range(1,len(element)+1),element):
    #多个变量迭代要用zip
    print("The %dth element in the list is %d"%(num,k))

