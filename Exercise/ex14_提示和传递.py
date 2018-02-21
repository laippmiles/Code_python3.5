from sys import  argv

script, user_name , likes = argv
prompt = '>'

print("Hi %s,I'm the <%s> script." %(user_name,script))
print("I'd like to ask you a few quertions.")
print("Do you like me %s?"%user_name)
#likes = input(prompt) #这神他妈我还以为是啥高深的魔法

print('Where do you live %s?' %user_name)
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print('''
Alright,so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice.
'''%(likes,lives,computer))

#加分题3：给你的脚本再添加一个参数，让你的程序用到这个参数。