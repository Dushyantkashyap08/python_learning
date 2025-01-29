#global keyword is used to access global variables inside a function

a = 10

def myFunc():

    global a #this will update the global variable
    a = 3
    print(a)
    

myFunc()
print(a)