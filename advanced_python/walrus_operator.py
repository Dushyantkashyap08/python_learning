#walrus operator (:=) is used to assign and evaluate a value in the same line.

#example 1
if ( n := int(input("Enter a number: ")) ) % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
    


#example 2
if (num := len([23, 45, 56, 676, 68, 345, 112])) > 5:
    print(f"list has MORE than required elements")
else:
    print(f"list has LESS than required elements")