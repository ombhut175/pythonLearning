# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = 9
nst=1

for i in range(n,0,-1):
    print("*"*nst)
    nst+=2