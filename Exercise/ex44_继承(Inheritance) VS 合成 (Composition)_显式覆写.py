class Parent:
    def __init__(self):
        print("This is parents.")
    def override(self):
        print("Parent override()")

class Child(Parent):
    def __init__(self):
        print("This is Child.")
    def override(self):
        print("Child override()")

print('-'*30)
dad = Parent()
print('-'*30)
son = Child()
print('-'*30)
dad.override()
print('-'*30)
son.override()