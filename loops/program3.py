#program to check if a number is prime or not

num = int(input("enter a number : "))

count = 0
for i in range(1, num+1):
    if(num%i == 0):
        count += 1
    else:
        continue

if(count == 2):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
#another way

num = int(input("enter a number : "))

for i in range(2, num):
    if(num%i == 0):
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")