#好的，我们可爱的脚本又要回来啦
from sys import argv

scrpit,input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
    #每次你运行 f.seek(0) 你就回到了文件的开始
    #seek(n)用于将读取起点定在第n个字节内
#中间插播一句，光标变粗按一下Insert就行

def print_a_line(line_count,f):
    print(line_count,f.readline())
    #readline() 里边的代码会扫描文件的每一个字节，直到找到一个 \n 为止，然后它停止读取文件，并且返回此前的文件内容

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind,kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)