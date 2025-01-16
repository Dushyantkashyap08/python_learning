#print the following pattern
'''
***
**
*
'''
def pattern(n):
    # n = int(input("Enter a number: "))
    for i in range(n, 0, -1):  # Loop from n down to 1
        print("*" * i)  # Print i asterisks in each row


pattern(5) #function call


print("SAME PATTERN USING RECURSION")

def patternRec(n):
    if n == 0:
        return
    print("*"*n)
    patternRec(n-1)
    
patternRec(5)