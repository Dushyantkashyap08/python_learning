#list comprehension is used to create a new list based on an existing list

#syntax: [expression for item in iterable if condition]

#print even num from 1 to 10
evens = [x for x in range(10) if x % 2 == 0]
print(evens)


#create a flattened list from 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)


#convert items into uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
