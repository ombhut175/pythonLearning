# Write a python program to rename a file to “renamed_by_ python.txt.

import os

str_path = os.path.dirname(os.path.abspath(__file__))
oldFilePath = os.path.join(str_path,"input.txt")
newFilePath = os.path.join(str_path,"renamed_by_ python.txt")

os.rename(oldFilePath,newFilePath)    