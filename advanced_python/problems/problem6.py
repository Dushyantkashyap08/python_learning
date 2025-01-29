#print table of 7 and then convert it into a vertical string of numbers

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(table) #list of table
print(s) #vertical string