def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()


#finally's main use can be understood when we use it with functions along with when we retrun values from functions. by default,when a function returns something then the further execution stops. but when we use finally then even after returning value the finally block will run