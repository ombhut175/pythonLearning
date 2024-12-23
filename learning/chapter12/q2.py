# Write a program to print third, fifth and seventh element from a list using enumerate function

list = [1,4,5,43,23,43,55,32]

for index,val in enumerate(list):
    if(index==3 or index==5 or index==7):
        print(val,end=" ")

