import os
import subprocess
import sys

f = open("random.dic", "r")
key = f.readlines()

for i in key:
	i = str(i.replace("\n",""))
	print (i)
	subprocess.run(["./program", i])
