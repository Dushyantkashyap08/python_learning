#create an empty dict and allow 4 friends tro enter their fav language as values and their names as keys. assume that the names are unique.

dict = {}
for i in range(4):
    name =input(f"enter the name of friend {i+1} : ")
    language = input(f"enter the fav language of {name} : ")
    dict[name] = language
    # dict.update({name : language})
print(dict)

#if any friend has same name then duplicate enteries will not be added , but will update the previous key-value pair
#becoz in dictionary keys are the identifiers and they should be unique otherwise will be updated

#if language is same then nothing will happen