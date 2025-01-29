#program to write a/b , where b is not 0 and if b is 0 thorw an error of zero division and print infinite

try:
    a=20
    b=0 
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")