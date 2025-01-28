#create a class Employee and add salary and increment properties to it

class Employee:
    def __init__(self, sal, increment):
        self.sal = sal
        self.increment = increment
        
    @property
    def salaryAfterIncrement(self):
        return self.sal+self.sal*(self.increment/100)

e = Employee(10000, 20)
print(e.sal)
print(e.salaryAfterIncrement)
print(e.increment)