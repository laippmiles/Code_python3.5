while True:
    try:
        num = input("你想玩第几关啊: ")

        if num == 'origin':
            print("你找到彩蛋啦")
            import 通过颜色选择性输出爬虫文本
            exit()  # exit():让程序停止运行

        num=int(num)
    except ValueError as e:
        print("输入错误，重来哦")
        continue

    if (num<=0|num>9):
        print("数字范围错误，重来哦")
        continue
    break

print('开始玩第',num,'关')

if num == 1:
    try:
        import 第一关
        # 用这个可以调用同一文件夹的其他py文件
    except ImportError as e:
        print("这关还不会过呢")
elif num == 2:
    try:
        import 第二关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 3:
    try:
        import 第三关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 4:
    try:
        import 第四关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 5:
    try:
        import 第五关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 6:
    try:
        import 第六关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 7:
    try:
        import 第七关
    except ImportError as e:
        print("这关还不会过呢")
elif num == 8:
    try:
        import 第八关hai
    except ImportError as e:
        print("这关还不会过呢")
elif num == 9:
    try:
        import 第九关
    except ImportError as e:
        print("这关还不会过呢")
exit()      #exit():让程序停止运行
