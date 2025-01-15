#recursion:  The function continues calling itself until it reaches a base case, which stops the recursion.

# Purpose:
# To break down a problem into smaller, more manageable subproblems.

'''
factorial(0) = 1 #base case
factorial(1) = 1 #base case
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1) #factorial being called in its own definition


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

print()
print()

print("Program to recursively adds all numbers from n down to 0 OR program to sum first n natural numbers")
def rec(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return n + rec(n-1) 
    
n = int(input("Enter a number: "))
print(f"The result is: {rec(n)}")