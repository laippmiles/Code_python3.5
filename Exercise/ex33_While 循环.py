def num_loop(num_loop,add_num):
    i = 0
    number = []
    while i < num_loop :
        print("At the top i is %d"%i)
        number.append(i)

        i += add_num
        print("Number now : ",number)
        print("At the bottom i is %d"%i)
    return number

def num_loop_2(num_loop,add_num):
    i = 0
    number = []
    for i in range(0,num_loop) :
        print("At the top i is %d"%i)
        number.append(i)
        i += add_num
        #for循环里的加值还是要留着的！
        print("Number now : ",number)
        print("At the bottom i is %d"%i)
    return number


#numbers = num_loop(6,1)
numbers = num_loop_2(6,1)
print("The numbers")
for num in numbers:
    print(num)

#加（song）分题写法如上