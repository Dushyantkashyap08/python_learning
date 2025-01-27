#create pets out of class animal further create a calss dog from pets. add a method bark to class dog

class Animals:
   def animal(self):
        print("this is main animal class")
        
    
        
class Pets(Animals):
   def pet(self):
        print("this is pets class derived from Animal class")
    
    
class Dogs(Pets):
    @staticmethod
    def bark():
        print("dog bark")
        
d = Dogs()
d.animal()
d.pet()
d.bark()
    
