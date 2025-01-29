#print 3,5 and 7 element of a list using enumerate function

list = ['wqe', 'qweq', 34, 565.7, True, "rahul", [1,2,3], "sdfds"]

for index ,item in enumerate(list):
    if index in [3,5,7]:
        print(f"the item at index{index} is {item}")
