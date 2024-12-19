# Write a program which finds out whether a given name is present in a list or not.

userList=["Om","raj","jay"]
user = "om"

lowerUser = user.lower()
lowerList = [userVal.lower() for userVal in userList]


print(lowerUser in lowerList)