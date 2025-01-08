a = int(input("Enter your age: "))

# If elif else ladder, 
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age") #elif used to include multiple conditions

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent") #last else will be executed if none of the above conditions are true


print("End of Program")


#Relational/Comparison operators : ==, !=, >, <, >=, <=
#these can be used along with if statements to further narrow down the conditions


#Logical operators : and, or, not
#&& (and) : if both the conditions are true then,it will be executed
#|| (or) : if any one of the conditions is true then it will be executed
# ! (not) : if the condition is false then it will be executed