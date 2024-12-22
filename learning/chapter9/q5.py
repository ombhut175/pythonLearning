# Repeat program 4 for a list of such words to be censored.

import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

censoredWords = ["donkey","motu","patlu"]

f = open(filePath)

data = f.read()
dataList = data.split()

# newData = data.replace("donkey","#####")

for i in dataList:
    if (i in censoredWords):
        data = data.replace(i , "#"*len(i))

f.close()

f = open(filePath,"w")
f.write(data)

f.close()