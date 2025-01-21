#__init__() is a special method which is called when an object is created. It takes self as a first default argument and can also take further arguments
#it is first run as soon as the obj is created. It is also called constructor

#methods in python starting with __ are also called dunder methods

class Student:
    subject = "Maths"
    grade = "A"
    
    def __init__(self, name, subject , grade):
        print("I am getting called everytime an obejct is getting created")
        self.name = name
        self.subject = subject
        self.grade = grade
        
    def getInfo(self): 
        print(f"The subject is {self.subject} and the grade is {self.grade}")
    
    @staticmethod 
    def greet(): 
        print("Good Morning")
        
    
student1 = Student("dushyant", "python", "A") #now when we set the value of name, subject and grade in init method ,we are passing them as arguments during function call
print(student1.name, student1.subject, student1.grade)
student1

