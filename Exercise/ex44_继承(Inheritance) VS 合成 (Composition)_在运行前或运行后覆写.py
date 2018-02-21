class Parents:
    def __init__(self):
        print("This is parents")

    def altered(self):
        print("Parent Altered()")

class Child(Parents):
    def __init__(self):
        print("This is child")

    def altered(self):
        print("Befort")
        #像上例一样覆写函数，不过接着你用 Python 的内置函数 super 来调用父类 Parent 里的版本。
        super(Child,self).altered()
        print("After")

print('-'*30)
dad = Parents()
print('-'*30)
son = Child()
print('-'*30)
dad.altered()
print('-'*30)
son.altered()
