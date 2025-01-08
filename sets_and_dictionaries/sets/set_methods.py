#sets methods

my_set = {1, 2, 3}
my_set.add(4) #Adds a single element to the set. If the element already exists, nothing happens.
print(len(my_set)) #length of set
print(my_set)  

my_set.discard(4) #Removes a single element from the set. If the element not found, nothing happens.
print(my_set)

my_set.remove(3) #Removes a single element from the set. If the element not found, throws KeyError.
print(my_set)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2) #Returns a new set containing all elements from both sets
print(result)  



set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2) #Returns a new set containing common elements
print(result)  

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2) #Returns a new set containing elements in the first set but not in the second
print(result)  

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2) #returns only unique elements from both sets
print(result)  

#you can also use other methods like issubset(), issuperset(), isdisjoint()

