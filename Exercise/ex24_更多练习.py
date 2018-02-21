print("Let's practice everything.")
print("You'd need to know'bout escapes with \\ that do \n newline \t tabs.")

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discorn \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
'''

print('-'*15)
print(poem)
print('-'*15)

five = 10 - 2 + 3 - 6#直接写5不好吗..
print("This should be five: %s"%(five))

def secret_formula(started):
    jerry_beans = started * 500
    jars = jerry_beans / 1000
    crates = jars / 100
    return jerry_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print("With a starting point of : %d"% start_point)
print("We'd have %d beans , %d jars, and %d crates."%(beans,jars,crates))

start_point = start_point/10

print("We can also do that this way:")
print("We'd have %d beans , %d jars, and %d crates."%secret_formula(start_point))