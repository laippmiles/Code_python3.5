class Other:
    def __init__(self):
        print("There is a class inited as 'other'.")

    def override(self):
        print("Other override()")

    def implicit(self):
        print("Other implicit()")

    def altered(self):
        print("Other altered")

class Child:

    def __init__(self):
        print("This is a child.")
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child,Before")
        self.other.altered()
        print("Child,After")

print('-'*30)
son = Child()
print('-'*30)
son.implicit()
print('-'*30)
son.override()
print('-'*30)
son.altered()