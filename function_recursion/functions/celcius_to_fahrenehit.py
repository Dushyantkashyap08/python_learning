#convert celcius to fahrenheit

def converter(f):
    c = 5*(f-32)/9
    return round(c, 2) #additionally rounding off the ans upto 2 decimal places

fah = int(input("enter the temp in fahrenheit : "))
print(f"temp in degree celcius is : {converter(fah)}")




#how do you prevent python from generating a new line

print("a")
print("b")
print("c", end = "") #end function will prevent python interpreter from generating a new line
print("d", end = "")