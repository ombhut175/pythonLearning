# 4. Write a program to filter a list of numbers which are divisible by 5.


l = [5,13,15,25,36]

newL = filter(lambda x : x%5==0 ,l)

print(list(newL))