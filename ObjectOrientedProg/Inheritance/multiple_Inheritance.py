#multiple inheritance: when child class inherits from more than one parent class

class Employee:#base class
    company = "Google"
    def show(self):
        print(f"The company is {self.company}")
    
class Coder:
    name = "dushyant"
    def showName(self):
        print(f"The name of coder is {self.name}")
    
class Programmer(Employee, Coder): #inheriting multiple classes
    language = "python"
    def showLanguage(self):
        print(f"The language is {self.language} and the company name is {self.company} and the coder is {self.name}")
   
   
a = Employee()
b = Programmer()
b.show() #accessing method of base class using instance of child class
# b.language = "java"
b.showLanguage() 
b.showName()