#write a program to format a string below using format function

#the name of student is harry, his marks are and his phone no. is 1234567890


name = input("enter your name :")
marks = int(input("enter your marks :"))

strr = "the name of student is {} and his marks are {} and his phone no. is 12345678".format(name,marks) 
print(strr)