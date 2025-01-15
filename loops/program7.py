#print the following pattern
'''
for n = 3
    * * *
    *   *
    * * *
'''
n = int(input("enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if(j == 1 or i == 1 or j == n or i==n or i == j or j==n-i+1) : #i == j or j==n-i+1 these conditions for making a cross between them
            print("* ", end = "")
        else:
            print("  ", end = "")
    print()