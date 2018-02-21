from sys import argv

script,filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that ,hit CTRL-C(^C)")
print("If you do want that,hit RETURN.")

input("?")

print("Open the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#target.write(line1+"\n"+line2+"\n"+line3+"\n")
print("And finally ,we close it.")
target.close()

#加分题2
target = open(filename)
print(target.read())
#加分题3：见上面杠掉的那行