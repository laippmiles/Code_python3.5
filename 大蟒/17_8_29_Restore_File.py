# coding=utf-8
import os
import time
source =[r'F:\Desktop\Python3.5\test']

target_dir =r'F:\backup'

target = target_dir + time.strftime('%Y%m%d%H') + '.rar'
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

#rar_command='winrar a %s %s' % (target,''.join(source))
rar_command = "WinRAR.exe a %s %s" % (target,''.join(source))
#设置环境变量后要重启IDE
print(rar_command)
if os.system(rar_command) == 0:
    #os.system 意思是执行系统命令，等于cmd里面输入命令
    print('Successful backup to', target)
else:
    print('Backup FAILED')