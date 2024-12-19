# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

n = 5
nst=1

# for i in range(n,0,-1):
#     for k in range(i-1):
#         print(end=" ")
#     for j in range(nst):
#         print("*",end="")

#     nst+=2
#     print()

for i in range(n,0,-1):
    # for k in range(i-1):
    #     print(end=" ")
    print(" "*(i-1),end="")
    # for j in range(nst):
    #     print("*",end="")
    print("*"*nst,end="")
    nst+=2
    print()