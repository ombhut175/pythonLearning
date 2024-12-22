# Write a program to find out whether a file is identical & matches the content of
# another file.

import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

f1 = open(filePath)
data = f1.read()
f1.close()

filePath2 = os.path.join(str_path,"input(copy).txt")
f2 = open(filePath2)
data2 = f2.read()
f2.close()
if(data==data2):
    print("both are same")
else:
    print("different")