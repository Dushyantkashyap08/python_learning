#create a dictionary with hindi words with their translation in english words. orovide user with an optionto look it up.

dict = {
    "achha" : "good",
    "bura" : "bad",
    "udharan" : "example",
    1 : "one",
    "satya" : True
} 

word = input("enter the hindi word you want to look up: ")
if word in dict:
    print(dict[word])
else:
    print("word not found")