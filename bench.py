import os
from sage.all_cmdline import reset
from sys import stdout
from os.path import splitext,split 
from glob import glob

logdir="log/"
for filename in glob("py/*.py"):
	#filename="py/r01_1.py"
	name,ending=splitext(split(filename)[1])
	f=open(filename, "r")
	#os.system("opcontrol --stop")
	os.system("opcontrol --reset")
	os.system("opcontrol --start")
	print filename
	for i in range(1,10):
		execfile(filename)
	os.system("opcontrol --stop")
	os.system("opreport 1>"+logdir+name+".log 2>"+logdir+name+".err")
	#os.system("opreport -l 1>"+name+".log2 2>"+name+".err2")
os.system('grep -r "pynac" log/* | printf "%-15s%-10s%-10s%s\n" `sed "s/\s\{1,\}/ /g"` >statistics10')
