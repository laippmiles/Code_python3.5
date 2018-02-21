def greet(func):
    def newfunc(*arg,**kwargs):
        print('start')
        func(*arg,**kwargs)
        print('end')
    return newfunc

@greet
def afunc(a,b):
    print(a,b)

afunc('Hello','World')