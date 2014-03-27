import os
import re
import subprocess
from os.path import expanduser
commands=[("sudo mkdir /usr/share/vlcSub","creating directory structure"),("sudo mkdir /usr/share/vlcSub/src/","creating directory structure"),("sudo mkdir /usr/share/vlcSub/images/",".."),("sudo cp src/vlcSub.py /usr/share/vlcSub/src/vlcSub.py",".."),("sudo cp vlcSub.desktop /usr/share/applications/vlcSub.desktop","copying files"),("sudo cp icons/vlcSub.png /usr/share/vlcSub/images/vlcSub.png","..")]

for command,text in commands:
    #print command
    p=subprocess.Popen(command,shell=True)
    p.wait()
    print text
print "creating entry in mimeapp list "
obj=open(expanduser("~")+"/.local/share/applications/mimeapps.list")
buff=obj.read()
obj.close()
flag=0
buff2=""
for line in buff.split("\n"):
    if line=="[Default Applications]":
        flag=1
    if flag==1:
        line=line.replace("vlc.desktop","vlcSub.desktop")
    buff2=buff2+line+"\n"
print buff2
#print x[0]
#buff.replace("vlc.desktop",)
#print buff
obj=open(expanduser("~")+"/.local/share/applications/mimeapps.list","w")
obj.write(buff2)
obj.close()
p=subprocess.Popen("sudo chmod +x /usr/share/vlcSub/src/vlcSub.py",shell=True)
p.wait()
