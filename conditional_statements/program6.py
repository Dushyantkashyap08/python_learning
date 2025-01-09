#program to find out the grade of student

marks = int(input("enter your marks : "))

if(marks<50):
    print("F")
elif(marks>50 and marks<60):
    print("D")
elif(marks>60 and marks<70):
    print("C")
elif(marks>70 and marks<80):
    print("B")
elif(marks>80 and marks<90):
    print("A")
else:
    print("A+")
            
#optimized way
# marks = int(input("Enter your marks: "))

# if marks < 50:
#     print("F")
# elif 50 <= marks < 60:
#     print("D")
# elif 60 <= marks < 70:
#     print("C")
# elif 70 <= marks < 80:
#     print("B")
# elif 80 <= marks < 90:
#     print("A")
# else:
#     print("A+")
