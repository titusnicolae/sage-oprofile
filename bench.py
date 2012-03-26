import os
from sage.all_cmdline import reset
from sys import stdout
from os.path import splitext 

filename="r01_1.py"
name,ending=splitext(filename)
f=open(filename, "r")
os.system("opcontrol --stop")
os.system("opcontrol --reset")
os.system("opcontrol --start")
s=f.read()
s="from sage.all_cmdline import reset\nreset()\n"+s
execfile(filename)
os.system("opcontrol --stop")
os.system("opreport 1>"+name+".log 2>"+name+".err")
#os.system("opreport -l 1>"+name+".log2 2>"+name+".err2")
