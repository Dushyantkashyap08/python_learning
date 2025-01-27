#make a class capable of finding square, cube and square root of a number

class operations:
    def __init__(self, num):
        self.num = num
        
    def square(self):
        return self.num * self.num
    
    def cube(self):
        return self.num * self.num * self.num
    
    def sqrt(self):
        return self.num ** 0.5
    
    @staticmethod
    def user():
        print("hello i am a user")
    
    def result(self):
        print(f"The square of {self.num} is {self.square()}")
        print(f"The cube of {self.num} is {self.cube()}")
        print(f"The square root of {self.num} is {self.sqrt()}")
        
num = int(input("Enter a number: "))
obj = operations(num)
obj.result()


