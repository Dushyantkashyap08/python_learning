#print a right angle star pattern using for loop

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print() 
    
#or another method
n = 5
for i in range(1,n+1):
    print("* "*i, end = "")
    print()
    
#print a square using for loop 

print("square pattern")
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()
    
print("triangle pattern (odd pattern)")

num = int(input("enter a number : "))

for i in range(1, num+1):
    print(" "* (num-i), end = " ")
    print("*"* (2*i-1), end = " ")
    print(" ")
    
#another way using nested loop
print("Triangle Pattern (even pattern)")

num = int(input("Enter a number: "))

for i in range(1, num + 1):  # Outer loop for each row
    for j in range(num - i):  # Inner loop for spaces
        print(" ", end="")
    for k in range(1,i+1):  # Inner loop for stars
        print("* ", end="")
    print()  # Move to the next line after completing the row
    
    

