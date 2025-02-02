#print a square star pattern using for loop
print("SQUARE")
for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print() 


#print a right triangle star pattern
print("RIGHT ANGLE TRIANGLE")
for i in range (1,6):
    for j in range (1, i+1):
        print("*", end = "")

    print()

#print a decreasing right triangle star pattern
print("DECREASING RIGHT ANGLE TRIANGLE")
for i in range (1,6):
    for j in range (i, 6):
        print("*", end = "")

    print()


#print a right triangle star pattern
print("RIGHT ANGLE TRIANGLE")
for i in range (1,6):
    for j in range (1, 6):
        print("", end = "")
    for j in range(1, i+1):
        print("*", end = "")
    print()


#print a right triangle star pattern
print("RIGHT ANGLE TRIANGLE")
for i in range (1,6):
    for j in range (1, 6):
        if(j in range(i, 6)):
            print("*", end = "")
        else:
            print(" ", end = "")

    print()
