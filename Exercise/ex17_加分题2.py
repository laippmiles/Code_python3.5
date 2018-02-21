from sys import argv
from os.path import exists
script,from_file,to_file = argv
print("Copying from %s to %s \n"%(from_file,to_file),
      "The file is %d bytes long\n"%len(open(from_file).read()) ,
      "Does the output file exist? %r\n"%exists(to_file),"键盘回车键按一下继续，CTRL+C退出")
input()
open(to_file,'w').write(open(from_file).read())
open(to_file).close()
#带着'w'close，文件会被清空掉
#read一旦运行，运行结束自动会close的
print("All Done")