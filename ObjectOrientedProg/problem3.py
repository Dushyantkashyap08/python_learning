#create a class attribute 'a' and then create an obj of class. not set  the value of a using obj. does that change the class attribute?

class prob:
    a = "this is class attribute"
    
obj = prob()
print(obj.a) #firstly checks if instance attribute is present or not, if not then print class attribute
obj.a = "hello" #here instance attribute is created and set to hello
print(obj.a) #printing instance attribute
print(prob.a) #class attribute still remains unchanged