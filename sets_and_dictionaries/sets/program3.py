#program check the length of a set after adding 20, 20.0 and '20' to it

s= set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

#length comes to 2 instead of 3, although we added a float and int of same value 20.0 and 20 respectively 
#but in python because they are numerically same they are treated as one value