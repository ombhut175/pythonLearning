# Write a program to wipe out the content of a file using python

import os

str_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(str_path,"input.txt")

with open(filePath,"w") as f1:
    pass
