#create a class programmer to store information of few programmers working at microsoft

class Programmer:
    
    company = "Microsoft"
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        
    def getInfo(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The designation of the programmer is {self.designation}")
        print(f"The company of the programmer is {self.company}") #class attribute
        print(f"The salary of the programmer is {self.salary}")
        
obj = Programmer("dushyant", "Software Engineer", 100000)
obj.getInfo()