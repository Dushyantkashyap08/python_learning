#operations in tuple

my_tuple = ("dushyant", 56, 645.5, True, "this is a tuple", 56)

print(my_tuple.count(56)) #count the no. of occurences of a particular value in tuple

print(my_tuple.index(56)) #returns the index of value , but in case of multiple occurences, it retruns the index of first val only else throws ValueError

tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1 + tuple2) #concatenation of tuples

print(tuple1 * 3) #repetition of tuples
 
print(len(tuple1)) #length of tuple

print(56 in my_tuple) #returns boolean, To check if a value exist in a tuple or not

a, b, c = tuple1
print(a, b, c) #unpacking tuple values in single variables

#similarly slicing in tuples can be done in the same way as done in lists
