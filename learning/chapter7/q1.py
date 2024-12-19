# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.


l = ["Harry", "Soham", "Sachin", "Rahul"]

for val in l:
    if(val.lower().startswith("s")):
        print(f"good morning {val}")

