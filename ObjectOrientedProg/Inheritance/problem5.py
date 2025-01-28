#create a vector of 3 dimensions and perfrom addition and multiplication on them

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __len__(self):
        return len([self.x, self.y, self.z])
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)  # Output: (5, 7, 9)
print(v1 * v2)  # Output: (4, 10, 18)
print(len(v2))
