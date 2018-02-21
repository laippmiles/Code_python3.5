class song:
    #python2中上一行要写作class song(object)：，这是关于type和object的历史问题
    # py3以后已经没必要在声明object了，object成为了所有类的基类（万物之爹？）
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def end(self):
        print('-'*30)

Happy_birthday = song(["祝你生日快乐",
                       "祝你生日快乐",
                       "祝你生日快乐啊",
                       "祝你生日快乐",
                       "咿呀嘿"])

bulls_on_parade = song([
    "They rally around the family",
    "With pockets full of shells"
])
Happy_birthday.sing_me_a_song()
Happy_birthday.end()
bulls_on_parade.sing_me_a_song()
bulls_on_parade.end()
