#program to display user entered name forllowed by Good Morning using input() function

name = input("enter your name :")
print("Good Morning",name)
print(f"Good Morning {name}") #better way is to mark it as a formatted sting (f) and dynamically insert the value


name = "Dear Dushyant,\nThis python course is nice.\n\tThanks!"
print(name)

name = "niharika"
print(name[0]) #strings are iterable