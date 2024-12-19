# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

def checkSpam(userMessage):
    spamMessages = ["Make a lot of money","buy now","subscribe this","click this"]
    for warning in spamMessages:
        if warning in userMessage:
            print("spam")
            return True
        
    return False

userMessage = "hello i want to buy"

print(checkSpam(userMessage))