def add(a,b):
    print("Add %d + %d :"%(a,b))
    return a+b

def subtract(a,b):
    print("Subtract %d - %d :"%(a,b))
    return a-b

def multiply(a,b):
    print("Multiply %d * %d :"%(a,b))
    return a*b

def divide(a,b):
    print("Divide %d / %d :"%(a,b))
    return a//b

print("Let's do some with just function!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age : %d,Height : %d,Weight : %d,IQ : %d"%(age,height,weight,iq))

#额外试着打一段奇怪的代码吧，先别管，跑出来你就知道了

print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That become ",what,"Can you do it by hand")
