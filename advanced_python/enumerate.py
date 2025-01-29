#enumerate function is used to simplify the use of indexing in a list or tuple

l = ["dushyant", "niharika", "rohan", "bhomik", "rahul"]

index = 0
for item in l:
    print(f"the item at index{index} is {item}")
    index+=1
    
    
#the above task can be simplified using enumerate function
print("using enumerate function")

for index,item in enumerate(l):
    print(f"the item at index{index} is {item}")