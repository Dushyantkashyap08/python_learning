#can you change the values inside the list contained in set s 

s = {1, 2, "harry", True, [34,45,56] }
print(s)

#this will throw a type error as we cannot conatin lists in a set. becoz all the element s of a set should be immutable and hashable(should be having fixed hash value)
#lists are mutable and not hashable