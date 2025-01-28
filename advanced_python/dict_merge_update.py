#we can merge dictionary 

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = d1 | d2 #merge using pipe operator
print(d3)

#updating dictionary

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1 |= dict2  # Update using |= instead of dict1.update(dict2) which will aslo give same output

print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
