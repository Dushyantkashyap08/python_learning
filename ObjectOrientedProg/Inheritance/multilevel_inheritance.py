#multilevel inheritance : when child class becomes a pernt class for another child class

class Employee:
    company = "Google"
    def showCompany(self):
        print(f"The company is {self.company}")
        
class Programmer(Employee):
    language = "python"
    def showLanguage(self):
        print(f"The language is {self.language}")
        
class Coder(Programmer):
    name = "dushyant"
    def showDetails(self):
        print(f"The name of coder is {self.name} and the language is {self.language} and the company name is {self.company}")
        
c = Coder()
c.showDetails()


#another example

class grandparent:
    a = 1
    
class parent(grandparent):
    b = 2
    
class child(parent):
    c = 3
    
o = child
print(o.a)
print(o.b)
print(o.c) 