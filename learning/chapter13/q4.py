# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
from functools import reduce

l = [1,31,21,19]

maxNum = reduce(max,l)

print(maxNum)