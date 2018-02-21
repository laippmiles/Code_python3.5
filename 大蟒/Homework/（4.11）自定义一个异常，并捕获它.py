class Oopsexcept(Exception):
    pass

list = [1,2,3,'yeh']


for something in list:
    if type(something) is not int:
        try:
            raise Oopsexcept(something)
        except Oopsexcept as something:
                print(something,'Caught an Oops')
