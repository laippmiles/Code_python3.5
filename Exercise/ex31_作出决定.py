print("前方有两扇门，你要进入门1（输入1）还是门2（输入2）？")

door = input('>')

if door == '1':
    print("这里有只大猫猫在吃芝士蛋糕，你怎么做？")
    print("1.把它的蛋糕抢走╮(╯▽╰)╭")
    print("2.朝他嗷嗷大叫！")

    BigMew = input('>')

    if BigMew == '1':
        print("大猫猫嗷地一下跳起来，抓破了你的脸！")
    elif BigMew == '2':
        print("大猫猫尾巴摇啊摇啊摇，突然向你的脚扑去！")
    else:
        print("这就对了......大猫猫走远啦")

elif door == '2':
    print("此刻你凝望着克苏鲁瞳上的无尽深渊")
    print("1.布丁！")
    print("2.李小龙！")
    print("3.可以理解的咆哮环绕声")
    insanty = input('>')

    if insanty == '1' or insanty == '2':
        print("恭喜你被果冻之魂拯救啦！")
    else:
        print("你逐渐癫狂，双眼被腐蚀成两滩烂泥...")

else:
    print("你跌跌撞撞地往下坠落，正好掉在一把刀的刀尖上，最后被戳死了。")