#try-except block is used to handle exceptions
#try block is used to execute a block of code that may raise an exception
#except block is used to handle the exception

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except Exception as e:   #default except block
    print(f"An error occurred: {e}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


#commented out code above are the custom exceptions that we can raise and handle
#also we can add multiple try except blocks 