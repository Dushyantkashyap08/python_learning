#program to find out wheather a given name is present in list or not.

listt = ["dushyant", "niharika", "rohan", "bhomik", "rahul"]

name = input("enter your name : ")

if(name in listt):
    print("name is present in list")
else:
    print("name is not present in list")