#sets : collection of non repetitive elements

s = set() #empty set
d = {} #empty dictionary, although bith dictionary and sets use {} to represent a collection
print(type(s))
print(type(d))

s = {1,3,4,4,4,56,76}
print(s) #as 4 is repeating, but it will print 4 only 1 time as it is non repetitive

#prop. of sets
    # Unordered: Elements in a set do not have a specific order.
    # Unique Elements: A set automatically removes duplicates.
    # Mutable: Sets are mutable, meaning elements can be added, removed, or updated.
    # Unindexed : Sets do not have an index, so accessing elements is not possible.


# Why Use Sets?
    # Removing duplicates in collections.
    # Useful in scenarios where collection uniqueness and efficient lookups are required, such as:
    # Data analysis
    # Data validation
    # Performing set operations like union, intersection, and difference