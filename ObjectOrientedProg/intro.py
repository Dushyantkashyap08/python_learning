#Classes and Objects in Python

#Class : a template for creating objects, contains all the attributes and methods
#Object : an instance of a class, a specific entity created from the class template. It implements and access the methods/functions and attributes of class

#memory is allocated only after the object is created (onject initalization)
#objects of a given class can invoke methods availbale to it without revealing the detailed info to user (encapsulation and abstraction)

class Employee: #defining a class
    company = "Google" #company and salary are class attributes/properties
    salary = 100

bulbul = Employee() #bulbul is an object of class Employee
bulbul.name = "bulbul coder" #also we can assign values to attributes(object attribute)
print(bulbul.name, bulbul.company, bulbul.salary)
    