from sys import exit

def start():
    print("你身处一个两眼一抹黑的怪大厅。")
    print("但你发现你的左右都有一扇大门")
    print("这时你决定")
    print("""
    1.左转（选1）
    2.右转（选2）
    3.直走（选3）
    """)
    select = ['1','2','3']
    while True:
        Togo = input('>')
        if Togo in select:
            if Togo == '1':
                bear_room()
                #break
            elif Togo == '2':
                cthulhu_room()
                #break
            elif Togo == '3':
                dead("你啪叽一下糊在墙上，可怜兮兮地屎掉了..")
                # break
        else:
            print("你就不能好好三选一嘛？")

def bear_room():
    print("这里有只熊")
    print("熊熊有蜂蜜")
    print("这只大肥熊好死不死还堵在出口")
    print("要怎样让熊挪个地？")
    bear_move = False
    while True:
        print("""
        1.抢它蜂蜜（选1）
        2.笑它肥（选2）
        3.直接开门（选3）
        """)
        Todo = input('>')
        select = ['1', '2', '3']
        if Todo not in select:
            print("三选一，三选一！")
            continue
        if Todo == '1':
            dead("生气的熊熊一掌把你扇屎了。")
        elif Todo == '2' and not bear_move:
            print("熊熊挪开了，赶紧出去吧")
            bear_move = True
        elif Todo == '2' and bear_move:
            dead("熊熊生气了，并噶几噶几地嚼掉了你的脚")
        elif Todo == '3' and bear_move:
            gold_room()
        else:
            print("哎呀出不去怎么办呢？")

def cthulhu_room():
    print("你看到了传说中的邪神克苏鲁")
    print("被它盯着会变疯癫的..")
    print("你是要逃命还是任凭邪神吃掉你的头")
    print("""
    1.撒丫子跑呀！！！（选1）
    2.跑个毛啊死了拉倒┓( ´ ` )┏
    """)
    while True:
        ToNext = input('>')
        select = ['1', '2']
        if ToNext not in select:
            print("二选一，二选一！")
            continue
        if ToNext == '1':
            start()
        elif ToNext == '2':
            dead("克苏鲁说今天的外卖很好吃。")

def gold_room():
    print("这个房间满是金子，你要拿点吗？拿多少？")
    while True:
        take = input('>')
        if take.isdigit():
            how_much = int(take)
            break
        else:
            print("哎哟你打个数字行不?")

    if how_much < 50:
        print("哎呀你也不算很贪心嘛，拿着金子走吧~")
        Restart()
    else:
        dead("你个贪婪的怪物！(啪叽)")

def dead (Why):
    print(Why)
    print("游戏结束")
    Restart()

def Restart():
    print("重新开始？(Y:重新开始)")
    Restart = input('>')
    if Restart == 'Y':
        start()
    else:
        exit(0)

start()