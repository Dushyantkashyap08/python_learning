#create a class 'Train' which has methods to book train tickets , get status of seats and get info of trains running on a particular route
from random import randint

class Train:
    
    def __init__(self, name, time, destination, trainNo):
        self.name = name
        self.time = time
        self.destination = destination
        self.trainNo = trainNo
    
    def setInfo(self):
        print(f"name of the passenger is: {self.name}")
        print(f"time of the passenger is: {self.time}")
        print(f"destination of the passenger is: {self.destination}")
        print(f"train no. is: {self.trainNo}")        
        print("Ticket Booked Successfully.!")
        
    def getStatus(self):
        print(f"the train {self.trainNo} is running on time {self.time}")
        
    def trainBook(self, fro ,to):
        print(f"the train {self.trainNo} is booked from {fro} to {to}")
        
    def fairPrice(self, fro, to):
        print(f"the ticket price from {fro} to {to} is : {randint(222,5555)}")
        
obj = Train("dushyant", 10.45, "Delhi", 12334)
obj.setInfo()
obj.getStatus()
obj.trainBook("punjab", "delhi")
obj.fairPrice("punjab", "delhi")
