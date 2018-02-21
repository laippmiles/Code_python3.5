from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s"%(from_file,to_file))

#以下的两行代码其实可以一行写
in_file = open(from_file)
indata = in_file.read()

print("The file is %d bytes long"%len(indata))

print("Does the output file exist? %r"%exists(to_file))
input("键盘任意键按一下继续，CTRL+C退出")

out_file = open(to_file,'w')
out_file.write(indata)

in_file.close()
out_file.close()

print("All Done")