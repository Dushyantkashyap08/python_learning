class Student:
    subject = "Maths"
    grade = "A"
    
    #self is not a keyword but a naming convention.
    def getInfo(self): #self represents the instance of the class itself and allows access to its attributes and methods. self is mandatory to give while defining a method weather we use it or not
        print(f"The subject is {self.subject} and the grade is {self.grade}")
    
    @staticmethod #we used static method decorator to avoid passing self as an argument as there was no use of object in this method so we declared it as a static method
    def greet(): 
        print("Good Morning")
        
    
student1 = Student()

#two ways to access class methods
Student.getInfo(student1) #by default python uses this way, when we call a method on an object, python automatically passes the object as the first argument
student1.getInfo()
student1.greet()


