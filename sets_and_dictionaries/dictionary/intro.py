#dictionary : collection of key value pairs. mixed data type can be stored

a = {} #empty dictionary
b = {
    "name":"dushyant", 
    "age":23, 
    "marks": 65.5,
    "fruits" : ['apple', 'banana', 'mango']
    } #dictionary with values
print(type(b)) #dictionary type
print(b)
print(b['name']) #accessing a particular value
b["age"] = 45 #modifying a value (mutable)
print(b)

#properties of dictionary
# mutable
# unordered
# indexed
# can contain duplicate keys


#need of dictionary
#like we could have also done like this 
b = [["name", "dushyant"], ["age", 23], ["marks", 65.5], ["fruits", ['apple', 'banana', 'mango']]]
#this is nested list structure, but accessing of values corresponding to a particular key would become very difficult and req. complex logic
#hence we use dictionary