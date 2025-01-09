#program to find out wheather a given username has less than 10 characters or not

username = input("enter your username : ")

length = len(username)

if(length<10):
    print("username is less than 10 characters")

else:
    print("username is more than 10 characters")