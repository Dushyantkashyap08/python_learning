#class decorator is used to create a class method

class Employee:
   a = 10
   
   @classmethod #when we apply classmethod then after making instance of this class , it will still pick the class attribute value rather than instance attribute value as the default behaviour
   def show(self):
       print(f"the class value of a is {self.a}")
       
       
e = Employee()
e.a = 20
e.show()
     