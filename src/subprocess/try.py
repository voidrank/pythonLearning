import subprocess
child = subprocess.Popen("ping www.baidu.com", shell=True)
print "parent process"
