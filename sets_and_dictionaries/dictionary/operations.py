#operations on dictionary

dict = {
    "name" : "dushyant",
    "age" : 23,
    "marks" : 65.5,
    "fruits" : ['apple', 'banana', 'mango'],
    0:"bhomik"
}

print(dict.items()) #gives key value pairs as tuples
print(dict.keys()) #gives only keys
print(dict.values()) #gives only values
print(dict.get("name")) #gives value of a particular key else output is None if key not found
print(dict["name"]) #gives value of a particular key else throws error if key not found

dict.update({"name" : "niharika", "hobby" : "coding"}) #modifying a key-value in dictionary and if key -value not found then append it in dictionary
print(dict)

#pop() : removes a key-value pair from dictionary and returns the value
print(dict.pop("name"))
print(dict)

#clear() : removes all key-value pairs from dictionary
dict.clear()
print(dict) #returns an empty dictionary


#similary there are other methods available in dictionary. search them from chat gpt and use accordingly