#隐式继承
class Parents :
    def __init__(self):
        print("This is parents.")

    def implicit(self):
        print("Parent implicit()")

class Child(Parents):
    def __init__(self):
        print("This is child.")

print('-'*30)
dad = Parents()
print('-'*30)
son = Child()
print('-'*30)
dad.implicit()
print('-'*30)
son.implicit()
