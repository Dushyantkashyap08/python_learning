#write a program to filter a list of num divisible by 5

lis = [1,2,3,4,5,66,7,8,9,10,15]

fil = lambda x: x%5==0

sup = filter(fil,lis)
print(list(sup))



#write a program to find maximum of numbers in a list using reduce

from functools import reduce

def great(a,b):
    if a>b:
        return a
    return b
    
sup = reduce(great, lis)
print(sup)

#without reduce
max = lis[0]
for i in lis:
    if i>max:
        max = i
print(max)