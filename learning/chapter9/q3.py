# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

import os

str_path = os.path.dirname(os.path.abspath(__file__))
folderName = "multiplicationTable"
folderpath = os.path.join(str_path,folderName)

os.makedirs(folderpath,exist_ok=True)

for i in range(2,21):
    filePath = os.path.join(folderpath,f"tableOf{i}")
    tempStr = ""
    for j in range(1,11):
        tempStr+=f"{i} * {j} = {i*j} \n"
    f = open(filePath,"w")
    f.write(tempStr)
    f.close()