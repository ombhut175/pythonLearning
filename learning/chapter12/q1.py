# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
pathOfFile1 = os.path.join(dir_name,"1.txt")
pathOfFile2 = os.path.join(dir_name,"2.txt")
pathOfFile3 = os.path.join(dir_name,"3.txt")
try:
    with (
        open(pathOfFile1) as f1,
        open(pathOfFile2) as f2,
        open(pathOfFile3) as f3
    ):
        pass
except FileNotFoundError as e:
    print("file not found")