# coding=utf-8
import os
import time
import zipfile
source =[r'F:\Desktop\Python3.5\test']

target_dir =r'F:\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

Now = time.strftime('%H%M%S')
Today = time.strftime('%Y%m%d')

Comment = input('Enter a Comment ----->')
if len(Comment) == 0:
    target = target_dir +'\\'+ Today + '\\' + Now + '.rar'
else:
    target = target_dir +'\\'+ Today + '\\' + Now + '_' + Comment.replace(' ','_') + '.rar'

if not os.path.exists(target_dir +'\\'+ Today):
    os.mkdir(target_dir +'\\'+ Today) # 创建目录

#rar_command='winrar a %s %s' % (target,''.join(source))
rar_command = "WinRAR.exe a %s %s" % (target,''.join(source))
#设置环境变量后要重启IDE
print(rar_command)
if os.system(rar_command) == 0:
    #os.system 意思是执行系统命令，等于cmd里面输入命令
    print('Successful backup to', target)
else:
    print('Backup FAILED')
