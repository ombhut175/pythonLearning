#  Write a program to mine a log file and find out whether it contains ‘python’.
# Write a program to find out the line number where python is present from ques 6.


import os

def lineNumber():
    str_path = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(str_path,"input.txt")
    f = open(filePath)
    lines = 0
    currLine = f.readline()
    while(currLine!=""):
        print(currLine)
        lines+=1
        if "python" in currLine:
            f.close()    
            return lines
        currLine = f.readline()
    return -1

print(lineNumber())