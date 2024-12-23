# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Temp:
    a = 3
    def printA(self):
        print(self.a)


tempObj = Temp()
tempObj.a = 0
tempObj.printA()