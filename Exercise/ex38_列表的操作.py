ten_thing = "Apple Oranges Crows Telephone Light Suger"
print("Wait there is not 10 thing in the list, let's fix that.")
stuff = ten_thing.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("Add:",next_one)
    stuff.append(next_one)
    print("There is %d item now"%len(stuff))

print("There we go",stuff)
print("Let's do something with stuff.")

print(stuff[-1])
print(stuff[1])
print(stuff.pop())#列表最后一个元素
print(' '.join(stuff))
print('#'.join(stuff[3:5]))