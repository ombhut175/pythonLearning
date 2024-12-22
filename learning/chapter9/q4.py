# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

f = open(filePath)

data = f.read()

newData = data.replace("donkey","#####")

f.close()

f = open(filePath,"w")
f.write(newData)

f.close()
# for i in data:
#     if (i=="donkey"):
#         data[data.index(i)] = "#####"



