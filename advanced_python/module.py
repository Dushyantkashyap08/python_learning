def myFunc():
    print("hello world")
    

print(__name__) #when we run this file, __name__ will return __main__ becoz this module is imported in main file
#when we run main file, then this function will return module becoz it tells the file name which is being imported

if __name__ == "__main__": #we do this if we dont want some fucntions to be executed when we import this module, we we run main file print(__name__) will return module and then function inside this will not be executed
    myFunc()
