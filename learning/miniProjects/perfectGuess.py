# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

compNumber = random.randint(0,100)    
print(compNumber)
guesses = 0


while(True):
    userInput = int(input("guess number between 0 to 100 "))
    guesses+=1
    if(userInput<compNumber):
        print("increase the size of your input")
    elif(userInput>compNumber):
        print("decrease the size of input")
    else:
        print("correct guess")
        break

print(f"you have guessed correct number {compNumber} in {guesses} guesses")