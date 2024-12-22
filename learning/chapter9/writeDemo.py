import os

str = "bhai padhay kar"
script_dir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(script_dir,"output.txt")

f = open(filePath,"w")

f.write(str)

f.close()