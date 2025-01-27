#create a class Employee and add salary and increment properties to it

class Employee:
    def __init__(self, sal):
        self.sal = sal
        
    def salary(self):
        print(f"my salary is {self.sal}")
        
    def increment(self):
        self.sal = self.sal + (self.sal * 0.1)
        return self.sal

e = Employee(10000)
e.salary()
print(e.increment())
