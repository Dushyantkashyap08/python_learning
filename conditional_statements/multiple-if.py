# Input a number from the user
number = int(input("Enter a number: "))

# Check different conditions using multiple if statements
if number > 0:
    print(f"{number} is a positive number.")

if number < 0:
    print(f"{number} is a negative number.")

if number % 2 == 0:
    print(f"{number} is an even number.")

if number % 2 != 0:
    print(f"{number} is an odd number.")
