Forbidden = (',','.','?','!',';','，','。')
def reverse(Text):
    return Text[::-1]
def is_palindrome(Text):
    return Text == Text[::-1]

text = input("Input SomeThing :")
Text = []

for i in text:
    if i not in Forbidden:
        Text.append(i)
#print(type(Text))
#刚提取出来的是列表
Text = ''.join(Text)
#用join将列表转换为字符串
#print(type(Text))
print('Text: ',Text)
if is_palindrome(Text) :
    print("Yes,it's palindrome" )
else:
    print("No,it's not palindrome")