#program to get the fruits name from user and form a list of it

fruits = []
n = int(input("enter number of fruits : "))
for i in range(n):
    fruit = input("enter fruit name : ")
    fruits.append(fruit)

print(fruits)

