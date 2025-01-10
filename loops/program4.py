#program to find sum of first n nautral numbers using while loop

num = int(input("enter a number : "))

i = 1
sum = 0

while (i<=num):
    sum = sum + i
    i = i + 1

print(sum)