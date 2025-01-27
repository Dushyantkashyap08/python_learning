#property decorator is used to set a property. it allows you to access the method like an attribute without parentheses.

# class Employee:
   
#    @property #@property is used to define a method as a getter
#    def name(self): #name is a getter method but will be used as a attribute to get the value
#        print(f"The name is {self.fname} {self.lname}")
       
#    @name.setter #@<property_name>.setter , to define a method as a setter for same property
#    def name(self,name):
#         self.fname = name.split(" ")[0]
#         self.lname = name.split(" ")[1]
       
# e = Employee()
# e.name = "dushyant kashyap"
# e.name
     
     
#split function acts on a string and splits a str into a list of substrings at the specified separator. in above case the seperator is a space


#another example

class Person:
    def __init__(self, name, age):
        # Private attributes
        self._name = name
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

# Usage
person = Person("Alice", 25)

# Using the getter
print(person.name)  # Alice
print(person.age)   # 25

person.age
person.name
