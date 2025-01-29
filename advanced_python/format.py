#format function is used to create a formatted string, it was used earlier before python 3.6

a = "{} is a good {}".format("dushyant", "boy")

b = "{1} is a good {0}".format("dushyant", "boy") #we can also provide numbers in the parathesis to specify the positions of values in the formatted string
print(a)
print(b)


#f-string is used to create a formatted string in python 3.6 and later versions
