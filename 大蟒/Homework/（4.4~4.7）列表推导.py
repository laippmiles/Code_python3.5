list = [num for num in range(0,10) if num % 2 == 0]
print(list)
dict = {num:num*num for num in range(1,10)}
print(dict)
odd = {num for num in range(0,10) if num % 2 == 1}
print(odd)
something = (('Got',num) for num in range(1,10))
for str in something :
    print(str)