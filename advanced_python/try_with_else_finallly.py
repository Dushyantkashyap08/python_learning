try:
    a = int(input("Hey, Enter a number: "))
    print(a)
   
except Exception as e:
    print(e) 

else:
    print("I am inside else")


#when try block is executed successfully then else block will be executed, otherwise the exception is handled as usual in the except block





try:
    a = int(input("Hey, Enter a number: "))
    print(a)
    
except Exception as e:
    print(e) 
    
finally:
    print("I am inside finally")
    
#code in finally will be executed irrespective of the result of the try block


