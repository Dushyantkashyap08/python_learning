#program to find greatest of three numbers

def greatest(a, b, c):
    if a>b and a>c:
        print(f"{a} is the greatest number.")
    if b>a and b>c:
        print(f"{b} is the greatest number.")
    if c>a and c>b:
        print(f"{c} is the greatest number.")
        
greatest(4,5,6)