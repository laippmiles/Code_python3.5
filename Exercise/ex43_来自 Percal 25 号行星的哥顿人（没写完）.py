from sys import exit
from random import randint

class Scene:
#可选择的事件或者地图
    def enter(self):#前进
        print("此场景仍未完成，将其划为子类并执行enter()函数")
        exit(1)

class Death(Scene):
#事件支线：BE

    quips = [
        "哎呀你屎了╮(╯▽╰)╭",
        "你娘生你还不如生块叉烧（啪叽！）",
        "你屎了，你个卢瑟",
        "你还不如我家的小奶狗（Duang！）"
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
#中央走廊
    def enter(self):
        print("这是中央走廊\n"
              "哥顿25号星人入侵了你的飞船\n"
              "除了你之外所有船员都屎掉了\n"
              "你最后一个任务是从军火库拿来中子自毁炸弹放在舰桥上\n"
              "然后坐上逃脱仓，在脱逃后炸了整个飞船\n"
              "你现在穿过中央走廊往军火库跑\n"
              "这时，一个野生的哥顿星人跳出来啦！\n"
              "哥顿星人通身红色鳞片，漆黑的牙齿，跟暴走的暴鲤龙似的。\n"
              "他（她？它？）挡在前方的门前，掏出武器想要灭了你")
        print('-'*30)
        print("这时你：\n"
              "1.掏出枪对射呀！\n"
              "2.抱头鼠窜！\n"
              "3.和它动之以理晓之以情（呜哇啦啦啦啦啦）\n")
        Select = ['1','2','3']
        while True:
            Selection = input('>')
            if Selection in Select:
                break
            print("三选一！三选一！")
        if Selection == '1':
            return 'Death'
        elif Selection == '2':
            return 'Death'
        elif Selection == '3':
            return 'Laser_Weapon_Armory'
class LaserWeaponArmoty(Scene):
#遇见激光军团
    def enter(self):
        print("我们遇见激光军团了")
        pass

class TheBridge(Scene):
#舰桥
    def enter(self):
        print("我们看到了舰桥")
        pass

class EscapePod(Scene):
#逃脱仓
    def enter(self):
        print("逃脱仓")
        pass

class Map(object):
    scenes = {
        'Central_Corridor':CentralCorridor(),
        'Laser_Weapon_Armory':LaserWeaponArmoty(),
        'The_Bridge':TheBridge(),
        'Escape_Pod':EscapePod(),
        'Death':Death()
    }

    def __init__(self, start_scene):
        print("地图初始化.")
        self.start_scene = start_scene

    def next_scene(self, Scene_name):
        print("下一步.")
        return Map.scenes.get(Scene_name)

    def opening_scene(self):
        print("打开地图.")
        return self.next_scene(self.start_scene)


class Engine(object):
    # 游戏选项
    def __init__(self, Scene_map):  # 载入当前地图
        self.Scene_map = Scene_map
        #print(dir(self.Scene_map)) #这个可以显示类的成员

    def play(self):
        current_scene = self.Scene_map.opening_scene()

        while True:
            print('\n', '-' * 30)
            #print(dir(current_scene))
            next_scene_name = current_scene.enter()
            current_scene = self.Scene_map.next_scene(next_scene_name)

A_map = Map('Central_Corridor')
#这里把类带进Engine类中，类中类出来咯
A_game = Engine(A_map)
A_game.play()