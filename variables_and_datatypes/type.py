#type() function and typecasting

a = 23
print(type(a))

b = 34.5
print(type(b))

c = "keshav"
print(type(c))

d = True
print(type(d))

#type casting : changing the data type from one type to another but that should be valid

a = 23
print(str(a)) #integer to sting
print(float(a)) # integer to floating
print(bool(a==23)) # integer to bool

# b = "this is a string"
# print(int(b)) #this will give an error as int() expects a valid integer value inside double quotes to be able to get converted into string

b = "123"
print(int(b)) #valid string to integer

# Mutability	=>     Data Types
# Mutable	    =>     List, Dictionary, Set, Bytearray
# Immutable	    =>     Integer, Float, String, Tuple, Frozenset, Bytes, Boolean