#prgram to print table of n using for loop in reverse order

n = int(input("enter a number: "))


for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")
    

#using while loop
print("using while loop......")
i = 10
while(i>=1):
    print(f"{n} x {i} = {n*i}")
    i = i-1
'''
    1 10
    2  9
    3  8 
    4  7 
    5  6
    6  5
    7  4
    8  3
    9  2
    10 1

sum of every pair comes to 11 that's why we wrote 11 there to get reverse order
'''