# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import os


def game():
    str_path = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(str_path,"Hi-score.txt")
    f = open(filePath)
    checkDataEmpty = False
    data = f.read()
    if(data != ""):
        data = int(data)
    else:
        checkDataEmpty = True
    newVal = int(input("enter new score"))
    if(checkDataEmpty or newVal>data):
        f.close()
        f = open(filePath,"w")
        f.write(str(newVal))
        f.close()
        return newVal
    return data


game()