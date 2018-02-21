def lbs2kg(lbs):
    kg = lbs*0.45359237
    return kg
def inch2cm(inch):
    cm = inch*2.54
    return cm
my_name = 'Zed A.Shaw'
my_age = 35 #不骗你
my_height = 74 #inchs 英寸
my_weight = 180 #lbs 磅
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("let's talk about %r." % my_name)
#%r:什么玩意都能给你搞出来
print("He's %r inches tall." % my_height)
print("He's %r pound heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes,my_hair)) #注意多个格式化字符串的写法
print("His teeth are usually %s depending on the coffee."%my_teeth)
#原文是这行有毛病，试着改好它？
print("If I add %d ,%d and %d I get %d."%(\
      my_age , my_height , my_weight , my_age + my_height + my_weight))

#加分题1：善用IDE的replace功能
#加分题2：善用%r
#加分题3：http://blog.csdn.net/freestyle4568world/article/details/48369057
#加分题4：
print("He's %2r cm tall." % inch2cm(my_height))
print("He's %.5r kg heavy." % lbs2kg(my_weight))
#格式化字符前加“.n”可控制保留 n 位数据