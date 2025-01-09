#using for loop with else statement

for i in range(1,6):
    print(i)
else:
    print("loop exit") #else statement will be executed at the end of loop
    
#break statement

for i in range(1,6):
    if(i==3):
        break  # break will exit the loop on a certain condition
    else:
        print(i)

#continue statement

for i in range(1,6):
    if(i==3):
        continue  # continue will skip a particular iteration on a certain condition
    else:
        print(i)
    
#pass statement : it instructs to do nothing, just passes the current execution
print("pass statement in python")
for i in range(1,6):
    pass #skips the for loop execution and shifts to while loop

i = 0
while(i<5):
    i+=1
    print(i)