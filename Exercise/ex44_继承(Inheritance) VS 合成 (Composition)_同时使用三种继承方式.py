class Parent:
    def __init__(self):
        print("This is a Parent")

    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def __init__(self):
        print("This is a Child")

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child ,before")
        super(Child,self).altered()
        #注意super的写法
        #继承父类的同名函数
        print("Child,after")
print('-'*30)
dad = Parent()
son = Child()
print('-'*30)
dad.implicit()
son.implicit()
print('-'*30)
dad.override()
son.override()
print('-'*30)
dad.altered()
son.altered()
print('-'*30)