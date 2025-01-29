#using list comprehension, print a table of a num entered by user

table = []
num = int(input("Enter a number: "))
for i in range (1, 11):
    table.append(num*i)
print(table)



#using list comrehension...

table = []
num = int(input("Enter a number: "))
table= [num*i for i in range (1,11)]
print (table)

with open("advanced_python/problems/table.txt", "a") as f1:
    f1.write(str(table) + "\n")
