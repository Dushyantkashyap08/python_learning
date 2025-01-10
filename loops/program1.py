#print a table of a number using for loop

num  = int(input("enter a number : "))

for i in range(1, 11):
    print(num*i)
    
    
print("using while loop")

i = 1
while(i<=10):
    print(num*i)
    i+=1