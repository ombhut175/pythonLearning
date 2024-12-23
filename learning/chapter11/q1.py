# Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.Create a class (2-D vector) and use it to create another class representing a 3-D

class TwoDVector:
    vect1 = 1
    vect2 = 2

class ThreeDVector(TwoDVector):
    vect3 = 3


tempObj = ThreeDVector()

print(f"{tempObj.vect1} {tempObj.vect3}")