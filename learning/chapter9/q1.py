# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

f = open(filePath)

data = f.read().split()


for i in data:
    if(i == "twinkle"):
        print("have word twinkle")
        break
    

