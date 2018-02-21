#coding:utf-8
import random
from urllib.request import urlopen
#from urllib import urlopen
#python2 的urlopen在urllib中
#python3 的urlopen在urllib的request模块中
import sys

Word_url = "http://learncodethehardway.org/words.txt"
Words = []

Phrases = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",

    "class %%%(object):\n\tdef __init__(self,***)":
    "class %%% has-a __init__ that takes self and *** parameters.",

    "class %%%(object):\n\tdef ***(self,@@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",

    "***.%%%()":
    "Set *** to an instance of class %%%.",

    "***.***(@@@)":
    "From *** get the *** function,and call it with parameters self,@@@.",

    "***.*** = '***'":
    "From *** get the *** attribute and set it to ***."
}

Phrases_First = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    Phrases_First = True

#在网站载入词汇
for word in urlopen(Word_url).readlines():
    word = word.decode()
    #这是从python2中移植来的程序，所以要加入decode解决两者间不同的编码问题
    #python3出来word是bytes格式，需要再转换才能有str格式
    Words.append(word.strip())

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in random.sample(Words,snippet.count("%%%"))]
    other_names = random.sample(Words,snippet.count("***"))
    results = []
    parameter_names = []

    for i in range(0,snippet.count("@@@")):
        parameter_count = random.randint(1,3)
        parameter_names.append(','.join(random.sample(Words,parameter_count)))

    for sentence in snippet,phrase:
        result = sentence[:]

        for word  in class_names:
            result = result.replace("%%%",word,1)
            #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in parameter_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(Phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = Phrases[snippet]
            question,answer = convert(snippet,phrase)
            if Phrases_First:
                question,answer = answer,question

            print(question)
            input('>')
            print("Answer: %s\n\n"%answer)

except EOFError:
    print("EOFError,bye\n")


