x = "There are %d type of people."%10
binary = 'binary'
do_not = "don't"
y = "Those know %s and those who %s ." %(binary,do_not)
print(x)
print(y)

print("I said: %r" %x)
print("I also said %s" %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny? "

print(joke_evaluation + "%r" %hilarious)

w = "This is the left side of ..."
e = "a string with right side."

print(w+e)