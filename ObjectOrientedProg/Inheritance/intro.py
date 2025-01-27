#Inheritance is a way if creating a new class from an existing one

class Employee:#base class
    company = "Google"
    def show(self):
        print(f"The company is {self.company}")
    
    
class Programmer(Employee): #child class inherinting parent class
    language = "python"
    def showLanguage(self):
        print(f"The language is {self.language}")
   
   
a = Employee()
b = Programmer()
b.show() #accessing method of base class using instance of child class
b.showLanguage() 

#we can use the methods and attributes of Employee class in Programmer class and add new methods in Programmer class

#types
    #single
    #multiple
    #multilevel

