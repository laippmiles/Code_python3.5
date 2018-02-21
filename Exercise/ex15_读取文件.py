from sys import argv

script,filename = argv

txt = open(filename)

print("Here is your file <%s>."%filename)
print(txt.read())
txt.close()
#用完就关养成好习惯

#顺手写了异常检测
while True:
    try:
        print('Type the file again:')
        file_again = input('>')
        txt = open(file_again)
        break
    except FileNotFoundError as error:
        print("文件不存在.")
        continue
print(txt.read())

txt.close()