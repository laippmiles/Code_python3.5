#这个和脚本差不多
def print_two(*args):
    arg1,arg2 = args
    #去掉这行的话，本来*args是不限制参数数目的
    print("arg1 ; %s\narg2 : %s"%(arg1,arg2))

#这是比较普通的自定义函数
def print_two_again(arg1,arg2):
    print("arg1 ; %s\narg2 : %s"%(arg1,arg2))

#只有一个参数的自定义函数
def print_one(arg1):
    print("arg1 ; %s" % (arg1))

#无参数函数
def print_none():
    print("这里什么都没有")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()