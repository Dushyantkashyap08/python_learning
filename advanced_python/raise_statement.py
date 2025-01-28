#raise statement is used to raise an exception when a certain condition is met. mostly used with if statement

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero") #when this exception is raised, then the program crashes there
else:
    print(f"The division a/b is {a/b}")
    
    
# try-except: Catches and handles exceptions that occur during execution.

# raise: Explicitly triggers an exception when a specific condition is met.