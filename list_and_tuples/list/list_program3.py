#program to sum a list with 4 numbers
num = [23, 32, 34, 54]

s = 0
for i in num:
    s = s + i
print(s)

#another way
print(sum(num)) # sum() function can be used to sum a list


#program to count the number of zeros in the following  tuple

tuple = (7,0,8,0,0,9)
print(tuple.count(0))