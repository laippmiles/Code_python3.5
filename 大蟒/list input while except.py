Flag=1
Flagadd=0
Flagdel=0
Flagins=0
data=[]
i=0

while Flag==1:
    try:
        begin=int(input('你要干嘛（1：添加 2：删除 3：插入数据 4：退出）'))
    except ValueError as e:
        print('输入数字谢谢')
        continue
        
    if begin==1:
        Flagadd=1
    elif begin==2:
         Flagdel=1
    elif begin==3:
        Flagins=1
    elif begin==4:
        Flag=0
    else:
        continue

    while Flagadd==1:
        try:
            print('指明第%d数据类型：(整型：1 浮点：2 字符串:3)' %(i+1))
            Class=int(input('                '))
            if Class==1:
                print('输入第%d个数据,类别为整型：'%(i+1))
                dataadd=int(input())
            elif Class==2:
                print('输入第%d个数据,类别为浮点：'%(i+1))
                dataadd=float(input())
            elif Class==3:
                print('输入第%d个数据,类别为字符串：'%(i+1))
                dataadd=str(input())
            else:
                continue
            Flagadd=int(input('是否继续输入（1/0）'))
            data.append(dataadd)
            i=i+1
        except ValueError as e:
            print('输入数字谢谢')
            continue
        #缩进内的都是循环体
    print(data)
    data1=data

    while Flagdel==1:
        if data1==[]:
            print('删你麻痹数组是空的')
            Flagdel=0
            break
        try:
            i=int(input('输入要删除数据的编码'))
            if i>(len(data1) - 1):
                print('索引有问题删不了')
                FlagDel=0
                break
            data1.pop(i-1)
            Flagdel=int(input('是否继续删除（1/0）'))
        except ValueError as e:
            print('输入数字谢谢')
            continue
        
    while Flagins==1:
        try:
            dataclass=int(input('指明插入数据类型：(整型：1 浮点：2 字符串:3)'))
            if dataclass==1:
                print('输入插入数据,类别为整型：')
                ins=int(input())
            elif dataclass==2:
                print('输入插入数据,类别为浮点：')
                ins=float(input())
            elif dataclass==3:
                print('输入插入数据,类别为字符串：')
                ins=str(input())
            else:
                continue
            j=int(input('输入要数据插入的编码位置'))
            if j>(len(data1) - 1):
                print('索引有问题')
                Flagins=0
                break
            data1.insert(j,ins)
            Flagins=int(input('是否继续插入（1/0）'))
        except ValueError as e:
            print('输入数字谢谢')
            continue
print(data1)
exit=input('Press any key to exit')
