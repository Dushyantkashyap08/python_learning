#list : can be used to store multiple value sof different data types

example = ["dushyant", 56, 645.5, True, "this is a list"]
print(example)
print(example[0]) #access a specific value


# name = "harry"
# mod = name[3] = 'u'
# print(mod) #this will throw an error as we discussed that strings are immutable and does not support re assignment, we can make a new string out of existing one but cannot change the existing string


#in case of list we can modify the existing ones (LISTS ARE MUTTABLE)
example = ["dushyant", 56, 645.5, True, "this is a list"]
mod = example[0] = "niharika"
print(example) #as we can see orignal list is modified
