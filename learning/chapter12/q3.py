# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.
import os


n = int(input("enter n : "))
dir_name = os.path.dirname(os.path.abspath(__file__))
pathOfFile1 = os.path.join(dir_name,"1.txt")

list = [n*i for i in range(1,11)]

with (
    open(pathOfFile1,"w") as f1
):
    f1.write(str(list))
