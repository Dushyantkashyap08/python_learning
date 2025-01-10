#program to calculate the factorial of a num

num = int(input("enter a number : "))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(factorial)