#operations in lists

example = ["dushyant", 56, 645.5, True, "this is a list"]
print(example[0:3]) #slicing in list can be done in the same way as done in strings
# print(example[5]) #this will throw error (index out of range) 

#list methods 

ex = [1,3,65,23,654,756]
ex.sort() # sorts the list in ascending order
print(ex)


ex.append("new") #adds new value at the end
print(ex)


ex.reverse() #reverse the list
print(ex)

ex.pop(4) #deletes the provided index in the list
print(ex)

ex.remove(654) #removes the actual value from the list else throw error if not found
print(ex)

ex.insert(3,"rohan") #adds a new value at a particular index 
print(ex)


#there are more methods on list which can be used depending on the use case