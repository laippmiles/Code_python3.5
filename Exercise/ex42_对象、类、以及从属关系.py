class mammals:
    pass

#is a
class Dog (mammals):

    def __init__(self,name):
        #has a
        self.name = name
        print("这条狗叫",self.name)

#is a
class Cat(mammals):

    def __init__(self,name):
        #has a
        self.name = name
        print("这只猫叫",self.name)

#is a
class Person:

    def __init__(self,name):
        #has a
        self.name = name
        print("这人叫",self.name)
        # has a
        self.pet = None
        #一开始并不需要赋值的变量可以这么搞
    def print_petname(self):
        if self.pet == None:
            print("%s 木有宠物."%self.name)
        else:
            print("%s 有只叫 %s的宠物"%(self.name,self.pet.name))
            #还可以连着两个点哎

#is a
class Employee(Person):

    def __init__(self,name,salary):
        #咦等会这是啥魔法
        super(Employee,self).__init__(name)
        #has a
        self.salary = salary
        print("%s 薪水为 %r"%(self.name,self.salary))

#is a
class Fish:
   def __init__(self):
       print("一条咸鱼。")

#is a
class Salmon(Fish):
    def __init__(self):
        print("啊我好怀念在南邮吃过的三斤三文鱼！")

#is a
class Halibut(Fish):
    def __init__(self):
        print("Halibut是泥鳅的意思的说（糸锯语气）")

#is a
rover = Dog("Rover")
print('↓'*30)

#is a
satan = Cat("Satan")
print('↓'*30)

#is a
mary = Person("Mary")
mary.print_petname()
print('↓'*30)

#is a
mary.pet = satan
mary.print_petname()
print('↓'*30)

#is a
frank = Employee("Frank",120000)
#这是月薪还年薪啊，有钱人
print('↓'*30)

#is a
frank.pet = rover
frank.print_petname()
print('↓'*30)

#is a
flipper = Fish()
print('↓'*30)

#is a
crouse = Salmon()
print('↓'*30)

#is a
harry = Halibut()
print('↓'*30)