#super keyword is user to access methods and properties of parent classes

class grandparent:
    a = 1
    def __init__(self):
        print("grandparent constructor")
    
class parent(grandparent):
    b = 2
    def __init__(self):
        super().__init__()
        print("parent constructor")
    
class child(parent):
    c = 3
    def __init__(self):
        super().__init__()
        print("child constructor")
    
o = child()
print(o.a)
print(o.b)
print(o.c) 