class TheThing:
    def __init__(self):
        self.number = 0

    def some_function(self):
        print("I got called.")

    def add_me_up(self,more):
        self.number += more
        return self.number

#创造两个实例

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()
print('-'*30)
print("Number of a:",a.number)
print("Number of b:",b.number)
print('-'*30)
print("Add a up:",a.add_me_up(20))
print("Add b up:",b.add_me_up(30))
print('-'*30)
print("Number of a:",a.number)
print("Number of b:",b.number)

#来，试试把一个实例里的变量传到另一个不同类的实例
class TheMultiplier:
    def __init__(self,base):
        self.base = base
        #和上一个类不同，这个类的实例创建的时候需要赋个初值

    def do_it(self,m):
        return self.base * m

x = TheMultiplier(a.number)
print("The base of x:",x.base)
print("In fact it's a * b:",x.do_it(b.number))