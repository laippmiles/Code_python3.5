text = '''我跟你讲
猫猫有
这--------->么
可爱
超可爱不骗你
'''

f = open('Text.txt','w')
#打开编辑模式
f.write(text)
f.close()

f = open('Text.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()