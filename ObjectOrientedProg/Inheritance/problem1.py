#create a class 2D vector and create another class 3dVector out of it

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def __str__(self):
        return f"{self.i}i + {self.j}j"
        
class ThreeDVector(TwoDVector):
    def __init__(self,i , j, k):
        super().__init__(i, j)
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
obj = ThreeDVector(1,2,3)
print(obj)