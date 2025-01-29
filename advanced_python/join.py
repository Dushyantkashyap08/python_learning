#join exp is used to join items of a list using a seperator

list = ['wqe', 'qweq', "rahul", "sdfds"]

# list = ['wqe', 'qweq', "rahul", "sdfds", 2, [3,5,6], True] #can be used when we have items other than strings
# result = ' : '.join(map(str, list)) 

result = ' : '.join(list)
print(result)
