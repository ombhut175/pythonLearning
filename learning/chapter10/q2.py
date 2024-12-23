# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math

class Calculator:
    def sqaure(self,n):
        print(n**2)
    def cube(self,n):
        print(n**3)
    def squareRoot(self,n):
        print(math.sqrt(n))
    @staticmethod
    def greetUser():
        print("good morning")


objCalcy = Calculator()
objCalcy.greetUser()
Calculator.greetUser()
objCalcy.sqaure(2)
objCalcy.cube(2)
objCalcy.squareRoot(4)