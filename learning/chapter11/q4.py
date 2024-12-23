# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self,i,j):
        self.n = complex(i,j)
    def __add__(self,complexNum):
        return self.n + complexNum.n
    def __sub__(self,complexNum):
        return self.n - complexNum.n
    def __mul__(self,complexNum):
        return self.n * complexNum.n
    def __str__(self):
        return f"real part = {self.n.real} complex part = {self.n.imag}"

num1 = Complex(3,5)
num2 = Complex(4,6)

print(num1)
print(num1 + num2)