# Write a program to make a copy of a text file “this. txt”
import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

f1 = open(filePath)
data = f1.read()
f1.close()

filePath2 = os.path.join(str_path,"input(copy).txt")
f2 = open(filePath2,"w")
f2.write(data)
f2.close()