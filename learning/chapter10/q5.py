# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
    name = str()
    noOfSeats = int()
    infoOfTrain = str()
    def __init__(self,name):
        self.name = name
    
    def bookTicket(self,noOfSeats,infoOfTrain):
        self.noOfSeats = noOfSeats
        self.infoOfTrain = infoOfTrain
    def getStatus(self):
        print(self.noOfSeats,self.infoOfTrain,self.name,sep=" ")


rakesh = Train("Rakesh")

rakesh.bookTicket(3,"geetanjali")
rakesh.getStatus()